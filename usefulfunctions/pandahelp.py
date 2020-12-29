import pandas as pd
import numpy as np
from IPython.core.display import HTML

def null_values(dataframe):
    """
    Returns a dataframe of the count of null and N/A values per column of
    the input dataframe
    
    Parameters:
    -----------
    dataframe: a pandas dataframe
    
    Returns:
    --------
    A pandas dataframe listing all column features and the sum of Null & Empty
    values per feature
    """

    a = dataframe.isnull().astype(int).sum()
    b = (dataframe=="").astype(int).sum()
    result = pd.DataFrame(data=[a,b], index=['Null','Empty']).T
    
    return result   


def multi_table(tables):
    """
    Prints multiple IpyTable objects side by side in Jupyter Notebook
    
    Parameters:
    -----------
    tables: a list of IpyTable objects (e.g. pandas DataFrames)
    
    Returns:
    -----------
    A HTML table with each IpyTable in a cell
    """
    return HTML('<table align=top><tr style="background-color:white; align:top">' + 
                ''.join(['<td>' + table._repr_html_() + 
                '</td>' for table in tables]) +
                '<tr><</table>')


def clean_column_names(columns):
    """
    Removes whitespace, converts '-' to '_' and makes all names lowercase
    for all items in columns.
    Useful for cleaning up pandas column names.

    Parameters:
    -----------
    columns: a list of column names

    Returns:
    --------
    a cleaned list of column names
    """
    columns = [col.replace(" ","") for col in columns]
    columns = [col.replace("-","_").lower() for col in columns]
    
    return columns
