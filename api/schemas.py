"""
Pydantic models (request/response schemas) for the API.
"""

from typing import Dict, Literal, Optional, Tuple, Union

from pydantic import BaseModel, Field, field_validator

from taiwanviz.models.enums import AdminLevel, ColorPalette

LegendLoc = Literal[
    "right", "left", "upper right", "upper left", "lower right", "lower left"
]

ResponseType = Literal["png", "base64", "json_url"]


class RenderConfigModel(BaseModel):
    """
    Render configuration mirror for ChoroplethRenderConfig with extras for API.
    """

    aspect: Literal["county", "town", "village"] = "county"
    show_inset: bool = True
    exclude_offshore: bool = True
    mainland_xlim: Tuple[float, float] = (118.5, 122.5)
    mainland_ylim: Tuple[float, float] = (21.0, 26.0)
    dpi: int = 300
    figsize: Tuple[int, int] = (8, 10)

    # API extensions
    title: Optional[str] = None
    show_legend: bool = False
    legend_loc: LegendLoc = "right"
    response_type: ResponseType = "png"


class ChoroplethRequest(BaseModel):
    """
    Request payload for choropleth rendering.
    """

    level: AdminLevel = Field(..., description="Administrative level to render.")
    data: Dict[str, float] = Field(
        ..., description="Mapping from region name to numeric value."
    )
    palette: Union[ColorPalette, str] = Field(
        ColorPalette.NORD, description="Color palette name."
    )
    config: Optional[RenderConfigModel] = Field(
        default=None, description="Optional rendering configuration overrides."
    )

    @field_validator("palette", mode="before")
    def cast_palette(cls, v):
        """
        Accept both enum and plain strings for palette.
        """
        if isinstance(v, str):
            return v
        if isinstance(v, ColorPalette):
            return v.value
        return v


class PaletteInfo(BaseModel):
    """
    Single palette information.
    """

    name: str
    default_edge: str
    default_fill: str
    colors: list[str]


class PalettesResponse(BaseModel):
    """
    Response for listing available palettes.
    """

    palettes: list[PaletteInfo]


class FontsResponse(BaseModel):
    """
    Response for listing packaged fonts.
    """

    fonts: list[str]
    default_family: Optional[str] = None


class HealthResponse(BaseModel):
    """
    Health/heartbeat response.
    """

    status: str = "ok"
