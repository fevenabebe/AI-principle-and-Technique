import heapq

# Define the adjacency list with costs
adjacency_list = {
    "Kartum": [("Humera", 21), ("Metema", 19)],
    "Humera": [("Kartum", 21), ("Shire", 8), ("Gondar", 9)],
    "Metema": [("Kartum", 19), ("Gondar", 7), ("Azezo", 7)],
    "Shire": [("Humera", 8), ("Axum", 2), ("Debark", 7)],
    "Gondar": [("Metema", 7), ("Humera", 9), ("Azezo", 1), ("Debark", 4)],
    "Azezo": [("Metema", 7), ("Gondar", 1), ("Bahirdar", 7)],
    "Debark": [("Gondar", 4), ("Shire", 7)],
    "Bahirdar": [("Debre Tabor", 4), ("Finote Selam", 6), ("Injibara", 4), ("Metekt", 11), ("Azezo", 7)],
    "Axum": [("Shire", 2), ("Adwa", 1), ("Asmera", 5)],
    "Adwa": [("Axum", 1), ("Adigrat", 4), ("Mekele", 7)],
    "Asmera": [("Axum", 5), ("Adigrat", 9)],
    "Adigrat": [("Adwa", 4), ("Mekelle", 4)],
    "Mekelle": [("Adigrat", 4), ("Adwa", 7), ("Sekota", 9), ("Alamata", 5)],
    "Debre Tabor": [("Bahirdar", 4), ("Lalibela", 8)],
    "Sekota": [("Mekele", 9), ("Alamata", 6), ("Lalibela", 6)],
    "Alamata": [("Mekelle", 5), ("Sekota", 6), ("Woldia", 3), ("Samara", 11)],
    "Lalibela": [("Sekota", 6), ("Debre Tabor", 8), ("Woldia", 7)],
    "Woldia": [("Alamata", 3), ("Lalibela", 7), ("Dessie", 6), ("Samara", 8)],
    "Samara": [("Fanti Rasu", 7), ("Alamata", 11), ("Woldia", 8), ("Gabi Rasu", 9)],
    "Dessie": [("Woldia", 6), ("Kemise", 4)],
    "Fanti Rasu": [("Kilbet Rasu", 6), ("Samara", 7)],
    "Kilbet Rasu": [("Fanti Rasu", 6)],
    "Gabi Rasu": [("Awash", 5), ("Samara", 9)],
    "Kemise": [("Dessie", 4), ("Debre Sina", 6)],
    "Awash": [("Gabi Rasu", 5), ("Matahara", 1), ("Chiro", 4)],
    "Debre Sina": [("Kemise", 6), ("Debre Birhan", 2), ("Debre Markos", 17)],
    "Matahara": [("Adama", 3), ("Awash", 1)],
    "Chiro": [("Awash", 4), ("Dire Dawa", 8)],
    "Debre Birhan": [("Addis Ababa", 5), ("Debre Sina", 2)],
    "Debre Markos": [("Finote Selam", 3), ("Debre Sina", 17)],
    "Adama": [("Addis Ababa", 3), ("Batu", 4), ("Assella", 4), ("Matahara", 3)],
    "Dire Dawa": [("Chiro", 8), ("Harar", 4)],
    "Addis Ababa": [("Ambo", 5), ("Adama", 3), ("Debre Birhan", 5)],
    "Finote Selam": [("Bahirdar", 6), ("Debre Markos", 3), ("Injibara", 2)],
    "Batu": [("Adama", 4), ("Butajira", 2), ("Shashemene", 3)],
    "Assella": [("Adama", 4), ("Assasa", 4)],
    "Harar": [("Dire Dawa", 4), ("Babile", 2)],
    "Ambo": [("Nekemt", 9), ("Addis Ababa", 5), ("Wolkite", 6)],
    "Injibara": [("Bahirdar", 4), ("Finote Selam", 2)],
    "Metekt": [("Bahirdar", 11)],
    "Butajira": [("Worabe", 2), ("Batu", 2)],
    "Shashemene": [("Batu", 3), ("Hossana", 7), ("Hwassa", 1), ("Dodolla", 3)],
    "Asassa": [("Assella", 4), ("Dodolla", 1)],
    "Babile": [("Harar", 2), ("Jijiga", 3), ("Goba", 28)],
    "Nekemt": [("Ambo", 9), ("Gimbi", 4), ("Bedelle", 3)],
    "Wolkite": [("Ambo", 6), ("Jimma", 8), ("Worabe", 5)],
    "Assosa": [("Dembi Dollo", 12)],
    "Worabe": [("Wolkite", 5), ("Butajira", 2), ("Hossana", 2)],
    "Hossana": [("Worabe", 2), ("Shashemene", 7), ("Wolaita Sodo", 4)],
    "Hwassa": [("Shashemene", 1), ("Dilla", 3)],
    "Dodolla": [("Shashemene", 3), ("Asassa", 1), ("Bale", 13)],
    "Jijiga": [("Babile", 3), ("Daga Habur", 5)],
    "Jimma": [("Wolkite", 8), ("Bedelle", 7), ("Bonga", 4)],
    "Gimbi": [("Nekemt", 4), ("Dembi Dollo", 6)],
    "Bedelle": [("Nekemt", 3), ("Gore", 6), ("Jimma", 7)],
    "Dembi Dollo": [("Assosa", 12), ("Gimbi", 6), ("Gambella", 4)],
    "Wolaita Sodo": [("Hossana", 4), ("Dawaro", 6), ("Arba Minch", 4)],
    "Dilla": [("Hwassa", 3), ("Bule Hora", 4)],
    "Bale": [("Dodolla", 13), ("Liben", 11), ("Goba", 18), ("Sofu Oumer", 23)],
    "Daga Habur": [("Jijiga", 5), ("Kebri Dehar", 6)],
    "Bonga": [("Jimma", 4), ("Tepi", 8), ("Mizan Teferi", 4), ("Dawaro", 10)],
    "Gore": [("Bedelle", 6), ("Tepi", 9), ("Gambella", 5)],
    "Gambella": [("Dembi Dollo", 4), ("Gore", 5)],
    "Dawaro": [("Wolaita Sodo", 6), ("Bonga", 10)],
    "Arba Minch": [("Konso", 4), ("Basketo", 10), ("Wolaita Sodo", 4)],
    "Bule Hora": [("Dilla", 4), ("Yabello", 3)],
    "Liben": [("Bale", 11)],
    "Goba": [("Bale", 18), ("Sofu Oumer", 6), ("Daga Habur", 28)],
    "Tepi": [("Mizan Teferi", 4), ("Bonga", 8), ("Gore", 9)],
    "Mizan Teferi": [("Bonga", 4), ("Tepi", 4)],
    "Basketo": [("Arba Minch", 10), ("Bench Maji", 5)],
    "Konso": [("Arba Minch", 4), ("Yabello", 3)],
    "Yabello": [("Bule Hora", 3), ("Konso", 3), ("Moyale", 6)],
    "Sofu Oumer": [("Goba", 6), ("Bale", 23), ("Gode", 23)],
    "Werder": [("Kebri Dehar", 6)],
    "Bench Maji": [("Basketo", 5), ("Juba", 22)],
    "Moyale": [("Yabello", 6), ("Nairobi", 22)],
    "Kebri Dahar": [("Daga Habur", 6), ("Werder", 6), ("Gode", 5)],
    "Juba": [("Bench Maji", 22)],
    "Nairobi": [("Moyale", 22)],
    "Gode": [("Kebri Dahar", 5), ("Dollo", 17), ("Sofu Oumer", 23), ("Mogadisho", 22)],
    "Dollo": [("Gode", 17)],
    "Mogadisho": [("Gode", 22)]
}

def uniform_cost_search(start, goal):
    # Priority queue to store (cost, path)
    priority_queue = []
    heapq.heappush(priority_queue, (0, [start]))  # Start with cost 0 and the starting city

    # Dictionary to track the minimum cost to reach each city
    visited = {}

    while priority_queue:
        # Get the city with the lowest cost
        current_cost, path = heapq.heappop(priority_queue)
        current_city = path[-1]

        # If we reach the goal, return the path and cost
        if current_city == goal:
            return path, current_cost
        
        # If this city has been visited with a lower cost, skip it
        if current_city in visited and visited[current_city] <= current_cost:
            continue
        
        # Mark this city as visited with the current cost
        visited[current_city] = current_cost

        # Explore neighbors
        for neighbor, cost in adjacency_list.get(current_city, []):
            new_cost = current_cost + cost
            new_path = path + [neighbor]
            heapq.heappush(priority_queue, (new_cost, new_path))

    return None  # Return None if there is no path found

# Example usage
path, cost = uniform_cost_search("Addis Ababa", "Lalibela")
if path:
    print("Path found:", path)
    print("Total cost:", cost)
else:
    print("No path found.")