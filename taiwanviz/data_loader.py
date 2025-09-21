from importlib.resources import files
import geopandas as gpd


def load_shapefile(level: str, filename: str) -> gpd.GeoDataFrame:
    """
    Load a shapefile from the packaged data and convert it to WGS84 (EPSG:4326).

    Parameters
    ----------
    level : str
        Administrative level folder ("county", "town", "village").
    filename : str
        Shapefile name (e.g., "COUNTY_MOI_1140318.shp").

    Returns
    -------
    GeoDataFrame
        Loaded shapefile as a GeoDataFrame in EPSG:4326 CRS.
    """
    shp_folder = files("taiwanviz.data.shp") / level
    path = shp_folder / filename
    return gpd.read_file(str(path)).to_crs(epsg=4326)