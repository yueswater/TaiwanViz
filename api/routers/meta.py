"""
Meta endpoints for palettes, fonts, and health checks.
"""

from fastapi import APIRouter
import matplotlib.pyplot as plt

from ..schemas import PalettesResponse, PaletteInfo, FontsResponse, HealthResponse
from taiwanviz.models.palette import ColorPaletteManager
from taiwanviz.utils.fonts import list_available_fonts

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """
    Basic health check endpoint.

    Returns
    -------
    HealthResponse
        Object with status "ok" when service is alive.
    """
    return HealthResponse(status="ok")


@router.get("/palettes", response_model=PalettesResponse)
def palettes() -> PalettesResponse:
    """
    List all available color palettes.

    Returns
    -------
    PalettesResponse
        Palette names with their default edge/fill and color lists.
    """
    out = []
    for name, conf in ColorPaletteManager.palettes.items():
        out.append(PaletteInfo(
            name=name,
            default_edge=conf["default_edge"],
            default_fill=conf["default_fill"],
            colors=conf["colors"],
        ))
    return PalettesResponse(palettes=out)


@router.get("/fonts", response_model=FontsResponse)
def fonts() -> FontsResponse:
    """
    List all packaged fonts and the current Matplotlib default family.

    Returns
    -------
    FontsResponse
        Available TTF files and current default family name.
    """
    return FontsResponse(
        fonts=list_available_fonts(),
        default_family=plt.rcParams.get("font.family")
    )
