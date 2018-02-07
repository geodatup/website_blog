Title:  Translating GeoPdf, all step for geoprocessing
Date: 2015-06-25 10:20
Category: Geotraitement
Tags: PDF Geospatial, bash, gdal, ogr, python, script
Lang: en
translation: true
Author:
Summary:

#Requirement
[<i class="icon-upload"></i> Download all scripts you need from my repo](https://github.com/yougis/geoscript/archive/master.zip)

#List all layers in all GeoPDF and write theire name in a text file

```bash
set DATA_DIR=[root\to\geopdf\files]
dir /b %DATA_DIR%\*.pdf>"file.txt"
for /f %a IN (file.txt) do python [root\to\python\script]gdalinfolayers.py %DATA_DIR%\%a >> infopdf.txt
```
# drop layers duplicate
```bash
python  [root\to\python\script]rmDuplicateLine.py infopdf.txt allLayersNoDpl.txt
```

# trier les layers pour plus de lisibilitee
```bash 
sort allLayersNoDpl.txt > layers.txt
```

# convertir certains layers du PDF en TIFF 
Il faut extraire les layers annotations. les points cotés, les buildings extraire uniquement le raster de fond (landuse) en TIFF.
Pour obtenir le nom de ces layers il faut utiliser la commande gdalinfo qui expose aussi les layer Raster contrairement a OGR qui n'expose que les layers vectoriels
```bash 
set DATA_DIR=[root\to\geopdf\files]
dir /b %DATA_DIR%\*.pdf>"file.txt"
for /f %a IN (file.txt) do (
gdal_translate -of GTiff --config GDAL_PDF_DPI 300 -co COMPRESS=LZW -co "TFW=YES" %DATA_DIR%\%a %DATA_DIR%\product\TIFF\%a.tiff
gdal_translate -of GTiff --config GDAL_PDF_DPI 300 -co COMPRESS=LZW -co "TFW=YES" --config GDAL_PDF_LAYERS "Map_Interior.Image" -a_nodata "255 255 255"  %DATA_DIR%\%a %DATA_DIR%\landuse_raster\%a.tiff
gdal_translate -of GTiff --config GDAL_PDF_DPI 300 -co COMPRESS=LZW -co "TFW=YES" --config GDAL_PDF_LAYERS "Map_Interior.Blue_Anno","Map_Interior.Black_Anno","Map_Interior.ElevationP","Map_Interior.BuildingP" -a_nodata "255 255 255" %DATA_DIR%\%a %DATA_DIR%\product\annotation\%a.tiff
)
```

#  reprojection du TIFF globale (geotransform issue ne permet pasde faire une mosaique virtuel)
```bash 
set DATA_DIR=[root\to\geopdf\files]\product\TIFF
dir /b %DATA_DIR%\*.tiff>"file_tiff.txt"
for /f %a IN (file_tiff.txt) do gdalwarp -of GTiff -co tiled=yes  -co COMPRESS=LZW -co "TFW=YES" -dstnodata 255 %DATA_DIR%\%a %DATA_DIR%\wrap\%a
gdalbuildvrt %DATA_DIR%\wrap\all.vrt %DATA_DIR%\wrap\*.tiff
gdal_translate -of Gtiff -co "COMPRESS=LZW" -co "TFW=YES" -co "BIGTIFF=YES"  %DATA_DIR%\wrap\all.vrt %DATA_DIR%\bigtiff\pdf.tiff
```

#  reprojection du TIFF annotation (geotransform issue ne permet pasde faire une mosaique virtuel)
```bash
set DATA_DIR=[root\to\geopdf\files]\product\annotation
dir /b %DATA_DIR%\*.tiff>"file_anno.txt"
for /f %a IN (file_anno.txt) do gdalwarp -of GTiff -co tiled=yes  -co COMPRESS=LZW -co "TFW=YES" -dstnodata 255 %DATA_DIR%\%a %DATA_DIR%\wrap\%a
gdalbuildvrt %DATA_DIR%\wrap\all.vrt %DATA_DIR%\wrap\*.tiff
gdal_translate -of Gtiff -co "COMPRESS=LZW" -co "TFW=YES" -co "BIGTIFF=YES"  %DATA_DIR%\wrap\all.vrt %DATA_DIR%\bigtiff\annotation.tiff
```


#  reprojection du TIFF de fond (geotransform issue ne permet pas de faire une mosaique virtuel)
```bash
set DATA_DIR=[root\to\geopdf\files]\product\landuse_raster
dir /b %DATA_DIR%\*.tiff>"file_landuse.txt"
for /f %a IN (file_landuse.txt) do gdalwarp -of GTiff -co tiled=yes  -co COMPRESS=LZW -co "TFW=YES" -dstnodata 255 %DATA_DIR%\%a %DATA_DIR%\wrap\%a
gdalbuildvrt %DATA_DIR%\wrap\all.vrt %DATA_DIR%\wrap\*.tiff
gdal_translate -of Gtiff -co "COMPRESS=LZW" -co "TFW=YES" -co "BIGTIFF=YES"  %DATA_DIR%\wrap\all.vrt %DATA_DIR%\bigtiff\landuse.tiff
```


# extraire les layers du PDF dans une base sqlite ET ajout du nom du pdf dans un attribut REF pour les tables listees dans c:\layers.txt
```bash 
set DATA_OUT_DIR=[root\to\geopdf\files]\product\sqlite
set DATA_IN_DIR=[root\to\geopdf\files]
dir /b %DATA_IN_DIR%\*.pdf>"file.txt"
for /f %a IN (file.txt) do (
ogr2ogr -f sqlite %DATA_OUT_DIR%\%a.sqlite %DATA_IN_DIR%\%a
for /f %b IN (c:\layers.txt) do (
ogrinfo %DATA_OUT_DIR%\%a.sqlite -sql "ALTER TABLE %b ADD COLUMN ref string(10)"
ogrinfo %DATA_OUT_DIR%\%a.sqlite -dialect SQLite -sql "UPDATE %b SET ref = '%a'"
)
)
```

# Creer une couche d'union virtuelle pour chaque Layers de chaque base sqlite. 
la liste doit se faire dans le fichier c:\layersL.txt et c:\layersA.txt
traduit les unions virtuelles en layers shapefile polygon et linestring
le script python ogr2vrt a été adapte pour supprimer les balises ouvrantes et fermantes afin de faire ne couche virtuelle Union
```bash
cd c:\
set DATA_OUT_DIR=[root\to\geopdf\files]\product\virtuals
set DATA_IN_DIR=[root\to\geopdf\files]\product\sqlite
set PYTHON_SCRIPT_DIR=C:\Users\yogis\Documents\FFI\script\Python
dir /b %DATA_IN_DIR%\*.sqlite>"file.txt"
for /f %b IN (c:\layersL.txt) do (
mkdir %DATA_OUT_DIR%\%b
cd c:\
for /f %a IN (file.txt) do (
python %PYTHON_SCRIPT_DIR%\ogr2unionvrt.py %DATA_IN_DIR%\%a %DATA_OUT_DIR%\%b\%a.txt %b
)
@echo ^<OGRVRTDataSource^>^<OGRVRTUnionLayer name="Union_%b"^> > %DATA_OUT_DIR%\%b.vrt
type %DATA_OUT_DIR%\%b\*.txt >> %DATA_OUT_DIR%\%b.vrt
@echo ^</OGRVRTUnionLayer^>^</OGRVRTDataSource^> >> %DATA_OUT_DIR%\%b.vrt
rd %DATA_OUT_DIR%\%b /S /Q
ogr2ogr -f "ESRI Shapefile" -skipfailures -nlt LINESTRING -overwrite %DATA_OUT_DIR%\..\shapefiles\%b.shp %DATA_OUT_DIR%\%b.vrt
cd c:\
)
for /f %b IN (c:\layersA_old.txt) do (
mkdir %DATA_OUT_DIR%\%b
cd c:\
for /f %a IN (file.txt) do (
python %PYTHON_SCRIPT_DIR%\ogr2unionvrt.py %DATA_IN_DIR%\%a %DATA_OUT_DIR%\%b\%a.txt %b
)
@echo ^<OGRVRTDataSource^>^<OGRVRTUnionLayer name="Union_%b"^> > %DATA_OUT_DIR%\%b.vrt
type %DATA_OUT_DIR%\%b\*.txt >> %DATA_OUT_DIR%\%b.vrt
@echo ^</OGRVRTUnionLayer^>^</OGRVRTDataSource^> >> %DATA_OUT_DIR%\%b.vrt
rd %DATA_OUT_DIR%\%b /S /Q
ogr2ogr -f "ESRI Shapefile" -skipfailures -nlt POLYGON -overwrite %DATA_OUT_DIR%\..\shapefiles\%b.shp %DATA_OUT_DIR%\%b.vrt
cd c:\
)
for /f %b IN (c:\layersP.txt) do (
mkdir %DATA_OUT_DIR%\%b
cd c:\
for /f %a IN (file.txt) do (
python %PYTHON_SCRIPT_DIR%\ogr2unionvrt.py %DATA_IN_DIR%\%a %DATA_OUT_DIR%\%b\%a.txt %b
)
@echo ^<OGRVRTDataSource^>^<OGRVRTUnionLayer name="Union_%b"^> > %DATA_OUT_DIR%\%b.vrt
type %DATA_OUT_DIR%\%b\*.txt >> %DATA_OUT_DIR%\%b.vrt
@echo ^</OGRVRTUnionLayer^>^</OGRVRTDataSource^> >> %DATA_OUT_DIR%\%b.vrt
rd %DATA_OUT_DIR%\%b /S /Q
ogr2ogr -f "ESRI Shapefile" -skipfailures -nlt POINT -overwrite %DATA_OUT_DIR%\..\shapefiles\%b.shp %DATA_OUT_DIR%\%b.vrt
cd c:\
)
```

