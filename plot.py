import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import os

def create_plot(*files):
    fig = go.Figure()

    for file in files:
        filename = os.path.basename(file)
        data = pd.read_csv(file, sep='\t', header=None)
        fig.add_trace(go.Scatter(x=data.iloc[:, 0], y=data.iloc[:, 1], name=filename))

    fig.update_layout(
        title='',
        xaxis_title='Raman Shift [cm⁻¹]',
        yaxis_title='Intensity [a.u.]',
        template='plotly_white',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    plot_div = pyo.plot(
        fig,
        include_plotlyjs=False,
        output_type='div',
        config={
            'displaylogo': False,
            'showLink': False,
            'modeBarButtonsToRemove': ['toImage'],
            'displayModeBar': True
        }
    )

    return plot_div