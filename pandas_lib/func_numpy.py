import numpy as np

def collect_info(array: np.ndarray):
    shape = array.shape
    dimensions = array.ndim
    size = array.size
    return f'Shape: {shape}; dimensions: {dimensions}; size: {size}'



def custom_sum(arg1, arg2):
    if isinstance(arg1, np.ndarray) or isinstance(arg2, np.ndarray):
        if isinstance(arg1, list) or isinstance(arg2, list):
            return "One argument is a list"
        return arg1 + arg2
    return "Both arguments are lists, not arrays"

