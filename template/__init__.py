"""Makes the template module a package."""

from .plotly import setup_plotly_template
from .matplotlib import setup_matplotlib_template
from .templates import get_colors,get_font, get_cmap
from .constants import FIGURE_WIDTH_PIXELS, FIGURE_HEIGHT_PIXELS, FIGURE_HEIGHT_INCHES, FIGURE_WIDTH_INCHES, FONT_SIZES
from .positioning_functions import finalize_figure_with_legend_and_disclaimer

__all__ = [
    'setup_plotly_template',
    'setup_matplotlib_template',
    'finalize_figure_with_legend_and_disclaimer',
    'get_colors',
    'get_font',
    'get_cmap',
    'FIGURE_WIDTH_PIXELS',
    'FIGURE_HEIGHT_PIXELS',
    'FIGURE_HEIGHT_INCHES',
    'FIGURE_WIDTH_INCHES',
    'FONT_SIZES'
]