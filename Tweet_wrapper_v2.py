#!/usr/bin/env python
# coding: utf-8




# !pip install -U -q tweepy
# !pip install -U -q emoji
# !pip install -U PyGithub
# !pip install -U -q tqdm

import pandas as pd
import time
import datetime
import os
import subprocess
from optparse import OptionParser
import sys


try:
    import tweepy
    import emoji
    from github import Github
    from github import InputGitAuthor
    from tqdm import tqdm
    from requests_oauthlib import OAuth1Session
    
except ImportError as error:
    print(error)
    print("""Se requieren los siguientes módulos:
          -> tweepy             (pip install -U -q tweepy)
          -> emoji              (pip install -U -q emoji)
          -> github             (pip install -U -q PyGithub)
          -> tqdm               (pip install -U -q tqdm)
          -> requests_oauthlib  (pip install -U -q requests-oauthlib)""")
    sys.exit()
    

# Process command-line options
parser = OptionParser(add_help_option=False)

# General options
parser.add_option('-h', '--help', action='store_true', help='Show this help message and exit.')
parser.add_option('-t', '--today', action='store_true', help='Extraer tweets de fecha actual')
parser.add_option('-d', '--day', type='int',  help='Días hacia atrás desde la fecha actual para recoger tweets')
parser.add_option('-c', '--count', type= 'int', help = 'Número de tweets a extraer por usaurio. Cuanto mayor más tiempo de ejecución')
parser.add_option("--tweets_source_info", action = 'store_true', help = "Muestra los usuario s de twitter empleados en la búsqueda")
parser.add_option("--git_token",  type= "str", help = "Token necesaria para acceder al repositorio de Github donde guardar los resultados")
parser.add_option("--git_repo",  type = "str", help = "Repositorio donde se desea guardar el archivo json generado tras la extracción de tweets")
parser.add_option("--git_autor",  type = "str", help = "Autor de los cambios realizados en el repositorio de Github")
parser.add_option("--git_autor_email", type = "str", help = "E-mail deñ Autor de los cambios realizados en el repositorio de Github")


(options, args) = parser.parse_args()

def print_usage():
    print("""
Información:
    Script que se encarga de extraer los tweets de diversas cuentas seleccionadas
    previamente a mano. La extracción de tweets se realiza mediante tweepy. 
    
    Es importante señalar que Twitter tiene unas "Rate limits". Entre ellas
    sólo deja realizar 180 requests en una ventana de 15 minutos. Una vez
    hayan pasado los 15 minutos después de la primera búsqueda, se vuelve a
    disponer de 180 requests. Esta es la razón por la que la extracción de tweets
    puede llevar algo de tiempo. No obstante, en el código se controla esta espera, 
    permitiendo que una vez hayan pasado los 15 minutos, se reanude la extracción
    de tweets.
    
    Señalar también que Twitter sólo deja extraer los tweets de hasta 7-daís 
    de antigüedad. El código está preparado para extraer los tweets del día 
    actual, del día anterior o un día disponible (más información abajo).

    Los tweets extraídos se guardan en formato json. Las cuentas que no dispogan
    de tweets no cren ningún archivo json. La información en los ficheros json es:
        - nombre de la cuenta
        - identificador del tweet
        - texto completo (tanto de tweet como retweet)
        - información sobre si la cuenta está verificada
        - fecha de creación del tweet
        - nº de veces que ha sido retweet
        - nº de veces que ha sido marcado como favorito
        - localización del tweet
        - url a la cuenta del usuario
        - entidades del tweets (enlaces, hastags etc)

Uso: 
    python Tweet_wrapper_v2.py [options]

Options:
    -t, --today              Recogemos los tweets de la fecha actual.
    -d, --day                Recogemos los tweets de la fecha "d" días atrás a la actual siendo 1 ayer. Type: int
    -c, --count              Indicamos la cantidad máxima de tweets que queremos extraer de cada usuario o hastag    
    --git_token              Token necesario para poder acceder al repositorio de Github
    --git_repo               Dirección del repositorio donde se desea guardar los archivos json con los tweets
    --tweets_source_info     Información sobre las cuentas de Twitter sobre las que se buscarán Tweets
    --git_autor              Autor de los cambios realizados en el repositorio de Github
    --git_autor_email        E-mail del autor de los cambios realizados en el repositorio de Github

Ejemplo. Cogemos hasta 100 tweets con la fecha del día de hoy:
    python Tweet_wrapper_v2_v2.py -t -c 100 --git_token XXX --git_repo Huertas97/tweets_collection""")
    sys.exit()

