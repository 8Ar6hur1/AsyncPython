from time import time

# Round Robin

def gen(s):
    for i in s:
        yield i


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)

        yield pattern.format(str(t))

        sum = 234 + 234
        print(sum)

g = gen_filename()