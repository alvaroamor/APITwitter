import dash
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from twarc import Twarc2
import tweepy
import webbrowser
import requests
from pandas import json_normalize 
import json
import ast
from datetime import date
import dash_daq as daq



colors = {
    'background': '#082255',
    'text': '#FFFFFF',
}
# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 60,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    'padding': '20px 10px',
    'background-color': '#061e44'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p',
    'background':  '#061e44'
    }

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#FFFFFF'
}

controls = dbc.Form(
    [
        dbc.Row([dbc.Col([html.P('Palabra a buscar: ', style={
            'textAlign': 'center', 'color': '#FFFFFF'
        }),
        dcc.Input(id='input-on-submit', type='text', value='ucam',style={
            'textAlign': 'center'
        })]), dbc.Col()]),

    ]
)

controls2 = dbc.Form(
    [
        
        dbc.Row([dbc.Col([html.P('PIN uso API: ', style={
            'textAlign': 'center', 'color': '#FFFFFF'
        }),
        dcc.Input(id='input4', type='text', value=' ',style={
            'textAlign': 'center'
        })]), dbc.Col([
        html.Br(),dbc.Button('1.Obtener PIN',
            id='show-secret3',
            n_clicks=0, 
            color='primary'
        )])]),

           html.Br(),
        
        dbc.Row([dbc.Col([html.P('Hashtag a buscar: ', style={
            'textAlign': 'center', 'color': '#FFFFFF'
        }),
        dcc.Input(id='input2', type='text', value=' ',style={
            'textAlign': 'center'
        })]), dbc.Col([
        html.Br(),dbc.Button('2.Obtener Hashtag',
            id='show-secret',
            n_clicks=0, 
            color='primary'
        )])]),
        html.Br(),

        dbc.Row([dbc.Col([html.P('Fecha desde la que desea buscar: ', style={
            'textAlign': 'center', 'color': '#FFFFFF'
        }),
        dcc.DatePickerSingle(id='input3',
            date=date(2022, 1, 21),
            display_format='YYYY-M-DD')]), 
            dbc.Col()]),
    ]
)

controls3 = dbc.Form(
    [

        dbc.Row([dbc.Col([html.P('Nombre de Usuario: ', style={
            'textAlign': 'center', 'color': '#FFFFFF'
        }),
        dcc.Input(id='input5', type='text', value='',style={
            'textAlign': 'center'
        })]), dbc.Col([
        html.Br(),dbc.Button('Followers',
            id='show-secret2',
            n_clicks=0, 
            color='primary'
        )])]),
    ]
)

controls4 = dbc.Form(
    [

        dbc.Row([dbc.Col([html.P('Nombre de Usuario: ', style={
            'textAlign': 'center', 'color': '#FFFFFF'
        }),
        dcc.Input(id='input6', type='text', value='',style={
            'textAlign': 'center'
        })]), dbc.Col([
        html.Br(),dbc.Button('Mes',
            id='show-secret4',
            n_clicks=0, 
            color='primary'
        )])]),
    ]
)


sidebar = html.Div(
    [
        html.H2('Parámetros', style=TEXT_STYLE),
        html.Hr(style={
            'backgroundColor': '#FFFFFF'
        }),
        html.Div(id='creation2', style={
            'backgroundColor': '#061e44'
        })

    ],
    style=SIDEBAR_STYLE
)


content_second_row = dbc.Row(
    [
        dbc.Col(
             dcc.Graph(
                    id='example-graph-2',
                         figure={}
             ),
        ),
        
    ]
)

content_third_row = dbc.Row(
    [
        html.Hr(),
        dcc.Loading(id="loading-2",
        children = [html.Div(id='textarea-example-output2', style={'whiteSpace': 'pre-line'})], type = "circle")
    ]
)

content_fifth_row = dbc.Row(
    [
        html.Hr(),
        dcc.Loading(id="loading-1",
        children = [html.Div(id='textarea-example-output4', style={'whiteSpace': 'pre-line'})], type = "circle")
    ]
)

content_fourth_row = dbc.Row(
    [
        html.Hr(),
        html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'}),
        dcc.Loading(id="loading-3",
        children = [html.Div(id='textarea-example-output3', style={'whiteSpace': 'pre-line'})], type = "circle")
        
    ]
)
content2 = html.Div([
        html.Br(),
        html.H2('Tus seguidores con más followers en Twitter', style=TEXT_STYLE),
        html.Hr(style={
            'backgroundColor': '#FFFFFF'
        }),
        html.Br(),
        content_third_row,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
         html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

],  style=CONTENT_STYLE)

content3 = html.Div([
        html.Br(),
        html.H2('Tweets que contienen tu hashtag ordenados', style=TEXT_STYLE),
        html.Hr(style={
            'backgroundColor': '#FFFFFF'
        }),
        html.Br(),
        content_fourth_row,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
         html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

],  style=CONTENT_STYLE)