def print_tweets_source_info():
    print("""Las cuentas de Twitter de las que extraemos los tweets son:
    
    Hastags
    #Plandemia
    #yonomeconfino
    #coronatimo
    #YoNoMeVacuno
    #covid1984
    #NoalaVacuna
    #VirusChino
    #VacunaRusa
    #PCRFraude
    #coronavirus
    #covid
    #vaccine
    #pfizer
    #moderna
    #biontech
    #notovaccine
    #notonewnormal
    #antivacunas
    #VaccinesSaveLives
    #BillGates
    #ChinaVirus
    
    # No fiable
    @No__Plandemia
    @ANTIMASCARILLA
    @FoxMuld88326271
    @PericoAFuego
    @DiegoMo53772865
    @the_raven77
    @LRsecreta
    @JL_MDesconocido
    @AtraviesaLoDesc
    @HomeopatiaY
    @NaturopatasCol
    @MiHerbolario
    @HerbolarioLola
    @PacienteL
    @elphabaz
    @IsTortugo
    @tecn_preocupado
    @BabylonDab
    @lamjort
    @VaccineXchange
    @gonzo_blogger
    @CarmCerb21
    @panguerrera1
    @AlbaGar74381296
    @MediterraneoDGT
    @JosPastr
    @velardedaoiz2
    @JordiFlynn
    @mitokondriac
    @AquAhora1
    @patrilaselma
    @doctor_papaya
    @Autnomacabread1
    @LaRetuerka
    @DathosBD
    @PorunChileDigno
    @1333Despierta
    @NoHayPandemia__
    @Musicolorista
    @ELMINIMALISTA1
    @Africamar
    @informate_infor
    @ElTrompetista78
    @Angelisimo2
    @_nWorder
    @papayaykware
    @trustdall271
    @elentirvigo
    @ProgreAzote
    
    
    # No fiable satira
    @elmundotoday
    @eljueves
    @LaVozdelBecario
    @HayNoticia
    @FrayJosepho
    @ChiguireBipolar
    @actualidadpanam
    @revisbarcelona
    @thecliniccl
    
    
    # dudoso, precipitado
    @tiramillas
    @20m
    @okdiario
    @ActualidadRT
    @ldpsincomplejos
    @hermanntertsch
    @NiusDiario
    @LaVozIberica
    @periodistadigit
    @CancerIntegral
    
    # Dudoso porque es traducción de Donald Trump
    @POTUS_Trump_ESP

    # Fiable, organizaciones
    @SaludPublicaEs
    @sanidadgob
    @andaluciadatos
    @opsoms
    @WHO
    @AEMPSGOB
    @FDAenEspanol
    @CDCespanol
    @policia
    @guardiacivil
    
    # Fiable, verificadores
    @malditobulo
    @maldita_ciencia
    @EFEVerifica
    @Chequeado
    @Newtral
    @FullFact
    @ElSabuesoAP
    @cotejoinfo
    @ECUADORCHEQUEA
    @lasillavacia
    
    
    # Periodicos Latino América
    @JustiaLatinAmer
    @14ymedio
    @ReutersLatam
    @UniNoticias
    @Pajaropolitico
    @elcomerciodigit
    @prensa_libre
    @ABCDigital
    @ObservadorUY
    @Milenio
    @ElMercurio_cl
    @elcomerciocom
    @ElMundoBolivia
    @laprensa
    @elespectador
    
    # Periodicos España
    @el_pais
    @eldiarioes
    @elmundoes
    @EFEnoticias
    @abc_es
    @telediario_tve
    @24h_tve
    
    # Periodicos Internacionales
    @bbcmundo
    
    # Periodicos médicos
    @diariomedico
    @Consalud_es
    @redaccionmedica
    @VaccineSafetyN
       """)
    sys.exit()

