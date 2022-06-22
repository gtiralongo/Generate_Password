import random as r

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
numbers = "0123456789"
symbol = "!#$%&/\*+-?¡¿@"

use_for = lower_case + upper_case + numbers + symbol
length_for_pass = 10

password = "".join(r.sample(use_for,length_for_pass))

print(password)