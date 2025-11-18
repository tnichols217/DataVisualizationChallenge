{ stdenv, python3, python3Packages, fetchurl, qol }:
let
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
    cp ${qol} ./data/qol.csv
    cp ${apmt} ./data/apmt.csv
    python -m src.clean
    python -m src.plot
  '';

  # Copy plots produced by the script
  installPhase = ''
    mkdir -p $out
    cp -r plots/* $out/
  '';
}
