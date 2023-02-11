class Codec:
    """
    Design an algorithm to encode a list of strings to a string.
    The encoded string is then sent over the network and is decoded back to the original list of strings.

    Best Case -
    Time complexity is O(n) since we have to traverse through all the elements of the array atleast once

    Sol -
    When encoding the string, we will be adding len of string followed by a delimiter and then the actual string
    """

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # This would get all the element from "i" to "j" excluding "j"
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
