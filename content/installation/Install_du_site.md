Title: Installation du site Yo Geomatic sur Python Anywhere
Date: 2015-06-26 10:48
Category: Installation
Tags: Serveur, Pelican, Blog
Lang: fr
translation: false
Author:
Summary: Simple procedure pour installer pelican sur Python Anywhere ou autre serveur Linux disposant de python


# Installation d'un environnement pour pelican
```bash
mkvirtualenv pelican
workon pelican
```
# Installation de pelican et de markdown
```bash
mkdir projects
cd ~/projects/
pip install pelican markdown
```
# Premier démarage
```bash
pelican quickstrart
```
# Creer un premier article pour que Pelican fonctionne
Deposer l'article avec l'extention .md dans ce dossier ou un sous dossier de celui-ci
```bash
cd content
```



# Installation de sitemap pour le referencement sur internet
```bash
cd ~
mkdir pelican-plugins
cd pelican-plugins
git clone https://github.com/dArignac/pelican-extended-sitemap.git
```
changer les parametres de pelican pour definir le nouveau plugin
```bash
cd ~/projects/
vim pelicanconf.py
```
