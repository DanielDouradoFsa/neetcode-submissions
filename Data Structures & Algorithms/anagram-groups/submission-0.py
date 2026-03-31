class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for word in strs:
            alphabet = [0] * 26
            for letter in word:
                alphabet[ord(letter)-ord("a")] += 1
            print(tuple(alphabet))
            anagrams_dict[tuple(alphabet)].append(word)
        return list(anagrams_dict.values())