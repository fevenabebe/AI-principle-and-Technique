from collections import deque  # Importing deque for queue operations

class TravelingEthiopia:  # Define the class
    def __init__(self, adj_list, start, goal):  # Constructor to initialize
        self.adj_list = adj_list  # Save the adjacency list
        self.start = start  # Save the starting state
        self.goal = goal  # Save the goal state

    def bfs(self):  # Breadth-First Search method
        queue = deque([[self.start]])  # Create a queue with the starting state
        visited = set()  # Create a set to keep track of visited nodes

        while queue:  # While there are paths in the queue
            path = queue.popleft()  # Get the first path
            current_state = path[-1]  # Get the last state in the path

            if current_state == self.goal:  # Check if we reached the goal
                return path  # Return the path if found

            if current_state not in visited:  # If not visited
                visited.add(current_state)  # Mark it as visited
                for neighbor in self.adj_list.get(current_state, []):  # Get neighbors
                    new_path = list(path)  # Copy the current path
                    new_path.append(neighbor)  # Add the neighbor to the new path
                    queue.append(new_path)  # Add the new path to the queue

        return None  # Return None if no path is found

    def dfs(self):  # Depth-First Search method
        stack = [[self.start]]  # Create a stack with the starting state
        visited = set()  # Create a set for visited nodes

        while stack:  # While there are paths in the stack
            path = stack.pop()  # Get the last path
            current_state = path[-1]  # Get the last state in the path

            if current_state == self.goal:  # Check if we reached the goal
                return path  # Return the path if found

            if current_state not in visited:  # If not visited
                visited.add(current_state)  # Mark it as visited
                for neighbor in self.adj_list.get(current_state, []):  # Get neighbors
                    new_path = list(path)  # Copy the current path
                    new_path.append(neighbor)  # Add the neighbor to the new path
                    stack.append(new_path)  # Add the new path to the stack

        return None  # Return None if no path is found

    def search(self, method):  # Method to choose search strategy
        if method == "bfs":
            return self.bfs()  # Call BFS method
        elif method == "dfs":
            return self.dfs()  # Call DFS method
        else:
            print("Error: Choose 'bfs' or 'dfs'.")  # Inform invalid strategy
            return None  # Return None for invalid strategy


