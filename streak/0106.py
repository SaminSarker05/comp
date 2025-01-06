class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # make two passes to calculate cost of balls on left and right sides
        res = [0] * len(boxes)
        n = len(boxes)
        
        # res[i] = (balls * i) - dist formula to caclulate total # of operations
        # take all balls and multiple by distance to index; then subtract distance already covered
        # if a ball found accumlate its dist and increment count of balls
        balls = 0
        dist = 0
        for i in range(len(boxes)):
            res[i] = (balls * i) - dist
            if boxes[i] == '1':
                balls += 1
                dist += i
        
        balls = 0
        dist = 0
        for i in range(len(boxes) - 1, -1, -1):
            # subtract from length to get dist of ball to index
            res[i] += (balls * (n - i)) - dist
            if boxes[i] == '1':
                balls += 1
                dist += (n - i)
        
        return res

        # INEFFICIENT WAY TO CACLULATE PREFIX AND SUFFIX
        # left pass
        balls = set()   # track indices where ball exists
        for i in range(len(boxes)):
            for j in balls:
                res[i] += (i - j)
            if boxes[i] == '1':
                balls.add(i)
        
        print(res)
        # right pass
        balls = set()
        for i in range(len(boxes) - 1, -1, -1):
            for j in balls:
                res[i] += (j - i)
            if boxes[i] == '1':
                balls.add(i)
        
        # print(right)
 
        return res
