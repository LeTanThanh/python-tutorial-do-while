if __name__ == "__main__":
  # Introduction to the do…while loop statement

  """
  If you have come from other programming languages such as JavaScript, Java or C#, you're a;ready familiar with the do ... while loop statement.

  Unlike the while loop, the do .. while loop statement executes at least one iteration.
  It checks the condition at the end of each iteration and executes a code block until the condition is False.

  The following shows the pseudocode for the do ... while loop in Python:

  do
    # code block
  while condition

  Unfortunately, Python doesn't support the do ... while loop.
  However, you can use the while loop and a break statement to emulate the do ... while loop statement.

  First, specify the condition as True in the while loop like this:

  while True:
    # code block

  This allows the code block to execute for the first time.
  However, since the condition is always True, it creates an indefinite loop.
  This is not what we expected.

  Second, place a condition to break out of the while loop:

  while True:
    # code block

    # break out of the loop
    if condition:
      break

  In this syntax, the code block always executes at least one for the first time and the condition is checked at the end of each iteration.
  """

  # Python do…while loop emulation example

  from random import randint

  MIN = 0
  MAX = 10

  secret_number = randint(MIN, MAX)

  attempt = 0

  while True:
    input_number = int(input(f"Enter a number between {MIN} and {MAX}: "))
    attempt += 1

    if input_number > secret_number:
      print("It should be smaller.")
    elif input_number < secret_number:
      print("It should be bigger.")
    else:
      print(f"Bingo! {attempt} attempt(s).")
      break
