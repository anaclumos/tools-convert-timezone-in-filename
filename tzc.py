#!/usr/bin/env python

import sys
import os
import datetime
import pathlib
from pytz import timezone

tzlong = "Asia/Seoul"
tz = "KST"


class termcolor:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def convertTimeZone(file_name, date_format="%y%m%d %H%M%S"):
    name = file_name
    date, time, *rest = name.split()
    datetime_obj = datetime.datetime.strptime(date + " " + time, "%y%m%d %H%M%S")
    datetime_obj_utc = datetime_obj.replace(tzinfo=timezone("UTC"))
    return (
        datetime_obj_utc.astimezone(timezone(tzlong)).strftime(date_format)
        + " "
        + tz
        + " "
        + " ".join(str(x) for x in rest)
    )


def run():
    for file in sys.argv[1:]:
        normalized_path = os.path.abspath(file)
        if not pathlib.Path(normalized_path).exists():
            print(termcolor.FAIL + "× " + termcolor.ENDC + normalized_path)
            continue
        basename = os.path.basename(normalized_path)
        dirname = os.path.dirname(normalized_path)
        timestamped_name = convertTimeZone(basename)
        print(
            termcolor.OKGREEN
            + "✓ "
            + termcolor.ENDC
            + dirname
            + "/"
            + termcolor.OKGREEN
            + timestamped_name
            + termcolor.ENDC
        )
        os.rename(normalized_path, dirname + "/" + timestamped_name)
