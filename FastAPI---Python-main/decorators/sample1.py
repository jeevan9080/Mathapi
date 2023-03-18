# Syntactic Decorator
def decorator(func):
  def wrapper():
    print("This is printed before the function is called")
    func()
    print("This is printed after the function is called")
  
  return wrapper

@decorator
def say_hello():
  print("Hello! The function is executing")


say_hello()
