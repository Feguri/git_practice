class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack != haystack.lower():
            return 0
        if not 0 <= len(haystack) and len(needle) <= 5 * 10**4 and needle != '':
            return 0
        return haystack.find(needle) 
        