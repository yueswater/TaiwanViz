from importlib.resources import files
import geopandas as gpd
from .base import BaseGeoLayer
from typing import Dict, Tuple


class CountyGeoLayer(BaseGeoLayer):
    """
    GeoLayer for Taiwan counties.

    Maps user data keyed by COUNTYNAME to the county-level geometry.
    """
    def map_data(self, data: Dict) -> gpd.GeoDataFrame:
        df = self.gdf.copy()
        df["value"] = df["COUNTYNAME"].map(data)
        return df


class TownGeoLayer(BaseGeoLayer):
    """
    GeoLayer for Taiwan towns (鄉鎮市區).

    Maps user data keyed by TOWNNAME to the town-level geometry.
    """
    def map_data(self, data: Dict) -> gpd.GeoDataFrame:
        df = self.gdf.copy()
        df["value"] = df["TOWNNAME"].map(data)
        return df


class VillageGeoLayer(BaseGeoLayer):
    """
    GeoLayer for Taiwan villages (村里).

    Maps user data keyed by VILLNAME to the village-level geometry.
    """
    def map_data(self, data: Dict) -> gpd.GeoDataFrame:
        df = self.gdf.copy()
        df["value"] = df["VILLNAME"].map(data)
        return df


def initialize_all_layers() -> Tuple[BaseGeoLayer]:
    """
    Load all three administrative layers (county, town, village)
    from the packaged shapefiles and return them as GeoLayer objects.

    Returns
    -------
    Tuple[BaseGeoLayer]
        (CountyGeoLayer, TownGeoLayer, VillageGeoLayer)
    """
    base = files("taiwanviz.data.shp")
    county_path = str(base / "county" / "COUNTY_MOI_1140318.shp")
    town_path = str(base / "town" / "TOWN_MOI_1140318.shp")
    village_path = str(base / "village" / "VILLAGE_NLSC_1140825.shp")

    return (
        CountyGeoLayer(county_path),
        TownGeoLayer(town_path),
        VillageGeoLayer(village_path)
    )
