{ stdenv, python3, python3Packages, curl, cacert }:
stdenv.mkDerivation {
  pname = "build-graphs";
  version = "0.0.1";

  outputHashMode = "flat";
  outputHashAlgo = "sha256";
  outputHash = "sha256-nGCQZAViOCjauaBlGeGN64GuC0D58j9aUaxskFHLsgc=";
  __contentAddressed = true;

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
    curl
    cacert
  ];

  # Run the Python script
  buildPhase = ''
    curl -L https://www.numbeo.com/quality-of-life/rankings.jsp -o rankings.jsp
    mkdir -p data
    python -m src.convert
  '';

  # Copy the outputted csv to the store
  installPhase = ''
    cp -r data/* $out
  '';
}
