"""
Given 3 numbers a, b and c as input, print Right Angled Triangle:Yes if they can be sides of a right angle triangle or else print Right Angled Triangle:No
Input-> a=10, b=20, c= 15
Output-> Right Angled Triangle:No
"""

a = 10
b = 20
c = 15
if ((a*a) + (b*b) == (c*c) or (a*a) + (c*c) == (b*b) or (b*b) + (c*c) == (a*a)):
  print("Right Angled Triangle:Yes")
else:
  print("Right Angled Triangle:No")
