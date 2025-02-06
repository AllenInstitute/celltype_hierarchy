from pathlib import Path


def get_path(verbose: bool = False) -> dict:
    """
    Get the root path of the package, for access to data files.
    """
    root_path = Path(__file__).parent.parent
    return str(root_path)
