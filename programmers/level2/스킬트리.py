def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)

    for tree in skill_trees:
        for s in skill_list:
            skill_idx = tree.find(s)
            tree = tree[:skill_idx + 1] + tree[skill_idx + 1:].replace(s, '')

        skill_list2 = skill_list
        for t in list(tree):
            if t in skill_list:
                if t in skill_list2 and skill_list2.index(t) == 0:
                    skill_list2 = skill_list2[1:]
                else:
                    break
            else:
                continue
        else:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
