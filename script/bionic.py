from color import Color
import string

# Edge Case: Does not account for hyphenated phrases.


class BionicCheaper:
    def __init__(self, og_text):
        self._og_text = og_text
        self._bc_text = self.bionify()

    @property
    def og_text(self):
        return self._og_text

    @og_text.setter
    def og_text(self, og_text):
        self._og_text = og_text
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
                mid = w_len // 2 + (0 if w_len % 2 == 0 else 1)
                ptr = 0

                for c in word:
                    if mid > 0:
                        mid -= c.isalnum()
                    else:
                        words[j] = (
                            Color.BOLD.value + word[:ptr] + Color.END.value + word[ptr:]
                        )
                        break

                    ptr += 1

            lines[i] = " ".join(words)

        return "\n".join(lines)

    def debug(self):
        lines = self._og_text.split("\n")

        for i, line in enumerate(lines):
            words = line.split(" ")

            for j, word in enumerate(words):
                w_len = sum(map(str.isalnum, word))
                mid = w_len // 2 + (0 if w_len % 2 == 0 else 1)
                ptr = 0

                for c in word:
                    if mid > 0:
                        mid -= c.isalnum()
                    else:
                        words[j] = "{" + word[:ptr] + "}" + word[ptr:]
                        break

                    ptr += 1

            lines[i] = " ".join(words)

        return "\n".join(lines)

    def __str__(self):
        return self._bc_text
