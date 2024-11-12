{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python3         # Python 3.x interpreter
    pkgs.python3Packages.pip      # pip package manager
    pkgs.python3Packages.django   # Django framework
    pkgs.python3Packages.djangorestframework # Django REST Framework
    pkgs.nano
  ];
}
