Title: Les cartes de météo France
Date: 2016-11-03 10:20
Authors: Hugo Roussaffa
Summary: 
lang: fr

# Météo france

le service renvois une fichier xml du type :

~~~
<Token xmlns="http://ws.apache.org/ns/synapse">__key__</Token>
~~~


- catalogue de service

~~~
https://donneespubliques.meteofrance.fr/inspire/services/
~~~


- utiliser un service, quelques exemples d'url

~~~
https://donneespubliques.meteofrance.fr/inspire/services/nom_service/?
https://donneespubliques.meteofrance.fr/inspire/services/ArpegeWMS?request=GetCapabilities&service=WMS&version=1.3.0&token=__xxx__
https://donneespubliques.meteofrance.fr/inspire/services/ArpegeWFS?request=GetCapabilities&version=2.0.0&service=WFS&token=__xxx__
https://donneespubliques.meteofrance.fr/inspire/services/MF-NWP-HIGHRES-AROME-001-FRANCE-WMS?request=GetCapabilities&service=WMS&version=1.3.0&token=__xxx__
https://donneespubliques.meteofrance.fr/inspire/services/ArpegeWFS?request=ListStoredQueries&version=2.0.0&service=WFS&token=__xxx__