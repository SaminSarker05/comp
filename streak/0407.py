class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = 0
        # 1. loop while sandwiches exist
        while sandwiches :
            # 2. if number of deques equal to len students then not possible and return len
            if count == len(students):
                return len(students)
            # 3. if matching need remove from stack and queue
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                count = 0
            # 4. else move student to back of queue
            else:
                students.append(students.pop(0))
                count += 1
        
        return len(students)