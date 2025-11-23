{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.python310Packages.pip
    pkgs.python310Packages.virtualenv
    pkgs.cairo
    pkgs.pkg-config
    pkgs.libffi
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = "${pkgs.lib.makeLibraryPath [
      pkgs.libffi
      pkgs.cairo
    ]}";
  };
}
