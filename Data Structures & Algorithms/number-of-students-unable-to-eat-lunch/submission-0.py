class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)

        for sd in sandwiches:
            if counter[sd] == 0:
                break
            counter[sd] -= 1

        return counter[0] + counter[1]