from dataclasses import dataclass
from typing import Tuple, Literal, Optional


@dataclass
class ChoroplethRenderConfig:
    """
    Configuration for rendering choropleth maps.

    Attributes
    ----------
    aspect : {"county", "town", "village"}, default "county"
        Administrative level of the map.
    show_inset : bool, default True
        Whether to display insets (Kinmen, Matsu, etc.).
    exclude_offshore : bool, default True
        Exclude Dongsha and Taiping islands from the map.
    mainland_xlim : tuple of float, default (118.5, 122.5)
        Longitude bounds for main island view.
    mainland_ylim : tuple of float, default (21.0, 26.0)
        Latitude bounds for main island view.
    dpi : int, default 300
        Resolution of the rendered figure.
    figsize : tuple of int, default (8, 10)
        Size of the figure in inches (width, height).
    title : str or None, optional
        Custom title for the map. If None, a default title is used.
    show_legend : bool, default False
        Whether to display a colorbar legend based on the data values.
    legend_loc : str, default "right"
        Position of the legend (e.g., "right", "left", "upper right",
        "lower left"). Passed to Matplotlib legend positioning logic.
    """
    aspect: Literal["county", "town", "village"] = "county"
    show_inset: bool = True
    exclude_offshore: bool = True
    mainland_xlim: Tuple[float, float] = (118.5, 122.5)
    mainland_ylim: Tuple[float, float] = (21.0, 26.0)
    dpi: int = 300
    figsize: Tuple[int, int] = (8, 10)

    title: Optional[str] = None
    show_legend: bool = False
    legend_loc: str = "right"
