from tabulate import tabulate
import sys

class Graphe:
    def __init__(self, sommets):
        self.num_sommets = sommets
        # Initialiser le graphe avec une matrice d'adjacence remplie de zéros
        self.graphe = []
        for ligne in range(sommets):
            ligne = [
                0
            ] * sommets  # Créer une ligne avec un nombre de zéros égal au nombre de sommets
            self.graphe.append(ligne)

    def set_graphe(self, graphe):
        self.graphe = graphe
        if len(self.graphe) != self.num_sommets:
            raise ValueError("Le nombre de sommets doit être le même que le nombre de lignes de la matrice d'adjacence.")
        



    def afficher_solution(self, distances):
        headers = ["Sommet", "Distance depuis la source"]
        table = [[sommet, distances[sommet]] for sommet in range(self.num_sommets)]

        print(tabulate(table, headers, tablefmt="grid"))

    def obtenir_sommet_min_distance(self, distances, ensemble_chemin_court):
        """Trouver le sommet avec la distance minimale parmi ceux qui n'ont pas encore été traités."""
        min_distance = sys.maxsize  # Utiliser une valeur très grande (infini)
        min_index = -1

        # Trouver le sommet avec la distance minimale qui n'a pas encore été ajouté à l'arbre des plus courts chemins
        for sommet in range(self.num_sommets):
            if distances[sommet] < min_distance and not ensemble_chemin_court[sommet]:
                min_distance = distances[sommet]
                min_index = sommet

        return min_index

    def dijkstra(self, source):
        """Implémentation de l'algorithme de Dijkstra pour trouver le plus court chemin depuis un sommet source."""

        # Initialiser les distances avec l'infini et définir la distance à la source à 0
        distances = [sys.maxsize] * self.num_sommets
        distances[source] = 0
        ensemble_chemin_court = [False] * self.num_sommets  # Suivre les sommets traités

        for _ in range(self.num_sommets):
            # Choisir le sommet avec la distance minimale parmi ceux qui n'ont pas encore été traités
            u = self.obtenir_sommet_min_distance(distances, ensemble_chemin_court)

            # Si aucun sommet valide n'est trouvé, sortir de la boucle
            if u == -1:
                break

            # Marquer le sommet choisi comme traité
            ensemble_chemin_court[u] = True

            # Mettre à jour la distance des sommets adjacents
            for v in range(self.num_sommets):
                if (
                    self.graphe[u][v] > 0  # Vérifier s'il y a un lien entre u et v
                    and not ensemble_chemin_court[v]  # v ne doit pas être traité
                    and distances[v] > distances[u] + self.graphe[u][v]  # La nouvelle distance doit être plus petite
                ):
                    distances[v] = distances[u] + self.graphe[u][v]

        self.afficher_solution(distances)
