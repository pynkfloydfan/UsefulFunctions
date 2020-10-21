
import numpy as np
import pandas as pd
from IPython.core.display import HTML
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.subplots
from PIL import Image
import os
import math


# set the default location of images to the Pictures directory (WINDOWS)
image_path = os.path.join(os.environ['USERPROFILE'], 'Pictures')


def cutimage(image, x_slices, y_slices, outpath=image_path):
    """
    Cuts an image into equal sized slices, x_slices long and y_slices high

    I wanted to expand an image over 2 pages in a pdf (via LaTeX) but 
    unfortunately it wouldn't automatically stretch over 2 pages, so instead I 
    decided to cut it in two and input each half to a separate page.
    
    Inspiration from here:
    https://tex.stackexchange.com/questions/22826/breaking-pictures-across-multiple-pages
    
    Parameters:
    -----------
    image: an image file
    x_slices: number of equal sized slices in the horizontal axis
    y_slices: number of equal sized slices in the vertical axis
    
    Returns:
    --------
    x_slices number of lists each with y_slices number of image items
    """

    # x, y image size
    xsize, ysize = image.size
    
    # size of each slice in each axis
    xstep = xsize // x_slices
    ystep = ysize // y_slices
    
    # all coordinates of each sub-image
    if x_slices > 1:
        xcoord = list(range(0, xsize + x_slices - 1, xstep))
    else:
        xcoord = [0, xsize]
    if xcoord[-1] < xsize: 
        xcoord[-1] = xsize
    
    if y_slices > 1:
        ycoord = list(range(0, ysize + y_slices - 1, ystep))
    else:
        ycoord = [0, ysize]
    if ycoord[-1] < ysize: 
        ycoord[-1] = ysize
        
    print(xcoord, ycoord)
    
    for y in range(y_slices):
        for x in range(x_slices):
            bbox = (xcoord[x], ycoord[y], xcoord[x+1], ycoord[y+1])
            image_slice = image.crop(bbox)
            image_slice.save(os.path.join(outpath, "slice_" + str(x) + "_" + str(y) + "_" + ".png"))
            # image_slice.show()
    
    return 'All images saved'


def plotly_base_fig(title, xtitle, ytitle, height=800, width=1500, **params):
    """
    The base figure for all plotly graphs in this project
    Parameters:
    -----------
    title: the chart title
    xtitle: the x-axis title
    ytitle: the y-axis title
    **params: any parameters to pass to the plotly.subplots.make_subplots() function
    
    Returns:
    -----------
    The plotly figure
    """

    fig = plotly.subplots.make_subplots(**params)
    fig.update_layout(height=height, width=width,
                    title=title,
                    xaxis_title=xtitle,
                    yaxis_title=ytitle,
                    legend=dict(x=0, y=1))

    fig.update_xaxes(rangeslider_visible=True,
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1, label="1m", step="month", stepmode="backward"),
                            dict(count=6, label="6m", step="month", stepmode="backward"),
                            dict(count=1, label="YTD", step="year", stepmode="todate"),
                            dict(count=1, label="1y", step="year", stepmode="backward"),
                            dict(count=5, label="5y", step="year", stepmode="backward"),
                            dict(step="all")
                                ])
                            )
                    )
    return fig


def missing_vals_heatmap(DataFrame, cmap='magma'):
    """
    Produces a heatmap figure of all missing values in the DataFrame

    Params:
    -------
    DataFrame: a pandas dataframe
    cmap: a seaborn compatible color_palette

    Returns:
    --------
    A seaborn heatmap figure
    """
    
    return sns.heatmap(DataFrame.isnull(), cbar=False, cmap=cmap)


def correlation_heatmap(corr_matrix, fontsize=10):
    """
    Produces a base figure for a correlation heatmap

    Params:
    -------
    corr_matrix: the correlation matrix
    fontsize: the size of the annotated text in each cell

    Returns:
    --------
    A seaborn heatmap figure
    """
    
    ax = sns.heatmap(corr_matrix*100, annot=True, fmt='.0f', annot_kws={'fontsize': fontsize})
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right',
        fontdict={'fontsize':13}
    )
    
    ax.set_yticklabels(
        ax.get_yticklabels(),
        fontdict={'fontsize':13}
    )
    
    return ax
          

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
    Prints multiple IpyTable objects side by side.
    
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

def haversine(origin, destination):
    """
    Calculates the haversine distance in km between two points

    Parameters:
    -----------
    origin: set or list of (latitude, longitude)
    destination: set or list of (latitude, longitude)

    Returns:
    --------
    haversine distance in km (assumes a straight line, no account for elevation changes)

    """ 
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def east_north_distance(origin, destination):
    """
    Calculates the distance between two coordinates expresses 
    in eastings/northings 

    Parameters:
    -----------
    origin: set or list of (easting, northing)
    destination: set or list of (easting, northing)

    Returns:
    --------
    straight line distance sqrt((E1-E2)^2+(N1-N2)^2)

    """ 
    E1, N1 = origin
    E2, N2 = destination

    d = math.sqrt((E1-E2)**2 +(N1-N2)**2)
    return d