Title: Créer ses comptes utilisateurs auprès des fournisseurs de services web cartographiques 
Date: 2016-11-03 10:20
Tags: Datapack
Slug: fournisseurs-webservices
Authors: Hugo Roussaffa
Summary: Voici les différents fournisseurs de webservices incoutournables ou presque auprès desquels vous allez avoir besoin de créer un compte utilisateur afin d'obtenir un clé d'accès aux webservices.
lang: fr

##Google maps

[https://developers.google.com/maps/web-services](https://developers.google.com/maps/web-services/)

- obtenir une clé
- Activer une clé > créer un projet > continuer
- nommer la clé
- définir les restrictions de la clé

retrouver ses clés :
[https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials)

###troubleshooting

~~~
RefererNotAllowedMapError	
Error	
The current URL loading the Google Maps JavaScript API has not been added to the list of allowed referrers. Please check the referrer settings of your API key on the Google Developers Console.

See API keys in the Google Developers Console. For more information, see Best practices for securely using API keys.
~~~



##Bing

création d'une clé:

[Bing](https://msdn.microsoft.com/en-us/library/ff428642.aspx)


- creer un compte microsoft
- My account > my key
- créer une clé dev/test


retrouver sa clé :

[https://www.bingmapsportal.com/](https://www.bingmapsportal.com/)


#IGN

Créer un compte sur le site de [l'IGN pro](http://professionnels.ign.fr/)

Créer un contrat d'accès aux "geoservices".

Modifier la sécurisation.

Définir l'usage de la clé sur QGIS , IP ou Refer selon le besoin.

Récupérer la clé.



#M#étéo France

- demander un compte via email

- générer la clé avec le service suivant :
[https://donneespubliques.meteofrance.fr/inspire/services/GetAPIKey?username=****&password=****](https://donneespubliques.meteofrance.fr/inspire/services/GetAPIKey?username=****&password=****)

Météo france fourni une procédure détaillée permettant d'obtenir des accès aux webservices.

demander un compte via email

Puis générer la clé avec le service suivant : 
[https://donneespubliques.meteofrance.fr/inspire/services/GetAPIKey?username=xxxx&password=xxxx](https://donneespubliques.meteofrance.fr/inspire/services/GetAPIKey?username=xxxx&password=xxxx)

Enfin le service renvois une fichier xml du type :

~~~
<Token xmlns="http://ws.apache.org/ns/synapse">__key__</Token>
~~~

ou ```key``` c'est votre clé. Pour accéder aux services connecter vous à leur catalogue comme indiqué dans ce post : Les cartes de météo France
