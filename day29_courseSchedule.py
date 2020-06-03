# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should
# also have finished course 1. So it is impossible.

import collections
def canFinish(numCourses, prerequisites):
    base_dict = collections.defaultdict(set) # Store base courses for advanced course
    adv_dict = collections.defaultdict(set) # Store advanced courses for base course
    for adv, base in prerequisites:
        base_dict[adv].add(base)
        adv_dict[base].add(adv)

    # Start to learn basest courses
    available_courses = collections.deque(
        [course for course in range(numCourses) if course not in base_dict]
    )

    while available_courses:
        course = available_courses.popleft()
        numCourses -= 1
        for adv in adv_dict[course]:
            base_dict[adv].remove(course)
            if not base_dict[adv]:
                available_courses.append(adv)
    return numCourses == 0


#print(canFinish(6, [[0],[1],[2,0],[3,2],[4],[5, 2],[5,4]]))
print(canFinish(2, [[1,0]]))