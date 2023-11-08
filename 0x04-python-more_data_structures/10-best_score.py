#!/usr/bin/python3

def best_score(a_dictionary):
    _max = {'name': '', 'score': 0}

    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        if _max['score'] < a_dictionary[k]:
            _max['name'] = k
            _max['score'] = v

    return _max['name']
