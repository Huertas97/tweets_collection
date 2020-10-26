![GitHub language count](https://img.shields.io/github/languages/count/Huertas97/tweets_collection?style=plastic) ![GitHub repo size](https://img.shields.io/github/repo-size/Huertas97/tweets_collection?style=plastic) ![GitHub watchers](https://img.shields.io/github/watchers/Huertas97/tweets_collection?style=social)

# **Autor** 
Álvaro Huertas García

# Índice
 
 * [TODO](##todo)
 * [Instrucciones para extraer los tweets](#instrucciones-para-extraer-los-tweets)
 * [Información del repositorio](#información-del-repositorio)

![](https://mermaid.ink/svg/eyJjb2RlIjoiXG5ncmFwaCBMUlxuQShUd2l0dGVyIFVzZXJuYW1lKSAtLT4gQiggVHdpdHRlciBBUEkgKVxuQiAtLSAuanNvbiBmaWxlICAtLT4gRChVcGxvYWQgdG8gR2l0aHViIClcblxuc3R5bGUgQSBmaWxsOiNmNWM1NDJcbnN0eWxlIEIgZmlsbDojZjVjNTQyXG5zdHlsZSBEIGZpbGw6I2Y1YzU0MlxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQiLCJ0aGVtZVZhcmlhYmxlcyI6eyJiYWNrZ3JvdW5kIjoid2hpdGUiLCJwcmltYXJ5Q29sb3IiOiIjRUNFQ0ZGIiwic2Vjb25kYXJ5Q29sb3IiOiIjZmZmZmRlIiwidGVydGlhcnlDb2xvciI6ImhzbCg4MCwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpIiwicHJpbWFyeUJvcmRlckNvbG9yIjoiaHNsKDI0MCwgNjAlLCA4Ni4yNzQ1MDk4MDM5JSkiLCJzZWNvbmRhcnlCb3JkZXJDb2xvciI6ImhzbCg2MCwgNjAlLCA4My41Mjk0MTE3NjQ3JSkiLCJ0ZXJ0aWFyeUJvcmRlckNvbG9yIjoiaHNsKDgwLCA2MCUsIDg2LjI3NDUwOTgwMzklKSIsInByaW1hcnlUZXh0Q29sb3IiOiIjMTMxMzAwIiwic2Vjb25kYXJ5VGV4dENvbG9yIjoiIzAwMDAyMSIsInRlcnRpYXJ5VGV4dENvbG9yIjoicmdiKDkuNTAwMDAwMDAwMSwgOS41MDAwMDAwMDAxLCA5LjUwMDAwMDAwMDEpIiwibGluZUNvbG9yIjoiIzMzMzMzMyIsInRleHRDb2xvciI6IiMzMzMiLCJtYWluQmtnIjoiI0VDRUNGRiIsInNlY29uZEJrZyI6IiNmZmZmZGUiLCJib3JkZXIxIjoiIzkzNzBEQiIsImJvcmRlcjIiOiIjYWFhYTMzIiwiYXJyb3doZWFkQ29sb3IiOiIjMzMzMzMzIiwiZm9udEZhbWlseSI6IlwidHJlYnVjaGV0IG1zXCIsIHZlcmRhbmEsIGFyaWFsIiwiZm9udFNpemUiOiIxNnB4IiwibGFiZWxCYWNrZ3JvdW5kIjoiI2U4ZThlOCIsIm5vZGVCa2ciOiIjRUNFQ0ZGIiwibm9kZUJvcmRlciI6IiM5MzcwREIiLCJjbHVzdGVyQmtnIjoiI2ZmZmZkZSIsImNsdXN0ZXJCb3JkZXIiOiIjYWFhYTMzIiwiZGVmYXVsdExpbmtDb2xvciI6IiMzMzMzMzMiLCJ0aXRsZUNvbG9yIjoiIzMzMyIsImVkZ2VMYWJlbEJhY2tncm91bmQiOiIjZThlOGU4IiwiYWN0b3JCb3JkZXIiOiJoc2woMjU5LjYyNjE2ODIyNDMsIDU5Ljc3NjUzNjMxMjglLCA4Ny45MDE5NjA3ODQzJSkiLCJhY3RvckJrZyI6IiNFQ0VDRkYiLCJhY3RvclRleHRDb2xvciI6ImJsYWNrIiwiYWN0b3JMaW5lQ29sb3IiOiJncmV5Iiwic2lnbmFsQ29sb3IiOiIjMzMzIiwic2lnbmFsVGV4dENvbG9yIjoiIzMzMyIsImxhYmVsQm94QmtnQ29sb3IiOiIjRUNFQ0ZGIiwibGFiZWxCb3hCb3JkZXJDb2xvciI6ImhzbCgyNTkuNjI2MTY4MjI0MywgNTkuNzc2NTM2MzEyOCUsIDg3LjkwMTk2MDc4NDMlKSIsImxhYmVsVGV4dENvbG9yIjoiYmxhY2siLCJsb29wVGV4dENvbG9yIjoiYmxhY2siLCJub3RlQm9yZGVyQ29sb3IiOiIjYWFhYTMzIiwibm90ZUJrZ0NvbG9yIjoiI2ZmZjVhZCIsIm5vdGVUZXh0Q29sb3IiOiJibGFjayIsImFjdGl2YXRpb25Cb3JkZXJDb2xvciI6IiM2NjYiLCJhY3RpdmF0aW9uQmtnQ29sb3IiOiIjZjRmNGY0Iiwic2VxdWVuY2VOdW1iZXJDb2xvciI6IndoaXRlIiwic2VjdGlvbkJrZ0NvbG9yIjoicmdiYSgxMDIsIDEwMiwgMjU1LCAwLjQ5KSIsImFsdFNlY3Rpb25Ca2dDb2xvciI6IndoaXRlIiwic2VjdGlvbkJrZ0NvbG9yMiI6IiNmZmY0MDAiLCJ0YXNrQm9yZGVyQ29sb3IiOiIjNTM0ZmJjIiwidGFza0JrZ0NvbG9yIjoiIzhhOTBkZCIsInRhc2tUZXh0TGlnaHRDb2xvciI6IndoaXRlIiwidGFza1RleHRDb2xvciI6IndoaXRlIiwidGFza1RleHREYXJrQ29sb3IiOiJibGFjayIsInRhc2tUZXh0T3V0c2lkZUNvbG9yIjoiYmxhY2siLCJ0YXNrVGV4dENsaWNrYWJsZUNvbG9yIjoiIzAwMzE2MyIsImFjdGl2ZVRhc2tCb3JkZXJDb2xvciI6IiM1MzRmYmMiLCJhY3RpdmVUYXNrQmtnQ29sb3IiOiIjYmZjN2ZmIiwiZ3JpZENvbG9yIjoibGlnaHRncmV5IiwiZG9uZVRhc2tCa2dDb2xvciI6ImxpZ2h0Z3JleSIsImRvbmVUYXNrQm9yZGVyQ29sb3IiOiJncmV5IiwiY3JpdEJvcmRlckNvbG9yIjoiI2ZmODg4OCIsImNyaXRCa2dDb2xvciI6InJlZCIsInRvZGF5TGluZUNvbG9yIjoicmVkIiwibGFiZWxDb2xvciI6ImJsYWNrIiwiZXJyb3JCa2dDb2xvciI6IiM1NTIyMjIiLCJlcnJvclRleHRDb2xvciI6IiM1NTIyMjIiLCJjbGFzc1RleHQiOiIjMTMxMzAwIiwiZmlsbFR5cGUwIjoiI0VDRUNGRiIsImZpbGxUeXBlMSI6IiNmZmZmZGUiLCJmaWxsVHlwZTIiOiJoc2woMzA0LCAxMDAlLCA5Ni4yNzQ1MDk4MDM5JSkiLCJmaWxsVHlwZTMiOiJoc2woMTI0LCAxMDAlLCA5My41Mjk0MTE3NjQ3JSkiLCJmaWxsVHlwZTQiOiJoc2woMTc2LCAxMDAlLCA5Ni4yNzQ1MDk4MDM5JSkiLCJmaWxsVHlwZTUiOiJoc2woLTQsIDEwMCUsIDkzLjUyOTQxMTc2NDclKSIsImZpbGxUeXBlNiI6ImhzbCg4LCAxMDAlLCA5Ni4yNzQ1MDk4MDM5JSkiLCJmaWxsVHlwZTciOiJoc2woMTg4LCAxMDAlLCA5My41Mjk0MTE3NjQ3JSkifX0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

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

    $python Tweet_wrapper_v2.py -t -c 100  --git_token XXX --git_repo Huertas97/tweets_collection

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


