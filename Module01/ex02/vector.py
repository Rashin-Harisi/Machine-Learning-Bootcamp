#!/usr/bin/env python3

def validate(data: list):
    if not isinstance(data, list) or len(data) == 0:
        return False
    
    if len(data) == 1:
        if not isinstance(data[0], list) or len(data[0])== 0:
            return False
        for element in data[0]:
            if not isinstance(element, float):
                return False
        return True
    if len(data) > 1:
        for element in data : 
            if (not isinstance(element, list) 
                or len(element) != 1 
                or not isinstance(element[0], float)):
                return False
        return True 

def create_shape(data: list):
    if len(data) == 1:
        return (1, len(data[0]))
    if len(data) > 1:
        return (len(data), 1)

class Vector:
    def __init__(self, data):
        if isinstance(data, list):
            if not validate(data):
                raise TypeError("Types of data must be a valid vector of floats")
            self.values = data
            self.shape = create_shape(data)
        elif isinstance(data, int):
            if data <= 0:
                raise ValueError("Size must be a positive integer")
            self.values=[[float(i)] for i in range(data)]
            self.shape=(data, 1)
        elif isinstance(data, tuple):
            if len(data) != 2:
                raise ValueError("Range must be a tuple of two integers")
            start, end = data
            if not isinstance(start, int) or not isinstance(end, int):
                raise ValueError("Range values must be integers")
            if start >= end:
                raise ValueError("In tuple(a, b), a should be smaller than b.")
            self.values=[[float(i)] for i in range(start,end)]
            self.shape=(end - start, 1)
        else:
            raise TypeError("Data must be a list, int or tuple.")
        
    def T(self):
        new_values = []
        if len(self.values) == 1:
            for element in self.values[0]:
                new_values.append([element])
        else :
            new_values.append([])
            for element in self.values:
                new_values[0].append(element[0])
        return Vector(new_values)

    def dot(self, data):
        if not isinstance(data, Vector):
            raise ValueError("Data must be Vector type.")
        if self.shape != data.shape:
            raise ValueError("Both vectors must be in the same shape.")
        result = 0
        if len(self.values) == 1:
            result = sum((self.values[0][i] * data.values[0][i]) for i in range(len(self.values[0])))
        else:
            result = sum((self.values[i][0] * data.values[i][0]) for i in range(len(self.values)))
        return result

    def __add__(self, data):
        if not isinstance(data, Vector):
            raise TypeError("Data must be Vector type.")
        if self.shape != data.shape:
            raise ValueError("Both vectors must be in the same shape.")
        new_vector=[]
        if len(self.values) == 1:
            new_vector.append([])
            for i in range(len(self.values[0])):
                new_vector[0].append(self.values[0][i] + data.values[0][i])
        else:
            for i in range(len(self.values)):
                new_vector.append([self.values[i][0] + data.values[i][0]])
        return Vector(new_vector)
        
    def __radd__(self, data):
        if not isinstance(data, Vector):
            raise TypeError("Data must be Vector type.")
        if self.shape != data.shape:
            raise ValueError("Both vectors must be in the same shape.")
        return self + data
    
    def __sub__(self, data):
        if not isinstance(data, Vector):
            raise TypeError("Data must be Vector type.")
        if self.shape != data.shape:
            raise ValueError("Both vectors must be in the same shape.")
        new_vector=[]
        if len(self.values) == 1:
            new_vector.append([])
            for i in range(len(self.values[0])):
                new_vector[0].append(self.values[0][i] - data.values[0][i])
        else:
            for i in range(len(self.values)):
                new_vector.append([self.values[i][0] - data.values[i][0]])
        return Vector(new_vector)
    
    def __rsub__(self, data):
        if not isinstance(data, Vector):
            raise TypeError("Data must be Vector type.")
        if self.shape != data.shape:
            raise ValueError("Both vectors must be in the same shape.")
        new_vector=[]
        if len(self.values) == 1:
            new_vector.append([])
            for i in range(len(self.values[0])):
                new_vector[0].append(data.values[0][i] - self.values[0][i])
        else:
            for i in range(len(self.values)):
                new_vector.append([data.values[i][0] - self.values[i][0]])
        return Vector(new_vector)
    
    
    def __truediv__(self, data):
        if not isinstance(data, (int, float)):
            raise TypeError("Scaler must be an int or float.")
        if data == 0:
            raise ZeroDivisionError("division by zero.")
        new_vector=[]
        if len(self.values) == 1:
            new_vector.append([])
            for i in range(len(self.values[0])):
                new_vector[0].append(self.values[0][i] / data)
        else:
            for i in range(len(self.values)):
                new_vector.append([self.values[i][0] / data])
        return Vector(new_vector)
        
    def __rtruediv__(self, data):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")
    
    
    def __mul__(self, data):
        if not isinstance(data, (int, float)):
            raise TypeError("Scaler must be an int or float.")
        new_vector=[]
        if len(self.values) == 1:
            new_vector.append([])
            for i in range(len(self.values[0])):
                new_vector[0].append(self.values[0][i] * data)
        else:
            for i in range(len(self.values)):
                new_vector.append([self.values[i][0] * data])
        return Vector(new_vector)
        
    def __rmul__(self, data):
        return self * data
    
    
    def __str__(self):
        return f"Vector({self.values})"
    
    def __repr__(self):
        return self.__str__()