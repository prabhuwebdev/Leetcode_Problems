class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_String=""
        List=s.split()
        for i,j in enumerate(List):
            reversed_String+=j[::-1]
            if i != len(List)-1:
                reversed_String+=" "
            

        return reversed_String
        