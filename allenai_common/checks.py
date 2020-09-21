"""
Functions and exceptions for checking that
modules are configured correctly.
"""
import logging

logger = logging.getLogger(__name__)


class ConfigurationError(Exception):
    """
    The exception raised by any object when it's misconfigured
    (e.g. missing properties, invalid properties, unknown properties).
    """

    def __init__(self, message: str):
        super().__init__()
        self.message = message

    def __str__(self):
        # TODO(brendanr): Is there some reason why we need repr here? It
        # produces horrible output for simple multi-line error messages.
        return self.message
