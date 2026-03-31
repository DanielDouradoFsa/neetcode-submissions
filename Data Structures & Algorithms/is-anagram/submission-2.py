class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters_count_s = {}
        letters_count_t = {}
        for i in range(len(s)):
            current_letter_s = s[i]
            current_letter_t = t[i]
            letters_count_s[current_letter_s] = 1 + letters_count_s.get(current_letter_s, 0)
            letters_count_t[current_letter_t] = 1 + letters_count_t.get(current_letter_t, 0)

        for key in letters_count_s:
            if letters_count_s[key] != letters_count_t.get(key):
                return False

        return True