def process_time(api):
    """
    Función encargada de extraer el nº de request restantes permitidas por
    la API de Twitter. También indica cuando se renueva la ventana temporal
    para continuar la extracción de tweets.

    Parameters
    ----------
    api : API object
        sesión de la API

    Returns
    -------
    None.

    """
    # Get the number of remaining requests
    remaining = int(api.last_response.headers['x-rate-limit-remaining'])
    print("Requests restantes:", remaining)
    reset = int(api.last_response.headers['x-rate-limit-reset'])
    reset = datetime.datetime.fromtimestamp(reset)
    print("La ventana temporal se resetea a ", reset)

def tweet_collect(user_name, text_query, since_date,  count, language, result_type):
    """
    Función encargada de hacer la request a Twitter de un usuario y recoger sus
    tweets.

    Parameters
    ----------
    user_name : string
        Nombre de la cuenta de Twitter
    text_query : string
        Filtros que aplicar a la búsqueda. Ej. "from: Usuario" solo busca en
        ese usuario
    since_date: datetime
        Fecha desde la cual se extraen tweets (desde esa fecha incluída hacia
        adelante)
    count : int, optional
        Número de tweets que queremos extraer. The default is 200
    language : string, optional
        Filtro de lenguaje del tweet. The default is "es".

    Returns
    -------
    tweets_df : pandas data frame
        Data Frame que contiene tweets en las filas y en las columnas: el id,
        el texto completo, la verificación de la cuenta, la fecha de creación,
        la localización el url de la cuenta y las entidades de cada tweet
        extraído.

    """
    
    query = text_query + user_name
    

    
    print("\nExtrayendo tweets de {0}, con la fecha: {1}".format(user_name, since_date.date()))
    next_day = since_date  + datetime.timedelta(1)
    try:
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.search,
                               q=query,
                               lang=language,
                               tweet_mode='extended',
                               result_type = result_type,
                               until = next_day.date()
                               ).items(count)
        
        # Extraemos la información de cada tweet
        tweets_list = []
        for tweet in tweets:
            if  since_date.date() == tweet.created_at.date():
                # Cojo todo el texto. Adaptado ha si es RT o tweet propio
                if 'retweeted_status' in tweet._json:
                    is_retweet = True
                    full_text = tweet._json['retweeted_status']['full_text']
                else:
                    is_retweet = False
                    full_text = tweet.full_text
                tweets_list.append([tweet.user.screen_name,
                                        tweet.id,
                                        is_retweet,
                                        full_text,
                                        tweet.user.verified,
                                        str(tweet.created_at),
                                        tweet.retweet_count, 
                                        tweet.favorite_count,
                                      #  tweet.reply_count, 
                                       # tweet.retweeted_status,
                                        tweet.user.location,
                                        tweet.user.url,
                                        tweet.entities
                                        ])
        # Mostramos el nº de request y ventana temporal disponible en la API
        process_time(api)
        # Creamos data frame
        print("Número de tweets extraídos:", len(tweets_list))
        if len(tweets_list) != 0:
            # Creation of dataframe from tweets list
            tweets_df = pd.DataFrame(tweets_list, columns=["screen_name",
                                                           "tweet_id",
                                                           "is_retweet",
                                                           "text",
                                                           "user_verified",
                                                           "created_at",
                                                           "retweet_count",
                                                           "favorite_count",
                                                          #  "reply_count",
                                                          # "retweet_status",
                                                           "user_location",
                                                           "user_url",
                                                           "entities"])
            # Procesamos los emojis a unicode
            tweets_df["text"] = tweets_df["text"].apply(emoji.demojize)
            
            return tweets_df
        else:
            pass

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)


def push(path, message, content, author, author_mail, branch = "main"):
    """
    Función encargada de subir los archivos encontrados a Github.

    Parameters
    ----------
    path : string
        Ruta del archivo que queremos subir.
    message : string
        Mensaje que queremos emplear para el commit.
    content : json
        Contenido del archivo que queremos subir a Github.
    branch : string, optional
        Rama donde queremos hacer push. The default is "main".

    Returns
    -------
    None.

    """
    author = InputGitAuthor(
        author,
        author_mail
    )
    try:   # If file already exists, update it
        # Retrieve old file to get its SHA and path
        contents = repo.get_contents(path, ref=branch)
        repo.update_file(contents.path,
                         message,
                         content,
                         contents.sha,
                         branch=branch,
                         author=author)  # Add, commit and push branch
        print("Update:", path)
        print()
    except:    # If file doesn't exist, create it
        repo.create_file(path,
                         message,
                         content,
                         branch=branch,
                         author=author)  # Add, commit and push branch
        print("Creating:", path)
        print()


