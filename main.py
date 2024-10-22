from djisktra import Graphe


if __name__ == "__main__":
    graphe = Graphe(7)
    graphe.set_graphe(
        [
            [0, 4, 0, 0, 0, 0, 0],
            [4, 0, 8, 0, 0, 0, 0],
            [0, 8, 0, 7, 0, 4, 0],
            [0, 0, 7, 0, 9, 0, 0],
            [0, 0, 0, 9, 0, 8, 0],
            [0, 0, 4, 0, 8, 0, 7],
            [0, 2, 0, 9, 0, 8, 0],
            
        ]
    )
    graphe.dijkstra(0)
