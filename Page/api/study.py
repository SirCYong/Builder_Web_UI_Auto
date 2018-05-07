import os


def find_min_and_max(*arge):
    if len(arge[0]) is 0:
        return (None, None)
    else:
        for number in arge:
            min_number = min(number)
            max_number = max(number)
            return (min_number, max_number)

    # return (max(arge), min(arge))
def fib(max):
    n, a, b = 1, 0, 1
    while n < max+1:
        print('a', a)
        print('b', b)
        print('n', n)
        a, b = b, a + b
        n = n + 1
    return 'done'

if __name__ == '__main__':
    fib(6)
    # number_list = [1, 2, 3, 4, 5, 11]
    # number_list = [4]
    # print(find_min_and_max(number_list))
    #
    # print([m + n for m in 'abc' for n in 'zxc'])
    # print([d for d in os.listdir('.')])
    my_list = ['Hello', 'World', 18, 'Apple', None]
    print([s.lower() for s in my_list if isinstance(s, str)])
    # for s in my_list:
    #     if isinstance(s, str):
    #         print(s.lower())
    #     else:
    #         continue
