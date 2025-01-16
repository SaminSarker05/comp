class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # bin() converts to binary with 0b prefix
        # .bit_count() returns # of set bits (1s) in number
        # XOR between two numbers is minimized when their binary representations are similar

        bits = 0
        # .bit_count() also works
        while num2:
            bits += (num2 & 1)
            num2 = num2 >> 1
        
        res = 0
        for i in range(31, -1, -1): # 32 bits [0, 31]
            if bits and num1 & (1 << i):    # most sig matters more since contributes larger to xor val
                res |= (1 << i)
                bits -= 1
        
        for i in range(32):  # add more if needed starting from least significant bit
            if bits and not (res & (1 << i)):    # if not already on then turn on
                res |= (1 << i)
                bits -= 1

        return res 

        # integers are 4 bytes (each 8 bits) = 32 bits in total
        bits = num2.bit_count()
        res = 0
        for i in range(31, -1, -1):
            if bits and num1 & (1 << i):    # start with most sig bit; if turned on then add to res
                res |= (1 << i)
                bits -= 1
        
        # if still need to turn on bits; start from least significant --> less xor contribution
        for i in range(32):
            if bits and not (res & (1 << i)):   # if not on then turn on
                res |= (1 << i)     # use or to add bit value
                bits -= 1
        
        return res





        change = num1.bit_count() - num2.bit_count()    # built in function

        # adjust set bits to be same # as num2 but as close to num1 as possible

        if change == 0: return num1 # minimize or 0 when same number
        
        if change > 0:
            # need to turn off some 1s; to minimize start with least significant; contributes less
            pass
            
        else:
            # add 1s starting from 
            res = num1
            for _ in range(-change):
                num1 |= num1 + 1
        
        return num1
        



        bits = 0
        while num2:
            bits += (num2 & 1)
            num2 = num2 >> 1
        
        binary = []
        while num1:
            binary.append(num1 & 1)
            num1 = num1 >> 1
        
        res = 0
        count = 0
        for i in range(len(binary)):
            if bits and binary[i] == 1:
                res += (2 ** i)
                bits -= 1
                count += 1
        
        if bits:
            remain = len(binary) - count
            bits -= remain
            i = len(binary)
            while bits:
                res += (2 ** i)
                bits -= 1
                i += 1

        return res 

        
        # xor; want to match identical 1s to minimize

        
