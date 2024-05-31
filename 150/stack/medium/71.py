class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = ""
        stack = []
        # 0. base case if length == 1
        if len(path) == 1: 
            if path[0] != "/": return "/" + path
            return path
        
        # 1. clean path by spliting and remove empty spaces
        values = path.split("/")
        values = [val for val in values if val != '']

        # 2. add values to stack; if .. encountered pop from back
        for val in values:
            if val == "..":
                if stack: stack.pop()
                else: continue
            elif val != ".": stack.append(val)
        
        # 3. return combination of values seperated by /
        for val in stack:
            res += ("/" + val)
        
        if res: 
            if res[-1] == "/": return res[:-1]
            else: return res
        return "/"