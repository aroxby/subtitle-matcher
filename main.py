#!/usr/bin/env python3
import os
import sys


def file_ext(file):
    return file.split('.')[-1]


def change_ext(file, ext):
    parts = file.split('.')
    parts[-1] = ext
    # HACK: drop non-sense things
    parts = [parts[0], parts[-1]]
    return '.'.join(parts)


def main(argv):
    VID_EXTS={'mkv'}
    SUB_EXTS={'srt'}

    vids = []
    subs = []
    files = [dirent.name for dirent in os.scandir(argv[1]) if dirent.is_file()]
    for file in files:
        ext = file_ext(file).lower()
        if ext in VID_EXTS:
            vids.append(file)
        elif ext in SUB_EXTS:
            subs.append(file)

    vids.sort()
    subs.sort()
    assert len(vids) == len(subs)

    for i in range(len(vids)):
        new_vid = change_ext(subs[i], file_ext(vids[i]))
        print(f"mv '{vids[i]}' '{new_vid}'")


if __name__ == '__main__':
    main(sys.argv)