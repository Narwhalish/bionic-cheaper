from bionic import BionicCheaper
import os, textwrap

if __name__ == "__main__":
    bc = BionicCheaper.sample(_debug=False)
    print(*bc, sep="\n")
