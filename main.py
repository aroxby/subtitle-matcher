#!/usr/bin/env python3
import os
import sys


def file_ext(file):
    return file.split('.')[-1]

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
    missing_vids = max(len(subs) - len(vids), 0)
    missing_subs = max(len(vids) - len(subs), 0)
    vids += [None] * missing_vids
    subs += [None] * missing_subs

    for i in range(len(vids)):
        print(vids[i], subs[i])


if __name__ == '__main__':
    main(sys.argv)