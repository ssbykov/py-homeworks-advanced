nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[[1, 2, None, [12, 13]], [16, 17]], 2
]

class FlatIterator:
    def __init__(self, values):
        self.values = values

    def __iter__(self):
        self.new_list = self._flat_iterator(self.values)
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor == len(self.new_list):
            raise StopIteration
        self.el = self.new_list[self.cursor]
        self.cursor += 1        
        return self.el

    def _flat_iterator(self, nested_list):
        for el in nested_list:
            if isinstance(el, list):
                ind = nested_list.index(el) 
                nested_list = nested_list[:ind] + nested_list[ind] + nested_list[ind + 1:] 
                return self._flat_iterator(nested_list)
        return nested_list

if __name__ == '__main__':
    for _ in FlatIterator(nested_list):
        print(_)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    