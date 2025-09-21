class ColorPaletteManager:
    """
    Manage color palettes for choropleth rendering.
    Each palette includes:
      - default_edge : str
      - default_fill : str
      - colors       : list[str]
    """

    palettes = {
        "nord": {
            "default_edge": "#fbfbfb",
            "default_fill": "lightgray",
            "colors": [
                "#2E3440",
                "#3B4252",
                "#434C5E",
                "#4C566A",
                "#D8DEE9",
                "#E5E9F0",
            ],
        },
        "nord_light": {
            "default_edge": "#2E3440",
            "default_fill": "lightgray",
            "colors": [
                "#ECEFF4",
                "#E5E9F0",
                "#D8DEE9",
                "#81A1C1",
                "#5E81AC",
                "#4C566A",
            ],
        },
        "morandi": {
            "default_edge": "#f0f0f0",
            "default_fill": "#d9d9d9",
            "colors": [
                "#A89D8D",
                "#C1B7A3",
                "#B4ADA3",
                "#8E9CA3",
                "#9CA89D",
                "#D6CFC7",
            ],
        },
        "economist": {
            "default_edge": "#0C0C0C",
            "default_fill": "#E9EDF0",
            "colors": [
                "#E3120B",
                "#006BA2",
                "#3EBCD2",
                "#379A8B",
                "#EBB434",
                "#B4BA39",
                "#9A607F",
                "#D1B07C",
                "#758D99",
            ],
        },
    }

    @staticmethod
    def get_palette(name: str) -> dict:
        """
        Get palette configuration by name.
        """
        return ColorPaletteManager.palettes.get(
            name, ColorPaletteManager.palettes["nord"]
        )
