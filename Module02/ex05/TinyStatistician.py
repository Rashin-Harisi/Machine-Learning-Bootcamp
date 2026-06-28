#!/usr/bin/env python3

import numpy as np
import numbers
import math

'''
numbers.Number : {
        int
        float
        numpy.int32
        numpy.int64
        numpy.float32
        numpy.float64
    }
np.array([1.2]).dtype => numpy.float64

'''

class TinyStatistician():
    
    def validation(self,x):
        if not isinstance(x, (list, np.ndarray)):
            return False
        if len(x) == 0:
            return False
        for item in x:
            if isinstance(item, bool):
                return False
            if not isinstance(item , numbers.Number):
                return False
        return True

    def mean(self, x):
        added = 0
        if not self.validation(x):
            return None
        length = len(x)
        for item in x:
            added += item
        return float(added / length)
        
    def median(self,x):
        if not self.validation(x) : 
            return None
        new = sorted(x)
        length = len(new)
        if length % 2 == 0:
            return self.mean([new[length // 2] , new[(length // 2) -1]])
        else:
            return float(new[length // 2])

    def quartile(self,x):
        if not self.validation(x):
            return None
        new = sorted(x)
        length = len(new)
        lower = new[length//4]
        upper = new[(3*length)//4]
        return [float(lower), float(upper)]
        
    def var(self,x):
        if not self.validation(x):
            return None
        mean_var = self.mean(x)
        new_list= []
        for value in x:
            new_list.append((value - mean_var)**2)
        return float(self.mean(new_list))
    
    def std(self,x):
        if not self.validation(x):
            return None
        variance = self.var(x)
        return float(math.sqrt(variance))