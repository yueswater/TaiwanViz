import geopandas as gpd
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


def plot_mainland(
    ax, mainland: gpd.GeoDataFrame, colors: pd.Series, edgecolor: str = "#fbfbfb"
):
    """
    Plot the main island of Taiwan.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes to draw on.
    mainland : GeoDataFrame
        Mainland geometries.
    colors : Series
        Color values mapped to each geometry.
    edgecolor : str, default "#fbfbfb"
        Color of the geometry borders.
    """
    mainland.plot(ax=ax, color=colors.loc[mainland.index], edgecolor=edgecolor)


def plot_inset(
    ax,
    gdf_focus: gpd.GeoDataFrame,
    colors: pd.Series,
    title: str,
    loc: str,
    edgecolor: str = "#fbfbfb",
    size: str = "30%",
):
    """
    Plot a focused region (e.g., Kinmen, Matsu, Penghu) as an inset.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Parent axes to attach the inset.
    gdf_focus : GeoDataFrame
        Focused geometries to plot in the inset.
    colors : Series
        Color values mapped to each geometry.
    title : str
        Title of the inset (region name).
    loc : str
        Location of the inset (matplotlib inset_axes location).
    edgecolor : str, default "#fbfbfb"
        Color of the geometry borders.
    size : str, default "30%"
        Relative size of the inset axes.

    Returns
    -------
    ax_inset : matplotlib.axes.Axes
        The inset axes object.
    """
    ax_inset = inset_axes(ax, width=size, height=size, loc=loc, borderpad=1.2)
    gdf_focus.plot(ax=ax_inset, color=colors.loc[gdf_focus.index], edgecolor=edgecolor)
    ax_inset.set_title(title, fontsize=9)
    ax_inset.axis("off")
    return ax_inset
