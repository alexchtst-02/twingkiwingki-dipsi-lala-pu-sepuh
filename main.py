from matplotlib import pyplot as plt
import numpy as np
import math as m

class findRoot(object):
    def __init__(self, itter):
        self.itter = itter
        self.root_record = []
        self.function_values = []
        self.function_value = 0  # to chect if the value goes to be diverge or converge

    def _reset_record(self):
        self.root_record = []
        self.function_values = []
        print("root record and function values record has been restart")

    # Bisection method
    def Bisection(self, a, b, function):
        self._reset_record()
        if function(a) * function(b) <= 0:
            fmin = min(function(a), function(b))
            fmax = max(function(a), function(b))
            xmin = a if min(function(a), function(b)) == function(a) else b
            xmax = a if max(function(a), function(b)) == function(a) else b
            for i in range(self.itter):
                t = 1/2 * (xmin + xmax)
                self.root_record.append(t)
                self.function_values.append(function(t))
                if function(t) < 0:
                    xmin = t
                elif function(t) > 0:
                    xmax = t
                else:
                    break
            self.root_record.append('selesai')
        else:
            self.root_record.append('selesai [f(a)f(b) tidak negatif]')

    # Newton Raphson
    def NewtonRaphson(self, initial, function, deriv_function):
        self._reset_record()
        root = initial
        self.root_record.append(root)
        self.function_values.append(function(root))
        for i in range(self.itter):
            root = root - function(root) / deriv_function(root)
            self.root_record.append(root)
            self.function_values.append(function(root))

        self.root_record.append('selesai')

    def Seccant(self, initial, function, h=0.01):
        self._reset_record()
        root = initial
        self.root_record.append(initial)
        self.function_values.append(function(root))
        temp_ = root
        
        # for initiate the first x0 = inital x1 = initial + h and x2 = root approximation
        root = root - (function(root)*h) / (function(root + h) - function(root))
        self.root_record.append(root)
        self.function_values.append(function(root))
        for i in range(self.itter - 1):
            h = root - temp_
            temp_ = root
            root = root - (function(root)*h) / (function(root + h) - function(root))
            
            self.root_record.append(root)
            self.function_values.append(function(root))
        self.root_record.append('selesai')
        

    def graph_root_record(self, save=False):
        rcd = self.root_record
        try:
            rcd.pop()
        except IndexError:
            pass
        # rcd = np.array(rcd)
        plt.title("the root value graph")
        plt.plot(rcd)
        plt.show()
        if save:
            plt.savefig("./root_record.png")

    def graph_root_loc(self, save=False):
        rcd = self.root_record
        try:
            rcd.pop()
            print("the root is: ", rcd[-1])
        except IndexError:
            pass
        y = [0]*len(rcd)
        color_line = np.linspace(0, 1, len(rcd))
        plt.title("Root Location is the yellow")
        plt.scatter(rcd, y, marker='x', c=color_line)
        plt.show()
        if save:
            plt.savefig("./root_loc.png")

def my_function(x):
    # return m.sin(x) + m.cos(x) - m.exp(x)
    return x**9 + 1

def deriv_my_function(x):
    # return 2*x + 2
    return 9*x

root = findRoot(itter=20)

root.NewtonRaphson(initial=0, function=my_function, deriv_function=deriv_my_function)
# root.Bisection(a=-5, b=-1, function=my_function)
# root.Seccant(initial=-3, function=my_function, h=2)

# print(root.root_record)
root.graph_root_record()
root.graph_root_loc()


# nih errornya

# Traceback (most recent call last):
# File "C:\PYTHON\METODE-NUMERIS\main.py", line 111, in <module>
# root.NewtonRaphson(initial=0, function=my_function, deriv_function=deriv_my_function)
# File "C:\PYTHON\METODE-NUMERIS\main.py", line 46, in NewtonRaphson
# root = root - function(root) / deriv_function(root)
#                 ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~
# ZeroDivisionError: division by zero