import heapq

class AStarSearch:
    def __init__(self, adjacency_list, heuristic_costs):
        self.adjacency_list = adjacency_list
        self.heuristic_costs = heuristic_costs

    def a_star(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))  # Priority queue for the open set
        came_from = {}
        g_score = {city: float('inf') for city in self.adjacency_list}  # Cost from start to each city
        g_score[start] = 0
        f_score = {city: float('inf') for city in self.adjacency_list}  # Estimated total cost
        f_score[start] = self.heuristic_costs[start]  # Initial heuristic cost

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                total_cost = g_score[goal]  # Get the total cost to reach the goal
                heuristic_cost = self.heuristic_costs[goal]  # Get the heuristic cost for the goal
                path = self.reconstruct_path(came_from, current)
                return path, total_cost, heuristic_cost  # Return path, total cost, and heuristic cost

            for neighbor, cost in self.adjacency_list[current]:
                tentative_g_score = g_score[current] + cost

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic_costs[neighbor]
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None  # No path found

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]  # Reverse the path

# Example heuristic costs
heuristic_costs = {
    "Kartum": 81,
    "Humera": 65,
    "Metema": 62,
    "Shire": 67,
    "Gondar": 56,
    "Azezo": 55,
    "Debark": 60,
    "Bahir Dar": 48,
    "Axum": 66,
    "Adwa": 65,
    "Asmera": 68,
    "Adigrat": 62,
    "Mekelle": 58,
    "Debre Tabor": 52,
    "Sekota": 59,
    "Alamata": 53,
    "Lalibela": 57,
    "Woldia": 50,
    "Samara": 42,
    "Dessie": 44,
    "Fanti Rasu": 49,
    "Kilbet Rasu": 55,
    "Gabi Rasu": 32,
    "Kemise": 40,
    "Awash": 27,
    "Debre Sina": 33,
    "Matahara": 26,
    "Chiro": 31,
    "Debre Birhan": 3,
    "Debre Markos": 39,
    "Adama": 23,
    "Dire Dawa": 31,
    "Addis Ababa": 26,
    "Finote Selam": 42,
    "Batu": 19,
    "Assella": 22,
    "Harar": 35,
    "Ambo": 31,
    "injibara": 44,
    "Metekt": 59,
    "Butajira": 21,
    "Shashemene": 16,
    "Asassa": 18,
    "Babile": 37,
    "Nekemt": 39,
    "Wolkite": 25,
    "Assosa": 51,
    "Worabe": 22,
    "Hossana": 21,
    "Hwassa": 15,
    "Dodolla": 19,
    "Jijiga": 40,
    "Jimma": 33,
    "Gimbi": 43,
    "Bedelle": 40,
    "Dembi Dollo": 49,
    "Wolaita Sodo": 17,
    "Dilla": 12,
    "Bale": 13,
    "Daga Habur": 45,
    "Bonga": 33,
    "Gore": 46,
    "Gambella": 51,
    "Dawaro": 23,
    "Arba Minch": 13,
    "Bule Hora": 8,
    "Liben": 11,
    "Goba": 40,
    "Tepi": 41,
    "Mizan Teferi": 37,
    "Basketo": 23,
    "Konso": 9,
    "Yabello": 6,
    "Sofu Oumer": 45,
    "Werder": 46,
    "Bench Maji": 28,
    "Moyale": 0,
    "Kebir Dahar": 40,
    "Juba": 50,
    "Nairobi": 22,
    "Gode": 35,
    "Dollo": 18,
    "Mogadisho": 40
}

