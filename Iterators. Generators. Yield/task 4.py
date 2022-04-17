nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[[1, 2, None, [12, 13]], [16, 17]], 2
]

def flat_list(nested_list, new_list):
    for el in nested_list:
        if isinstance(el, list):
            flat_list(el, new_list)
        else:
            new_list.append(el)
    return new_list

def flat_generator(nested_list):
    nested_list = flat_list(nested_list, [])
    for n_list in nested_list:
        yield n_list

if __name__ == '__main__':
    for item in  flat_generator(nested_list):
        print(item)