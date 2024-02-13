from sklearn.metrics import accuracy_score
import numpy as np
from class_neurone import *
import matplotlib.pyplot as plt

# ... (autres importations et initialisations)

neurore = Neurone()
liste_analyse = data_analyse()
liste_cible_analyse = paire_cible(cible(liste_analyse))
liste_E = neurore.exec()


# Obtenez les prédictions du modèle pour les données d'analyse
y_learn_liste = [neurore.prediction(liste_analyse[i], liste_analyse[i + 1]).value for i in range(0, len(liste_analyse), 2)]


# Définition des seuils de classification pour lesquels on va calculer
# les scores d'accuracy
threshold_array = np.linspace(0, 1, 100)
accuracy_list = []

for threshold in threshold_array:
    # Labels prédits pour un seuil donné
    label_pred_threshold = (np.array(y_learn_liste) > threshold).astype(int)
    # Calcul de l'accuracy pour un seuil donné
    accuracy_threshold = accuracy_score(
        y_true=liste_cible_analyse, y_pred=label_pred_threshold
    )

    accuracy_list.append(accuracy_threshold)

plt.plot(threshold_array, accuracy_list)
plt.xlabel('Seuil de classification')
plt.ylabel('Accuracy')
plt.title('Évolution de l\'accuracy en fonction du seuil de classification')
plt.show()