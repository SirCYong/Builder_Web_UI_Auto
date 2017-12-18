import random

# b = '0',  '1'
#
# print(random.sample(b, 1))
# print(type(random.sample(b, 1)))
# a = random.sample(b, 1)
a = random.randint(0, 1)


def test(switch):
    print(type(switch))
    if switch:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    test(a)