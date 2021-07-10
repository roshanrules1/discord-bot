from subprocess import check_output
from json import loads


def format_check(url):
    reply = check_output(["youtube-dl", url, "--skip-download", "-j"])
    formats = loads(reply)["formats"]
    useable_formats = []
    for format_dict in formats:

        if (
            format_dict["filesize"] is not None
            and int(format_dict["filesize"]) < 8000000
            and format_dict["acodec"] != "none"
            and format_dict["vcodec"] != "none"
        ):
            useable_formats.append(
                {"format_id": format_dict["format_id"], "height": format_dict["height"]}
            )
    try:
        return max(useable_formats, key=lambda fd: int(fd["height"]))["format_id"]
    except:
        return "Big"


def audio_format(url):
    reply = check_output(["youtube-dl", url, "--skip-download", "-j"])
    formats = loads(reply)["formats"]
    for format_dict in formats:

        if (
            format_dict["filesize"] is not None
            and int(format_dict["filesize"]) < 8000000
            and format_dict["acodec"] != "none"
        ):
            return format_dict["format_id"]
        else:
            return "Big"
