from pydantic import BaseModel
from typing import Dict
from taiwanviz.models.enums import AdminLevel, ColorPalette
from taiwanviz.models.palette import ColorPaletteManager


class MapDataInput(BaseModel):
    """
    Input schema for choropleth map rendering.

    Attributes
    ----------
    level : AdminLevel
        Administrative level of the map ("county", "town", "village").
    data : dict[str, float]
        Mapping from region name to numerical value.
    palette : ColorPalette, default NORD
        Color palette used for rendering.
    """
    level: AdminLevel
    data: Dict[str, float]
    palette: ColorPalette = ColorPalette.NORD