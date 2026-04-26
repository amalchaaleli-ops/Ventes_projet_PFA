# 📊 Automatisation des Ventes - PFA Logiciels

**Faculté des Sciences de Tunis (FST)**

## 1. Description & Objectifs

Ce projet constitue le Projet de Fin d'Année (PFA) pour la matière **Logiciels**. Il vise à automatiser l'analyse de données massives pour une entreprise de e-commerce dont le volume de ventes dépasse les capacités d'un tableur classique.

### Points Forts Techniques :

* **Scalabilité :** Lecture dynamique des fichiers CSV par blocs (`chunksize`) pour optimiser l'utilisation de la mémoire vive (RAM).
* **Qualité Logicielle :** Code formaté selon les standards PEP 8 avec l'outil **Black** et implémentation du module `logging` pour un suivi professionnel de l'exécution.
* **Rigueur Mathématique :** Calcul automatisé du CA Brut, application des remises, calcul de la TVA (20%) et identification des produits à fort bénéfice.

## 2. Architecture du Projet

* `app.py` : Script principal contenant la logique métier et l'analyse.
* `ventes.csv` : Jeu de données généré dynamiquement par le script.
* `resultats_final.csv` : Rapport consolidé après analyse.
* `graphique_CA.png` : Visualisation graphique des performances par produit via Matplotlib.
* `requirements.txt` : Liste des dépendances pour garantir la portabilité du projet.

## 3. Prérequis

* **Python 3.x**

* **Visual Studio Code** avec l'extension officielle Python

## 4. Installation et Configuration

Afin de garantir l'isolation des dépendances et éviter les conflits de versions, ce projet s'exécute dans un environnement virtuel.

```bash
# 1. Clonage du dépôt distant
git clone https://github.com/amalchaaleli-ops/Ventes_projet_PFA.git
cd Ventes_projet_PFA

# 2. Création et activation de l'environnement virtuel
python -m venv env
.\env\Scripts\activate   # Commande pour Windows

# 3. Installation des bibliothèques nécessaires
pip install -r requirements.txt

## 5. Utilisation
Une fois l'environnement activé, lancez l'automatisation via la commande :
```bash
python app.py