class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        binary = bin(n)[2:]   # convert to binary
        flipped = ""

        for bit in binary:
            if bit == '0':
                flipped += '1'
            else:
                flipped += '0'

        return int(flipped, 2)