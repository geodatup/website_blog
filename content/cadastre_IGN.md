Title: Cadastre / parcellaire en carte dynamique
Date: 2016-11-03 10:20
Authors: Hugo Roussaffa
tags: Datapack
Summary: Quel fournisseur de fond cadastrale choisir (IGN, Cadastre.gouv.fr, OSM) et comment l'utiliser
lang: fr

##Quels fonds cadastrales (parcellaires)

De nombreuses discussions ont lieux au sujet des données du cadastre. Vous trouverez sur le [https://georezo.net/blog/parcellair/](blog parcell'air) de Georezo.fr de quoi vous éclairer en profondeur nottament sur le format de donnée MAJIIC.

Je vais plutôt montrer un aperçu légé et purement fonctionnel.
On obtient les ressources grâce à une clé de l'IGN ou bien via [cadastre.gouv.fr](cadastre.gouv.fr) On peut aussi disposer de ces données via OpenStreetMap mais on est alors limité à son utilisation dans OSM...

Notons des différences possibles entre les différentes ressources (date de mise à jour). La plus à jour est [Cadastre.gouv.fr](Cadastre.gouv.fr).

Pour utiliser la ressource du cadastre, il faudra connaitre le code INSEE de la commune qui vous interesse car la ressource [Cadastre.gouv.fr](Cadastre.gouv.fr) est sans contium spatial,  c'est à dire qu'il y a 1 url par code INSEE. Pour obtenir ce code, j'utilises le maillage Geofla disponible sur [Data.gouv.fr](Data.gouv.fr) et réalise une requêtte sur le code postal ou le nom de la commune que je cherche. Vous pouvez aussi très bien utliser un moteur de recherche mais les résultats sont aléatoires et pas automatisable (à moins de trouver un service web qui publie cette info en json par ex).


## Tricks
Dans Qgis, la connection au service se fait via l'interface de connection WM(T)S. Notez un détail important, pour eviter des effets d'erreur affichage des tuiles, il faut configurer la taille des tuiles d'image sur 256x256.