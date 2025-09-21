from enum import Enum


class AdminLevel(str, Enum):
    """
    Enumeration of administrative levels in TaiwanViz.

    - COUNTY  : county/city level (縣市)
    - TOWN    : township level (鄉鎮市區)
    - VILLAGE : village level (村里)
    """

    COUNTY = "county"
    TOWN = "town"
    VILLAGE = "village"


class ColorPalette(str, Enum):
    """
    Enumeration of available color palettes for choropleth rendering.

    - NORD         : dark Nord theme
    - LIGHT_NORD   : light Nord theme
    - MORANDI      : soft muted Morandi colors
    - ECONOMIST    : The Economist official style
    - SELF_DEFINED : user-defined palette
    """

    NORD = "nord"
    LIGHT_NORD = "light_nord"
    MORANDI = "morandi"
    ECONOMIST = "economist"
    SELF_DEFINED = "self_defined"
