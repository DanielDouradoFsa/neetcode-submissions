class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters_and_times_s1 = Counter(s1)
        size = len(s1)

        for l in range(len(s2) - size + 1):
            letters_and_times_copy = letters_and_times_s1.copy()
            r = l

            while r < l + size:
                char = s2[r]

                if char not in letters_and_times_copy:
                    break

                letters_and_times_copy[char] -= 1
                if letters_and_times_copy[char] == 0:
                    del letters_and_times_copy[char]

                r += 1

            if not letters_and_times_copy and r == l + size:
                return True

        return False