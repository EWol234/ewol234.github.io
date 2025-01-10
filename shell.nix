let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.11";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in

pkgs.mkShellNoCC {
  packages = with pkgs; [
    hugo
    nodejs
    electron-chromedriver_31
    xclip
    (pkgs.python3.withPackages (python-pkgs: [
        python-pkgs.requests
        python-pkgs.selenium
        python-pkgs.beautifulsoup4
      ]))
  ];
}
