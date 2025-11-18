{ stdenv, python3, python3Packages, fetchurl }:
let
  qol = fetchurl {
    url = "https://www.numbeo.com/quality-of-life/rankings.jsp";
    hash = "sha256-8U8XTp8z9peZ7Yl4CP+KE621knFRNYWx+9OXCO2V25o=";
  };
  apmt = fetchurl {
    url = "https://assets.ctfassets.net/jeox55pd4d8n/7jLDkOc80R392YvAPqDxQ/90d7821e7337a593df39067e618aca76/Apartment_List_Rent_Estimates_2025_10.csv";
    hash = "sha256-uHFVPbTkXqQ9cVqV3iAz7TiDsXUr4JYje+V7l0Q4IFc=";
  };
in
stdenv.mkDerivation {
  pname = "build-graphs";
  version = "0.0.1";

  src = ./.;

  buildInputs = [
    (python3.withPackages (
      ps: with ps; [
        matplotlib
        pandas
        scipy
        beautifulsoup4
      ]
    ))
  ];

  # Run the Python script
  buildPhase = ''
    mkdir -p data plots
    cp ${qol} ./rankings.jsp
    cp ${apmt} ./data/apmt.csv
    python -m src.main
  '';

  # Copy plots produced by the script
  installPhase = ''
    mkdir -p $out
    cp -r plots/* $out/
  '';
}
