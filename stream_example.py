"""

Stream to functions

"""
from os import listdir


def read_file(arq):
    with open(arq) as _file:
        return _file.read()


def double(vals):
    return [x*2 for x in vals]


def concat(vals):
    return ''.join([read_file(val) for val in vals])


class Stream:
    def __init__(self):
        self.pipes = []
        self.values = []
        self.last_result = False

    def source(self, vals):
        for val in vals:
            self.values.append(val)

        return self

    def pipe(self, func):
        self.pipes.append(func)

        return self

    def execute(self):
        for pipe in self.pipes:
            if not self.last_result:
                self.last_result = pipe(self.values)
            else:
                self.last_result = pipe(self.last_result)

        return self.last_result


stream_1 = Stream()

test_1 = stream_1.source(listdir('.'))\
        .pipe(concat)\
        .execute()

print(test_1)

stream_2 = Stream()

test_2 = stream_2.source([1, 2, 3, 4, 5])\
        .pipe(double)\
        .pipe(double)\
        .pipe(double)\
        .execute()


print(test_2)
