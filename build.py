def solution(dic):
    last_index_of_target = None
    #temp_list = []

    for value in dic.values():
	if isinstance(value,list):
		temp_list = value
    #print temp_list

    for i in temp_list:
        if isinstance(i,dict):
	    temp_dict = i
    #print temp_dict

    for value in temp_dict.values():
    	if isinstance(value,list):
	    temp_list = value
    #print temp_list

    for i in temp_list:
    	if isinstance(i,dict):
            temp_dict = i
    #print temp_dict

    for value in temp_dict.values():
        if isinstance(value,list):
            temp_list = value
    #print temp_list

    for i in temp_list:
        last_index_of_target = temp_list[len(temp_list)-1]
    return last_index_of_target
    #return last_index_of_target


dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
