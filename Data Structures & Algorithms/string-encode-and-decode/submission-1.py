class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += (str(len(word)) + "#" + word)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            #we have to find the len of the word
            number = ""
            while s[index] != "#":
                number+=s[index]
                index+=1
            index+=1 
            # we arive at the first character of the word
            length = int(number)
            word = ""
            while length:
                word += s[index]
                index+=1
                length -=1
            result.append(word)
        return result






