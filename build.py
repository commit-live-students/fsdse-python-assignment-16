def solution(dic):
    last_index_of_target = None
    '''
    Enter your code here
    '''
    find = list(dic.values())
    for i in find[0]:
	if type(i) == dict:
		x = list(i.values())
		for i2 in x[0]:
			if type(i2) == dict:
				x2 = list(i2.values())
				return x2[0][-1]



dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
