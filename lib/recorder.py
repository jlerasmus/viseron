import datetime
import logging
import os
import subprocess as sp
from queue import Empty

LOGGER = logging.getLogger(__name__)


class FFMPEGRecorder:
    def __init__(self, config, frame_buffer):
        LOGGER.info("Initializing ffmpeg recorder")
        self.config = config
        self.is_recording = False
        self.writer_pipe = None
        self.frame_buffer = frame_buffer

    def write_frames(self, file_name, width, height, fps):
        # fmt: off
        command = ['/root/bin/ffmpeg',
                   '-loglevel', 'panic',
                   '-hwaccel', 'vaapi', '-vaapi_device', '/dev/dri/renderD128',
                   '-threads', '8',
                   '-y',
                   '-f', 'rawvideo', '-pix_fmt', 'nv12', '-s:v',
                   f'{width}x{height}',
                   '-r', str(fps), '-i', 'pipe:0',
                   '-an',
                   '-movflags', '+faststart',
                   '-vf', 'format=nv12|vaapi,hwupload',
                   '-vcodec', 'h264_vaapi',
                   '-qp', '19', '-bf', '2',
                   file_name]
        # fmt: on
        LOGGER.debug(f"FFMPEG command: {' '.join(command)}")
        LOGGER.debug(f"Filename: {file_name}")

        writer_pipe = sp.Popen(
            command, stdin=sp.PIPE, bufsize=int(width * height * 1.5)
        )

        while self.is_recording:
            try:
                frame = self.frame_buffer.get(timeout=1)
                # LOGGER.debug(f"Writing frame of size {sys.getsizeof(frame)} to file.")
                writer_pipe.stdin.write(frame["frame"])
            except Empty:
                LOGGER.error("Timed out")

        writer_pipe.stdin.close()
        writer_pipe.wait()
        LOGGER.info("FFMPEG recorder stopped")

    def subfolder_name(self, today):
        return f"{today.year:04}-{today.month:02}-{today.day:02}"

    def start_recording(self, width, height, fps):
        LOGGER.info("Starting recorder")
        self.is_recording = True

        if self.config.recorder.folder is None:
            LOGGER.error("Output directory is not specified")
            return

        # Create filename
        now = datetime.datetime.now()
        file_name = f"{now.strftime('%H:%M:%S')}.{self.config.recorder.extension}"

        # Create foldername
        subfolder = self.subfolder_name(now)
        full_path = os.path.normpath(
            os.path.join(self.config.recorder.folder, f"./{subfolder}")
        )
        try:
            if not os.path.isdir(full_path):
                LOGGER.info(f"Creating folder {full_path}")
                os.makedirs(full_path)
            else:
                LOGGER.info("Folder already exists")
        except FileExistsError:
            LOGGER.error("Folder already exists")

        self.write_frames(os.path.join(full_path, file_name), width, height, fps)

    def stop(self):
        LOGGER.info("Stopping recorder")
        self.is_recording = False
        return
