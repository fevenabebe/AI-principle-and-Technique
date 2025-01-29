# Define the adjacency list
adjacency_list = {
    "Kartum": ["Humera", "Metema"],
    "Humera": ["Kartum", "Shire", "Gondar"],
    "Metema": ["Kartum", "Gondar", "Azezo"],
    "Shire": ["Humera", "Axum", "Debark"],
    "Gondar": ["Metema", "Humera", "Azezo", "Debark"],
    "Azezo": ["Metema", "Gondar", "Bahirdar"],
    "Debark": ["Gondar", "Shire"],
    "Bahirdar": ["Debre Tabor", "Finote Selam", "Injibara", "Metekt", "Azezo"],
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
# Initialize a stack
stack = []

# Function to push a city and its neighbors onto the stack
def push_with_neighbors(city):
    if city in adjacency_list:
        stack.append(city)  # Push the city itself
        print(f"Pushed {city} onto the stack with neighbors: {adjacency_list[city]}")
        
        # Push each neighbor onto the stack
        
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
push_with_neighbors("Mogadisho")