content4 = html.Div([
        html.Br(),
        html.H2('Resumen de tu último mes', style=TEXT_STYLE),
        html.Hr(style={
            'backgroundColor': '#FFFFFF'
        }),
        html.Br(),
        content_fifth_row,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
         html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

],  style=CONTENT_STYLE)



content = html.Div(
    [   html.Br(),
        html.H2('Número de tweets por hora', style=TEXT_STYLE),
        html.Hr(style={
            'backgroundColor': '#FFFFFF'
        }),
        #content_first_row,
        html.Br(),
        content_second_row,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        
        

    ],
    style=CONTENT_STYLE,
)

footer = html.Footer('Made by: Álvaro Amor García', style= {'backgroundColor': '#061e44', 'textAlign': 'center',
    'color': '#FFFFFF'})

header = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    dbc.Col(dbc.NavbarBrand("Twitter API", className="ms-2")),
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dcc.Location(id='url', refresh=False),
                    dbc.Collapse(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Tweets", href='/')),
                                dbc.NavItem(dbc.NavLink("Hashtag", href='/page-3')),
                                dbc.NavItem(dbc.NavLink("Month", href='/page-4')),
                                dbc.NavItem(
                                    dbc.NavLink("Followers", href='/page-2'),
                                    # add an auto margin after page 2 to
                                    # push later links to end of nav
                                    className="me-auto",
                                ),
                                dbc.NavItem(dbc.NavLink("Help")),
                                dbc.NavItem(dbc.NavLink("About")),
                            ],
                            # make sure nav takes up the full width for auto
                            # margin to get applied
                            className="w-100",
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                # the row should expand to fill the available horizontal space
                className="flex-grow-1",
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color="dark",
    fixed=True,
)

body= html.Div(id='creation', style={
            'backgroundColor': '#061e44'
        })




app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([header, sidebar, body, footer], style={
            'backgroundColor': '#061e44'
        })

app.title = 'Twitter API'
app.validation_layout = html.Div([
    sidebar, content
])

consumer_key = "lerGpwvPLv2NmdWgqTVxV2HS1"
consumer_secret = "lVB3lpOK80dYdmpQkswA4WFlePzvb8MdfSzLMgzsxXuKMAdCq8"
callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)

@app.callback(Output('creation', 'children'),
              Output('creation2', 'children'),
              Input('url', 'pathname'))
              
def display_page(pathname):
    if pathname == "/page-2":
        return content2, controls3
    elif pathname == "/page-3":
        return content3, controls2
    elif pathname == '/page-4':
        return content4, controls4
    else:
        return content, controls


@app.callback(
    #Output('container-button-basic', 'children'),
    Output('example-graph-2', component_property='figure'),
    Input('input-on-submit', 'value'),
    
)

def test(values):

    try:
        client = Twarc2(bearer_token='AAAAAAAAAAAAAAAAAAAAADJ4YgEAAAAAFwk25e%2F81SqiGWgm1B%2FLJtlygjY%3DRKt05inoMkFCMzx4ABbRcRJvJMSP8bjXlIE1Kso0kxFj05nLL3')
        
        query = values
        #input("Introduce la palabra deseada")
        search_results = client.counts_all(query, granularity ='hour')
            # search_results = client.counts_recent(query, granularity ='hour')
        for page in search_results:

            data = page['data']
                

        day = []

        tweet_counts = []

        for d in data:
            day.append(d['start'][:40])
            tweet_counts.append(d['tweet_count'])

            
        fig = go.Figure(data=[go.Bar(x=day, y=tweet_counts)])
        
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
        )

        return fig
    except NameError:
        print("Error")
        
@app.callback(
    Output(component_id='textarea-example-output3', component_property='children'),
    Input(component_id='show-secret3', component_property='n_clicks'),
)

def testpin(n_clicks):

    if n_clicks >= 1:
        redirect_url = auth.get_authorization_url()
        webbrowser.open(redirect_url)
        print(redirect_url)
        
    

    return "OK"


@app.callback(
    Output(component_id='textarea-example-output', component_property='children'),
    Input(component_id='show-secret', component_property='n_clicks'),
    Input(component_id='input2', component_property='value'),
    Input(component_id='input3', component_property='value'),
    Input(component_id='input4', component_property='value')
)
    
