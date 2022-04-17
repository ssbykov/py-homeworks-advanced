nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[[1, 2, None, [12, 13]], [16, 17]], 2
]

def flat_generator(nested_list):
    for el in nested_list:
        if isinstance(el, list):
            yield from flat_generator(el)
        else:
            yield el

if __name__ == '__main__':
    for item in  flat_generator(nested_list):
        print(item)