import logging
from Page.web.get_now_time import get_now_dates

logging.basicConfig(filename='logger.log', level=logging.INFO)


def bar(func):
    func()


def use_logging(leavel):
    def dec(func):

        def wrapper(*args, **inf):  # *arge  表list ** 是支持的元组
            print(1111)
            if leavel == 'warn':
                logging.warn("%s is running" % func.__name__)  # 函数名字
                print(leavel, func.__name__)
            elif leavel == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args, **inf)
        print(22222, func.__name__, 3333)
        return wrapper
    print(44444)
    return dec


@use_logging(leavel='warn')
def foo(name, hh, age=None):
    print("%s is name time is %s age = %s %s" % (name, get_now_dates(), age, hh))

if __name__ == '__main__':
    # foo = use_logging('warn')(foo)
    print(1)
    print(foo.__name__)
    print(2)

    foo('cy', '12',{'age':'13'})  # age{'age':'13'} == age='13'