# Number of option arguments. First arguments is always the own file name
numOpts = len(sys.argv)

# No options... print help.
if numOpts < 2:
    print_usage()
elif options.help:
    print_usage()
    
if options.today: #  and not options.yesterday: 
    # Creamos la fecha correspondiente al día empezando en 00:00h
    now_datetime = datetime.datetime.now()
    since_date = now_datetime.replace(hour=23, minute=59, second=59,
                                      microsecond=999999)
    
if options.day:
    since_date = datetime.datetime.now() - datetime.timedelta(options.day)
    since_date = since_date.replace(hour=23, minute=59, second=59, 
                                   microsecond=999999)
if not options.count:
    options.count = 200
    
if options.tweets_source_info:
    print_tweets_source_info()

# CREDENTIALS
api_key = "h50aoVmiuNFuHI8o3dZE7C15N"
api_secret_key = "Dz6jeUBUdGp43uJugObOgIqnVdCbUrbrkwkcjAibmlDQwq6sdL"
access_token = "1311739853307027457-HqUEzNSGtzdFqkFDFmdYg5UcMEjPv2"
access_token_secret = "iabmz6wZ0gucIodSNJ9TfSfnrT17yJXjDAu13y4QF8hLI"


if options.git_token and options.git_repo:
    g = Github(options.git_token)
    repo = g.get_repo(options.git_repo)
else:
    print("\nImportante: Se requiere un repositorio de GitHub y un Token de acceso")
    print_usage()
    
if options.git_autor:
    autor = options.git_autor
else:
    autor = "Huertas97"

if options.git_autor_email:
    email = options.git_autor_email
else:
    email = "ahuertasg01@gmail.com"
    





# STARTING API
twitter = OAuth1Session(api_key,
                        client_secret=api_secret_key,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)

# OAuth 1a (application-user). Rate limit: 180 requests in 15 min window
# auth = tweepy.OAuthHandler(api_key, api_secret_key)
# auth.set_access_token(access_token, access_token_secret)

# OAuth 2 (application-only). Rate limit: 450 requets in 15 min window
auth = tweepy.AppAuthHandler(api_key, api_secret_key)

# When we set wait_on_rate_limit to True, we will have our program wait
# automatically 15 minutes so that Twitter does not lock us out, whenever we
# exceed the rate limit and we automatically continue to get new data!
api = tweepy.API(auth, wait_on_rate_limit=True)


