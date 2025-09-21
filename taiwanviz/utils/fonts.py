import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import logging
from typing import List
from importlib.resources import files

logging.basicConfig(level=logging.INFO)

DEFAULT_ZH_FONT = "NotoSansTC-Regular.ttf"


def _iter_ttf_files(base):
    """Recursively yield all .ttf files under a Traversable directory."""
    for entry in base.iterdir():
        if entry.is_dir():
            yield from _iter_ttf_files(entry)
        elif entry.name.lower().endswith(".ttf"):
            yield entry


def register_all_fonts():
    """
    Register all packaged fonts under taiwanviz/fonts.
    """
    font_dir = files("taiwanviz.fonts")
    count = 0
    for path in _iter_ttf_files(font_dir):
        try:
            fm.fontManager.addfont(str(path))
            logging.debug(f"Registered font: {path.name}")
            count += 1
        except Exception as e:
            logging.error(f"Failed to register {path}: {e}")
    logging.info(f"Registered {count} fonts from {font_dir}")


def set_default_zh_font():
    """
    Set Matplotlib default font to Noto Sans TC (for Chinese text).
    """
    font_dir = files("taiwanviz.fonts").joinpath("noto-sans")
    path = font_dir.joinpath(DEFAULT_ZH_FONT)
    if not path.exists():
        raise FileNotFoundError(f"Default Chinese font not found: {path}")
    font_prop = fm.FontProperties(fname=str(path))
    plt.rcParams["font.family"] = font_prop.get_name()
    logging.info(f"Default Chinese font set to {font_prop.get_name()}")
    return font_prop


def set_default_font(filename: str):
    """
    Set Matplotlib default font to a specific TTF file inside fonts directory.
    """
    font_dir = files("taiwanviz.fonts")
    candidates = [p for p in _iter_ttf_files(font_dir) if p.name == filename]
    if not candidates:
        raise FileNotFoundError(f"Font file {filename} not found in {font_dir}")
    path = candidates[0]

    font_prop = fm.FontProperties(fname=str(path))
    plt.rcParams["font.family"] = font_prop.get_name()
    logging.info(f"Default font set to {font_prop.get_name()} ({filename})")
    return font_prop


def list_available_fonts() -> List[str]:
    """
    List all available TTF fonts under taiwanviz/fonts.
    """
    font_dir = files("taiwanviz.fonts")
    fonts = [p.name for p in _iter_ttf_files(font_dir)]
    logging.info(f"Found {len(fonts)} fonts: {fonts}")
    return fonts
