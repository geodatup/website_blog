# Démarrer le blog en local pour dev

## Sur mac

~~~
source Virtualenvs/blogpelican/bin/activate
cd Projets/website_blog/output
sudo python -m pelican.server 81
~~~

go to http://localhost:81/

Relancer la génération d'article et redemarrer sur un port libre
~~~
cd ..
pelican content --debug

cd output
sudo python -m pelican.server 81
~~~