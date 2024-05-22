class Solution(object):
    def openLock(self, deadends, target):
        q = deque()
        q.append(("0000"), 0)
        seen = set()
        while q:
            string, depth = q.popleft()
            if string == target:
                return depth
            if string not in deadends:
                for i in range(4):
                    digit = string[i]
                    for direction in [-1, 1]:
                        new_d = (int(digit) + direction) % 10
                        new_s = string[:i] + str(new_d) + string[i+1:]
                        if new_s not in seen:
                            q.append((new_s, depth + 1))
          
        return -1
