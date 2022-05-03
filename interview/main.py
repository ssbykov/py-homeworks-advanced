class Stack():
    def __init__(self):
        self.stack_buffer = []

    def isempty(self):
        if self.stack_buffer:
            return False
        else:
            return True

    def push(self, el):
        self.stack_buffer.append(el)

    def pop(self):
        if len(self.stack_buffer):
            self.stack_buffer.pop(-1)

    def peek(self):
        if len(self.stack_buffer):
            return self.stack_buffer[-1]

    def size (self):
        return len(self.stack_buffer)


if __name__ == '__main__':
    bracket = Stack()
    str_bracket = input('Введите последовательность скобок: ')
    dict_bracket = {'(': ')', '[': ']', '{': '}'}
    for br in str_bracket:
        if br in dict_bracket:
            bracket.push(br)
        elif not bracket.peek():
            bracket.push(br)
            break
        elif dict_bracket[bracket.peek()] == br and bracket.size():
            bracket.pop()
        else:
            break
    if bracket.isempty():
        print('Последовательность сбалансированна.')
    else:
        print('Последовательность несбалансированна.')
