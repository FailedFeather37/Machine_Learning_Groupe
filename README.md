# LE MACHINE LEARNING
Un neurone est un composant de l'apprentissage automatique et il est au coeur de l'apprentissage en profondeur. La strucure d'un réseau de neurones est inspiré du cerveau humain, imitant la manière dont les neurones biologiques s'envoient des signaux.	
Un neurone artificiel est constitué de couches nodales,
contenant une couche d'entrée, une ou plusieurs couches cachées pour les réseaux de neurones
 et une couche de sortie. Un neurone possède un poid et un seuil associé.	
 Si la sortie du neurone est supérieure à la valeur de seuil spécifiée,
 ce neurone est activé et envoie des données à la couche suivante du réseau.
 Sinon, aucune donnée n'est transmise à la couche suivante du réseau.	
Les réseaux de neurones s'appuient sur des données d'entraînement
 pour apprendre et améliorer leur précision au fil du temps, on représentera cette
évolution à l'aide de la bibliothèque matplotlib. 

Ce projet pour l'instant ne comprend qu'un seul neurone
permettant, en prennant 2 valeurs comprises en 0 et 1, de predire un ET logique.
 
# Contenu du répertoire

|**Fichier**|Description|
|---------------:|----------|
|[class_neurone.py](class_neurone.py)| Fichier principal : implantation de l'algorithme d'apprentissage        |
|[deriv.py](deriv.py)        | Calcul de quelques opérations mathématiques, y inclus le gradient         |
|[init_data.py](init_data.py)    | Initialisation des données         |
	
# Shéma d'un neurone
![alt tag](https://github.com/FailedFeather37/Machine_Learning_Groupe/blob/main/shema_neurone.png)
# Les bibliothèques utilisées 


|**Bibliothèque**| Description |
|---------------:|-----------|
|Matplotlib      | *Destinée à tracer et visualiser des données sous forme de graphiques. Elle peut être combinée avec les bibliothèques python de calcul scientifique comme NumPy*|
|Scikit-learn    |*Pour l'analyse prédictive de données réutilisables dans différents contextes construit sur NumPy et matplotlib*|
|math            | *Permet d'avoir des fonctions mathématiques supplémentaires*       |
|tqdm        | *Fait en sorte que vos boucles affichent instantanément un compteur de progression intelligent*|
|numpy| *Permet d'effectuer des calculs numériques avec Python. Elle introduit une gestion facilitée des tableaux de nombres.*    |
|random       | *Une fonction permettant de produire des nombres aléatoires*       |


# Documentation
### Initialisation des données : [init_data.py](init_data.py)
Initiatisation des données pour l'apprentissage avec x1 et x2 et des poids w1 et w2 puis équilibrage des données avec sur-échantillonage et génération des cibles pour les paires de données.Calcul du produit scalaire de f(X,W) avec le biais et calcul des erreurs. Même processus pour la génération de données pour l'analyse. 	

Expression mathématique representative : 
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"> <mi>z</mi> <mo>=</mo> <mi>S</mi> <mrow data-mjx-texclass="INNER"> <mo data-mjx-texclass="OPEN">(</mo> <msub> <mi>w</mi> <mn>0</mn> </msub> <mo>+</mo> <munderover> <mo data-mjx-texclass="OP">&#x2211;</mo> <mrow data-mjx-texclass="ORD"> </munderover>  <msub> <mi>w</mi> <mi>i</mi> </msub> <msub> <mi>x</mi> <mi>i</mi> </msub> <mo data-mjx-texclass="CLOSE">)</mo> </mrow> </math>

### Modèle de dérivation : [deriv.py](deriv.py)
Modèle de dérivation partiel basique 
avec une classe Variable comprenant une valeur et un gradient (le gradient étant associé à la dérivé de la valeur).
En reprenant le schéma d'un arbre binaire comprenant chaque composante de l'expression nous pouvons calculer la somme des gradient en fonction de l'erreur et du rapport

### Création du neurone : [class_neurone.py](class_neurone.py)
Cette partie permet la rétropropagation du gradient pour ajuster les poids cela permettant l'apprentissage du neurone avec les EPOCHS ( nombre de passages d'un dataset d'entraînement par un algorithme).Nous lui fournissons ensuite de nouvelles données et faisons l'accurary avec sklearn pour verifier la flexibilité du neurone à s'adapter à de nouveaux data set.
### Comment interpréter le résultat
Suite à l'éxecution du programme un graphique est généré qui représente l'évolution des sommes des erreurs à chaque EPOCH.
Executer le programme [class_neurone.py](class_neurone.py) sur Python. 
De plus dans [init_data.py](init_data.py) : Génération du graphique de la position des x1 et x2

Le logiciel est testé et développé sur Python 3.7.

## Auteurs
Griguer Nathan
Colombani Mael
Mattei Kylian
Besson Harry
