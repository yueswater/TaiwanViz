"""
Rendering routes for choropleth maps.
"""

import base64
import os
from io import BytesIO

import matplotlib.pyplot as plt
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse

from taiwanviz.models.choropleth import ChoroplethMap
from taiwanviz.models.config import ChoroplethRenderConfig

from ..schemas import ChoroplethRequest, RenderConfigModel

router = APIRouter()


def _to_render_config(cfg: RenderConfigModel | None) -> ChoroplethRenderConfig:
    """
    Convert RenderConfigModel (API) to ChoroplethRenderConfig (internal).
    """
    if cfg is None:
        return ChoroplethRenderConfig()

    return ChoroplethRenderConfig(
        aspect=cfg.aspect,
        show_inset=cfg.show_inset,
        exclude_offshore=cfg.exclude_offshore,
        mainland_xlim=cfg.mainland_xlim,
        mainland_ylim=cfg.mainland_ylim,
        dpi=cfg.dpi,
        figsize=cfg.figsize,
        title=cfg.title,
        show_legend=cfg.show_legend,
        legend_loc=cfg.legend_loc,
    )


@router.post("/choropleth")
def render_choropleth(req: ChoroplethRequest):
    """
    Render a choropleth map and return according to response_type.

    Supported response types:
    - "png"     : Return a PNG image stream (default).
    - "base64"  : Return a JSON object with base64-encoded PNG.
    - "json_url": Save as file under /tmp and return a JSON with file path.
    """
    try:
        # Build map object
        m = ChoroplethMap(
            level=req.level.value, data=req.data, palette_name=req.palette
        )

        # Render using config
        cfg = _to_render_config(req.config)
        m.render(cfg)

        # Grab current figure and serialize to PNG
        fig = plt.gcf()
        buf = BytesIO()
        fig.savefig(buf, format="png", dpi=cfg.dpi, bbox_inches="tight")
        plt.close(fig)
        buf.seek(0)

        # Select response type
        response_type = req.config.response_type if req.config else "png"

        if response_type == "png":
            return StreamingResponse(buf, media_type="image/png")

        elif response_type == "base64":
            img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
            return JSONResponse(content={"image": img_b64})

        elif response_type == "json_url":
            output_path = f"/tmp/choropleth_{os.getpid()}.png"
            with open(output_path, "wb") as f:
                f.write(buf.getvalue())
            return JSONResponse(content={"url": output_path})

        else:
            raise HTTPException(
                status_code=400, detail=f"Unsupported response_type: {response_type}"
            )

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Rendering failed: {e}")
