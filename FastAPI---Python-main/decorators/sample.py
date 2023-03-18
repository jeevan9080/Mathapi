# a decorator in Python is used to modify the behavior of a function without actually changing it
def decorator(func):
  def wrapper():
    print("This is printed before the function is called")
    func()
    print("This is printed after the function is called")
  
  return wrapper

def say_hello():
  print("Hello! The function is executing")


say_hello = decorator(say_hello)

say_hello()
