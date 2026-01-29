"""
#get number from the user
x=int(input("Enter a number: "))
  print(f"You entered: {x}")

#cathes a value error:

try:
    x=int(input("Enter a number: "))
    print(f"You entered: {x}")
except ValueError:
    print("x is not an integer .")

#
while True:
    try:
        y=int(input("what is y? "))
    except:
        print(f"x is not an integer")
    else:
      break
print(f"y is: {y}") 
"""
#optimise the code

def main():

    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what is x? "))
        except :
            pass
main()  