# Example adjacency list
adjacency_list = {
    "Kartum": [("Humera", 21), ("Metema", 19)],
    "Humera": [("Kartum", 21), ("Shire", 80), ("Gondar", 9)],
    "Metema": [("Kartum", 19), ("Gondar", 7), ("Azezo", 7)],
    "Shire": [("Humera", 8), ("Axum", 2), ("Debark", 7)],
    "Gondar": [("Metema", 7), ("Humera", 9), ("Azezo", 1), ("Debark", 4), ("Debre Tabor", 6)],
    "Azezo": [("Metema", 7), ("Gondar", 1), ("Bahir Dar", 7)],
    "Debark": [("Gondar", 4), ("Shire", 7)],
    "Bahir Dar": [("Debre Tabor", 4), ("Finote Selam", 6), ("injibara", 4), ("Metekt", 11), ("Azezo", 7)],
    "Axum": [("Shire", 2), ("Adwa", 1), ("Asmera", 5)],
    "Adwa": [("Axum", 1), ("Adigrat", 4), ("Mekele", 7)],
    "Asmera": [("Axum", 5), ("Adigrat", 9)],
    "Adigrat": [("Adwa", 4), ("Mekele", 4)],
    "Mekelle": [("Adigrat", 4), ("Adwa", 7), ("Sekota", 9), ("Alamata", 5)],
    "Debre Tabor": [("Bahir Dar", 4), ("Lalibela", 8), ("Gondar", 6)],
    "Sekota": [("Mekelle", 9), ("Alamata", 6), ("Lalibela", 6)],
    "Alamata": [("Mekelle", 5), ("Sekota", 6), ("Woldia", 3), ("Samara", 11)],
    "Lalibela": [("Sekota", 6), ("Debre Tabor", 8), ("Woldia", 7)],
    "Woldia": [("Alamata", 3), ("Lalibela", 7), ("Dessie", 6), ("Samara", 8)],
    "Samara": [("Fanti Rasu", 7), ("Alamata", 11), ("Woldia", 8), ("Gabi Rasu", 10)],
    "Dessie": [("Woldia", 6), ("Kemise", 4)],
    "Fanti Rasu": [("Kilbet Rasu", 6), ("Samara", 7)],
    "Kilbet Rasu": [("Fanti Rasu", 6)],
    "Gabi Rasu": [("Awash", 5), ("Samara", 10)],
    "Kemise": [("Dessie", 4), ("Debre Sina", 7)],
    "Awash": [("Gabi Rasu", 5), ("Matahara", 1), ("Chiro", 4)],
    "Debre Sina": [("Kemise", 7), ("Debre Birhan", 2), ("Debre Markos", 17)],
    "Matahara": [("Adama", 3), ("Awash", 1)],
    "Chiro": [("Awash", 4), ("Dire Dawa", 8)],
    "Debre Birhan": [("Addis Ababa", 5), ("Debre Sina", 2)],
    "Debre Markos": [("Finote Selam", 3), ("Debre Sina", 17), ("Addis Ababa", 13)],
    "Adama": [("Addis Ababa", 3), ("Batu", 4), ("Assella", 4), ("Matahara", 3)],
    "Dire Dawa": [("Chiro", 8), ("Harar", 4)],
    "Addis Ababa": [("Ambo", 5), ("Adama", 3), ("Debre Birhan", 5), ("Debre Markos", 13)],
    "Finote Selam": [("Bahirdar", 6), ("Debre Markos", 3), ("injibara", 2)],
    "Batu": [("Adama", 4), ("Butajira", 2), ("Shashemene", 3)],
    "Assella": [("Adama", 4), ("Assasa", 4)],
    "Harar": [("Dire Dawa", 4), ("Babile", 2)],
    "Ambo": [("Nekemt", 8), ("Addis Ababa", 5), ("Wolkite", 6)],
    "injibara": [("Bahirdar", 4), ("Finote Selam", 2)],
    "Metekt": [("Bahirdar", 11)],
    "Butajira": [("Worabe", 2), ("Batu", 2), ("Wolkite", 4)],
    "Shashemene": [("Batu", 3), ("Hossana", 7), ("Hwassa", 1), ("Dodolla", 3)],
    "Asassa": [("Asella", 4), ("Dodolla", 1)],
    "Babile": [("Harar", 2), ("Jijiga", 3), ("Goba", 28)],
    "Nekemt": [("Ambo", 8), ("Gimbi", 4), ("Bedelle", 4)],
    "Wolkite": [("Ambo", 6), ("Jimma", 8), ("Worabe", 5), ("Butajira", 4), ("Hossana", 5)],
    "Assosa": [("Dembi Dollo", 12), ("Gimbi", 8)],
    "Worabe": [("Wolkite", 5), ("Butajira", 2), ("Hossana", 2)],
    "Hossana": [("Worabe", 2), ("Shashemene", 6), ("Wolaita Sodo", 4), ("Wolkite", 5)],
    "Hwassa": [("Shashemene", 1), ("Dilla", 3)],
    "Dodolla": [("Shashemene", 3), ("Asassa", 1), ("Bale", 13)],
    "Jijiga": [("Bablie", 3), ("Daga Habur", 5)],
    "Jimma": [("Wolkite", 8), ("Bedelle", 7), ("Bonga", 4)],
    "Gimbi": [("Nekemt", 4), ("Dembi Dollo", 6), ("Assosa", 8)],
    "Bedelle": [("Nekemt", 4), ("Gore", 6), ("Jimma", 7)],
    "Dembi Dollo": [("Assosa", 12), ("Gimbi", 6), ("Gambella", 4)],
    "Wolaita Sodo": [("Hossana", 4), ("Dawaro", 6), ("Arba Minch", 4)],
    "Dilla": [("Hwassa", 3), ("Bule Hora", 4)],
    "Bale": [("Dodolla", 13), ("Liben", 11), ("Goba", 18), ("Sofa Oumer", 23)],
    "Daga Habur": [("Jijiga", 5), ("Kebri Dehar", 6)],
    "Bonga": [("Jimma", 4), ("Tepi", 8), ("Mizan Teferi", 4), ("Dawaro", 10)],
    "Gore": [("Bedelle", 6), ("Tepi", 9), ("Gambella", 5)],
    "Gambella": [("Dembi Dollo", 4), ("Gore", 5)],
    "Dawaro": [("Wolita Sodo", 6), ("Bonga", 10)],
    "Arba Minch": [("Konso", 4), ("Basketo", 10), ("Wolita Sodo", 4)],
    "Bule Hora": [("Dilla", 4), ("Yabello", 2)],
    "Liben": [("Bale", 11), ("Moyale", 11)],
    "Goba": [("Bale", 18), ("Sofu Oumer", 6), ("Daga Habur", 28)],
    "Tepi": [("Mizan Teferi", 4), ("Bonga", 8), ("Gore", 9)],
    "Mizan Teferi": [("Bonga", 4), ("Tepi", 4)],
    "Basketo": [("Arba Minch", 10), ("Bench Maji", 5)],
    "Konso": [("Arba Minch", 4), ("Yabello", 3)],
    "Yabello": [("Bule Hora", 2), ("Konso", 3), ("Moyale", 6)],
    "Sofu Oumer": [("Goba", 6), ("Bale", 23), ("Gode", 23)],
    "Werder": [("Kebri Dehar", 6)],
    "Bench Maji": [("Basketo", 5), ("Juba", 22)],
    "Moyale": [("Yabello", 6), ("Nairobi", 22), ("Liben", 11), ("Dollo", 18)],
    "Kebir Dahar": [("Daga Habur", 6), ("Werder", 6), ("Gode", 5)],
    "Juba": [("Bench Maji", 22)],
    "Nairobi": [("Moyale", 22)],
    "Gode": [("Kebri Dahar", 5), ("Dollo", 17), ("Sofu Oumer", 23), ("Mokadisho", 22)],
    "Dollo": [("Gode", 17), ("Moyale", 18)],
    "Mogadisho": [("Gode", 22), ("Moyale", 40)]
}

# Create an instance of AStarSearch
a_star = AStarSearch(adjacency_list, heuristic_costs)

# Find the path from "Addis Ababa" to "Moyale"
path, total_cost, heuristic_cost = a_star.a_star("Addis Ababa", "Moyale")
print("Path found:", path)
print("Total cost:", total_cost)
print("Heuristic cost to goal:", heuristic_cost)