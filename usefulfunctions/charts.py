import matplotlib.pyplot as plt
import seaborn as sns
import plotly



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


def missing_vals_heatmap(dataframe, cmap='magma'):
    """
    Produces a heatmap figure of all missing values in the DataFrame

    Params:
    -------
    dataframe: a pandas dataframe
    cmap: a seaborn compatible color_palette

    Returns:
    --------
    A seaborn heatmap figure
    """
    
    return sns.heatmap(dataframe.isnull(), cbar=False, cmap=cmap)


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
