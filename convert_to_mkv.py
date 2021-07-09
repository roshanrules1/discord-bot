import ffmpeg
import os


def convert_to_mp4(file_):
    name, ext = os.path.splitext(file_)
    out_name = name + ".mp4"
    ffmpeg.input(file_).output(out_name).run()
    print("Finished converting {}".format(file_))
