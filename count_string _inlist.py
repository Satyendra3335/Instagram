
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
            return result
    for item in flatten_list:
        count=0
        if item is str:
            count=count+1
    return count

        
nested_list = [1, ['hello', [3, 'world'], 'python'], [42, ['GPT']]]
print(flatten_list(nested_list))