# usurarios de los que recoger tweets
dic_user = {
    # Hastags
    "Plandemia": ["es", "#", "mixed"],
    "yonomeconfino": ["es", "#", "mixed"],
    "coronatimo": ["es", "#", "mixed"],
    "YoNoMeVacuno": ["es", "#", "mixed"],
    "covid1984": ["es", "#", "mixed"],
    "NoalaVacuna": ["es", "#", "mixed"],
    "#VirusChino": ["es", "#", "mixed"],
    "#VacunaRusa": ["es", "#", "mixed"],
    "#PCRFraude": ["es", "#", "mixed"],
    "#FactCHAT": ["en", "#", "mixed"],
    "#FakePCR": ["es", "#", "mixed"],
    # infodemia 
    
    
    # No fiable
    "No__Plandemia": ["es", "from:"],
    "ANTIMASCARILLA": ["es", "from:"],
    "FoxMuld88326271": ["es", "from:"],
    "PericoAFuego": ["es", "from:"],
    "DiegoMo53772865": ["es", "from:"],
    "the_raven77": ["es", "from:"],
    "LRsecreta": ["es", "from:"],
    "JL_MDesconocido": ["es", "from:"],
    "AtraviesaLoDesc": ["es", "from:"],
    "HomeopatiaY": ["es", "from:"],
    "NaturopatasCol": ["es", "from:"],
    "MiHerbolario": ["es", "from:"],
    "HerbolarioLola": ["es", "from:"],
    "PacienteL": ["es", "from:"],
    "elphabaz": ["es", "from:"],
    "IsTortugo": ["es", "from:"],
    "tecn_preocupado": ["es", "from:"],
    "BabylonDab": ["es", "from:"],
    "lamjort": ["es", "from:"],
    "VaccineXchange": ["en", "from:"],
    "gonzo_blogger": ["es", "from:"],
    "CarmCerb21": ["es", "from:"],
    "panguerrera1": ["es", "from:"],
    "AlbaGar74381296": ["es", "from:"],
    "MediterraneoDGT": ["es", "from:"],
    "JosPastr": ["es", "from:"],
    "velardedaoiz2": ["es", "-filter:replies AND-filter:retweet AND from:"],
    "JordiFlynn": ["es", "(coronavirus OR cov OR covid OR sars) AND from:"],
    "mitokondriac": ["es", "from:"],
    "AquAhora1": ["es", "from:"],
    "patrilaselma": ["es", "from:"],
    "doctor_papaya": ["es", "from:"],
    "Autnomacabread1": ["es", "(virus OR coronavirus OR covid OR sars) AND from:"],
    "LaRetuerka": ["es", "from:"],
    "DathosBD": ["es", "-filter:replies AND (virus OR coronavirus OR covid OR sars) AND from:"],
    "PorunChileDigno": ["es", "-filter:replies AND from:"], # Chile
    "1333Despierta": ["es", "-filter:replies AND from:"],
    "NoHayPandemia__": ["es", "-filter:replies AND from:"],
    "Musicolorista": ["es", "-filter:replies AND from:"],
    "ELMINIMALISTA1": ["es", "-filter:replies AND from:"],
    "Africamar": ["es", "-filter:replies  AND from:"],
    "informate_infor": ["es", "-filter:replies  AND from:"],
    "ElTrompetista78": ["es", "-filter:replies  AND from:"],
    "Angelisimo2": ["es", "-filter:replies  AND from:"],
    "_nWorder": ["es", "-filter:replies  AND from:"],
    "papayaykware": ["es", "-filter:replies  AND from:"],
    "trustdall271": ["es", "-filter:replies AND from:"],
    "elentirvigo": ["es", "-filter:replies AND from:"],
    "ProgreAzote": ["es", "-filter:replies AND from:"],
    "The_Cling_On": ["en", "from:"], # Australia
    
    
    # No fiable satira
    "elmundotoday": ["es", "from:"],
    "eljueves": ["es", "from:"],
    "okdiario": ["es", "from:"],
    "LaVozdelBecario": ["es", "from:"],
    "HayNoticia": ["es", "from:"],
    "FrayJosepho": ["es", "from:"],
    "ChiguireBipolar": ["es", "from:"], # Venezuela
    "actualidadpanam": ["es", "from:"],# Colombia
    "revisbarcelona": ["es", "from:"],# Argentina
    "thecliniccl": ["es", "from:"],# Chile
    "TheBabylonBee": ["en", "from:"], # US 
    "TheOnion": ["en", "from:"], # US 
    
    
    
    # dudoso, precipitado
    "tiramillas": ["es", "from:"],
    "20m": ["es", "from:"],
    "ActualidadRT": ["es", "from:"],
    "ldpsincomplejos": ["es", "-filter:replies AND from:"],
    "hermanntertsch": ["es", "-filter:replies AND -filter:retweet AND from:"],
    "NiusDiario": ["es", "from:"], # no es tan dudoso pero habría que chequear
    "LaVozIberica": ["es", "from:"],
    "periodistadigit": ["es", "from:"],
    "CancerIntegral": ["es", "from:"],
    
    # Dudoso porque es traducción de Donald Trump
    "POTUS_Trump_ESP": ["es", "-filter:replies AND -filter:retweet AND from:"],
    
    # Fiable, organizaciones
    "SaludPublicaEs": ["es", "from:"],
    "sanidadgob": ["es", "from:"],
    "andaluciadatos": ["es", "from:"],
    "opsoms": ["es", "from:"],
    "WHO": ["en", "from:"],
    "AEMPSGOB": ["es", "from:"],  # agencia española del medicamento
    "FDAenEspanol": ["es", "from:"],
    "CDCespanol": ["es", "from:"],
    "policia": ["es", "from:"],
    "guardiacivil": ["es", "from:"],
    "US_FDA": ["en", "from:"],
    "FDA_Drug_Info": ["en", "from:"],
    "FDArecalls": ["en", "from:"],
    "CDCgov": ["en", "from:"],
    "NIH": ["en", "from:"],
    "NEJM": ["en", "from:"],
    "HopkinsMedicine": ["en", "from:"],
    "MayoClinic": ["en", "from:"],
    
    # Revistas cientificas
    "NatureComms": ["en", "from:"],
    "researchnews": ["en", "from:"],
    "CellPressNews": ["en", "from:"],
    "TrendsMolecMed": ["en", "from:"],
    "embojournal": ["en", "from:"],
    
    # Fiable, verificadores
    "malditobulo": ["es", "from:"], # España
    "maldita_ciencia": ["es", "from:"], # España
    "EFEVerifica": ["es", "from:"], # España
    "Chequeado": ["es", "from:"], # Argentina
    "Newtral": ["es", "from:"], # España
    "FullFact":  ["en", "from:"], # Inglés
    "ElSabuesoAP": ["es", "from:"], # Mexico
    "cotejoinfo": ["es", "from:"], # Venezuela
    "ECUADORCHEQUEA": ["es", "from:"], # Ecuador
    "lasillavacia": ["es", "from:"], # Colombia
    "AP": ["en", "from:"], # US
    "AfricaCheck": ["en", "from:"], # Africa
    "aosfatos": ["pt", "from:"], # Brasil
    "AAPNewswire": ["en", "from:"], # Australia
    "boomlive_in": ["en", "from:"], # India
    "correctiv_org": ["de", "from:"], # Alemania
    "Check_Your_Fact": ["en", "from:"], # USA
    "CheckCongo": ["fr", "from:"], # Congo
    "DemagogPL": ["pl", "from:"], # Polonia
    "dubawaNG": ["en", "from:"], # Nigeria
    "estadaoverifica": ["pt", "from:"], # Brasil
    "FactlyIndia": ["en", "from:"], # India
    "FactCrescendo": ["en", "from:"], # India
    "FactCheckNI": ["en", "from:"], # United Kingdom
    "ghana_fact": ["en", "from:"], # Ghana
    "Fatabyyano_com": ["ar", "from:"], # Jordania
    "FerretScot": ["en", "from:"], # United Kingdom (Scotland)
    "Observateurs": ["fr", "from:"], # Francia
    "lemondefr": ["fr", "from:"], # Francia
    "CheckNewsfr": ["fr", "from:"], # Australia
    "LogicallyAI": ["en", "from:"], # United Kingdom
    "MaharatNews": ["ar", "from:"], # Libano
    "Poynter": ["en", "from:"], # Internacional
    "mediawise": ["en", "from:"], # USA
    "NewsMobileIndia": ["en", "from:"], # India
    "NewsMeter_In": ["en", "from:"], # India
    "observadorpt": ["pt", "from:"], # Portugal
    "PesaCheck": ["en", "from:"], # Kenya
    "JornalPoligrafo": ["pt", "from:"], # Portugal
    "ABCFactCheck": ["en", "from:"], # Australia
    "rapplerdotcom": ["en", "from:"], # Filipinas
    "ReutersAgency": ["en", "from:"], # United States
    "ClimateFdbk": ["en", "from:"], # France
    "eye_digit": ["en", "from:"], # India
    "SouthAsiaCheck": ["en", "from:"], # Nepal
    "StopFakingNews": ["ru", "from:"], # Ucrania
    "IndiaToday": ["en", "from:"], # India
    "factchecknet": ["en", "from:"], # Internacional
    "thedispatch": ["en", "from:"], # USA
    "ThipMedia": ["en", "from:"], # India
    "TheQuint": ["en", "from:"], # India
    "GlennKesslerWP": ["en", "from:"], # chief writer of Washington Post's Fact Checker
    "thejournal_ie": ["en", "from:"], # Ireland
    "USATODAY": ["en", "from:"], # USA
    "verafiles": ["en", "from:"], # Filipinas
    "newsvishvas": ["en", "from:"], # India
    "dpa": ["de", "from:"], # Alemania
    "dogrulukpayicom": ["tr", "from:"], # Turquia
    "PagellaPolitica": ["it", "from:"], # Italia
    "teyitorg": ["tr", "from:"], # Turquia
    "NUnl": ["nl", "from:"], # Holanda
    "snopes": ["en", "from:"], # USA
    "franceinfo": ["fr", "from:"], # France
    
    
    # Periodicos Latino América
    "JustiaLatinAmer": ["es", "from:"], # Latino América
    "ReutersLatam": ["es", "from:"], # Latino América
    "UniNoticias": ["es", "from:"], # Latino América
    "14ymedio": ["es", "from:"], # Cuba
    "prensa_libre": ["es", "from:"], # Guatemala (Recomendado por The Guardian)
    "ABCDigital": ["es", "from:"], # Paraguay (Recomendado por The Guardian)
    "ObservadorUY": ["es", "from:"], # Urugay (Recomendado por The Guardian) 
    "Milenio": ["es", "from:"], # México (Recomendado por The Guardian)
    "ElMercurio_cl": ["es", "from:"], # Chile (Recomendado por The Guardian)
    "elcomerciocom": ["es", "from:"], # Ecuador (Recomendado por The Guardian)
    "ElMundoBolivia": ["es", "from:"], # Bolivia (Recomendado por The Guardian)
    "laprensa": ["es", "from:"], # Nicaragua (Recomendado por The Guardian)
    "elespectador": ["es", "from:"], # Colombia (Recomendado por The Guardian)
    
    # Periodicos Latino América reconocidos
    "Pajaropolitico": ["es", "from:"], # reconocido por Poynter
    "elcomerciodigit": ["es", "from:"], # The Trust Project Perú
    "LANACION": ["es", "from:"], # The Trust Project Argetina
    "ElUniversal": ["es", "from:"], # The Trust Project Venezuela
    
    # Periodicos US
    "nytimes": ["en", "from:"], # US
    "AmPress": ["en", "from:"], # US
    
    # Periodicos España
    "el_pais": ["es", "from:"],
    "eldiarioes": ["es", "from:"],
    "elmundoes": ["es", "from:"],
    "EFEnoticias":  ["es", "from:"],
    "abc_es": ["es", "from:"],
    "telediario_tve": ["es", "from:"],
    "24h_tve": ["es", "from:"],
    
    # Periodico internacional
    "bbcmundo": ["es", "from:"], # Internacional
    
    # Periodicos médicos España
    "diariomedico": ["es", "from:"],
    "Consalud_es": ["es", "from:"],
    "redaccionmedica": ["es", "from:"],
    "VaccineSafetyN": ["en", "from:"]

}

