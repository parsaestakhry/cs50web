def announce(f):
    def wrapper():
        print("about to run the function")
        f()
        print("done with the function")
    return wrapper

#takes the hello function and acts as an input to the announce function
@announce
def hello():
    print("Hello, world!")

hello()