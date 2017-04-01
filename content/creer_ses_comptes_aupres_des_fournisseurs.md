Title: Des fournisseurs de services web cartographiques gratuits
Date: 2016-11-03 10:20
Tags: Datapack
Slug: fournisseurs-webservices
Authors: Hugo Roussaffa
Summary: Voici les différents fournisseurs de webservices incoutournables ou presque auprès desquels vous allez avoir besoin de créer un compte utilisateur afin d'obtenir un clé d'accès gratuit aux webservices.
lang: fr

##Google maps

Pour utiliser les fonds de cartes Google, nous devons avoir une clé API. Ceci leur permet de mesurer votre consommation et d'en faire leur buisness.

[https://developers.google.com/maps/web-services](https://developers.google.com/maps/web-services/)

- obtenir une clé
- Activer une clé > créer un projet > continuer
- nommer la clé
- définir les restrictions de la clé

retrouver ses clés :
[https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials)

Avec une clé vous serez donc limité dans votre usage.

###troubleshooting
Votre clé n'est pas compatible :

~~~
RefererNotAllowedMapError	
Error	
The current URL loading the Google Maps JavaScript API has not been added to the list of allowed referrers. Please check the referrer settings of your API key on the Google Developers Console.

See API keys in the Google Developers Console. For more information, see Best practices for securely using API keys.
~~~



##Bing

Même logique que google.

Création d'une clé:

[Bing](https://msdn.microsoft.com/en-us/library/ff428642.aspx)


- creer un compte microsoft
- My account > my key
- créer une clé dev/test


retrouver sa clé :

[https://www.bingmapsportal.com/](https://www.bingmapsportal.com/)


#IGN

L'IGN propose des clés avec différentes licences. Une clé d'essai est disponnible, renouvelable tous les ans et limité à 10 000 transaction. Cette limite peut être suffisante pour certaines PME.

- Créer un compte sur le site de [l'IGN pro](http://professionnels.ign.fr/)

- Créer un contrat d'accès aux "geoservices".

- Modifier la sécurisation.

- Définir l'usage de la clé sur QGIS , IP ou Refer selon le besoin.

- Récupérer la clé et l'utiliser dans les urls des webservices



#Météo France

Certaines données Météo france sont ouvertes donc accessible gratuitement. Il faut pour autant : 

- demander un compte via email à cette adresse `support.inspire@meteo.fr`

~~~
Bonjour,

j'aimerais disposer d'une clé pour un accès au services INSPIRE de météo france.

pouvez vous me fournir un identifiant ?

Bien cordialement,
~~~

- Monsieur Goupil vous répond alors

~~~
Bonjour,

Voici vos identifiants pour utiliser les géoservices Inspire :

user: ***
mot de passe: ***

Cordialement,

Y. Goupil pour le support INSPIRE.
~~~

- Générez ensuite la clé avec le service suivant :
[https://donneespubliques.meteofrance.fr/inspire/services/GetAPIKey?username=****&password=****](https://donneespubliques.meteofrance.fr/inspire/services/GetAPIKey?username=****&password=****)

Météo france fourni une procédure détaillée permettant d'obtenir des accès aux webservices.

Enfin le service renvois une fichier xml du type :

~~~
<Token xmlns="http://ws.apache.org/ns/synapse">__key__</Token>
~~~

ou ```key``` c'est votre clé. Pour accéder aux services connectez vous à leur catalogue mais ça c'est l'objet d'un autre post.