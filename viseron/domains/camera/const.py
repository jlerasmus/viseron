"""Camera domain constants."""
from typing import Any, Dict

DOMAIN = "camera"


# Event topic constants
EVENT_STATUS = "{camera_identifier}/camera/status"
EVENT_STATUS_DISCONNECTED = "disconnected"
EVENT_STATUS_CONNECTED = "connected"

EVENT_RECORDER_START = "{camera_identifier}/recorder/start"
EVENT_RECORDER_STOP = "{camera_identifier}/recorder/stop"

EVENT_CAMERA_START = "{camera_identifier}/camera/start"
EVENT_CAMERA_STOP = "{camera_identifier}/camera/stop"


# MJPEG_STREAM_SCHEMA constants
CONFIG_MJPEG_WIDTH = "width"
CONFIG_MJPEG_HEIGHT = "height"
CONFIG_MJPEG_DRAW_OBJECTS = "draw_objects"
CONFIG_MJPEG_DRAW_MOTION = "draw_motion"
CONFIG_MJPEG_DRAW_MOTION_MASK = "draw_motion_mask"
CONFIG_MJPEG_DRAW_OBJECT_MASK = "draw_object_mask"
CONFIG_MJPEG_DRAW_ZONES = "draw_zones"
CONFIG_MJPEG_ROTATE = "rotate"
CONFIG_MJPEG_MIRROR = "mirror"

DEFAULT_MJPEG_WIDTH = 0
DEFAULT_MJPEG_HEIGHT = 0
DEFAULT_MJPEG_DRAW_OBJECTS = False
DEFAULT_MJPEG_DRAW_MOTION = False
DEFAULT_MJPEG_DRAW_MOTION_MASK = False
DEFAULT_MJPEG_DRAW_OBJECT_MASK = False
DEFAULT_MJPEG_DRAW_ZONES = False
DEFAULT_MJPEG_ROTATE = 0
DEFAULT_MJPEG_MIRROR = False


# THUMBNAIL_SCHEMA constants
CONFIG_SAVE_TO_DISK = "save_to_disk"
CONFIG_FILENAME_PATTERN = "filename_pattern"

DEFAULT_SAVE_TO_DISK = True
DEFAULT_FILENAME_PATTERN = "%H:%M:%S"


# RECORDER_SCHEMA constants
CONFIG_LOOKBACK = "lookback"
CONFIG_IDLE_TIMEOUT = "idle_timeout"
CONFIG_RETAIN = "retain"
CONFIG_FOLDER = "folder"
CONFIG_FILENAME_PATTERN = "filename_pattern"
CONFIG_EXTENSION = "extension"
CONFIG_THUMBNAIL = "thumbnail"

DEFAULT_LOOKBACK = 5
DEFAULT_IDLE_TIMEOUT = 10
DEFAULT_RETAIN = 7
DEFAULT_FOLDER = "/recordings"
DEFAULT_FILENAME_PATTERN = "%H:%M:%S"
DEFAULT_EXTENSION = "mp4"
DEFAULT_THUMBNAIL: Dict[str, Any] = {}


# BASE_CONFIG_SCHEMA constants
CONFIG_NAME = "name"
CONFIG_PUBLISH_IMAGE = "publish_image"
CONFIG_MJPEG_STREAMS = "mjpeg_streams"
CONFIG_RECORDER = "recorder"

DEFAULT_NAME = None
DEFAULT_PUBLISH_IMAGE = False
DEFAULT_MJPEG_STREAMS: Dict[str, Any] = {}
DEFAULT_RECORDER: Dict[str, Any] = {}
