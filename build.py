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
            if type(dicValue[-1]) == dict:
                for secondKey in dicValue[-1]:
                    secondDicValue = dicValue[-1]
                    if type(secondDicValue[secondKey]) == list:
                        secondList = secondDicValue[secondKey]
                        if type(secondList[-1]) == dict:
                            for thirdKey in secondList[-1]:
                                thirdDicValue = secondList[-1]
                                thirdList = thirdDicValue[thirdKey]
                                last_index_of_target = thirdList[-1]
                                break
                    break
            break

        else:
            print type(dic[key])
    return last_index_of_target




dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
solution(dic)
