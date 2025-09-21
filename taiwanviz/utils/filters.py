import geopandas as gpd


def exclude_islands(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Exclude Dongsha (Pratas) and Taiping islands
    based on centroid coordinates.
    """
    if gdf.crs.is_geographic:
        gdf_proj = gdf.to_crs(epsg=3826)
        centroids = gdf_proj.centroid.to_crs(epsg=4326)
    else:
        centroids = gdf.centroid

    mask = ~(
        (
            (20.3 <= centroids.y)
            & (centroids.y <= 20.6)
            & (116.3 <= centroids.x)
            & (centroids.x <= 116.7)
        )  # Dongsha
        | (
            (9.5 <= centroids.y)
            & (centroids.y <= 11.0)
            & (113.5 <= centroids.x)
            & (centroids.x <= 115.0)
        )  # Taiping
    )
    return gdf[mask]


def get_mainland(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Return mainland Taiwan by excluding Kinmen and Matsu counties.
    """
    return gdf[~gdf["COUNTYNAME"].isin(["金門縣", "連江縣"])]


def get_kinmen(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Return GeoDataFrame for Kinmen (金門縣),
    limited to the five main towns.
    """
    return gdf[
        (gdf["COUNTYNAME"] == "金門縣")
        & (gdf["TOWNNAME"].isin(["金城鎮", "金沙鎮", "烈嶼鄉", "金寧鄉", "金湖鎮"]))
    ]


def get_matsu(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Return GeoDataFrame for Matsu (連江縣),
    limited to Beigan and Nangan.
    """
    return gdf[
        (gdf["COUNTYNAME"] == "連江縣") & (gdf["TOWNNAME"].isin(["北竿鄉", "南竿鄉"]))
    ]
