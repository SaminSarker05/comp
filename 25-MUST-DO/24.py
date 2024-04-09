class Solution(object):
    def permute(self, nums):
      # backtracking problem

      k = len(nums)
      res = []

      def backtrack(curr):
        # 1. if len of array equal to len of desired return and add to res
        if len(curr) == k:
          # 2. return splice to get a copy of list; otherwise data lost
          res.append(curr[:])
          return 
        # 3. loop through nums add add to curr if not matching len
        for val in nums:
          # 4. only add elem if unique
          if val not in curr:
            curr.append(val)
            backtrack(curr)
            # 5. remove elem to backtrack
            curr.pop()
      
      backtrack([])
      return res



      