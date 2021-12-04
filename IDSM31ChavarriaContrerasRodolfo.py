import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("student-mat.csv")

# df = df.groupby(["type","title","director","cast","country","rating","duration","listed_in"])[['release_year']].mean()
# df.reset_index(inplace=True)
# print(df)


app.layout = html.Div([
    html.H1("Student Alcohol Consumption", style= {'text-align': 'center'}),
html.H4("A practical case is presented below where data was collected in a survey of students of mathematics and "
        "Portuguese courses in high school. It contains a lot of interesting social, gender and studies information "
        "about the students. These data will be used to know how much influence parents and their past education had so that their children ended "
        "up drinking alcoholic beverages, the analysis is carried out with the help of personalized graphs on the aspects "
        "to consider to draw conclusions and be able to act within these secondary schools"),
    dcc.Dropdown(id="slct_type",
                options=[
                    {"label": "Female", "value": "F"},
                    {"label": "Male", "value": "M"}],
                    multi = False,
                    placeholder="Student Gender",
                    style = {'width': "40%",'text-align':'center'}
                ),

    dcc.Dropdown(id="slct_type2",
                options=[
                    {"label": "Mother", "value": 1},
                    {"label": "Father", "value": 2}],
                    multi = False,
                    placeholder="Mom / Dad",
                    style = {'width': "40%",'text-align':'center'}
                ),

    dcc.Dropdown(id="slct_type3",
                options=[
                    {"label": "None", "value": 0},
                    {"label": "Primary Education", "value": 1},
                    {"label": "5th to 9th grade", "value": 2},
                    {"label": "Secondary", "value": 4},],
                    multi = False,
                    placeholder="Parent Education",
                    style = {'width': "40%",'text-align':'center'}
                ),
html.Div(style= {'text-align':'center'},id = 'output_container', children = []),
html.Br(),

dcc.Graph(id = 'alcohol_graph', figure = {},style= {'text-align': 'center'}),
dcc.Graph(id = 'alcohol2_graph', figure = {}),
dcc.Graph(id = 'alcohol3_graph', figure = {}),
dcc.Graph(id = 'alcohol4_graph', figure = {}),
dcc.Graph(id = 'alcohol5_graph', figure = {}),
dcc.Graph(id = 'alcohol6_graph', figure = {}),

html.H4("Source Information",style={'text-align': 'center'}),
html.H6("P. Cortez and A. Silva. Using Data Mining to Predict Secondary School Student Performance. "
        'In A. Brito and J. Teixeira Eds., Proceedings of 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008) '
            'pp. 5-12, Porto, Portugal, April, 2008, EUROSIS, ISBN 978-9077381-39-7.'"",style={'text-align': 'center'}),
html.H6("Fabio Pagnotta, Hossain Mohammad Amran. Email:fabio.pagnotta@studenti.unicam.it, mohammadamra.hossain '@' "
        "studenti.unicam.it. University Of Camerino https://archive.ics.uci.edu/ml/datasets/STUDENT+ALCOHOL+CONSUMPTION",style={'text-align': 'center'}),
])


@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='alcohol_graph', component_property='figure'),
     Output(component_id='alcohol2_graph', component_property='figure'),
     Output(component_id='alcohol3_graph', component_property='figure'),
     Output(component_id='alcohol4_graph', component_property='figure'),
    Output(component_id='alcohol5_graph', component_property='figure'),
     Output(component_id='alcohol6_graph', component_property='figure'),],
    [Input(component_id='slct_type', component_property='value'),
     Input(component_id='slct_type2', component_property='value'),
     Input(component_id='slct_type3', component_property='value'),]
)
def update_graph(option_slctd, option_slctd2, option_slctd3):
    print(option_slctd)
    print(type(option_slctd))

    container = "DASHBOARD"

    dff = df.copy()
    dff = dff[dff["sex"] == option_slctd]
    if option_slctd2 == 1:
        dff = dff[dff["Medu"] == option_slctd3]
    else:
        dff = dff[dff["Fedu"] == option_slctd3]



    fig = px.density_heatmap(
        data_frame=dff,
        x='guardian',
        y='reason',
        title='Guardian and Reasons'

    )
    fig2 = px.pie(
        data_frame=dff,
        names='age',
        title='Age Percentage',
        hover_name='age'
    )
    fig3 = px.bar(
        data_frame=dff,
        y='internet',
        title = 'Internet Availability'
    )
    fig4 = px.histogram(
        data_frame=dff,
        x='Mjob',
        facet_col_spacing= 0.5,
        facet_row_spacing= 0.7,
        title='Mother Job'
    )
    fig5 = px.histogram(
        data_frame=dff,
        x='Fjob',
        facet_col_spacing=0.5,
        facet_row_spacing=0.7,
        title='Father Job'
    )
    fig6 = px.scatter(
        data_frame=dff,
        x='traveltime',
        y='age',
        title='Travel time to school'
    )

    return container, fig, fig2, fig3, fig4, fig5, fig6
if __name__ == '__main__':
    app.run_server(debug=True)