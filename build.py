def solution(dic):
    l1 = dic.values()
    print l1[0]
    l2 = l1[0][3]
    l3 = l2.values()
    l4 = l3[0]
    l5 = l4[3].values()
    l6 = l5[0]
    l7 = l6[3]
    print l7
    return l7


dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
