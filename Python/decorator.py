def decarator(function):
    def wrapper(*args,**kwargs):
        key_part=function(*args,**kwargs)
        print("hh")
        return key_part
    return wrapper

@decarator
def hello_world(person):
    return f"hello world {person}"


print(hello_world("lal"))
