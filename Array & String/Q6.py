# 14. Longest Common Prefix

''' Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. '''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans_string = ""
        L = sorted(strs)
        first = L[0]
        last = L[len(L)-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                break
            ans_string += first[i]
        return ans_string
