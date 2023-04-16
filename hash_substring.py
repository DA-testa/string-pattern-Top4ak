# 13.grupa 221RDB014

class RabinKarpSearch:

    def __init__(self, ag=256, q=101):
        self.ag = ag
        self.q = q

    def read_input(self):
        ievade = input()

        if "F" in ievade:
            Fails = 'tests/06'
            with open(Fails, 'r') as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()

        elif "I" in ievade:
            pattern = input().rstrip()
            text = input().rstrip()

        return pattern, text

    def print_occurrences(self, output):
        print(' '.join(str(x) for x in output))

    def get_occurrences(self, pattern, text):
        pg = len(pattern)
        tg = len(text)

        indeks = []
        p_hash = 0
        t_hash = 0
        h = 1

        for i in range(pg - 1):
            h = (h * self.ag) % self.q

        for i in range(pg):
            p_hash = (self.ag * p_hash + ord(pattern[i])) % self.q
            t_hash = (self.ag * t_hash + ord(text[i])) % self.q

        for i in range(tg - pg + 1):
            if p_hash == t_hash:
                if pattern == text[i:i + pg]:
                    indeks.append(i)

            if i < tg - pg:
                t_hash = (self.ag * (t_hash - ord(text[i]) * h) + ord(text[i + pg])) % self.q
                t_hash = (t_hash + self.q) % self.q

        return indeks


if __name__ == '__main__':
    rabin_karp_search = RabinKarpSearch()
    rabin_karp_search.print_occurrences(rabin_karp_search.get_occurrences(*rabin_karp_search.read_input()))
