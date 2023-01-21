from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('../winequelity.csv')

all_columns_names = df.columns.to_list()
all_options = {
    'MODEL REGRESJI': all_columns_names,
    'MODEL KLASYFIKACJI': all_columns_names
}

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



app.layout = html.Div([
    html.H4(children='PLIK: winequality.csv'),
    generate_table(df),

    html.Br(),
    html.H4(children='WYBIERZ MODEL:'),

    dcc.RadioItems(
        list(all_options.keys()),
        'MODEL REGRESJI',
        id='radio-model',
    ),
    html.Hr(),

    dcc.RadioItems(id='radio-kolumna'),

    html.Hr(),
    html.H4(children='WYKRES:'),
    dcc.Graph(id='wykres')
])


@app.callback(
    Output('radio-kolumna', 'options'),
    Input('radio-model', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('radio-kolumna', 'value'),
    Input('radio-kolumna', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('wykres', 'figure'),
    Input('radio-model', 'value'),
    Input('radio-kolumna', 'value'))
def set_display_children(selected_model, selected_column):
    if(selected_model == 'MODEL REGRESJI'):
        fig = px.scatter(df, x=df["pH"], y=df[selected_column],log_x=True)
        return fig
    else :
        fig = px.scatter(df, x=df[selected_column], y=df["target"],log_x=True)
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
