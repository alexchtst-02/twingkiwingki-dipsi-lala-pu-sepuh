from matplotlib import pyplot as plt
import numpy as np

class findRoot(object):
    def __init__(self, itter):
        self.itter = itter
        self.root_record = []
    
    # Bisection method
    def Bisection(self, a, b, function):
        if function(a) * function(b) <= 0:
            fmin = min(function(a), function(b))
            fmax = max(function(a), function(b))
            xmin = a if min(function(a), function(b)) == function(a) else b
            xmax = a if max(function(a), function(b)) == function(a) else b
            for i in range(self.itter):
                t = 1/2 * (xmin + xmax)
                self.root_record.append(t)
                if function(t) < 0:
                    xmin = t
                elif function(t) > 0:
                    xmax = t
                else:
                    break
            self.root_record.append('selesai')
        else:
            self.root_record.append('selesai [f(a)f(b) tidak negatif]')
    
    # isi lagi newton raphson
    
    def graph_root_record(self, save=False):
        rcd = self.root_record
        rcd.pop()
        # rcd = np.array(rcd)
        plt.plot(rcd)
        plt.show()
        if save :
            plt.savefig("./root_record.png")
            
    def graph_root_loc(self, save=False):
        rcd = self.root_record
        rcd.pop()
        print("the root is: ", rcd[-1])
        y = [0]*len(rcd)
        color_line = np.linspace(0, 1, len(rcd))
        plt.scatter(rcd, y, marker='x', c=color_line)
        plt.show()
        if save :
            plt.savefig("./root_loc.png")

# def pos_def(x):
#     return x**2 + 6*x + 1

# root = findRoot(itter=100)
# root.Bisection(a=10, b=-2, function=pos_def)