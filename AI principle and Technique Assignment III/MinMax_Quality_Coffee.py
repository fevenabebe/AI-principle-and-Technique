class MiniMaxAgent:
    def __init__(self, graph, utility):
        self.graph = graph
        self.utility = utility

    def minimax(self, node, depth, alpha, beta, maximizing_player):
        # Base case: return utility if a terminal node is reached
        if node in self.utility:
            return self.utility[node], [node]

        if depth == 0:
            return None, []  # Indicate no valuable path

        if maximizing_player:
            max_eval = float('-inf')
            best_path = []
            for neighbor in self.graph[node]:
                eval, path = self.minimax(neighbor, depth - 1, alpha, beta, False)
                if eval is not None and eval > max_eval:  # Only consider valid evaluations
                    max_eval = eval
                    best_path = [node] + path  # Build the path
                alpha = max(alpha, max_eval)
                if beta <= alpha:  # Cutoff
                    break
            return (max_eval, best_path) if max_eval != float('-inf') else (None, [])
        else:
            min_eval = float('inf')
            best_path = []
            for neighbor in self.graph[node]:
                eval, path = self.minimax(neighbor, depth - 1, alpha, beta, True)
                if eval is not None and eval < min_eval:  # Minimize for adversary
                    min_eval = eval
                    best_path = [node] + path  # Build the path
                beta = min(beta, min_eval)
                if beta <= alpha:  # Cutoff
                    break
            return (min_eval, best_path) if min_eval != float('inf') else (None, [])

    def find_best_move(self, start_state, depth):
        best_value = float('-inf')
        best_move = None
        best_path = []
        alpha = float('-inf')
        beta = float('inf')

        for neighbor in self.graph[start_state]:
            move_value, path = self.minimax(neighbor, depth - 1, alpha, beta, False)
            if move_value is not None and move_value > best_value:
                best_value = move_value
                best_move = neighbor
                best_path = [start_state] + path  # Start path with the initial state
                
        return best_move, best_value, best_path


# Graph and utility definitions
graph = { 
    "Addis Ababa": ["Ambo", "Butajira", "Adama"],
    "Ambo": ["Addis Ababa", "Gedo", "Nekemt"],
    "Butajira": ["Addis Ababa", "Worabe", "Wolkite"],
    "Adama": ["Addis Ababa", "Diredawa", "Mojo"],
    "Gedo": ["Ambo", "Fincha", "Shambu"],
    "Nekemt": ["Ambo", "Gimbi", "Limu"],
    "Worabe": ["Butajira", "Hossana", "Durame"],
    "Wolkite": ["Butajira", "Tepi", "Bench Maji"],
    "Diredawa": ["Adama", "Harar", "Chiro"],
    "Mojo": ["Adama", "Kaffa", "Dilla"],
    "Fincha": ["Gedo"],
    "Shambu": ["Gedo"],
    "Gimbi": ["Nekemt"],
    "Limu": ["Nekemt"],
    "Hossana": ["Worabe"],
    "Durame": ["Worabe"],
    "Tepi": ["Wolkite"],
    "Bench Maji": ["Wolkite"],
    "Harar": ["Diredawa"],
    "Chiro": ["Diredawa"],
    "Kaffa": ["Mojo"],
    "Dilla": ["Mojo"]
}

utility = { 
    "Fincha": 5,
    "Shambu": 4,
    "Gimbi": 8,
    "Limu": 8,
    "Hossana": 6,
    "Durame": 5,
    "Tepi": 6,
    "Bench Maji": 5,
    "Harar": 10,
    "Chiro": 6,
    "Kaffa": 7,
    "Dilla": 9
}

# Create a MiniMax agent
agent = MiniMaxAgent(graph, utility)

# Start state and depth for the search
start_state = "Addis Ababa"
depth = 3  # Adjust the depth based on your requirements

best_move, best_value, best_path = agent.find_best_move(start_state, depth)

print(f"The best move for the agent from '{start_state}' is to '{best_move}' with a utility value of {best_value}.")
print(f"The path to the terminal node is: {' -> '.join(best_path)}")