from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.read_csv('datosE.csv')
df1= df[df['RATE']>=8.5]

fig = px.bar(df, x="DATE", y="RATE", color="DATE", barmode="stack")

app.layout = html.Div(children=[
    html.H1(children='Unemployment Rate - 20 Yrs'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
   



