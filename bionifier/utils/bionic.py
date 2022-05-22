from bionifier.utils.color import Color
import textwrap

# Edge Case: Does not account for hyphenated phrases.
# TODO: Fix 1 letter edge case.


class BionicCheaper:
    SAMPLE = "Bionic Reading is a new method facilitating the reading process by guiding the eyes through text with artificial fixation points. As a result, the reader is only focusing on the highlighted initial letters and lets the brain center complete the word. In a digital word dominated by shallow forms of reading, Bionic Reading aims to encourage a more in-depth reading and understanding of written content."

    @staticmethod
    def sample(_debug=False):
        if _debug:
            bc = BionicCheaper(BionicCheaper.SAMPLE, "{", "}")
        else:
            bc = BionicCheaper(BionicCheaper.SAMPLE, Color.BOLD.value, Color.END.value)

        return tuple((bc.og_text, bc.bc_text))

    def __init__(self, og_text, left=Color.BOLD.value, right=Color.END.value):
        self._og_text = og_text if og_text else BionicCheaper.SAMPLE
        self._left = left
        self._right = right
        self._bc_text = self.bionify()

    @property
    def og_text(self):
        return self._og_text

    @og_text.setter
    def og_text(self, og_text):
        self._og_text = og_text if og_text else BionicCheaper.SAMPLE
        self._bc_text = self.bionify()

    @property
    def bc_text(self):
        return self._bc_text

    def bionify(self):
        lines = self._og_text.split("\n")

        for i, line in enumerate(lines):
            words = line.split(" ")

            for j, word in enumerate(words):
                w_len = sum(map(str.isalnum, word))

                if w_len <= 3:
                    words[j] = self._left + word[0] + self._right + word[1:]
                    continue

                mid = w_len // 2 + (0 if w_len % 2 == 0 else 1)
                ptr = 0

                for c in word:
                    if mid > 0:
                        mid -= c.isalnum()
                    else:
                        words[j] = self._left + word[:ptr] + self._right + word[ptr:]
                        break

                    ptr += 1

            lines[i] = " ".join(words)

        return "\n".join(lines)

    def __str__(self):
        return self._bc_text
