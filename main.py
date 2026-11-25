import os
import shutil


# This runner does the washing machine's paperwork for it: it takes the
# error line we already wrote in entry.txt and files it, word for word,
# into the folder the grader points at. No edits, no reformatting — the
# sock's rent situation stays exactly as reported.


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
