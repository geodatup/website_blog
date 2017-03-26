Pelican  commandes blog geodatup 

# Relancer la génération des articles et pelican en dev

~~~
cd [pelican/path]
pelican content --debug

cd output
python -m pelican.server
~~~

modif du template : remove and reinstall

~~~
pelican-themes --remove pure-single-yo
pelican-themes --install ../pure-single-yo
~~~

#Déploiement prod

git clone blog + template + plugins

~~~
sudo git clone https://github.com/geodatup/website_blog.git
sudo git clone https://github.com/yougis/pure-single-yo.git
sudo git clone git://github.com/getpelican/pelican-plugins.git
~~~

dans l'environnement virtuel du website

~~~
sudo pip install pelican markdown
~~~

Installer un theme

~~~
cd /var/www/webapps/website_blog 
sudo pelican-themes --install ../pure-single-yo
~~~

lancer la génération des pages statics

~~~
sudo pelican content --debug
~~~

#En production
configurer nginx pour afficher le contenu du blog lors de l'acces url blog.geodatup.fr

~~~

sudo touch /etc/nginx/sites-available/website_blog
sudo nano /etc/nginx/sites-available/website_blog
~~

créer un lien symbolique dans les application enabled
~~~
cd /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/website_blog website_blog
~~~

~~~
server {

    listen [::]:84;
    listen 84;

    server_name blog.geodatup.fr;
    root /var/www/webapps/website_blog/output;
    
    access_log /var/log/nginx/website-blog-access.log;
    error_log /var/log/nginx/website-blog-error.log;
    
    location = / {
        # Instead of handling the index, just
        # rewrite / to /index.html
        rewrite ^ /index.html;
    }

    location / {
        # Serve a .gz version if it exists
        gzip_static on;
        # Try to serve the clean url version first
        try_files $uri.htm $uri.html $uri =404;
    }

    location ^~ /theme {
        # This content should very rarely, if ever, change
        expires 1y;
    }
}
~~~


redemarer nginx
~~~
sudo /etc/init.d/nginx restart
~~~