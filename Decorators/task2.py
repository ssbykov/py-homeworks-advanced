from datetime import datetime

file_log_path = 'file_2.log'

def logger_decor_path(file_path):
    def logger_decor(func):
        def inner(*args, **kwargs):
            with open(file_path, "a", encoding='utf-8') as f:
                result = func(*args, **kwargs)
                log_str = f'{datetime.now()} - {func.__name__} - {args} - {kwargs} - {result}\n'
                f.write(log_str)
            return result
        return inner
    return logger_decor

@logger_decor_path(file_log_path)
def sum(a, b):
    return a + b

sum(3, 7)
