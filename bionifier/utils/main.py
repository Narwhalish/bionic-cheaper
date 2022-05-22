from bionic import BionicCheaper
import os, textwrap

INPUT_DIR = "input"
OUTPUT_DIR = "output"

if __name__ == "__main__":
    for filename in os.listdir(INPUT_DIR):
        if os.path.isfile(os.path.join(INPUT_DIR, filename)):
            with open(os.path.join(INPUT_DIR, filename), "r") as fi, open(
                os.path.join(OUTPUT_DIR, filename), "w+"
            ) as fo:
                bc = BionicCheaper(fi.read())
                fo.write(str(bc))
                print(bc)
