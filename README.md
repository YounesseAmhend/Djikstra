# Algorithme de Dijkstra

## Fichiers du Projet

- **Makefile** : Utilisé pour automatiser les tâches de construction.
- **README.md** : Ce fichier de documentation.
- **`__pycache__`** : Contient les fichiers de cache Python compilés.
- **`djisktra.py`** : Contient l'implémentation de l'algorithme de Dijkstra.
- **`main.py`** : Point d'entrée du programme, où l'algorithme est exécuté.
- **`requirements.txt`** : Liste des dépendances Python nécessaires pour le projet.

## Prérequis

Avant d'exécuter le projet, assurez-vous d'avoir installé Python 3.x sur votre machine. Vous pouvez vérifier l'installation de Python avec la commande suivante :

```bash
python --version
```

## Installation

### Étapes d'installation

1. Clonez le dépôt :

```bash
git clone https://github.com/YounesseAmhend/Djikstra
cd Djikstra
```

1. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Exécution du Programme

Pour exécuter le programme, utilisez la commande suivante :

```bash
python main.py
```

## Comment ça fonctionne ?

### 1. Initialisation

Le programme commence par initialiser un graphe avec un nombre de sommets spécifié. Les liens entre les sommets sont représentés par une matrice d'adjacence, où chaque cellule contient la distance entre deux sommets. Si aucune liaison n'existe, la valeur est 0.

### 2. Algorithme de Dijkstra

L'algorithme de Dijkstra fonctionne en trouvant le sommet avec la distance minimale qui n'a pas encore été traité. Il marque ce sommet comme traité et met à jour les distances de ses sommets adjacents.

### 3. Affichage des Résultats

Une fois que tous les sommets ont été traités, le programme affiche les distances minimales depuis le sommet source vers tous les autres sommets.

## Exemple d'utilisation

Vous pouvez modifier `main.py` pour changer le graphe ou le sommet source. Assurez-vous que la matrice d'adjacence est correctement définie dans le fichier `djisktra.py`.
