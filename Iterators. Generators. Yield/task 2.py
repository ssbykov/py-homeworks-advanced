nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(nested_list):
    for n_list in nested_list:
        for n_l in n_list:
            yield n_l

if __name__ == '__main__':
    for item in  flat_generator(nested_list):
        print(item)