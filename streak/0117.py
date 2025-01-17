class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
            properties of xor:
                - commutative axorb == bxora
                - associative
                - identity axor0 = a
                - self-inverse axora = 0
                - inverse
                    if axorb = c then  
                        bxorc = a
                        cxora = b
        """

        # use inversion property of xor
        # derived[i]=original[i]XORoriginal[i+1]
        # original[i+1]=derived[i]XORoriginal[i]

        # first element of original can be 0 or 1; try both
        original = [0 for i in range(len(derived))]
        for i in range(len(derived)):
            if i == len(derived) - 1:
                # check circular condition
                if original[i] == derived[i] ^ original[0]: return True
            else: original[i + 1] = derived[i] ^ original[i]
        
        # try with 1 being first number in original
        original = [1 for i in range(len(derived))]
        for i in range(len(derived)):
            if i == len(derived) - 1:
                # check circular condition
                if original[i] == derived[i] ^ original[0]: return True
            else: original[i + 1] = derived[i] ^ original[i]
        
        # if not possible return false
        return False



        
