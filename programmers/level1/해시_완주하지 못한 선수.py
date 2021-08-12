def solution(participant, completion):
    answer = {}
    for i in participant:
        answer[i] = answer.get(i, 0) + 1

    for j in completion:
        answer[j] -= 1

    for k in answer:
        if answer[k]:
            return k

def solution_new(participant, completion):
    answer = {}
    set_person = set(participant) - set(completion)

    return set_person.pop()


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))
print(solution_new(participant, completion))
