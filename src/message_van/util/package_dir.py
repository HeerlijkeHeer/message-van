from pathlib import Path


def get_package_dir(start_path: Path) -> Path:
    return _get_package_dir(start_path.resolve())


def _get_package_dir(current_path: Path) -> Path:
    if _is_src_dir(parent_path := current_path.parent):
        return current_path

    return _get_package_dir(parent_path)


def _is_src_dir(path: Path) -> bool:
    return path.name == "src" or path.name == "site-packages"
