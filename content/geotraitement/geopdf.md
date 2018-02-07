Title: Traduction en lot de GeoPdf, toutes les étapes du geotraitement
Date: 2015-06-25 10:20
Category: GeoScript
Tags: PDF Geospatial, bash, Gdal/Ogr, Python, script, géotraitement, Windows, DOS
Lang: fr
translation: false
Author:
Summary: Vous disposez d'un lot de PDF Geospatial conséquent et vous voulez exploiter leurs informations dans un logiciel SIG tel que QGIS ou Arcgis.
La meilleure solution reste probablement la traduction dans des formats raster et vectoriels mieux gerées tels que TIFF, SQLite ou SHapefile. Gdal/Ogr dispose d'un driver adapté pour effectuer ces traductions.


###Pré-requis
- [<i class="icon-upload"></i> Télécharger les scripts utilisés depuis mon dépot git](https://github.com/yougis/geoscript/archive/master.zip)
- Installer Gdal/OGR 1.11 et python depuis OSGEO pour Windows
- Demarer le terminal DOS
- Definir les variables d'environnement grace au fichier osgeo4W.bat


## Traitement raster

Une carte publiée en geoPDF contient certainement des annotations ou bien meme une image de fond. Elle contient aussi tout un ensemble d'information tels que la legende ou des logos qui ne nous interesseront pas.
Pour obtenir le nom des couches qui nous interessent, vous pouvez ouvrir le pdf avec un lecteur PDF ou exposer leur nom avec gdalinfo. 

####Obtenir le nom des couches à extraire
Vous obtiendrez aussi le nom des couches par la commande gdalinfo qui expose aussi le nom des couches Raster contrairement à OGR qui n'expose que les layers vectoriels.
```bash 
gdalinfo [pdf] -mdd LAYERS
```

#### Organiser les produits issus des traductions
Afin d'organiser ces produits exporter, nous créons le dossier "product" et des sous-dossiers nommées par des variables définies.

Les variables suivantes doivent etre renseignées en fonction de vos datasource et datastore. Remplacer [chemin\vers\fichiersPDF] et [nomdudossier].

```bash
set DATA_DIR_PDF=[chemin\vers\fichiersPDF]
set DIR_PRODUCT_TIFF_NAME=[nomdudossierTIFF]
set DIR_PRODUCT_BASELAYER_NAME=[nomdudossierBASELAYER]
set DIR_PRODUCT_ANNOTATION_NAME=[nomdudossierANNOTATION]
set DIR_PRODUCT_SQLITE_NAME=[nomdudossierSQLITE]
set DIR_PRODUCT_VRT_NAME=[nomdudossierVRT]
set DATA_DIR_PRODUCT_SHP_NAME=[nomdudossierSHP]
set PYTHON_SCRIPT_DIR=[chemin\vers\dossier\script\python]
```

Puis lancer les commandes suivantes afin de créer l'arboressence des dossiers et sous-dossiers
```bash
cd %DATA_DIR_PDF%
mkdir product
cd product 
mkdir %DIR_PRODUCT_TIFF_NAME%
mkdir %DIR_PRODUCT_BASELAYER_NAME%
mkdir %DIR_PRODUCT_ANNOTATION_NAME%
mkdir %DIR_PRODUCT_SQLITE_NAME%
mkdir %DIR_PRODUCT_VRT_NAME%
cd %DATA_DIR_PDF%\product\%DIR_PRODUCT_TIFF_NAME%
mkdir wrap
mkdir bigtiff
cd %DATA_DIR_PDF%\product\%DIR_PRODUCT_BASELAYER_NAME%
mkdir wrap
mkdir bigtiff 
cd %DATA_DIR_PDF%\product\%DIR_PRODUCT_ANNOTATION_NAME%
mkdir wrap
mkdir bigtiff 
cd c:\


set DATA_DIR_PRODUCT_TIFF=%DATA_DIR_PDF%/product/%DIR_PRODUCT_TIFF_NAME%
set DATA_DIR_PRODUCT_BASELAYER=%DATA_DIR_PDF%/product/%DIR_PRODUCT_BASELAYER_NAME%
set DATA_DIR_PRODUCT_ANNOTATION=%DATA_DIR_PDF%/product/%DIR_PRODUCT_ANNOTATION_NAME%
set DATA_DIR_PRODUCT_SQLITE=%DATA_DIR_PDF%/product/%DIR_PRODUCT_SQLITE_NAME%
set DATA_DIR_PRODUCT_VRT=%DATA_DIR_PDF%/product/%DIR_PRODUCT_VRT_NAME%
set DATA_DIR_PRODUCT_SHP=%DATA_DIR_PDF%/product/%DATA_DIR_PRODUCT_SHP_NAME%

```


#### Convertir toutes et/ou certaines couches du geoPDF en TIFF géoreferencé
Nous allons effectuer 3 differents export. Le premier est une traduction du PDF à l'identique. Le second. la traduction d'une seule couche. Le troisieme, la traduction de plusieurs couches. 
Concernant le second et le troisieme nous allons devoir definir une valeur de puxel en nodata afin de disposer d'une transparance.

```bash 
dir /b %DATA_DIR_PDF%\*.pdf>"Fichier_pdf.txt"
for /f %a IN (Fichier_pdf.txt) do (
gdal_translate -of GTiff --config GDAL_PDF_DPI 300 -co COMPRESS=LZW -co "TFW=YES" %DATA_DIR_PRODUCT_TIFF%\%a.tiff
gdal_translate -of GTiff --config GDAL_PDF_DPI 300 -co COMPRESS=LZW -co "TFW=YES" --config GDAL_PDF_LAYERS "[Couche.nom]" -a_nodata "255 255 255"  %DATA_DIR_PDF%\%a %DATA_DIR_PRODUCT_BASELAYER%\%a.tiff
gdal_translate -of GTiff --config GDAL_PDF_DPI 300 -co COMPRESS=LZW -co "TFW=YES" --config GDAL_PDF_LAYERS "[Couche_annotation.nom]", "[...]" -a_nodata "255 255 255" %DATA_DIR_PDF%\%a %DATA_DIR_PRODUCT_ANNOTATION%\%a.tiff
)
```

###Créer des mosaiques d'images grace aux fichiers virtuels VRT
Dans le cas ou une balise geotransform est contenue dans le geoPdf, gdalvrt ne vous permettra pas de créer une mosaique virtuelle. 

####Reprojeter les TIFF, créer une mosaique virtuelle et produire un fichier bigTiff
On effectue une boucle sur chaque fichier tiff. Ensuite, on realise un fichier virtuel puis on traduit la mosaique virtuelle en bigtiff.
```bash 
dir /b %DATA_DIR_PRODUCT_TIFF%\*.tiff>"Fichier_tiff.txt"
for /f %a IN (Fichier_tiff.txt) do gdalwarp -of GTiff -co tiled=yes  -co COMPRESS=LZW -co "TFW=YES" -dstnodata 255 %DATA_DIR_PRODUCT_TIFF%\%a %DATA_DIR_PRODUCT_TIFF%\wrap\%a
gdalbuildvrt %DATA_DIR_PRODUCT_TIFF%\wrap\all.vrt %DATA_DIR_PRODUCT_TIFF%\wrap\*.tiff
gdal_translate -of Gtiff -co "COMPRESS=LZW" -co "TFW=YES" -co "BIGTIFF=YES"  %DATA_DIR_PRODUCT_TIFF%\wrap\all.vrt %DATA_DIR_PRODUCT_TIFF%\bigtiff\pdf.tiff
```

####Reprojeter les TIFF annotation, créer une mosaique virtuelle et produire un fichier bigTiff
On effectue une boucle sur chaque fichier tiff. Ensuite, on realise un fichier virtuel puis on traduit la mosaique virtuelle en bigtiff.
```bash
dir /b %DATA_DIR_PRODUCT_ANNOTATION%\*.tiff>"Fichier_anno.txt"
for /f %a IN (Fichier_anno.txt) do gdalwarp -of GTiff -co tiled=yes  -co COMPRESS=LZW -co "TFW=YES" -dstnodata 255 %DATA_DIR_PRODUCT_ANNOTATION%\%a %DATA_DIR_PRODUCT_ANNOTATION%\wrap\%a
gdalbuildvrt %DATA_DIR_PRODUCT_ANNOTATION%\wrap\all.vrt %DATA_DIR_PRODUCT_ANNOTATION%\wrap\*.tiff
gdal_translate -of Gtiff -co "COMPRESS=LZW" -co "TFW=YES" -co "BIGTIFF=YES"  %DATA_DIR_PDF%\wrap\all.vrt %DATA_DIR_PDF%\bigtiff\annotation.tiff
```


#  reprojecter les TIFF baselayer, créer une mosaique virtuelle et produire un fichier bigTiff
On effectue une boucle sur chaque fichier tiff. Ensuite, on realise un fichier virtuel puis on traduit la mosaique virtuelle en bigtiff.

```bash
dir /b %DATA_DIR_PRODUCT_BASELAYER%\*.tiff>"Fichier_baselayer.txt"
for /f %a IN (Fichier_baselayer.txt) do gdalwarp -of GTiff -co tiled=yes  -co COMPRESS=LZW -co "TFW=YES" -dstnodata 255 %DATA_DIR_PRODUCT_BASELAYER%\%a %DATA_DIR_PRODUCT_BASELAYER%\wrap\%a
gdalbuildvrt %DATA_DIR_PRODUCT_BASELAYER%\wrap\all.vrt %DATA_DIR_PRODUCT_BASELAYER%\wrap\*.tiff
gdal_translate -of Gtiff -co "COMPRESS=LZW" -co "TFW=YES" -co "BIGTIFF=YES"  %DATA_DIR_PRODUCT_BASELAYER%\wrap\all.vrt %DATA_DIR_PRODUCT_BASELAYER%\bigtiff\baselayer.tiff
```



## Traitement vectoriel
###Lister le nom des couches vectorielles contenus dans chaque GeoPDF.
Nous considerons que les lots de données sont semblables mais peuvent contenir des informations héterogenes. Ainsi les noms de couches peuvent varier d'un fichier PDF à l'autre.
Au cours de cette etape nous allons extraire le nom des couches vectorielles contenues dans les metadonnées des geoPDF. On enleve ensuite de cette longue liste les couches dupliquées, on les tries et on obtient une liste de toutes les couches vectorielles disponibles. Cette permettra de faire le trie des couches utiles à traduire par la suite.
```bash
dir /b %DATA_DIR_PDF%\*.pdf>"FichierPDF.txt"
for /f %a IN (FichierPDF.txt) do python  %PYTHON_SCRIPT_DIR%\ogrinfolayers.py %DATA_DIR_PDF%\%a >> infopdf.txt
```
# supprimer les noms des layers dupliqués
```bash
python  %PYTHON_SCRIPT_DIR\rmDuplicateLine.py infopdf.txt allLayersNoDpl.txt
```
# trier les layers pour plus de lisibilitee
```bash 
sort allLayersNoDpl.txt > layers.txt
```

###Extraire les layers du PDF dans une base sqlite 
Nous ajoutons le nom du pdf dans un attribut REF pour les tables qui sont listees dans le fichier c:\layers.txt

```bash 
dir /b %DATA_DIR_PDF%\*.pdf>"FichierPDF.txt"
for /f %a IN (FichierPDF.txt) do (
ogr2ogr -f sqlite %DATA_DIR_PRODUCT_SQLITE%\%a.sqlite %DATA_DIR_PDF%\%a
for /f %b IN (c:\layers.txt) do (
ogrinfo %DATA_DIR_PRODUCT_SQLITE%\%a.sqlite -sql "ALTER TABLE %b ADD COLUMN ref string(10)"
ogrinfo %DATA_DIR_PRODUCT_SQLITE%\%a.sqlite -dialect SQLite -sql "UPDATE %b SET ref = '%a'"
)
)
```

####Creer une couche shapefile a partir d'une union virtuelle de couche de meme noms
Les shapefiles ne peuvent contenir qu'un seul type de geometrie (polyline, polygon, point). Le script ne permet pas de faire la distinction entre les geometries. le trie doit s'effectuer manuellement (pour l'instant).
> **Note:** 
L'operation s'effectue en plusieurs boucles imbriquées
> -On boucle sur l'ensemble un ensemble de couches (layersL.txt)
> -On créer un dossier par nom de layer pour y stocker l'ensemble des fichiers virtuels
> -On utilise un script ogr python (ogr2vrt[^ogr2unionvrt])permetant de creer un fichier virtuel (.txt) pour chaque layers dans chaque base. Attention ces ficiers > sont sans balises d'ouverture et de fermeture (donc inutilisable en l'état).
> -On créer le fichier virtuel final avec les balise d'ouverture de source et d'ouverture d'union virtuelle
> -On ecrit l'ensemble des contenues des fichiers .txt dans le fichier virtuel
> -On ferme ensuite les balises du fichier virtuel, ce qui le rend propre l'usage
> -On traduit ensuite le fichier vrt en shapefile LINESTRING
Ces operations sont ensuite effectuées a nouveau pour les fichiers layerA.txt et layerP.txt pour creer respectivement les POLYGON et le POINT


```bash
dir /b %DATA_DIR_PRODUCT_SQLITE%\*.sqlite>"FichierSQLITE.txt"
for /f %b IN (c:\layersL.txt) do (
mkdir %DATA_DIR_PRODUCT_VRT%\%b
cd c:\
for /f %a IN (FichierSQLITE.txt) do (
python %PYTHON_SCRIPT_DIR%\ogr2unionvrt.py %DATA_DIR_PRODUCT_SQLITE%\%a  %DATA_DIR_PRODUCT_VRT%\%b\%a.txt %b
)
@echo ^<OGRVRTDataSource^>^<OGRVRTUnionLayer name="Union_%b"^> >  %DATA_DIR_PRODUCT_VRT%\%b.vrt
type  %DATA_DIR_PRODUCT_VRT%\%b\*.txt >> %DATA_DIR_PRODUCT_VRT%\%b.vrt
@echo ^</OGRVRTUnionLayer^>^</OGRVRTDataSource^> >> %%DATA_DIR_PRODUCT_VRT%%\%b.vrt
rd  %DATA_DIR_PRODUCT_VRT%\%b /S /Q
ogr2ogr -f "ESRI Shapefile" -skipfailures -nlt LINESTRING -overwrite %DATA_DIR_PRODUCT_SHP%\%b.shp  %DATA_DIR_PRODUCT_VRT%\%b.vrt
cd c:\
)
for /f %b IN (c:\layersA.txt) do (
mkdir %%DATA_DIR_PRODUCT_VRT%%\%b
cd c:\
for /f %a IN (FichierSQLITE.txt) do (
python %PYTHON_SCRIPT_DIR%\ogr2unionvrt.py %DATA_DIR_PRODUCT_SQLITE%\%a %%DATA_DIR_PRODUCT_VRT%%\%b\%a.txt %b
)
@echo ^<OGRVRTDataSource^>^<OGRVRTUnionLayer name="Union_%b"^> > %%DATA_DIR_PRODUCT_VRT%%\%b.vrt
type %%DATA_DIR_PRODUCT_VRT%%\%b\*.txt >> %%DATA_DIR_PRODUCT_VRT%%\%b.vrt
@echo ^</OGRVRTUnionLayer^>^</OGRVRTDataSource^> >> %%DATA_DIR_PRODUCT_VRT%%\%b.vrt
rd %%DATA_DIR_PRODUCT_VRT%%\%b /S /Q
ogr2ogr -f "ESRI Shapefile" -skipfailures -nlt POLYGON -overwrite %DATA_DIR_PRODUCT_SHP%\%b.shp %%DATA_DIR_PRODUCT_VRT%%\%b.vrt
cd c:\
)
for /f %b IN (c:\layersP.txt) do (
mkdir %%DATA_DIR_PRODUCT_VRT%%\%b
cd c:\
for /f %a IN (FichierSQLITE.txt) do (
python %PYTHON_SCRIPT_DIR%\ogr2unionvrt.py %DATA_DIR_PRODUCT_SQLITE%\%a %%DATA_DIR_PRODUCT_VRT%%\%b\%a.txt %b
)
@echo ^<OGRVRTDataSource^>^<OGRVRTUnionLayer name="Union_%b"^> > %%DATA_DIR_PRODUCT_VRT%%\%b.vrt
type %%DATA_DIR_PRODUCT_VRT%%\%b\*.txt >> %%DATA_DIR_PRODUCT_VRT%%\%b.vrt
@echo ^</OGRVRTUnionLayer^>^</OGRVRTDataSource^> >> %%DATA_DIR_PRODUCT_VRT%%\%b.vrt
rd %%DATA_DIR_PRODUCT_VRT%%\%b /S /Q
ogr2ogr -f "ESRI Shapefile" -skipfailures -nlt POINT -overwrite %%DATA_DIR_PRODUCT_SHP%\%b.shp %DATA_DIR_PRODUCT_VRT%\%b.vrt
cd c:\
)
```




# Amelioration possible
A l'usage on se rend compte des ameliorations possibles de ces procedures faite maison. IL est clair qu'on peut synthetiser, au risque de perdre la lisibilite des étapes. A plusieurs reprises la definition des variables sont répétées mais cela permet néanmoins de rendre chaque section indépendante les unes des autres.



[^ogr2unionvrt]: ogr2unionvrt est le script python ogr2vrt qui a été adapté pour supprimer les balises ouvrantes et fermantes afin de créer par la suite une couche virtuelle d'union.