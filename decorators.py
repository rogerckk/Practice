def announce(f):
    def wrapper():
        print("About to tun the functions")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello World")

hello()