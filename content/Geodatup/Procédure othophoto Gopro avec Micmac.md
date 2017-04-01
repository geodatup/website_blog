Title: Réaliser une orthophoto à partir d'une Gopro et de Micmac
Date: 2017-03-03 10:20
Authors: Hugo Roussaffa
tags: Drone, Micmac, Opensource
Summary: Voici la procédure pour réaliser une orthophoto à partir d'une Gopro, bien sûr, la qualité est médiocre surtout du point de vu géométrique de l'image mais c'est un bon moyen pour progresser.
lang: fr


> Faire de la photogrammetrie avec une Gopro 3 c'est tentant mais je vous arrête tout de suite, c'est vraiment pas pro. Ce matériel n'est pas destiné à cet usage. Les parametres d'aquisition sont automatiques et ça c'est très déconseillé. Vous allez voir de vous même la qualité du rendu. Mais passons sur les prérequis techniques pour l'instant. Nous allons plutôt nous concentrer sur le protocol en lui même et manipuler un peu Micmac.

Tout d'abord, effectuez la campagne d'acquisition pour obtenir des images. 

Pour ma part, j'ai un plan de vol à 30m et un autre à 50m d'altitude.

La gopro doit être configurée en Time Laps afin de prendre suffisement d'images de votre scène (ça, c'est pas très pro mais bon). 


Une fois les images faites, triez vos photo pour évacuer les 
images de décolage et d'atterissage. 

Uploadez de vos images sur un ordinateur. 

Séléctionnez entre 5 et 10 images d'une scène commune, destinées à la calibration de la camera. Les images doivent au mieux avoir de grandes différence de profondeurs (typiquement des photos d'un batiment haut). Si votre terrain est plat, il faudra faire votre calibration sur un mur chez vous.

Renommer les images de calibration avec un préfixe du genre (CALIB_nom_image.JPG)

## MicMac 
Pour ma part j'ai installé MicMac sous Unix (Mac).