def test2(n_clicks, word,date,pin):
    
    if n_clicks >= 1:

            
            user_pint_input = pin
            auth.get_access_token(user_pint_input)
            
            api = tweepy.API(auth, wait_on_rate_limit=True)
            words = word
            date_since= date
            numtweet = 100
                # Creating DataFrame using pandas
            db = pd.DataFrame(columns=['username',
                                        'description',
                                        'location',
                                        'following',
                                        'followers',
                                        'totaltweets',
                                        'retweetcount',
                                        'text',
                                        'hashtags'])
        
                # We are using .Cursor() to search
                # through twitter for the required tweets.
                # The number of tweets can be
                # restricted using .items(number of tweets)
            tweets = tweepy.Cursor(api.search_tweets,
                                    words, lang="en",
                                    since_id=date_since,
                                    tweet_mode='extended').items(numtweet)
        
            
                # .Cursor() returns an iterable object. Each item in
                # the iterator has various attributes
                # that you can access to
                # get information about each tweet
            listaordenada = []
            list_tweets = [tweet for tweet in tweets]
            
                # Counter to maintain Tweet Count
            i = 1
                
                # we will iterate over each tweet in the
                # list for extracting information about each tweet
            for tweet in list_tweets:
                
                    username = tweet.user.screen_name
                    description = tweet.user.description
                    location = tweet.user.location
                    following = tweet.user.friends_count
                    followers = tweet.user.followers_count
                    totaltweets = tweet.user.statuses_count
                    retweetcount = tweet.retweet_count
                    hashtags = tweet.entities['hashtags']

        
                        # Retweets can be distinguished by
                        # a retweeted_status attribute,
                        # in case it is an invalid reference,
                        # except block will be executed
                    text = tweet.full_text
                    hashtext = list()
                    for j in range(0, len(hashtags)):
                            hashtext.append(hashtags[j]['text'])
        
                        # Here we are appending all the
                        # extracted information in the DataFrame
                    ith_tweet = [username, description,
                                    location, following,
                                    followers, totaltweets,
                                    retweetcount, text, hashtext]

                    columnas = ["username", "description",
                                    "location", "following",
                                    "followers", "totaltweets",
                                    "retweetcount", "text", "hashtext"]

                    db.loc[len(db)] = ith_tweet
        
                        # Function call to print tweet data on screen
                        
                    i = i+1
                    listaordenada.append(ith_tweet)


                    #listaordenada = listaordenada + ith_tweet
            def Sort(listaordenada):
        
            # reverse = None (Sorts in Ascending order)
            # key is set to sort using second element of 
            # sublist lambda has been used
                listaordenada.sort(key = lambda x: x[6], reverse=True)
                return listaordenada



            print(Sort(listaordenada))

            df = pd.DataFrame(data=listaordenada, columns=columnas)
            print(df)
                    
            return dash_table.DataTable(df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            fixed_rows={'headers': True},
            page_size=20, style_table={'height': '300px', 'overflowY': 'auto'}
            ,style_data={'backgroundColor': '#082255', 'color': 'white'
    }, )


@app.callback(
    Output(component_id='textarea-example-output2', component_property='children'),
    Input(component_id='show-secret2', component_property='n_clicks'),
    Input(component_id='input5', component_property='value')
)
def test3(n_clicks, id):
    if n_clicks >= 1:
        

        bearer_token = "AAAAAAAAAAAAAAAAAAAAADJ4YgEAAAAAFwk25e%2F81SqiGWgm1B%2FLJtlygjY%3DRKt05inoMkFCMzx4ABbRcRJvJMSP8bjXlIE1Kso0kxFj05nLL3"
        
        def create_url2():
            # Replace with user ID below
            user_id = id
            return "https://api.twitter.com/2/users/by/username/{}".format(user_id)


        def bearer_oauth2(r):
            """
            Method required by bearer token authentication.
            """

            r.headers["Authorization"] = f"Bearer {bearer_token}"
            r.headers["User-Agent"] = "v2FollowersLookupPython"
            return r


        def connect_to_endpoint2(url2):
            response = requests.request("GET", url2, auth=bearer_oauth2)
            print(response.status_code)
            if response.status_code != 200:
                raise Exception(
                    "Request returned an error: {} {}".format(
                        response.status_code, response.text
                    )
                )
            return response.json()
        
        url2 = create_url2()
        json_response2 = connect_to_endpoint2(url2)
    
        username = json_response2['data']['id']

        def create_url():

            user_id = username
            return "https://api.twitter.com/2/users/{}/followers".format(user_id)


        def get_params():
            return {"user.fields": "public_metrics"}


        def bearer_oauth(r):
            """
            Method required by bearer token authentication.
            """

            r.headers["Authorization"] = f"Bearer {bearer_token}"
            r.headers["User-Agent"] = "v2FollowersLookupPython"
            return r


        def connect_to_endpoint(url, params):
            response = requests.request("GET", url, auth=bearer_oauth, params=params)
            print(response.status_code)
            if response.status_code != 200:
                raise Exception(
                    "Request returned an error: {} {}".format(
                        response.status_code, response.text
                    )
                )
            return response.json()
        
        url = create_url()
        params = get_params()
        json_response = connect_to_endpoint(url, params)
        
        
        df = json_normalize(json_response, 'data')
        
        df.sort_values(by=['public_metrics.followers_count'], ignore_index=True, inplace=True, ascending=False)

        return dash_table.DataTable(df.to_dict('records'), 
        [{"name": i, "id": i} for i in df.columns],
        fixed_rows={'headers': True},
        page_size=20, style_table={'width': 'auto', 'overflow': 'hidden'},
        style_cell={
        'width': '{}%'.format(len(df.columns))},style_data={'backgroundColor': '#082255', 'color': 'white'},
         style_as_list_view=True,)
        
