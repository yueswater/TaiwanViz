"""
App startup/shutdown hooks.

- Switch Matplotlib backend to Agg (headless)
- Register packaged fonts and set default Chinese font
"""

import logging

import matplotlib

from taiwanviz.utils.fonts import register_all_fonts, set_default_zh_font

logger = logging.getLogger(__name__)


def on_startup():
    """
    Startup hook to prepare rendering environment.
    """
    # Use non-interactive backend suitable for servers/containers
    matplotlib.use("Agg")

    # Register packaged fonts and set default Chinese font
    register_all_fonts()
    set_default_zh_font()

    logger.info("Startup complete: Matplotlib Agg + fonts registered.")


def on_shutdown():
    """
    Shutdown hook. Reserved for future cleanup if needed.
    """
    logger.info("Shutdown complete.")
