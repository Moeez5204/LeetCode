class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        Tree = {i: [] for i in range(numCourses)}
        for course, prerequisites in prerequisites:
            Tree[course].append(prerequisites)

        visit = set()

        def dfs(crs):

            if Tree[prerequisites] == []:
                return True

            if course in visit:
                return False

            visit.add(course)

            for number in Tree[course]:
                if not dfs(number):
                    return False

            visit.remove(course)

            Tree[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True