@app.callback(
    Output(component_id='textarea-example-output4', component_property='children'),
    Input(component_id='show-secret4', component_property='n_clicks'),
    Input(component_id='input6', component_property='value')
)
def test3(n_clicks, username):
    if n_clicks >= 1:

        def create_twitter_url():
            handle = username
            max_results = 100
            mrf = "max_results={}".format(max_results)
            q = "query=from:{}".format(handle)
            url = "https://api.twitter.com/2/tweets/search/all?{}&{}".format(mrf, q)
            return url

        def twitter_auth_and_connect(bearer_token, url):
            headers = {"Authorization": "Bearer {}".format(bearer_token)}
            response = requests.request("GET", url, headers=headers)
            return response.json()

        def lang_data_shape(res_json):
            data_only = res_json["data"]
            doc_start = '"documents": {}'.format(data_only)
            str_json = "{" + doc_start + "}"
            dump_doc = json.dumps(str_json)
            doc = json.loads(dump_doc)
            return ast.literal_eval(doc)

        def connect_to_azure():
            azure_url = "https://tweetmining2.cognitiveservices.azure.com/"
            language_api_url = "{}text/analytics/v2.1/languages".format(azure_url)
            sentiment_url = "{}text/analytics/v2.1/sentiment".format(azure_url)
            subscription_key = "117b56e488b3477596d79ae86bacfb41"
            return language_api_url, sentiment_url, subscription_key

        def azure_header(subscription_key):
            return {"Ocp-Apim-Subscription-Key": subscription_key}

        def generate_languages(headers, language_api_url, documents):
            response = requests.post(language_api_url, headers=headers, json=documents)
            return response.json()

        def combine_lang_data(documents, with_languages):
            langs = pd.DataFrame(with_languages["documents"])
            lang_iso = [x.get("iso6391Name")
                        for d in langs.detectedLanguages if d for x in d]
            data_only = documents["documents"]
            tweet_data = pd.DataFrame(data_only)
            tweet_data.insert(2, "language", lang_iso, True)
            json_lines = tweet_data.to_json(orient="records")
            return json_lines

        def add_document_format(json_lines):
            docu_format = '"' + "documents" + '"'
            json_docu_format = "{}:{}".format(docu_format, json_lines)
            docu_align = "{" + json_docu_format + "}"
            jd_align = json.dumps(docu_align)
            jl_align = json.loads(jd_align)
            return ast.literal_eval(jl_align)

        def sentiment_scores(headers, sentiment_url, document_format):
            response = requests.post(
                sentiment_url, headers=headers, json=document_format)
            return response.json()

        def week_logic(week_score):
            if week_score > 0.75 or week_score == 0.75:
                return "Tuviste un mes positivo"
            elif week_score > 0.45 or week_score == 0.45:
                return "Tuviste un mes neutro"
            else:
                return "Tuviste un mes negativo, espero que vaya a mejor"

        def mean_score(sentiments):
            sentiment_df = pd.DataFrame(sentiments["documents"])
            return sentiment_df["score"].mean()

        
        
        url = create_twitter_url()
        bearer_token = "AAAAAAAAAAAAAAAAAAAAADJ4YgEAAAAAFwk25e%2F81SqiGWgm1B%2FLJtlygjY%3DRKt05inoMkFCMzx4ABbRcRJvJMSP8bjXlIE1Kso0kxFj05nLL3"
        res_json = twitter_auth_and_connect(bearer_token, url)
        documents = lang_data_shape(res_json)
        language_api_url, sentiment_url, subscription_key = connect_to_azure()
        headers = azure_header(subscription_key)
        with_languages = generate_languages(headers, language_api_url, documents)
        json_lines = combine_lang_data(documents, with_languages)
        document_format = add_document_format(json_lines)
        sentiments = sentiment_scores(headers, sentiment_url, document_format)
        week_score = mean_score(sentiments)
        print(week_score)
        retorno = week_logic(week_score)


        return html.H2([daq.LEDDisplay(id='our-LED-display',label="Tu resultado es:",value=week_score, color='#FFFFFF', backgroundColor='#082255'),html.Br(),html.H3(retorno)], style=TEXT_STYLE)

if __name__ == '__main__':
    app.run_server(port='8085')