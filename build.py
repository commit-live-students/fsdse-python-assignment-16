def solution(dic):
    '''
    Enter your code here
    '''
    if 'target' in dic:
        return dic['target'][-1]
    for key in dic:
        if isinstance(dic[key], list):
            for item in dic[key]:
                if isinstance(item, dict):
                    return solution(item)


dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
