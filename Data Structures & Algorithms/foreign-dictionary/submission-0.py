class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        state = {}  # 1=visiting, 2=done
        result = []

        def dfs(c) -> bool:
            if c in state:
                return state[c] == 2
            state[c] = 1
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            state[c] = 2
            result.append(c)
            return True

        for c in adj:
            if not dfs(c):
                return ""

        return "".join(reversed(result))