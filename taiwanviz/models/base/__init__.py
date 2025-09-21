"""
Base classes and layer initialization utilities for TaiwanViz.

- BaseGeoLayer: abstract class for loading and handling shapefiles.
- initialize_all_layers: helper to load county, town, and village layers at once.
"""

from .base import BaseGeoLayer
from .layers import CountyGeoLayer, TownGeoLayer, VillageGeoLayer, initialize_all_layers
