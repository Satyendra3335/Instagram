def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

nested_list = [1, ['hello', [3, 'world'], 'python'], [42, ['GPT']]]

flat = flatten_list(nested_list)

count = 0
for item in flat:
    if type(item) is str:
        count=count+1
        

print( flat)
print( count)
