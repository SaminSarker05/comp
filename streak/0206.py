class Solution:
    def minimumDeletions(self, s: str) -> int:

        # we can't have an A appear after a B
        # can't have Bs until As seen
        # make optimal choice per char not blocks --> more complex logic
        # stack not needed just track freq of B

        # greedy choice when an A is seen
        # either delete the A, adding one remove operation OR delete all prev B
        # remove operations will always be minimum of two choices

        b_freq = 0
        removes = 0
        for c in s:
            if c == "b":
                b_freq += 1
            else:
                removes = min(removes + 1, b_freq)
            
        return removes




        # we can't have an A appear after a B
        # can't have Bs until As seen

        # aababbab
        # aaaabbbb

        # bbaaaaabb
        # aaaaabbbb


        # entire sequence of a is ok
        # stack only tracking b's
        # only invalid bs can invalide us
        # either remove b or a, remove whichver is less

        def dfs(i, Bs):
            if i == len(s):
                return 0
            removes = 0
            if s[i] == "b":
                return dfs(i + 1, Bs + 1)
            
            if s[i] == "a" and Bs != 0:
                j = i
                while j < len(s) and s[j] == "a":
                    j += 1
                freq_a = j - i

                removeB = Bs + dfs(i + 1, 0)
                removeA = freq_a + dfs(i + 1, Bs)

                return min(removeA, removeB)
            
            return dfs(i + 1, Bs)

        return dfs(0, 0)


        # entire sequence of a is ok
        # stack only tracking b's
        # only invalid bs can invalide us
        # either remove b or a, remove whichver is less


        removes = 0
        stack = []
        for i in range(len(s)):
            if s[i] == "b":
                stack.append(i)
            elif s[i] == "a" and len(stack) != 0:
                j = i
                while j < len(s) and s[j] == "a":
                    j += 1
                freq_a = j - i
                if len(stack) < freq_a:
                    removes += len(stack)
                    stack = []
                else:
                    removes += freq_a

        
        return removes










        
