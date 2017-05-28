def solution(dic):
    last_index_of_target = None
    counter = 0
    '''
    Enter your code here
    '''
    #lenKey = len(dic.keys())

    for key in dic:
        #print dic[key]
        if type(dic[key]) == list:
            dicValue = dic[key]
            for listValue in dicValue:
                if type(listValue) == dict:
                    for secondKey in listValue:
                        if type(listValue[secondKey]) == list:
                            for secondList in listValue[secondKey]:
                                if type(secondList) == dict:
                                    for thirdKey in secondList:
                                        if type(secondList[thirdKey]) == list:
                                            thirdList = secondList[thirdKey]
                                            last_index_of_target = thirdList[-1]
                                            break
                                    break
                            break
                    break
            break
        else:
            print type(dic[key])
    return last_index_of_target




dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
solution(dic)
