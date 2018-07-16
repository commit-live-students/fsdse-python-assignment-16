def solution(dic):
    last_index_of_target = None
    for key,val in dic.iteritems():
        for indi in val:
            if type(indi) is dict:
                for keyInner,valInner in indi.iteritems():
                    for key,val in valInner[len(valInner)-1].iteritems():
                        last_index_of_target = val[-1]
                        break

    return last_index_of_target


dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
