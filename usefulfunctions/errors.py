import numpy as np
    
"""
A package of functions to measure errors
"""
    
    

def RMSE(prediction, actual):
    """
    Calculate the root mean squared error

    Parameters:
    -----------
    prediction: a list, numpy array or series of predicted values
    actual: a list, numpy array or series of actual values
    
    Returns:
    -----------
    root mean squared error value
    """

    rmse = np.sqrt(((prediction - actual) ** 2).mean())
    return rmse

def error_margin(prediction, actual):
    """
    Calculate the error margin
    
    Parameters:
    -----------
    prediction: a list, numpy array or series of predicted values
    actual: a list, numpy array or series of actual values
    
    Returns:
    -----------
    error margin = rmse/(max(actual) - min(actual))
    """

    errormargin = RMSE(prediction, actual)/(actual.max() - actual.min())
    return errormargin
