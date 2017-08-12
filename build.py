def solution(dic):
    last_index_of_target = None
    if type(dic) is dict:
        a_list = dic.itervalues().next()
    else:
        a_list = dic
    if type(a_list) is list:
        return solution(a_list[-1])

    return a_list


dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
