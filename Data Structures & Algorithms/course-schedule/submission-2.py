class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requires = defaultdict(list)
        memo = defaultdict(list)

        for p in prerequisites:
            requires[p[0]].append(p[1])

        for c in range(numCourses):
            _, cycle = self.get_all_prereq(c, requires, memo, [])
            if cycle:
                return False

        return True

    def get_all_prereq(self, course_id, requires, memo, path):
        if course_id in path:
            return [], True

        if course_id in memo:
            return memo[course_id], False

        if not requires[course_id]:
            memo[course_id] = []
            return [], False

        req = []
        req.extend(requires[course_id])

        for c in requires[course_id]:
            r, cycle = self.get_all_prereq(c, requires, memo, [*path, course_id])
            if cycle:
                return req, True
            memo[c] = r
            req.extend(r)

        return req, False
