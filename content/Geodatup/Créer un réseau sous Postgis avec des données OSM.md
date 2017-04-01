Title: Créer un réseau sous Postgis avec des données OSM
Date: 2017-01-03 10:00
Authors: Hugo Roussaffa
tags: Datapack, OpenStreetMap, PostGIS, Pgrouting, osm2pgrouting, Geotraitement
Summary: De l'installation des briques logicielles de PGroutig à l'intégration des données OSM via OSM2PO
lang: fr

##Création d'un réseau sous Postgis à partir des routes OpenStreetMap

###Installer osm2pgrouting

~~~ 
sudo apt-get osm2pgrouting
~~~ 

###Creer la base et les extentions GIS

~~~ 
psql
CREATE DATABASE osmnetdb;
#[CTRL + D to exit]
psql -d osmnetdb -c 'create extension postgis'
psql -d osmnetdb -c 'create extension pgrouting'


createdb -U user pgrouting-workshop
psql -U user -d pgrouting-workshop -c "CREATE EXTENSION postgis;"
psql -U user -d pgrouting-workshop -c "CREATE EXTENSION pgrouting;"
Verifier la version de pgrouting dans osmnetdb

psql
\connect osmnetdb;
SELECT pgr_version();
~~~ 

###Télécharger les données OSM


Download using Overpass XAPI (larger extracts possible than with default OSM API).
Définir une BBOX et lancer le téléchargement

Les coordonnées de la BBOX peuvent être obtnues sur ... [à définir] 

~~~ 
BBOX="-122.8,45.4,-122.5,45.6"
wget --progress=dot:mega -O "sampledata.osm" "http://www.overpass-api.de/api/xapi?*[bbox=${BBOX}][@meta]"
~~~


###Importer les données OSM

####Faire des données OSM routable avec OSM2PO

~~~
set GISDATA_DIR=C:\Users\Yogis\Documents\GIS_DataBase\OSM-and-OBF\OSM\region_france
~~~

####Conversion de tous les fichiers osm

ça se fait avec java, on convertit dans un premier temps 

~~~
java -jar osm2po-core-5.0.0-SR1.jar cmd=c prefix=li %GISDATA_DIR%\limousin-latest.osm.pbf
java -jar osm2po-core-5.0.0-SR1.jar cmd=c prefix=c %GISDATA_DIR%\centre-latest.osm.pbf
java -jar osm2po-core-5.0.0-SR1.jar cmd=c prefix=p %GISDATA_DIR%\poitou-charentes-latest.osm.pbf
java -jar osm2po-core-5.0.0-SR1.jar cmd=c prefix=lo %GISDATA_DIR%\pays-de-la-loire-latest.osm.pbf
~~~

puis on fait une fusion de tous les fichiers osm dans un seul dossier

~~~
java -jar osm2po-core-5.0.0-SR1.jar cmd=m prefix=lilopc li p c lo
~~~

On créé ensuite un fichier SQL permettant de faire un import dans POSTGIS

~~~
java -jar osm2po-core-5.0.0-SR1.jar cmd=sp prefix=lilopc
~~~

Une fois connecté au serveur de la base de donnée, on insert les données dans la base PGSQL

~~~ 
psql -U postgres -d osmdb -q -f "/media/MediasPartages/OSM-and-OBF/network/lilopc_2po_4pgr.sql"
~~~

Il faudrais ensuite effectuer des mises à jours régulières de la base (vue que OSM évolu en permanance). Mais je n'ai pas trouvé de solution sexy avec OSM2POSTGRES pour effectuer cela. Ce n'est pas possible pour le moment à moins de tout cracher et relancer. 
Voir la question sur [gis.stackexchange](http://gis.stackexchange.com/questions/174491/is-it-possible-to-convert-osm2postgres-table-to-pgrouting-with-osm2po).



