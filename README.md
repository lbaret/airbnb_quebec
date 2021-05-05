# 🏡 - Airbnb Quebec City

## 👨‍🏫 - Présentation

Pour ce projet technique, l'objectif est l'analyse et le traitement de données, ainsi que la construction d'un modèle de *Machine Learning* sur le *dataset* d'Airbnb pour la ville de Québec 🏡.  
Par soucis de temps, je n'ai pas eu l'opportunité de construire ma première *Github Page* 🕛.

## 📑 - Organisation

Le projet est structuré en sections et sous-sections :  
- **analyse**
    - *data_discovery* : première ouverture et découverte des données.
    - *EDA* : Exploration et Analyse de Données.
    - *feature_selection* : premiers modèles afin d'étudier l'impact des *features*.
- **config** : variables générales (chemins d'accès, etc..)
- **data** : répertoire contenant les fichiers de données (.csv)
    - *download.py* : téléchargement et extraction des données.
- **functions** : les fonctions utiles et réutilisables.
- **model**
    - *deep_learning* : modèles de *Machine Learning*.
- *garbage* : *notebook* pour tester divers morceaux de codes.
- *requirements.txt* : les librairies nécessaires pour éxécuter les *notebooks*.

Tout le cheminement est expliqué et détaillé dans les divers *notebooks* concernés 📝.

## ❓ - Problématique
Pour la partie sélection de features et construction de modèles, la problématique était la suivante :  
**Peut-on prédire prix d'un logement en location en fonction des informations générales d'Airbnb ?**

Bien évidemment, il était possible de choisir plusieurs objectifs divers et variés comme :  
- Combien de jours le logement sera-t-il loué/disponible durant les 30 prochains jours ?
- En fonction d'une *review* (texte), est-il possible de prédire la note qui lui serait associée ?
- Un système de recommandation de location Airbnb pour la ville de Québec.

## 📊 - Conclusion
Il était très intéressant d'analyser et de traiter les données d'Airbnb Québec, nous avons pu observer quelques faits étonants.
À commencer par le fait que d'être proche du centre-ville (chateau Frontenac plus précisement), n'implique pas forcément des prix plus élevés.
Pourtant, le coeur historique et touristique de Québec se situe aux alentours du chateau Frontenac, sans parler des services à proximité.

De plus, nous avons appris que pendant la période des vacances d'été, de Juillet à Septembre, il y avait en moyenne une hausse des prix de 20$ par nuit.

Concernant les reviews, la plupart des notes générales sont supérieures à 80%, quelque soit la sous-catégorie.

L'étude de l'importance et de l'impact des *features* sur des modèles dits classiques n'a pas été pertinente, puisque seul la méthode du *Lasso* a permis de bien distinguer l'impact de chacune des *features* sur un modèle linéaire.
Nous y retrouvons le nombre de voyageurs que peut acceuillir le logement, le nombre de chambre, le score générale et le nombre de reviews durant les 12 derniers mois.

Les modèles d'apprentissage profond, à savoir le *Multi Layer Perceptron* (MLP) et le *ResNet*, ont donné des résultats intéressants.  
D'un côté le MLP a bien performé et s'est bien adapté au jeu de données, ce qui permet d'affirmer que d'ajouter une discontinuité permettait d'obtenir de meilleurs résultats.  
De l'autre le *ResNet* n'a pas eu les résultats attendus, il a eu tendance à moyenner le jeu de données afin de minimiser sa *MSE*.

# 👨‍💻 - Pour aller plus loin

Il aurait été intéressant de pousser la réfléxion sur la gestion des valeurs manquantes, qui peuvent néanmoins avoir un impact considérables au vu de leur nombre et du faible nombre d'exemples dans le jeu de données.  

Il aurait également été intéressant de se pencher sur la deuxième problématique mentionnée, à savoir :
- En fonction d'une *review* (texte), est-il possible de prédire la note qui lui serait associée ?  
Un modèle de langue combiné à une couche régressive aurait peut-être été efficace et aurait présenté des résultats surprenants !
  
Bien évidemment, les modèles qui ont été présentés auraient pu être améliorés :
- Ajouter plus de régularisation (ex: Dropout, Batchnorm, etc..).
- Utiliser un auto-encodeur pour obtenir un espace latent de plus faible dimension et pertinent à étudier.
- Utiliser un réseau avec des tâches diverses et multiples afin de booster le modèle.
- Retravailler le *ResNet*.

## 🎇
*Merci d'avoir pris le temps de lire et d'étudier ce projet technique*
