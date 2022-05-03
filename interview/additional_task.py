a = [2, 7, 11, 15]
b = 17

def chech_list(a, b):
    for i in range(len(a)):
        for j, _ in enumerate(a[i + 1:]):
            if a[i] + _ == b:
                return [i, i +j +1]

print(chech_list(a, b))
