numbers = [1, [2, 3], [4, [5, 6]]]

result = []

def flatten(data):
    for item in data:
        if isinstance(item, list):
            flatten(item)
        else:
            result.append(item)

flatten(numbers)

print(result)