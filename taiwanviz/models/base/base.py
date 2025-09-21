from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict

import geopandas as gpd


@dataclass
class BaseGeoLayer(ABC):
    """
    Abstract base class for geographic layers in TaiwanViz.

    - Loads a shapefile into a GeoDataFrame (EPSG:4326).
    - Provides an abstract `map_data` method for mapping user data
      (e.g., county names → values) onto the geometry.

    Subclasses must implement `map_data` to attach user-provided values.
    """

    shp_path: str

    def __post_init__(self):
        # Load shapefile as GeoDataFrame in WGS84 CRS
        self.gdf = gpd.read_file(self.shp_path).to_crs(epsg=4326)

    @abstractmethod
    def map_data(self, data: Dict) -> gpd.GeoDataFrame:
        """Attach user data to the GeoDataFrame."""
        ...
