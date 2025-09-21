import numpy as np
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from dataclasses import dataclass, field
from typing import Dict, Union, Literal
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

from taiwanviz.models.base.layers import initialize_all_layers
from taiwanviz.models.palette import ColorPaletteManager
from taiwanviz.models.enums import ColorPalette
from taiwanviz.models.config import ChoroplethRenderConfig
from taiwanviz.utils import (
    exclude_islands,
    get_mainland,
    get_kinmen,
    get_matsu,
    compute_colors,
    plot_mainland,
    plot_inset,
    register_all_fonts,
    set_default_zh_font
)


@dataclass
class ChoroplethMap:
    """
    ChoroplethMap renders Taiwan administrative maps (county, town, or village level)
    with data-driven coloring. Supports excluding offshore islands and adding insets
    for Kinmen, Matsu, and optionally other small regions.
    """
    level: Literal["county", "town", "village"]
    data: Dict
    palette_name: Union[str, ColorPalette]

    default_edge: str = field(init=False)
    default_fill: str = field(init=False)

    countys: gpd.GeoDataFrame = field(init=False)
    towns: gpd.GeoDataFrame = field(init=False)
    villages: gpd.GeoDataFrame = field(init=False)

    def __post_init__(self):
        """
        Initialize layers, palette, and fonts.
        """
        # initialize palette
        if isinstance(self.palette_name, ColorPalette):
            name = self.palette_name.value
        elif isinstance(self.palette_name, str):
            name = self.palette_name
        else:
            raise ValueError("palette must be a string or ColorPalette")

        palette_conf = ColorPaletteManager.get_palette(name)
        self.palette_colors = palette_conf["colors"]
        self.default_edge = palette_conf["default_edge"]
        self.default_fill = palette_conf["default_fill"]

        self.countys, self.towns, self.villages = initialize_all_layers()

        # initialize fonts
        register_all_fonts()
        set_default_zh_font()


    def get_layer(self):
        """Return the GeoLayer object corresponding to the specified level."""
        if self.level == "county":
            return self.countys
        elif self.level == "town":
            return self.towns
        elif self.level == "village":
            return self.villages
        else:
            raise ValueError(f"Unsupported level: {self.level}")

    def render(self, config: ChoroplethRenderConfig = ChoroplethRenderConfig()):
        """Render the choropleth map with mainland + insets."""
        gdf = self.get_layer().map_data(self.data).copy()

        if config.exclude_offshore:
            gdf = exclude_islands(gdf)

        # Compute color mapping
        values = gdf["value"]
        colors = compute_colors(values, self.palette_colors, self.default_fill)

        # Mainland
        mainland = get_mainland(gdf)
        fig, ax = plt.subplots(figsize=config.figsize, dpi=config.dpi)
        plot_mainland(ax, mainland, colors, edgecolor=self.default_edge)
        ax.set_xlim(config.mainland_xlim)
        ax.set_ylim(config.mainland_ylim)

        # title
        if config.title:
            ax.set_title(config.title, fontsize=14)
        else:
            ax.set_title("Taiwan Map with Insets", fontsize=14)

        ax.axis("off")

        # Insets
        if config.show_inset:
            if self.level == "county":
                town_gdf = self.towns.map_data(self.data).copy()
                if config.exclude_offshore:
                    town_gdf = exclude_islands(town_gdf)

                kinmen_focus = get_kinmen(town_gdf)
                matsu_focus = get_matsu(town_gdf)

                town_values = town_gdf["value"]
                town_colors = compute_colors(town_values, self.palette_colors, self.default_fill)

                plot_inset(ax, matsu_focus, town_colors, "Matsu", "upper left", edgecolor=self.default_edge)
                plot_inset(ax, kinmen_focus, town_colors, "Kinmen", "lower left", edgecolor=self.default_edge)

            else:
                kinmen_focus = get_kinmen(gdf)
                matsu_focus = get_matsu(gdf)

                plot_inset(ax, matsu_focus, colors, "Matsu", "upper left", edgecolor=self.default_edge)
                plot_inset(ax, kinmen_focus, colors, "Kinmen", "lower left", edgecolor=self.default_edge)

        # colorbar
        if config.show_legend and not values.dropna().empty:
            norm = mcolors.Normalize(vmin=values.min(), vmax=values.max())
            cmap = mcolors.LinearSegmentedColormap.from_list("custom", self.palette_colors, N=256)
            sm = cm.ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])

            cbar = fig.colorbar(sm, ax=ax, orientation="vertical", shrink=0.6, pad=0.02)
            cbar.ax.set_ylabel("Value", fontsize=9)

            if config.legend_loc == "left":
                cbar.ax.yaxis.set_ticks_position("left")
                cbar.ax.yaxis.set_label_position("left")

        plt.show()