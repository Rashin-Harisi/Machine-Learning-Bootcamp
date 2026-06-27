#/usr/bin/env python3

"""
    - getattr(object, attribute_name, default_value), 
            default_value is used to return instead of AttributeErrot 
            when the object does not have the attribute 
    - setattr(object, attribute_name, value)
    - hasattr()
    - delattr()

    def function(*args):
        print(args)
    *args => suppose you do not know how many numbers the user will pass
    args is a tuple
    * -> means collect all positional arguments into one tuple
    
    def function(**kwargs):
        print(kwargs)
    **kwargs=> suppose instead of numbers, you want to arbitrary named arguments
    kwargs is a dictionary
    **-> means collect all keyword arguments into one dictionary

    def function(*args, **kwargs):
        print(args)
        print(kwargs)

    def function(*args, **kwargs, other_normal_arguments):
        print(args)
        print(kwargs)
        print(other_normal_arguments)

    numbers=[1,2,3]
    function(numbers) => function([1,2,3])
    function(*number) =?function(1,2,3) =>pyton unpack the list
    person={
        "name" : "Rashin",
        "age" : 35
    }
    function(person) => function({"name" : "Rashin", "age" : 35})
    function(**person) => function("name" : "Rashin", "age" : 35) => python unpack the dictionary

    """

"""
    Object vs. Dictionary
    object is an instance of a class and owns the dictionary that contains all 
    object's attributes and their value. (obj.__dict__)
    So when you are looking for an attribute, you cannot search like key_values pair 
    in dictionary. They are totally different.
"""
class ObjectC(object):
    def __init__(self):
        pass



def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()
    for i,item in enumerate(args):
        attr_name = f"var_{i}"
        if hasattr(obj, attr_name):
            return None
        setattr(obj, attr_name, item)

    for key,value in kwargs.items():
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)

    return obj


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)