from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px
from dash import dash_table

def render_tab(df_days,df_customer):
    fig = px.bar(df_customer, x="Store_type", y="count", color="Gender", title="Customer information")
    n1 = "\n"
    layout = html.Div([html.H1('Sklepy',style={'text-align':'center'}),
                       html.Div([html.Div([dcc.Graph(id='customer',figure=fig)],style={'width':'50%'}),
                       html.Label("Table that shows the days with the most transactions and the corresponding total amout of transactions",style={"font-weight": "bold"}),
                       html.Div([dash_table.DataTable(df_days.to_dict('records'),[{"name":i, "id":i} for i in df_days.columns],style_cell={'textAlign': 'left'})])       
                       ])])
    
    return layout