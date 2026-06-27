#!/usr/bin/env python3
"""
    contex management is about manage resources correctly during specific block of code.
    it has three phases: before the block, execute the block, cleanup
    it is for guaranteeing cleanup
    ways: try...finally / try...else / with ... as ...

    When a with statement is executed, the immediately proceeding expression part must 
    evaluate to a context manager. At its core, a context manager must produce an object 
    that includes and supports two methods: __enter__() and __exit__().

    The __enter__() returns the resource that needs to be managed (technically, we “enter” 
    the runtime context; the with statement will bind this method's return value to the 
    “target,” the term after as). The __exit__() method ensures that the object is properly 
    closed, shut down, or cleaned up when the block ends. Crucially, both methods are called 
    every time the with statement is executed, regardless of how the code block terminates 
    (even if the block exits with an exception).
    the __exit__() method accepts three arguments: 
        the exception's type, value/instance, and its “traceback.”
"""
class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if sep != ',' and sep != ';':
            raise ValueError("Seperator character can only be ',' or ';'. ")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.data = []


    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
        except FileNotFoundError:
            return None
        reading = self.file.read().splitlines()
        for item in reading:
            self.data.append(item.split(self.sep))
        if not self.data:
            self.file.close()
            return None
        len_header = len(self.data[0])
        for item in self.data:
            if len(item) != len_header:
                self.file.close()
                return None
            for field in item:
                if field.strip() == "" :
                    self.file.close()
                    return None
        return self

    def __exit__(self, excep_type, excep_value, traceback):
        if self.file is not None:
            self.file.close()


    def getdata(self):
        start = self.skip_top
        if self.header is True:
            start += 1
        end = len(self.data) - self.skip_bottom
        return self.data[start : end]
    
    def getheader(self):
        if self.header is True:
            return self.data[0]
        else:
            return None