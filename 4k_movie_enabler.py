import os
import sys

if len(sys.argv) < 2:
    print("4k_movie_enabler.py" + ": Usage is " + "4k_movie_enabler.py" + " \"<ff_xv_root>\"")
    sys.exit(1)

FFXV_MOVIE_PATH = os.path.join(sys.argv[1], "datas", "movie")
FFXV_MOVIE_EXTENSION = ".bk2"

for root, dirs, files in os.walk(FFXV_MOVIE_PATH):
    if not files:
        continue
    for f in files:
        name, ext = os.path.splitext(f)

        if ext == FFXV_MOVIE_EXTENSION:
            # We should find the equivalent file without 4k.
            # 2 cases: either the name it's the same but without "4k", or "4k" gets replaced by "pc"
            hd_index = name.find("4k")
            if hd_index == -1:
                continue
            else:
                with_pc = os.path.join(root, name[ : hd_index] + "pc" + ext)
                without_pc = os.path.join(root, name[ : hd_index - 1] + ext)
                hd_file = os.path.join(root, f)

                if os.path.exists(with_pc):
                    os.rename(with_pc, with_pc + ".back")
                    os.rename(hd_file, with_pc)
                elif os.path.exists(without_pc):
                    os.rename(without_pc, without_pc + ".back")
                    os.rename(hd_file, without_pc)
