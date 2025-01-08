import ctypes

from numpy.typing import ArrayLike
from ezndi import NDIlib_send_instance_t

import numpy

from ezndi import NDI, NDIlib_send_create_t, NDIlib_video_frame_v2_t


def initialize_ndi():
    if not NDI.NDIlib_initialize():
        raise SystemError("failed to initialize NDI.")


def destroy_ndi():
    NDI.NDIlib_destroy()


def create_ndi_sender(name: str, clock_video: int = 1, clock_audio: int = 0):
    create_desc = NDIlib_send_create_t(
        p_ndi_name = name.encode("utf-8"),
        p_groups = None,
        clock_video = clock_video,
        clock_audio = clock_audio
    )
    ndi_sender = NDI.NDIlib_send_create(ctypes.byref(create_desc))
    if not ndi_sender:
        raise SystemError("failed to create NDI sender.")

    return ndi_sender


def destroy_ndi_sender(ndi_send: NDIlib_send_instance_t):
    NDI.NDIlib_send_destroy(ndi_send)


def send_frame(ndi_send: NDIlib_send_instance_t, frame: ArrayLike):
    """
    Send a frame to NDI sender.

    :param ndi_send: NDI sender instance.
    :param frame: (height, width, 3) Frame to send in sRGB.
    """
    height, width = frame.shape[:2]

    data = 255 * numpy.ones((height, width, 4), dtype=numpy.uint8) # RGBA
    data[:, :, :3] = (frame*255).astype(numpy.uint8) # RGB

    frame = NDIlib_video_frame_v2_t(
        xres = width, yres = height,
        FourCC = ord("R") | (ord("G")<<8) | (ord("B")<<16) | (ord("A")<<24), # NDIlib_FourCC_type_RGBA
        frame_rate_N = 60, frame_rate_D = 1, # 60fps
        picture_aspect_ratio = width/height,
        frame_format_type = 1, # NDIlib_frame_format_type_e.progressive
        timecode = (2 ** 63) - 1, # NDIlib_send_timecode_synthesize
        p_data = data.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
        line_stride_in_bytes = 0,
        p_metadata = None,
        timestamp = 0,
    )
    NDI.NDIlib_send_send_video(ndi_send, ctypes.byref(frame))
