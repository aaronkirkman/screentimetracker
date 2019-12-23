#!/usr/bin/env python3

import argparse
import ctypes
import logging
import os
import psutil
import time
import Xlib
import Xlib.display


def get_focused_window_process(display):
    root = display.screen().root
    win = root.get_full_property(display.intern_atom("_NET_ACTIVE_WINDOW"), Xlib.X.AnyPropertyType)
    if win is not None:
        win_id = win.value[0]
        win_obj = display.create_resource_object('window', win_id)
        prop = win_obj.get_full_property(display.intern_atom("_NET_WM_PID"), Xlib.X.AnyPropertyType)
        return psutil.Process(prop.value[0]).name() if prop is not None else ""
    return ""


def set_process_name(process_name):
    # https://stackoverflow.com/a/923034
    libc = ctypes.cdll.LoadLibrary('libc.so.6')
    buff = ctypes.create_string_buffer(len(process_name)+1)
    buff.value = process_name.encode("utf-8")
    libc.prctl(15, ctypes.byref(buff), 0, 0, 0)


def main(interval, log_file, process_name):
    set_process_name(process_name)

    display = Xlib.display.Display()

    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(created)f,%(message)s")
    while True:
        logging.info(get_focused_window_process(display))
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--interval", type=int, help="Specify update interval in seconds", default=60)
    parser.add_argument("-", "--logfile", type=str, help="Specify log file location",
                        default=os.path.expanduser("~/.screentime.log"))
    parser.add_argument("-p", "--process", type=str, help="Specify custom process name",
                        default="screentimetracker")
    args = parser.parse_args()
    main(args.interval, args.logfile, args.process)
