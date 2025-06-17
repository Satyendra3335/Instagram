def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

nested_list = [1, ['hello', [3.5, 'world'], 'python'], [42, ['GPT']]]

# First flatten the list
flat = flatten_list(nested_list)

# Then count string items
count = 0  
for item in flat:
    if isinstance(item, int):
        count += 1
    elif isinstance(item, float):
        count += 1

print("Flattened List:", flat)
print("Number of strings:", count)
