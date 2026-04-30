class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requires = defaultdict(list)
        wanted_by = {i: [] for i in range(numCourses)}
        memo = defaultdict(list)

        for p in prerequisites:
            requires[p[0]].append(p[1])
            wanted_by[p[1]].append(p[0])
        
        q = deque()
        for c in range(numCourses):
            if not wanted_by[c]:
                q.append(c)
        
        if not q:
            return False
        
        visited = set()

        while q:
            c = q.popleft()

            if not wanted_by[c]:
                visited.add(c)
                for s in requires[c]:
                    if c in wanted_by[s]:
                        wanted_by[s].remove(c)
                        q.append(s)
        
        return len(visited) == numCourses