# Adjacency list of the graph
adjacency_list = {
    "Kartum": ["Humera", "Metema"],
    "Humera": ["Kartum", "Shire", "Gondar"],
    "Metema": ["Kartum", "Gondar", "Azezo"],
    "Shire": ["Humera", "Axum", "Debark"],
    "Gondar": ["Metema", "Humera", "Azezo", "Debark"],
    "Azezo": ["Metema", "Gondar", "Bahirdar"],
    "Debark": ["Gondar",  "Shire"],
    "Bahirdar": ["Debre Tabor","Finote Selam", "Injibara", "Metekt", "Azezo"],
    "Axum": ["Shire", "Adwa", "Asmera"],
    "Adwa": ["Axum", "Adigrat", "Mekele"],
    "Asmera": ["Axum", "Adigrat"],
    "Adigrat": ["Adwa", "Mekelle"],
    "Mekelle": ["Adigrat", "Adwa", "Sekota", "Alamata"],
    "Debre Tabor": ["Bahirdar", "Lalibela"],
    "Sekota": ["Mekelle", "Alamata", "Lalibela"],
    "Alamata": ["Mekelle", "Sekota", "Woldia", "Samara"],
    "Lalibela": ["Sekota", "Debre Tabor", "Woldia"],
    "Woldia": ["Alamata", "Lalibela", "Dessie", "Samara"],
    "Samara": ["Fanti Rasu", "Alamata", "Woldia", "Gabi Rasu"],
    "Dessie": ["Woldia", "Kemise"],
    "Fanti Rasu": ["Kilbet Rasu", "Samara"],
    "Kilbet Rasu": ["Fanti Rasu"],
    "Gabi Rasu": ["Awash", "Samara"],
    "Kemise": ["Dessie", "Debre Sina"],
    "Awash": ["Gabi Rasu", "Matahara", "Chiro"],
    "Debre Sina": ["Kemise", "Debre Birhan", "Debre Markos"],
    "Matahara": ["Adama", "Awash"],
    "Chiro": ["Awash", "Dire Dawa"],
    "Debre Birhan": ["Addis Ababa", "Debre Sina"],
    "Debre Markos": ["Finote Selam", "Debre Sina"],
    "Adama": ["Addis Ababa", "Batu", "Assella", "Matahara"],
    "Dire Dawa": ["Chiro", "Harar"],
    "Addis Ababa": ["Ambo", "Adama", "Debre Birhan"],
    "Finote Selam": ["Bahirdar", "Debre Markos", "Injibara"],
    "Batu": ["Adama", "Butajira", "Shashemene"],
    "Assella": ["Adama", "Assasa"],
    "Harar": ["Dire Dawa", "Babile"],
    "Ambo": ["Nekemt", "Addis Ababa", "Wolkite"],
    "Injibara": ["Bahirdar", "Finote Selam"],
    "Metekt": ["Assosa", "Bahirdar"],
    "Butajira": ["Worabe", "Batu"],
    "Shashemene": ["Batu", "Hossana", "Hwassa", "Dodolla"],
    "Asassa": ["Assella", "Dodolla"],
    "Babile": ["Harar", "Jijiga"],
    "Nekemt": ["Ambo", "Gimbi", "Bedelle"],
    "Wolkite": ["Ambo", "Jimma", "Worabe"],
    "Assosa": ["Metekt", "Dembi Dollo"],
    "Worabe": ["Wolkite", "Butajira", "Hossana"],
    "Hossana": ["Worabe", "Shashemene", "Wolaita Sodo"],
    "Hwassa": ["Shashemene", "Dilla"],
    "Dodolla": ["Shashemene", "Assasa", "Bale"],
    "Jijiga": ["Babile", "Daga Habur"],
    "Jimma": ["Wolkite", "Bedelle", "Bonga"],
    "Gimbi": ["Nekemt", "Dembi Dollo"],
    "Bedelle": ["Nekemt", "Gore", "Jimma"],
    "Dembi Dollo": ["Assosa", "Gimbi", "Gambella"],
    "Wolaita Sodo": ["Hossana", "Dawaro", "Arba Minch"],
    "Dilla": ["Hwassa", "Bule Hora"],
    "Bale": ["Dodolla", "Liben", "Goba", "Sofu Oumer"],
    "Daga Habur": ["Jijiga", "Goba", "Kebri Dehar"],
    "Bonga": ["Jimma", "Tepi", "Mizan Teferi", "Dawaro"],
    "Gore": ["Bedelle", "Tepi", "Gambella"],
    "Gambella": ["Dembi Dollo", "Gore"],
    "Dawaro": ["Wolaita Sodo", "Bonga", "Basketo"],
    "Arba Minch": ["Konso", "Basketo", "Wolaita Sodo"],
    "Bule Hora": ["Dilla", "Yabello"],
    "Liben": ["Bale"],
    "Goba": ["Bale", "Sofu Oumer", "Daga Habur"],
    "Tepi": ["Mizan Teferi", "Bonga", "Gore"],
    "Mizan Teferi": ["Bonga", "Tepi", "Basketo"],
    "Basketo": ["Arba Minch", "Dawaro", "Mizan Teferi", "Bench Maji"],
    "Konso": ["Arba Minch", "Yabello"],
    "Yabello": ["Bule Hora", "Konso", "Moyale"],
    "Sofu Oumer": ["Goba", "Bale", "Kebri Dehar"],
    "Werder": ["Kebri Dehar"],
    "Bench Maji": ["Basketo", "Juba"],
    "Moyale": ["Yabello", "Nairobi"],
    "Kebri Dahar": ["Daga Habur", "Sofu Oumer", "Werder", "Gode"],
    "Juba": ["Bench Maji"],
    "Nairobi": ["Moyale"],
    "Gode": ["Kebri Dahar", "Dollo", "Mogadisho"],
    "Dollo": ["Gode"],
    "Mogadisho": ["Gode"]
}

# Get initial and goal states from user input
initial_state = input("Enter the initial state: ")
goal_state = input("Enter the goal state: ")

# Instantiate the TravelingEthiopia class
search_problem = TravelingEthiopia(adjacency_list, initial_state, goal_state)

# Perform BFS and DFS
bfs_path = search_problem.search("bfs")
dfs_path = search_problem.search("dfs")

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)