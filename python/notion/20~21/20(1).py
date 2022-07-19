from curses import A_ALTCHARSET
from re import A

from pyrsistent import b


number = 123
n = 0
result = 0
while number > 1*(10**n):
    number, remainder = divmod(number, 10)
    result += remainder
print(sum)


