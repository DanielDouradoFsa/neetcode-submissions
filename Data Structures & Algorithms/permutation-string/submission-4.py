class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters_and_times_s1 = Counter(s1)
        size = len(s1)
        for l in range(len(s2)-size+1):
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
            if not letters_and_times_copy:
                return True
        return False
                    


        #The substring "cab" is a permutation of "abc" and is present in "lecabee".

        #Discover how to represent an permutation.
        #Ex:abc
        #-abc
        #-acb
        #-bac
        #-bca
        #-cba
        #-cab

        #in any of this cases, has 1A, 1B, 1C


        #example:
        #s1 = "abc", s2 = "lecabee"

        #"lecabee"
        #l can be a permutation of s1? 
            #No because l not in [a:1,b:1,c:1]
        #e can be a permutation of s1? 
            #No because e not in [a:1,b:1,c:1]
        #c can be a permutation of s1? 
            #Yes because c are in [a:1,b:1,c:1]:
            #So, i have to find after c, 1 A or 1B or 1-1C
                #while letters <= 3(1A+1B+1C)
                    #a can be a permutation of s1? 
                    #Yes because a are in [a:1,b:1,c:0]:
                        #continue search
                    #---
                    #b can be a permutation of s1? 
                    #Yes because b are in [a:0,b:1,c:0]:
                        #continue search
                #[a:0,b:0,c:0], has discover that all letters of s2 are in a substring of s1
