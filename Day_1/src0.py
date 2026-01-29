






# Demonstrates defining a main function

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

# Demonstrates defining a main function

def main():
 name = input("What's your name? ")
 hello(name)
 
 def hello(to="world"):
    print("hello,", to)

main()

# Demonstrates defining a function with a return value

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
def square(n):
 return n * n

main()