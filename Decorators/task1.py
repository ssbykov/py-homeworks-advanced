from datetime import datetime

def logger_decor(func):
    def inner(*args, **kwargs):
        with open("file_1.log", "a", encoding='utf-8') as f:
            result = func(*args, **kwargs)
            log_str = f'{datetime.now()} - {func.__name__} - {args} - {kwargs} - {result}\n'
            f.write(log_str)
        return result
    return inner

@logger_decor    
def sum(a, b):
    return a + b

sum(5, 7)