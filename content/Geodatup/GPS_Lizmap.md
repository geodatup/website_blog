Title: Utiliser ses coordonnées GPS dans Lizmap
Date: 2017-01-03 10:00
Authors: Hugo Roussaffa
tags: GNSS, GPS, LIZMAP
Summary: Comment configurer Lizmap pour créer des données à partir de la position connue du GPS.
lang: fr




## Utiliser les coordonnées GPS dans Lizmap

###Prérequis materiel

GNSS (reach)

### Prérequis logiciel

gpspipe (pour convertir le flux TCP en fichier nmea)
[http://catb.org/gpsd/gpspipe.html](http://catb.org/gpsd/gpspipe.html)

~~~
gpspipe [-h] [-d] [-l] [-o filename] [-n count] [-r] [-R] [-s serial-device] [-t] [-T timestamp-format] [-u] [-p] [-w] [-S] [-2] [-v] [-D debug-level] [server [:port [:device]]]
~~~

gpsbabel (pour filtrer les données GPS)
[http://www.gpsbabel.org/htmldoc-development/Data_Filters.html](http://www.gpsbabel.org/htmldoc-development/Data_Filters.html)