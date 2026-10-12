class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_string = ""

        if not strs :
            return "@:null:@"

        for i in range(0, len(strs)):
            encode_string = encode_string + strs[i] + ':;'

        return encode_string[:-2]

    def decode(self, s: str) -> List[str]: 
        if s == "@:null:@":
            return []
        
        return s.split(":;")
