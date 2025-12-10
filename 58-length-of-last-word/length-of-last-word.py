class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Splited=s.split()
        return len(Splited[-1])
        