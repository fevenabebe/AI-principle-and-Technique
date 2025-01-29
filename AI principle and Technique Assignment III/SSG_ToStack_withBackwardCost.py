# Define the adjacency list with costs
adjacency_list = {
    "Kartum": [("Humera", 21), ("Metema", 19)],
    "Humera": [("Kartum", 21), ("Shire", 80), ("Gondar", 9)],
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
    "Goba": [("Bale", 18), ("Sofu Oumer", 23), ("Daga Habur", 28)],
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

# Initialize a stack
stack = []

# Function to push a city and its neighbors onto the stack
def push_with_neighbors(city):
    if city in adjacency_list:
        stack.append(city)  # Push the city itself
        print(f"Pushed {city} onto the stack." )
        
        # Push neighbors onto the stack with costs
        for neighbor, cost in adjacency_list[city]:
            stack.append(neighbor)
            print(f"Pushed neighbor {neighbor} onto the stack with cost {cost}.")
    else:
        print(f"City '{city}' not found in the adjacency list.")

# Example usage
push_with_neighbors("Kartum")
push_with_neighbors("Humera"),
push_with_neighbors("Metema"),
push_with_neighbors("Shire"),
push_with_neighbors("Gondar")
push_with_neighbors("Azezo"),
push_with_neighbors("Debark"),
push_with_neighbors("Bahirdar"),
push_with_neighbors("Axum"),
push_with_neighbors("Adwa")
push_with_neighbors("Asmera"),
push_with_neighbors("Adigrat"),
push_with_neighbors("Mekelle"),
push_with_neighbors("Debre Tabor")
push_with_neighbors("Sekota"),
push_with_neighbors("Debark"),
push_with_neighbors("Alamata"),
push_with_neighbors("Lalibela"),
push_with_neighbors("Woldia")
push_with_neighbors("Samara"),
push_with_neighbors("Dessie"),
push_with_neighbors("Fanti Rasu"),
push_with_neighbors("Kilbet Rasu")
push_with_neighbors("Gabi Rasu"),
push_with_neighbors("Kemise"),
push_with_neighbors("Awash"),
push_with_neighbors("Debre Sina"),
push_with_neighbors("Matahara")
push_with_neighbors("Chiro"),
push_with_neighbors("Debre Birhan"),
push_with_neighbors("Debre Markos"),
push_with_neighbors("Adama")
push_with_neighbors("Dire Dawa"),
push_with_neighbors("Addis Ababa"),
push_with_neighbors("Finote Selam"),
push_with_neighbors("Batu"),
push_with_neighbors("Assella")
push_with_neighbors("Harar"),
push_with_neighbors("Ambo"),
push_with_neighbors("Injibara"),
push_with_neighbors("Metekt")
push_with_neighbors("Butajira"),
push_with_neighbors("Shashemene"),
push_with_neighbors("Asassa"),
push_with_neighbors("Babile"),
push_with_neighbors("Nekemt")
push_with_neighbors("Wolkite"),
push_with_neighbors("Assosa"),
push_with_neighbors("Worabe"),
push_with_neighbors("Hossana")
push_with_neighbors("Hwassa"),
push_with_neighbors("Dodolla"),
push_with_neighbors("Jijiga"),
push_with_neighbors("Jimma"),
push_with_neighbors("Gimbi")
push_with_neighbors("Bedelle"),
push_with_neighbors("Dembi Dollo"),
push_with_neighbors("Wolaita Sodo"),
push_with_neighbors("Dilla")
push_with_neighbors("Bale"),
push_with_neighbors("Daga Habur"),
push_with_neighbors("Bonga"),
push_with_neighbors("Gore"),
push_with_neighbors("Gambella")
push_with_neighbors("Dawaro"),
push_with_neighbors("Arba Minch"),
push_with_neighbors("Bule Hora"),
push_with_neighbors("Liben")
push_with_neighbors("Goba"),
push_with_neighbors("Tepi"),
push_with_neighbors("Mizan Teferi"),
push_with_neighbors("Basketo"),
push_with_neighbors("Konso")
push_with_neighbors("Yabello"),
push_with_neighbors("Sofu Oumer"),
push_with_neighbors("Werder"),
push_with_neighbors("Bench Maji"),
push_with_neighbors("Moyale")
push_with_neighbors("Kebri Dahar"),
push_with_neighbors("Juba"),
push_with_neighbors("Nairobi"),
push_with_neighbors("Gode")
push_with_neighbors("Dollo"),
push_with_neighbors("Mogadisho"),