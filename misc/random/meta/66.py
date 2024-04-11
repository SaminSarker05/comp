class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        temp = digits[::-1]

        remainder = 1
        for i in range(len(temp)):
            total = temp[i] + remainder
            if total >= 10:
                temp[i] = total % 10
            else:
                temp[i] = total
                remainder = 0
        
        if remainder:
            temp.append(1)
        
        return temp[::-1]