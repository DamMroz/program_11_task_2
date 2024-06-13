from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px
import string

def render_tab(df_days,df_customer):
    fig = px.bar(df_customer, x="Store_type", y="count", color="Gender", title="Customer information")
    translation_table = str.maketrans('', '', string.digits)
    df_days=df_days[['Store_type','day']].to_string()
    n1 = "\n"
    layout = html.Div([html.H1('Sklepy',style={'text-align':'center'}),
                       html.Div([html.Div([dcc.Graph(id='customer',figure=fig)],style={'width':'50%'}),
                       html.Div([dcc.Textarea(
                       value=f'Table that shows days with the most transactions: {n1} {n1} {df_days.translate(translation_table)}',
                       style={'width': '100%'})])])])
    
    return layout