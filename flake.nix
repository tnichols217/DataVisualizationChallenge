{
  description = "Data Analysis Homework 2";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      treefmt-nix,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };

        python = pkgs.python3.withPackages (
          ps: with ps; [
            black
            matplotlib
            pandas
            numpy
            scipy
            pandas-stubs
            beautifulsoup4
            (ps.buildPythonPackage rec {
              pname = "matplotlib_stubs";
              version = "0.3.11";
              pyproject = true;
              src = pkgs.fetchPypi {
                inherit pname version;
                sha256 = "sha256-9rpvn6WYi3jDcyhPJueFA04zYNZrLKQcZanWJyBvfIs=";
              };

              build-system = with ps; [
                hatchling
                setuptools-scm
              ];

              dependencies = with ps; [
                matplotlib
                numpy
                pandas
              ];
            })
          ]
        );

        treefmtconfig = treefmt-nix.lib.evalModule pkgs {
          projectRootFile = "flake.nix";
          programs = {
            nixfmt.enable = true;
            yamlfmt.enable = true;
          };
        };
      in
      {
        formatter = treefmtconfig.config.build.wrapper;

        devShells = {
          default = pkgs.mkShell {
            packages = with pkgs; [
              ruff
              nil
              nixd
              nixfmt
              basedpyright
            ] ++ [
              python
            ];
          };
        };

        packages = rec {
          default = plots;
          qol = pkgs.callPackage ./qol_src.nix {};
          plots = pkgs.callPackage ./build.nix { inherit qol; };
        };
      }
    );
}
