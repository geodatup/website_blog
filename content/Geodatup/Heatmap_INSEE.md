Title: Réaliser une carte de chaleur sur la répartition des entreprises et de la démographie française
Date: 2017-01-03 10:00
Authors: Hugo Roussaffa
sidebarimage: /../..images/carte-stat-INSEE.jpg
tags: Cartographie, Statistique, INSEE
Summary: Une démarche pour créer une carte de chaleur à partir des données INSEE.
lang: fr


> La création d'une carte statistique peut se faire avec des outils opensources comme QGIS ou R (+rcarto) et bien d'autre.

## Obtenir les données

Dans un premier temps nous avons besoin d'obtenir les données INSEE sur leur site. Puis nous avons besoin des mailles géographiques communale et IRIS pour la représentation des données.

## Joindre COMMUNES et démographie des entreprises

Afin d'associer la démographie des entreprises à chaque commune nous réalisons un jointure sur les champs de la couche COMMUNE (CODE-GEO) et de la couche DEMO ENTR (INSEE_COM)

## Joindre IRIS et démographique de la population

Nous réalisation la même opération sur les données de population mais à une maille plus fine IRIS. Voici les champs de jointure :

IRIS (DCOMIRIS) et DEMO POP (IRIS)

## Carte de chaleur INSEE

Afin de représenter les données sous une forme de carte de chaleur (heatmap) nous avons besoin de créer un centroïde pour chaque maille géographique (commune et Iris). Attention, il faut conserver tous les attributs à l'issue des jointures.

Créons maintenant un Raster carte de chaleur. Afin d'avoir une cohérence dans la visualisation des données, je conseils quelques paramètres. Pour la carte des populations à l'échelle de la France :

8 km de rayon
options avancés :

- augmenter la résolution
- pondérer par le champ POP2012
- créer des camemberts sur la typologie des entreprises

Il est maintenant assez simple d'afficher un camembert de la typologie des entreprise sur la géométrie des centroïdes.