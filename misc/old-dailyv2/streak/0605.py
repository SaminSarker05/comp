class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        # 0. base case
        if len(hand) % groupSize != 0: return False
        # 1. make hashmap of freq
        freq = Counter(hand)

        # 2. go through keys of freq
        for key in sorted(freq.keys()):
            # 3. if key exists then see if hand can be made of len groupsize
            if freq[key] > 0:
                # 4. freq of next key must be >= curr to make valid hands
                for i in range(1, groupSize):
                    if freq[key + i] < freq[key]: return False
                    freq[key + i] -= freq[key]  # update freq of hand
        # 5. if everything words return True
        return True
        

        # NAIVE APPROACH
        # 0. base case
        if len(hand) % groupSize != 0: return False
        # 1. sort hand 
        hand.sort()

        # 2. nested for loop to see if consecutive groupings exists
        for i in range(len(hand)):
            # 3. use None to mark used values
            if hand[i] != None:
                curr = hand[i]
                k = groupSize - 1
                # 4. nest for loop to search for hand
                for j in range(i + 1, len(hand)):
                    if k == 0: break
                    if hand[j] == curr + 1:
                        curr = hand[j]
                        hand[j] = None
                        k -= 1
                # 5. if hand incomplete then return False
                if k != 0: return False
        
        return True



        
