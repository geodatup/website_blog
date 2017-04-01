Title: Mettre en cache ses fonds de carte avec LIZMAP
Date: 2017-01-24 10:00
Authors: Hugo Roussaffa
tags: SIG, WebSIG, Lizmap, Geopoppy, Cartodroid
Summary: Toute la procédure pour mettre en cache des données pour partir sur le terrain avec des propres fonds de carte.
lang: fr

# Mise en cache des données pour le terrain


ouvrir le docker Lizmap

~~~
docker exec -it geopoppy_lizmap_1 bash
~~~

Déplacer vous ici

~~~
cd /var/www/websig/lizmap/scripts/
~~~

Lancer le script php (de vérification) avec les parametres nom_de_projet, le/les fond_de_carte à mettre en cache et un EPSG (facultatif)
 
exemple :

~~~
php script.php lizmap~wmts:capabilities geopoppy Rouyre_cadastre_imagerie
php script.php lizmap~wmts:capabilities geopoppy Rouyre_Imagerie drone_janvier_2016 EPSG:3857
php script.php lizmap~wmts:capabilities geopoppy Rouyre_Imagerie drone_janvier_2016 EPSG:2154
php script.php lizmap~wmts:capabilities geopoppy Rouyre_cadastre_imagerie ign_cadastre_rouyre_10k EPSG:2154
~~~

Ce script verifie que tous les parametres sont au vert et vous montre les échelles d'affichage des couches en paramètre du script.

Viens ensuite le moment de **seeder** réellement (semer ou créer les tuiles). Les parametres sont les mêmes que précédement sauf qu'on ajouter les echelles supérieur et inferieur à seeder. 

ex.

~~~
php script.php lizmap~wmts:seeding -v -f geopoppy Rouyre_Imagerie drone_janvier_2016 EPSG:2154 0 8

php script.php lizmap~wmts:seeding -v -f geopoppy Rouyre_cadastre_imagerie Imagerie EPSG:2154 0 6

php script.php lizmap~wmts:seeding -v -f geopoppy Rouyre_cadastre_imagerie ign_cadastre_rouyre_1k EPSG:2154 4 5

php script.php lizmap~wmts:seeding -v -f geopoppy Rouyre_cadastre_imagerie ign_cadastre_rouyre_10k EPSG:2154 0 3

php script.php lizmap~wmts:seeding -v -f geopoppy Rouyre_Imagerie osm_mapnik EPSG:3857 0 23

php script.php lizmap~wmts:seeding -v -f geopoppy Rouyre_Imagerie osm_mapnik EPSG:3857 0 8

php /var/www/websig/lizmap/scripts/script.php lizmap~wmts:seeding -v -f geopoppy Rouyre_Imagerie ign-photo EPSG:2154 0 5
~~~

Les tuiles viennent s'écrirent dans un dossier /tmp.

Une fois qu'on a seeder, il faut s'assurer que les droits d'accès aux tuilles sont les bons, donc on peut relancer ces commandes :

~~~
chown :www-data /tmp -R
chmod 775  /tmp -R
~~~


#Vider le cache server

Se connecter en tant qu'admin sur l'application Lizmap. Dans la console d'admin, aller dans le projet et cliquer sur "vider le cache". 

Vérfier si le log n'est pas remplis par des erreurs.

~~~
lizmap/project/.../var/log
~~~
 
auquel cas il faut bien redonner les droits d'écriture à `www-data` (cf. troobleshooting)

L'opération peut prendre plusieurs minutes. Afin de voir si le déroulement de la vidange s'effectue correctement, vérifier que la taille du dossier /tmp diminue.

Même opération depuis le container lizmap :

~~~
du -sch /tmp/ 
~~~

Consulter les log depuis la machine hote :

~~~
/home/Geopoppy/lizmap/project/.../var/log
~~~

#Troubleshootig 

Impossible de supprimer le cache. Erreur interne Jelix. le fichier log indique une permission denied sur le dossier /tmp.


le répertoire du cache n'est pas accessible 
```/var/www/websig/lib/jelix-plugins/cache/file/file.cache.php     106```

Il faut adresser les bons droits au dossier. Toujours en étant dans le container Lizmap :

~~~
chown :www-data /tmp -R
chmod 775  /tmp -R
~~~




