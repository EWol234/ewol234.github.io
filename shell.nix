let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-unstable";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in

pkgs.mkShellNoCC {
  packages = with pkgs; [
    hugo
    nodejs
    electron-chromedriver_36
    xclip
    claude-code
    uv
    (pkgs.python3.withPackages (python-pkgs: [
        python-pkgs.requests
        python-pkgs.selenium
        python-pkgs.beautifulsoup4
      ]))
  ];
}