dic_user = {
    # Hastags
     "US_FDA": ["en", "from:"]
         
    }


# today = datetime.date.today()
date = since_date.date()
print(date)

for key, value in tqdm(dic_user.items(), desc="Progess"):
    user_name = key
    language = value[0]
    text_query = value[1]
    try:
        result_type = value[2]
    except:
        result_type = "recent"
    tweets_df = tweet_collect(count = options.count,
                              language = language,
                              text_query = text_query,
                              user_name = user_name,
                              result_type = result_type,
                              since_date=since_date
                              )
    # If a df is returned push it
    if isinstance(tweets_df, pd.DataFrame):
        local_file_name = user_name+"-"+str(date)+".json"
        git_file_name = user_name+"-"+str(date)+".txt"
        
        # Pandas df to json format
        tweets_df.to_json(local_file_name)
        # Extract tweets_id and save it as txt
        tweets_df["tweet_id"].to_csv(git_file_name, header=None, index=None, sep=' ', mode='w')
        
        # create folders and move json file to that folder by date
        subprocess.call(['mkdir',"-p", "./tweets/" + str(date)])
        subprocess.call(['mv',  git_file_name,  './tweets/'+ str(date)])
        
        subprocess.call(['mkdir',"-p", "../local_tweets/" + str(date)])
        subprocess.call(['mv',  local_file_name,  '../local_tweets/'+ str(date)])
        
        
        # Create path to reach the file to push
        path = os.path.join(".", "tweets", str(date), str(git_file_name)).replace("\\","/") 
        
        # GitHub will only receive tweets ids (Twitter Privacy Conditions)
        # Extract the content to push
        file_content = open(path, "r").read()
        push(path = path, message = "Tweets from: " + str(date), content = file_content,
             author = autor, author_mail = email)
    
