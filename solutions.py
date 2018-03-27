"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

"""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True

"""

def common_end(a, b):
  if (a[0] == b[0] or a[-1] == b[-1]):
    return True
  else:
    return False

"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
"""

def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
    if str[0:3] == 'xyz':
      return True
  return False



"""
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
If the string is shorter than length 2, return whatever there is, 
so "X" yields "X", and the empty string "" yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'

"""
def first_two(str):
  if len(str) == 0:
    return str
  else:
    return str[:2]


"""
The number 6 is a truly great number. Given two int values, a and b, return True 
if either one is 6. Or if their sum or difference is 6. 
Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True

"""

def love6(a, b):
  if a == 6 or b == 6 or abs(a - b) == 6 or a + b ==6:
    return True
  return False






















