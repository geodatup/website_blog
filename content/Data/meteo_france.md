Title: Les cartes de météo France
Date: 2016-11-03 10:20
Authors: Hugo Roussaffa
tags: Datapack
Summary: Comment obtenir les cartes de météo france dans son SIG ?
lang: fr

## Données Météo france

Je me suis retrouvé confronté à devoir obtenir différentes ressources publiques et gratuites provenant de chez Meteo France. 
Mon premier reflexe est de consulter les catalogues de données du gouvernement, dont celui de [meteo france](https://donneespubliques.meteofrance.fr) et les 2 principaux français que sont celui de [geocatalogue.fr](l'IGN) et [data.gouv.fr](data.gouv.fr).

Grace au catalogue de meteo France, nous devrions être en mesure de connaitre les différentes ressources disponible, et leur urls d'accès par geoservices (webservices OGC). Mais ce n'est vraiment pas évident. Leur site ne montre pas clairement les urls à utiliser. 

## Procédure de Météo france

La procédure d'accès aux données de météo france est expliquée dans un précédent post ou sur ce [PDF](https://donneespubliques.meteofrance.fr/client/gfx/utilisateur/File/documentation-webservices-inspire.pdf)

Il nous donne des exemples d'urls et tout le toutim.

Mais si vous chercher les urls via leur geocatalogue vous êtes foutu (ou alors je suis totalement bigleu).

## Mon astuce
Lorsque vous consulter leur catalogue de service à partir de cette adresse 

[https://donneespubliques.meteofrance.fr/inspire/services/](https://donneespubliques.meteofrance.fr/inspire/services/)

Vous disposer de l'ensemble des services publiés par leur serveur. **Ne cliquez** surtout pas sur un lien car il vous renvera une belle page 404 sur leur site.

[https://donneespubliques.meteofrance.fr/services/**nom_service**](https://donneespubliques.meteofrance.fr/services/**nom_service**)

Il manque simplement le chemin INSPIRE à leur url. Je ne sais pas s'ils le font exprès mais franchement c'est pas très ergonomique.

Nous noterons que les urls des services doivent être obligatoirement sous cette forme :

~~~
https://donneespubliques.meteofrance.fr/inspire/services/**nom_service**/?
~~~ 

Donc copier le nom du service depuis leur url et coller le dans votre url à la place de **nom_service**.

S'ajoute ensuite les paramètres de requete WMS ou WFS qui sont sous cette forme là pour le WMS

~~~
request=GetCapabilities&service=WMS&version=1.3.0&token=__xxx__
~~~

et cette forme pour le WFS :

~~~
request=ListStoredQueries&version=2.0.0&service=WFS&token=__xxx__
~~~

Voici en prime quelques exemples d'url toute faite :

~~~
https://donneespubliques.meteofrance.fr/inspire/services/ArpegeWMS?request=GetCapabilities&service=WMS&version=1.3.0&token=__xxx__
https://donneespubliques.meteofrance.fr/inspire/services/ArpegeWFS?request=GetCapabilities&version=2.0.0&service=WFS&token=__xxx__
https://donneespubliques.meteofrance.fr/inspire/services/MF-NWP-HIGHRES-AROME-001-FRANCE-WMS?request=GetCapabilities&service=WMS&version=1.3.0&token=__xxx__
https://donneespubliques.meteofrance.fr/inspire/services/ArpegeWFS?request=ListStoredQueries&version=2.0.0&service=WFS&token=__xxx__
~~~


https://donneespubliques.meteofrance.fr/services/CAMS50-SILAM-ANALYSIS-01-EUROPE-WMS?request=GetCapabilities