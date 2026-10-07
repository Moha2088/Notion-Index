import logging
import colorlog

log_format = "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"

stream_handler = colorlog.StreamHandler()
stream_handler.setFormatter(colorlog.ColoredFormatter(fmt=log_format))
stream_handler.setLevel(logging.DEBUG)

logger = colorlog.getLogger(__name__)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)