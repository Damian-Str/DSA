class Solution:
    # doesnt work
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     shortest_word_len = len(min(strs, key=len))
    #     lcp = ""

    #     for letter in range(shortest_word_len):        
    #         for word in strs:
    #             if lcp == "" or letter > len(lcp):
    #                 lcp += word[letter]
    #             elif word[letter] == lcp[-1]:
    #                 continue
    #             else:
    #                 break
    #     return lcp

    # # fixed
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if not strs:
    #         return ""

    #     shortest_word_len = len(min(strs, key=len))
        # lcp = ""

    #     for i in range(shortest_word_len):
    #         current_char = strs[0][i]

    #         for word in strs:
    #             if word[i] != current_char:
    #                 return lcp

    #         lcp += current_char

    #     return lcp

    # gpt
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]

        