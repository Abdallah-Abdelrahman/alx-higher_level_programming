#!/usr/bin/python3

def best_score(a_dictionary):
    _max = {'name': '', 'score': 0}

    if a_dictionary is None:
        return None
    for k, v in a_dictionary:
        if _max['score'] < a_dictionary[k]:
            _max['name'] = k
            _max['score'] = v
    return _max['name']