Tout d'abord verifier que votre installation est fonctionnel puis ajouter micmac à votre variable d'environnement (ceci afin de disposer des commandes micmac sans avoir à appeler les fichiers binaires avec une url à ralonge :

~~~
export PATH=$PATH:/Applications/3D/MicMacOs/bin/
~~~




Assurez que Micmac reconnaise votre caméra. Il vous faudra soit modifier le fichier DicoCamera situé `MicMacOS/include/XML_MicMac/`
Si la gropo n'est pas connue, ajouter la :

~~~
<!-- GoPro -->

	<CameraEntry>
		<Name> GoPro HD Hero </Name>
		<SzCaptMm> 4.28 5.75 </SzCaptMm>
		<ShortName> GoPro HD Hero </ShortName>
	</CameraEntry>
	<CameraEntry>
		<Name> GoPro HD2</Name>
		<SzCaptMm> 4.69 6.24 </SzCaptMm>
		<ShortName> GoPro HD Hero 2</ShortName>
	</CameraEntry>
	<CameraEntry>
		<Name> GoPro HERO3 White Edition</Name>
		<SzCaptMm> 6.10 8.13 </SzCaptMm>
		<ShortName> GoPro HD Hero 3</ShortName>
	</CameraEntry>
	<CameraEntry>
		<Name> GoPro HERO3 Silver Edition</Name>
		<SzCaptMm> 5.64 7.53 </SzCaptMm>
		<ShortName> GoPro HD Hero 3</ShortName>
	</CameraEntry>
	<CameraEntry>
		<Name> GoPro HERO3 Black Edition</Name>
		<SzCaptMm> 6.63 8.84 </SzCaptMm>
		<ShortName> GoPro HD Hero 3</ShortName>
	</CameraEntry>
	<CameraEntry>
		<Name> GoPro HERO3+ Silver Edition</Name>
		<SzCaptMm> 5.64 7.53 </SzCaptMm>
		<ShortName> GoPro HD Hero 3</ShortName>
	</CameraEntry>
	<CameraEntry>
		<Name> GoPro HERO3+ Black Edition</Name>
		<SzCaptMm> 6.63 8.84 </SzCaptMm>
		<ShortName> GoPro HD Hero 3</ShortName>
	</CameraEntry>
	<CameraEntry>
		<Name> GoPro YHDC5170 </Name>
		<SzCaptMm> 2.54 5.91 </SzCaptMm>
		<ShortName> GoPro </ShortName>
	</CameraEntry>
~~~

### Convertir ses images 

J'ai lu sur un blog qu'il fallait convertir ses images pour corriger l'effet fish eye de la gorpo.

~~~
for file in ./*.JPG; do
  convert "$file" -distort barrel "0.06335 -0.18432 -0.13009" "fisheyeless/${file%.JPG}"_corrige.JPG
done
~~~

Cette opération n'est finalement pas nécessaire car Micmac dispose des algorithmes performant pour effectuer les corrections nécessaires.



## Etape 1 - Tapioca : Points homologues / points de liaison 


Nous recherchons les principaux points homologues entres les images mais sur un sous éhantillonage pour optimiser le temps de traitement. Cette étape sera réaliser une nouvelle fois plus tard sans échantillonage.

~~~
mm3d Tapioca MulScale ".*JPG" 300 1000 ExpTxt=1
~~~

## Etape 2 Tapas : Orientation relative

###la calibration initiale
Cette opération se fait dans un premier temps uniquement sur les image de calibration. Il faut relancer Tapioca sur ce sous ensemble d'image puis Tapas.

~~~
mm3d Tapioca MulScale "calib/.*.JPG" 300 1000
mm3d Tapas FishEyeEqui "calib/.*.JPG" Out='Cal1'
~~~

Vous pouvez aussi lancer la calibration avec un expression régulière ne prenant en compte que certain numéro d'image

~~~
mm3d Tapas FishEyeEqui "G0028(820|821|822|823).JPG" Out=Cal1 ExpTxt=1
~~~

### L'orientation relative
Lancer maintenant Tapas pour réaliser l'orientation relative sur toutes vos images avec votre Calibration (InCal=Cal1) en parametre

~~~
mm3d Tapas FishEyeEqui ".*JPG" InCal=Cal1 Out=Ori1 ExpTxt=1
~~~

si micmac ne trouve pas la calibration vous devrier copier le dossier  Ori-Ini pour le déposer dans le dossier des images à traiter.



## Etape 3 - Apericloud : pour un premier nuage de point

Apericloud va créer un permier nuage de point à partir  des oientations. Ce nuage va nous permettre de visualiser la situation des sommets de prise de vue de nos images. j'adore ce moment :)

~~~
mm3d AperiCloud ".*JPG" Ori1 Out=PosCams.ply ExpTxt=1
~~~

Ce fichier .ply sera visualisable dans Meshlab 

[Meshlab pour mac](https://sourceforge.net/projects/meshlab/files/meshlab/MeshLab%20v1.3.3/MeshLabMac_v133.dmg/download)



### Etape 4 - Malt : création de l'orthophoto

Malt va réaliser le matching.

Je saute volontairement quelques étape d'optimisation, comme la création d'une ligne d'incidence et la création d'un masque. Nous aurons l'occasion d'en reparler dans d'autres projets.

Malt est une commande qui est appelée par d'autres comme C3DC mais je ne vais pas trop rentrer dans les détails.

Malt prend en parametre les photos puis  dossier Ori, issue de Tapas.

~~~
Malt Ortho ".*JPG" Ori1 "DirMEC=Resultats" UseTA=1 ZoomF=4 ZoomI=32 Purge=true
~~~


j'ai fixer les parametres `ZoomF=4 ZoomI=32 ` pour ne pas effectuer le traitement sur les zooms maximums .

### Etape 5 - Tawny : mosaicage des images 

~~~
mm3d Tawny Ortho-Resultats/ Out=Orthophotomosaic.tif
~~~

### Etape 6 - Nuage2ply : Modèle numérique de surface, production d'un nuage de point dense
~~~
Nuage2Ply Resultats/NuageImProf_STD-MALT_Etape_6.xml Attr="Ortho-Resultats/Ortho-Eg-Test-Redr.tif"
~~~

### Etape 7 GrShade : création d'un ombrage 

~~~
mm3d GrShade Malt-OC-F1/Z_Num1_DeZoom1_Malt-Ortho-UnAnam.tif ModeOmbre=IgnE
~~~