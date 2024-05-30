from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    html.Button('Click here:', id='submit-button', n_clicks=0),
    html.Div(id='button-click-container', children='You\'ve not yet clicked the button. Click it.'), 
    html.Button('Click to disagree<3', id='disagree-button', n_clicks=0),
    html.Div(id='disagree-container', children=''),
])


@callback(
    Output('button-click-container', 'children'),
    Input('submit-button', 'n_clicks'),
    prevent_initial_call=True
)
def update_output(n_clicks):
    return 'VSCHT je lepsi <3.'


@callback(
    Output('disagree-container', 'children'),
    Input('disagree-button', 'n_clicks'),
    prevent_initial_call=True
)
def update_second_output(n_clicks):
    return 'Dobrej pokus, ale stejne je VSCHT lepsi <3.'



if __name__ == '__main__':
    app.run(debug=True)