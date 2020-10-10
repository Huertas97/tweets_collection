# **Autor** 
Álvaro Huertas García

# Índice
 
 * [TODO](##todo)
 * [Instrucciones para extraer los tweets](#instrucciones-para-extraer-los-tweets)
 * [Información del repositorio](#información-del-repositorio)

[![](https://mermaid-js.github.io/mermaid-live-editor/#/view/eyJjb2RlIjoiXG5ncmFwaCBMUlxuQShUd2l0dGVyIFVzZXJuYW1lKSAtLT4gQihUd2l0dGVyIEFQSSlcbkIgLS0gLmpzb24gZmlsZSAtLT4gRChVcGxvYWQgdG8gR2l0aHViKVxuXG5zdHlsZSBBIGZpbGw6I2Y1YzU0Mlxuc3R5bGUgQiBmaWxsOiNmNWM1NDJcbnN0eWxlIEQgZmlsbDojZjVjNTQyXG4iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCIsInRoZW1lVmFyaWFibGVzIjp7ImJhY2tncm91bmQiOiJ3aGl0ZSIsInByaW1hcnlDb2xvciI6IiNFQ0VDRkYiLCJzZWNvbmRhcnlDb2xvciI6IiNmZmZmZGUiLCJ0ZXJ0aWFyeUNvbG9yIjoiaHNsKDgwLCAxMDAlLCA5Ni4yNzQ1MDk4MDM5JSkiLCJwcmltYXJ5Qm9yZGVyQ29sb3IiOiJoc2woMjQwLCA2MCUsIDg2LjI3NDUwOTgwMzklKSIsInNlY29uZGFyeUJvcmRlckNvbG9yIjoiaHNsKDYwLCA2MCUsIDgzLjUyOTQxMTc2NDclKSIsInRlcnRpYXJ5Qm9yZGVyQ29sb3IiOiJoc2woODAsIDYwJSwgODYuMjc0NTA5ODAzOSUpIiwicHJpbWFyeVRleHRDb2xvciI6IiMxMzEzMDAiLCJzZWNvbmRhcnlUZXh0Q29sb3IiOiIjMDAwMDIxIiwidGVydGlhcnlUZXh0Q29sb3IiOiJyZ2IoOS41MDAwMDAwMDAxLCA5LjUwMDAwMDAwMDEsIDkuNTAwMDAwMDAwMSkiLCJsaW5lQ29sb3IiOiIjMzMzMzMzIiwidGV4dENvbG9yIjoiIzMzMyIsIm1haW5Ca2ciOiIjRUNFQ0ZGIiwic2Vjb25kQmtnIjoiI2ZmZmZkZSIsImJvcmRlcjEiOiIjOTM3MERCIiwiYm9yZGVyMiI6IiNhYWFhMzMiLCJhcnJvd2hlYWRDb2xvciI6IiMzMzMzMzMiLCJmb250RmFtaWx5IjoiXCJ0cmVidWNoZXQgbXNcIiwgdmVyZGFuYSwgYXJpYWwiLCJmb250U2l6ZSI6IjE2cHgiLCJsYWJlbEJhY2tncm91bmQiOiIjZThlOGU4Iiwibm9kZUJrZyI6IiNFQ0VDRkYiLCJub2RlQm9yZGVyIjoiIzkzNzBEQiIsImNsdXN0ZXJCa2ciOiIjZmZmZmRlIiwiY2x1c3RlckJvcmRlciI6IiNhYWFhMzMiLCJkZWZhdWx0TGlua0NvbG9yIjoiIzMzMzMzMyIsInRpdGxlQ29sb3IiOiIjMzMzIiwiZWRnZUxhYmVsQmFja2dyb3VuZCI6IiNlOGU4ZTgiLCJhY3RvckJvcmRlciI6ImhzbCgyNTkuNjI2MTY4MjI0MywgNTkuNzc2NTM2MzEyOCUsIDg3LjkwMTk2MDc4NDMlKSIsImFjdG9yQmtnIjoiI0VDRUNGRiIsImFjdG9yVGV4dENvbG9yIjoiYmxhY2siLCJhY3RvckxpbmVDb2xvciI6ImdyZXkiLCJzaWduYWxDb2xvciI6IiMzMzMiLCJzaWduYWxUZXh0Q29sb3IiOiIjMzMzIiwibGFiZWxCb3hCa2dDb2xvciI6IiNFQ0VDRkYiLCJsYWJlbEJveEJvcmRlckNvbG9yIjoiaHNsKDI1OS42MjYxNjgyMjQzLCA1OS43NzY1MzYzMTI4JSwgODcuOTAxOTYwNzg0MyUpIiwibGFiZWxUZXh0Q29sb3IiOiJibGFjayIsImxvb3BUZXh0Q29sb3IiOiJibGFjayIsIm5vdGVCb3JkZXJDb2xvciI6IiNhYWFhMzMiLCJub3RlQmtnQ29sb3IiOiIjZmZmNWFkIiwibm90ZVRleHRDb2xvciI6ImJsYWNrIiwiYWN0aXZhdGlvbkJvcmRlckNvbG9yIjoiIzY2NiIsImFjdGl2YXRpb25Ca2dDb2xvciI6IiNmNGY0ZjQiLCJzZXF1ZW5jZU51bWJlckNvbG9yIjoid2hpdGUiLCJzZWN0aW9uQmtnQ29sb3IiOiJyZ2JhKDEwMiwgMTAyLCAyNTUsIDAuNDkpIiwiYWx0U2VjdGlvbkJrZ0NvbG9yIjoid2hpdGUiLCJzZWN0aW9uQmtnQ29sb3IyIjoiI2ZmZjQwMCIsInRhc2tCb3JkZXJDb2xvciI6IiM1MzRmYmMiLCJ0YXNrQmtnQ29sb3IiOiIjOGE5MGRkIiwidGFza1RleHRMaWdodENvbG9yIjoid2hpdGUiLCJ0YXNrVGV4dENvbG9yIjoid2hpdGUiLCJ0YXNrVGV4dERhcmtDb2xvciI6ImJsYWNrIiwidGFza1RleHRPdXRzaWRlQ29sb3IiOiJibGFjayIsInRhc2tUZXh0Q2xpY2thYmxlQ29sb3IiOiIjMDAzMTYzIiwiYWN0aXZlVGFza0JvcmRlckNvbG9yIjoiIzUzNGZiYyIsImFjdGl2ZVRhc2tCa2dDb2xvciI6IiNiZmM3ZmYiLCJncmlkQ29sb3IiOiJsaWdodGdyZXkiLCJkb25lVGFza0JrZ0NvbG9yIjoibGlnaHRncmV5IiwiZG9uZVRhc2tCb3JkZXJDb2xvciI6ImdyZXkiLCJjcml0Qm9yZGVyQ29sb3IiOiIjZmY4ODg4IiwiY3JpdEJrZ0NvbG9yIjoicmVkIiwidG9kYXlMaW5lQ29sb3IiOiJyZWQiLCJsYWJlbENvbG9yIjoiYmxhY2siLCJlcnJvckJrZ0NvbG9yIjoiIzU1MjIyMiIsImVycm9yVGV4dENvbG9yIjoiIzU1MjIyMiIsImNsYXNzVGV4dCI6IiMxMzEzMDAiLCJmaWxsVHlwZTAiOiIjRUNFQ0ZGIiwiZmlsbFR5cGUxIjoiI2ZmZmZkZSIsImZpbGxUeXBlMiI6ImhzbCgzMDQsIDEwMCUsIDk2LjI3NDUwOTgwMzklKSIsImZpbGxUeXBlMyI6ImhzbCgxMjQsIDEwMCUsIDkzLjUyOTQxMTc2NDclKSIsImZpbGxUeXBlNCI6ImhzbCgxNzYsIDEwMCUsIDk2LjI3NDUwOTgwMzklKSIsImZpbGxUeXBlNSI6ImhzbCgtNCwgMTAwJSwgOTMuNTI5NDExNzY0NyUpIiwiZmlsbFR5cGU2IjoiaHNsKDgsIDEwMCUsIDk2LjI3NDUwOTgwMzklKSIsImZpbGxUeXBlNyI6ImhzbCgxODgsIDEwMCUsIDkzLjUyOTQxMTc2NDclKSJ9fX0)]

## TODO


# Instrucciones para extraer los tweets
El primer paso es clonar el repositorio en la carpeta personal de interés:

`$ git clone https://github.com/Huertas97/tweets_collection.git`

O descargar tan sólo el archivo Tweet_wrapper_v2.py si se desea sólo extraer tweets. Las cuentas de las que se extraen los tweets pueden ser modificadas en este código. 
Una vez descargado, si se intenta emplear el programa lo más probable es que no funcione dado que se requieren una serie de librerías específicas. El programa notifica cuales son estas librerías. No obstante, por aclaración se muestran a continuación:

```
!pip install -U -q tweepy
!pip install -U -q emoji
!pip install -U PyGithub
!pip install -U -q tqdm
```

Igualemente, se puede acceder a la ayuda del programa con el comando:
`$ python Tweet_wrapper_v2.py --help`

El programa requiere
Uso: 
```
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
```
    
Ejemplo. 
Cogemos hasta 100 tweets con la fecha del día de hoy:

    $python Tweet_wrapper_v2_v2.py -t -c 100  --git_token XXX --git_repo Huertas97/tweets_collection

# **Información del repositorio** 
Repositorio donde se almacenan los tweets extraídos de diversas cuentas y hastags (total 113) de Twitter desde el 1 de Octubre de 2020. Diariamente se añaden los tweets extraídos del día anterior. Aunque no se aplica ningún filtro de contenido a los tweets extraídos (por ejemplo no se pone como requisito que en el tweet aparezca el término COVID-19), los hastags y las cuentas han sido seleccionadas manualmente en función de si su contenido se ajustaba a la situación actual de emergencia sanitaria de la COVID-19. 

Los tweets extraídos se encuentran organizados por fecha (día) y por usuario o hastags.  
Los tweets extraídos se guardan en formato json. Las cuentas que no dispogan de tweets no cren ningún archivo json. La información en los ficheros json es:

 * nombre de la cuenta
 * identificador del tweet
 * si es un retweet
 * texto completo (tanto de tweet como retweet)
 * información sobre si la cuenta está verificada
 * fecha de creación del tweet
 * nº de veces que ha sido retweet
 * nº de veces que ha sido marcado como favorito
 * localización del tweet
 * url a la cuenta del usuario
 * entidades del tweets (enlaces, hastags etc)

Las cuentas y hastags empleados en la extracción de tweets se muestran a continuación:

| Hastags  (Nº = 9)      |
|----------------|
| #Plandemia     |
| #yonomeconfino |
| #coronatimo    |
| #YoNoMeVacuno  |
| #covid1984     |
| #NoalaVacuna   |
| #VirusChino    |
| #VacunaRusa    |
| #PCRFraude     |


| Usuarios no institucionales (No fiable, Nº = 49) |
|--------------------------------------------------|
| @No__Plandemia                                   |
| @ANTIMASCARILLA                                  |
| @FoxMuld88326271                                 |
| @PericoAFuego                                    |
| @DiegoMo53772865                                 |
| @the_raven77                                     |
| @LRsecreta                                       |
| @JL_MDesconocido                                 |
| @AtraviesaLoDesc                                 |
| @HomeopatiaY                                     |
| @NaturopatasCol                                  |
| @MiHerbolario                                    |
| @HerbolarioLola                                  |
| @PacienteL                                       |
| @elphabaz                                        |
| @IsTortugo                                       |
| @tecn_preocupado                                 |
| @BabylonDab                                      |
| @lamjort                                         |
| @VaccineXchange                                  |
| @gonzo_blogger                                   |
| @CarmCerb21                                      |
| @panguerrera1                                    |
| @AlbaGar74381296                                 |
| @MediterraneoDGT                                 |
| @JosPastr                                        |
| @velardedaoiz2                                   |
| @JordiFlynn                                      |
| @mitokondriac                                    |
| @AquAhora1                                       |
| @patrilaselma                                    |
| @doctor_papaya                                   |
| @Autnomacabread1                                 |
| @LaRetuerka                                      |
| @DathosBD                                        |
| @PorunChileDigno                                 |
| @1333Despierta                                   |
| @NoHayPandemia__                                 |
| @Musicolorista                                   |
| @ELMINIMALISTA1                                  |
| @Africamar                                       |
| @informate_infor                                 |
| @ElTrompetista78                                 |
| @Angelisimo2                                     |
| @_nWorder                                        |
| @papayaykware                                    |
| @trustdall271                                    |
|     @elentirvigo                                 |
|    @ProgreAzote                                  |


| Preiódicos de Sátira (No fiable, Nº = 9) |
|------------------------------------------|
| @elmundotoday                            |
| @eljueves                                |
| @LaVozdelBecario                         |
| @HayNoticia                              |
| @FrayJosepho                             |
| @ChiguireBipolar                         |
| @actualidadpanam                         |
| @revisbarcelona                          |
| @thecliniccl                             |

| Bases periodísticas Dudosas o Precipitadas de interés (Cuestionable, N = 10) |
|----------------------------------------------------------------|
| @tiramillas                                                    |
| @20m                                                           |
| @okdiario                                                      |
| @ActualidadRT                                                  |
| @ldpsincomplejos                                               |
| @hermanntertsch                                                |
| @NiusDiario                                                    |
| @LaVozIberica                                                  |
| @periodistadigit                                               |
| @CancerIntegral                                                |

| Traducción NO OFICIAL de Donald Trump (Cuestionable, Nº = 1) |
|------------------------------------------------------|
| @POTUS_Trump_ESP                                     |



| Organizaciones institucionales (Fiables, Nº = 10) |
|---------------------------------------------------|
| @SaludPublicaEs                                   |
| @sanidadgob                                       |
| @andaluciadatos                                   |
| @opsoms                                           |
| @WHO                                              |
| @AEMPSGOB                                         |
| @FDAenEspanol                                     |
| @CDCespanol                                       |
| @policia                                          |
| @guardiacivil                                     |


| Verificadores acreditados por Poynter (Fiable, Nº = 10) |
|---------------------------------------------------------|
| @malditobulo  (España)                                          |
| @maldita_ciencia  (España)                                   |
| @EFEVerifica  (España)                                           |
| @Chequeado (Argentina)                                             |
| @Newtral (España)                                        |
| @FullFact (UK)                                               |
| @ElSabuesoAP (México)                                           |
| @cotejoinfo (Venezuela)                                            |
| @ECUADORCHEQUEA (Ecuador)                                        |
| @lasillavacia (Colombia)                                          |

| Bases periodísticas sobre medicina (Nº = 17) |
|----------------------------------------------|
| @JustiaLatinAmer                             |
| @ReutersLatam                                |
| @UniNoticias                                 |
| @14ymedio(Cuba)                              |
| @prensa_libre (Guatemala)                    |
| @ABCDigital (Paraguay)                       |
| @ObservadorUY (Uruguay)                      |
| @Milenio (México)                            |
| @ElMercurio_cl (Chile)                       |
| @elcomerciocom (Ecuador)                     |
| @ElMundoBolivia (Bolivia)                    |
| @laprensa (Nicaragua)                        |
| @elespectador (Colombia)                     |
| @Pajaropolitico                              |
| @elcomerciodigit (Perú, The Trust Project)   |
| @LANACION (Argetina, The Trust Project)      |
| @ElUniversal (Venezuela, The Trust Project)  |

| Bases periodísticas España (Nº = 7) |
|-------------------------------------|
| @el_pais                            |
| @eldiarioes                         |
| @elmundoes                          |
| @EFEnoticias                        |
| @abc_es                             |
| @telediario_tve                     |
| @24h_tve                            |


| Bases periodísticas internacionales (Nº = 1) |
|-------------------------------------|
| @bbcmundo                             |

| Bases periodísticas sobre medicina (Nº = 4) |
|---------------------------------------------|
| @diariomedico                               |
| @Consalud_es                                |
| @redaccionmedica                            |
| @VaccineSafetyN                             |


