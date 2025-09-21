"""
TaiwanViz Models

This package provides core classes for building choropleth maps:

- BaseGeoLayer: abstract base class for loading shapefiles.
- ChoroplethMap: main class to render county/town/village maps.
- MapDataInput: helper for preparing user data for mapping.
- AdminLevel, ColorPalette: enums for level and color palettes.
- ColorPaletteManager: manages available color palettes.
"""

from .base.base import BaseGeoLayer
from .choropleth import ChoroplethMap
from .data_input import MapDataInput
from .enums import AdminLevel, ColorPalette
from .palette.palette import ColorPaletteManager
