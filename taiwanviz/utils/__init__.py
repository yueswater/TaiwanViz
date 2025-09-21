"""
Utility functions for TaiwanViz choropleth rendering.

This package provides helpers for:
- filters: GeoDataFrame filtering (mainland, islands, Kinmen, Matsu, Penghu, etc.)
- colors:  color mapping utilities
- plotting: standardized drawing functions for main map and insets
"""

from .colors import compute_colors
from .filters import exclude_islands, get_kinmen, get_mainland, get_matsu
from .fonts import register_all_fonts, set_default_zh_font
from .plotting import plot_inset, plot_mainland

__all__ = [
    # filters
    "exclude_islands",
    "get_mainland",
    "get_kinmen",
    "get_matsu",
    "get_penghu",
    # colors
    "compute_colors",
    # plotting
    "plot_mainland",
    "plot_inset",
    # fonts
    "register_all_fonts",
    "set_default_zh_font",
]
