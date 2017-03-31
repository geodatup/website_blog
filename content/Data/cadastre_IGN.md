Title: Cadastre / parcellaire en carte dynamique
Date: 2016-11-03 10:20
Authors: Hugo Roussaffa
tags: Datapack
Summary: Quel fournisseur de fond cadastrale choisir (IGN, Cadastre.gouv.fr, OSM) et comment l'utiliser
lang: fr

##Quels fonds cadastrales (parcellaires)

De nombreuses discusions ont lieux sur le sujet de la nature et la réglmentation au sujet des données du cadastre. Vous trouverez sur Georezo.fr de quoi vous éclairer en profondeur.

On obtient les ressources grace à un clé de l'IGN ou bien via cadastre.gouv.fr On peut aussi disposer de ces données via OpenStreetMap mais on est alors limité à son utilisation dans OSM...

Notons les différences possibles entre les différentes ressources (date de mise à jour). La plus à jour est [Cadastre.gouv.fr](Cadastre.gouv.fr)

Il faudra connaitre le code INSEE de la commune qui vous interesse car la ressource [Cadastre.gouv.fr](Cadastre.gouv.fr) est sans contium spatial : c'est à dire qu'il y a 1 url par code INSEE. Pour obtenir ce code, j'utilise le maillage Geofla disponible sur [Data.gouv.fr](Data.gouv.fr) et réalise une requette sur le code postal de la commune que je cherche. Vous pouvez aussi très bien chercher sur un moteur de recherche mais les résultats sont aléatoires et pas automatisable (à moins de trouver un service web qui publie cette info en json par ex).


## Tricks
Dans Qgis, la connection au service se fait via l'interface de connection WM(T)S. Noter un détail important, pour eviter des effets d'erreur affichage des tuiles, il faut configurer la taille des tuiles d'image sur 256x256.