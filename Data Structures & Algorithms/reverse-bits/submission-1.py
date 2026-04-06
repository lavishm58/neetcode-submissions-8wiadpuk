class Solution:
    def reverseBits(self, n: int) -> int:
        # print(n)
        s = ''

        while(n>0):
            s+=str(n%2)
            n = n//2
        s = s[::-1]
        # bits = ''
        # while n > 0:
        #     bits = str(n % 2) + bits
        #     n //= 2 
        # s = bits       
        s = '0'* (32-len(s)) + s
        
        #00000000111001011110000010100101
        #00000010100101000001111010011100
        # print(s)
        num  = 0
        for i, c in enumerate(s):
            num += (2**i)*int(c)

        return num