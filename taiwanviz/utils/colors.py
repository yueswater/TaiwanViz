import pandas as pd
import numpy as np
import matplotlib.colors as mcolors


def compute_colors(values: pd.Series, palette_list: list, default_fill: str = "lightgray") -> pd.Series:
    """
    Map numeric values to colors using a continuous colormap.

    Parameters
    ----------
    values : pd.Series
        Series of numeric values to be mapped.
    palette_list : list
        List of colors used to build the colormap.
    default_fill : str, default "lightgray"
        Color assigned to missing (NaN) values.

    Returns
    -------
    pd.Series
        Series of color values corresponding to the input.
    """
    if values.dropna().empty:
        return pd.Series([default_fill] * len(values), index=values.index)

    norm = mcolors.Normalize(vmin=np.nanmin(values), vmax=np.nanmax(values))
    cmap = mcolors.LinearSegmentedColormap.from_list("custom", palette_list, N=256)
    return values.map(lambda v: cmap(norm(v)) if pd.notna(v) else default_fill)