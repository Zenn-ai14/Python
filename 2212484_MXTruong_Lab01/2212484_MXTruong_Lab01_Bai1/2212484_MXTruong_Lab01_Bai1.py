def print_poem():
    poem = """Twinkle, twinkle, little star,
How I wonder what you are! 
Up above the world so high,   
Like a diamond in the sky. 
Twinkle, twinkle, little star, 
How I wonder what you are"""
    lines = poem.splitlines()
    print(lines[0])
    print("\t" + lines[1])
    print("\t\t" + lines[2])
    print("\t\t" + lines[3])
    print(lines[4])
    print("\t" + lines[5])
print_poem()

#2. 
import sys
print(f"Python version: {sys.version}")
print(f"Python version info: {sys.version_info}")

#3.
from datetime import datetime
now = datetime.now()
print("Current date and time :")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#4.
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
print(f"r = {radius}")
print(f"Area = {area}")

#5.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name, first_name)

#6.
def get_list_and_tuple():
    """
    Accepts a sequence of comma-separated numbers from the user, 
    generates a list and a tuple of those numbers, and prints them.
    Returns:
        None
    """
    numbers_str = input("Enter a sequence of comma-separated numbers: ")
    numbers_list = numbers_str.split(",")
    numbers_tuple = tuple(numbers_list)
    print("List :", numbers_list)
    print("Tuple :", numbers_tuple)
if __name__ == "__main__":
    get_list_and_tuple()

#7.
def get_file_extension():
  """Gets a filename from the user and prints the extension.
  Returns:
      None
  """
  filename = input("Enter a filename: ")
  extension = filename.split(".")[-1]
  print(f"Extension: {extension}")
if __name__ == "__main__":
  get_file_extension()

#8.
color_list = ["Red", "Green", "White", "Black"]
first_color = color_list[0] 
last_color = color_list[-1] 
print("First Color:", first_color)
print("Last Color:", last_color)

#9.
exam_st_date = (11, 12, 2014)
day, month, year = exam_st_date
exam_date = f"{day}/{month}/{year}"
print(f"The examination will start from : {exam_date}")

#10.
def sum_of_n(n):
  """
  Computes the value of n+nn+nnn for a given integer n.
  Args:
    n: The integer input.
  Returns:
    The sum of n, nn, and nnn.
  """
  nn = int(str(n) * 2)  # Concatenate n with itself to form nn
  nnn = int(str(n) * 3)  # Concatenate n with itself three times to form nnn
  return n + nn + nnn
n = int(input("Enter an integer: "))
result = sum_of_n(n)
print(f"The sum of n+nn+nnn for n={n} is: {result}")

#11.
def print_function_doc(func_name):
  """
  Prints the documentation of the given Python built-in function.
  Args:
    func_name: The name of the function as a string.
  """
  try:
    func = getattr(__builtins__, func_name)
    docstring = func.__doc__
    print(docstring)
  except AttributeError:
    print(f"Function '{func_name}' not found.")
func_name = input("Enter the name of the built-in function: ")
print_function_doc(func_name)

#12
import calendar
def print_calendar(year, month):
  """
  Prints the calendar for the given month and year.

  Args:
    year: The year (integer).
    month: The month (integer, 1-12).
  """
  try:
    cal = calendar.month(year, month)
    print(cal)
  except ValueError:
    print("Invalid month. Please enter a number between 1 and 12.")
if __name__ == "__main__":
  year = int(input("Enter the year: "))
  month = int(input("Enter the month (1-12): "))
  print_calendar(year, month)

  #13
  docstring = """
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
print(docstring)

#14
from datetime import date

def days_between_dates(date1, date2):
    """
    Calculates the number of days between two dates.

    Args:
        date1: The first date as a tuple (year, month, day).
        date2: The second date as a tuple (year, month, day).

    Returns:
        The number of days between the two dates.
    """
    date1 = date(*date1)  # Create date objects from tuples
    date2 = date(*date2)
    delta = date2 - date1
    return delta.days
date1 = (2014, 7, 2)
date2 = (2014, 7, 11)
num_days = days_between_dates(date1, date2)
print(f"Number of days between {date1} and {date2}: {num_days} days")

#15
import math

def sphere_volume(radius):
  """
  Calculates the volume of a sphere.
  Args:
    radius: The radius of the sphere.
  Returns:
    The volume of the sphere.
  """
  return (4/3) * math.pi * radius**3
radius = 6
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")

#16
def difference_from_17(num):
  """
  Calculates the difference between a given number and 17. 

  Args:
    num: The input number.

  Returns:
    The difference between the number and 17. 
    If the number is greater than 17, returns twice the absolute difference.
  """
  if num > 17:
    return 2 * abs(num - 17)
  else:
    return abs(num - 17)
number = 20 
result = difference_from_17(number)
print(f"The difference from 17 for {number} is: {result}")

#17
def near_thousand(n):
  """
  Checks if a number is within 100 of 1000 or 2000.

  Args:
    n: The number to check.

  Returns:
    True if the number is within 100 of 1000 or 2000, False otherwise.
  """
  return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)
num = int(input("Enter a number: "))
if near_thousand(num):
  print("The number is within 100 of 1000 or 2000.")
else:
  print("The number is not within 100 of 1000 or 2000.")

#18
def sum_three(a, b, c):
  """
  Calculates the sum of three given numbers. If the values are equal, 
  returns three times their sum.

  Args:
    a: The first number.
    b: The second number.
    c: The third number.

  Returns:
    The sum of the three numbers, or three times their sum if they are equal.
  """
  if a == b == c:
    return (a + b + c) * 3
  else:
    return a + b + c
num1 = 2
num2 = 2
num3 = 2
result = sum_three(num1, num2, num3)
print("Result:", result)

#19
def add_is(string):
  """
  Adds "Is" to the beginning of a string if it doesn't already start with "Is".

  Args:
    string: The input string.

  Returns:
    The string with "Is" added to the beginning if it doesn't already start with "Is", 
    otherwise returns the original string.
  """
  if string.startswith("Is"):
    return string
  else:
    return "Is" + string
my_string = "beautiful"
new_string = add_is(my_string)
print(new_string) 
my_string = "Is amazing"
new_string = add_is(my_string)
print(new_string) 

#20
def string_copies(string, n):
  """
  Returns a string that is n (non-negative integer) copies of a given string.

  Args:
    string: The input string.
    n: The number of copies.

  Returns:
    A string that is n copies of the input string.
  """

  if n < 0:
    raise ValueError("n must be a non-negative integer.")
  return string * n
my_string = "hello"
num_copies = 3
result = string_copies(my_string, num_copies)
print(result)  