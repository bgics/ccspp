{
  pkgs,
  # lib,
  # config,
  ...
}: {
  languages = {
    python = {
      enable = true;
      uv.enable = true;
      uv.sync.enable = true;
    };
  };

  packages = with pkgs; [basedpyright ruff];
}
