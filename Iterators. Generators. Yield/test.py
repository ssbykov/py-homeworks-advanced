
# def infinity(start):
#     yield start
#     for x in infinity(start + 1):
#         yield x

# for item in  infinity(0):
#     print(item)

# def star(str_init):
#     if len(str_init) == 2:
#         return str_init[0] + '*' + str_init[1]
#     elif len(str_init) == 1:
#         return str_init
#     else:
#         return str_init[0] + '*' + star(str_init[1:-1]) + '*' + str_init[-1]

# print(star('qwertuiop'))

# def mirr(str_init):
#     if len(str_init) < 1:
#         return ''
#     else:
#         if str_init[0] == '(':
#             return '(' + mirr(str_init[1:]) + ')'
#         else:
#             return str_init[0] + mirr(str_init[1:]) +  str_init[0]
# string = '(((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqo'
# mirr_str = mirr(string)
# if mirr_str == "(((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqooqk))r)m))p)xs))s))imu)d)ktm))))))))y)d))))s))xlm)h)))m)v))e)v))wv)))))))e))))xk))y))p))t)))":
#     print(mirr(mirr_str))

def decorator(func):
    def inner():
        print('Начало...')
        func()
        print('Конец....')
    return inner
    
def say():
    print('Привет!')

d = decorator(say)
d()