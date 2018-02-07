Title: Installation du site Yo Geomatic sur Python Anywhere
Date: 2015-06-26 10:48
Category: Installation
Tags: Serveur, Pelican, Blog
Lang: en
translation: true
Author:
Summary: Simple process to install pelican on Python Anywhere or other Linux server with python


# Install the virtual environment for pelican
```bash
mkvirtualenv pelican
workon pelican
```
# Install pelican and markdown
```bash
mkdir projects
cd ~/projects/
pip install pelican markdown
```
# First run
```bash
pelican quickstrart
```
# First article for running pelican
create files with .md extention here
```bash
cd content
```



# Install sitemap for web referencing
```bash
cd ~
mkdir pelican-plugins
cd pelican-plugins
git clone https://github.com/dArignac/pelican-extended-sitemap.git
```
change parameters to define the new plugin
```bash
cd ~/projects/
vim pelicanconf.py
```
