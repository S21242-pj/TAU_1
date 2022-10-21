"""
Python 3.1 @PJATK TAU_1 Szymon Dejewski s21242
Reverse Polish Notation Calculator v.1
"""


def rpn(s):
    fields = s.split(" ")

    nums = []

    for field in fields:
        if field == "+":
            n1, n2 = popargs(nums)
            nums.append(n1 + n2)
        elif field == "*":
            n1, n2 = popargs(nums)
            nums.append(n1 * n2)
        else:
            try:
                nums.append(float(field))
            except ValueError:
                raise Exception("expected a number")

        print(nums)

    return nums.pop()

@property
def divided(self):
    try:
        return self.number1 / self.number2
    except ZeroDivisionError:
        return None

def popargs(nums):
    if len(nums) < 2:
        raise Exception("too few operands")
    else:
        return nums.pop(), nums.pop()