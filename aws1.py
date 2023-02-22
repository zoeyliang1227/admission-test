def count(input):   
    dict={}
    for i in input:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

def group_by_key(input):
    dict={}
    for i in input:
        if i['key'] in dict:
            dict[i['key']] += i['value']
        else:
            dict[i['key']] = i['value']

    return dict        

input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}