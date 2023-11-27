# restaurant_recommendation.py

def recommend_restaurants():
    cuisine_type = input("Enter the type of food you desire: ").lower()
    # Sample data structure to store restaurant information
    restaurants = {
        "Thai Orchid": "Thai",
        "Thai Food Hub": "Thai",
        "Happy Kings" :"Thai",
        "Thai Paradise": "Thai",
        "Spicy Tables": "Thai",
        "Sakura Sushi": "Japanese",
        "Nobu": "Japanese",
        "Sushi Place": "Japanese",
        "Momo Sushi": "Japanese",
        "Kappa maki": "Japanese",
        "La Cucina di Mamma": "Italian",
        "Buca di Beppo": "Italian",
        "Enoteca": "Italian",
        "Tavola Calda": "Italian",
        "La Dolce Vitta": "Italian",
        "Bella Italia": "Italian",
        "Taco Time": "Mexican",
        "El Pollo Loco": "Mexican",
        "Nacho Daddy": "Mexican",
        "Burrito Boys": "Mexican",
        "Taco Fiesta": "Mexican",
        "Curry Mantra": "Indian",
        "Desi Dera": "Indian",
        "Chennai Express": "Indian",
        "Masala Magic": "Indian",
        "Dosa World": "Indian"
    }

    # Validate user input
    if cuisine_type not in restaurants.values():
        print("Invalid cuisine type. Please enter a valid cuisine from the following options:")
        names = []
        for restaurant, cuisine in restaurants.items():
            if cuisine in names:
                continue
            else:
                names.append(cuisine)
        print(f"{names}")
        recommend_restaurants()

    # Filter restaurants based on cuisine type
    recommended_restaurants = []
    for restaurant, cuisine in restaurants.items():
        if cuisine == cuisine_type:
            recommended_restaurants.append(restaurant)

    # Display recommended restaurants
    print(f"Recommended restaurants for {cuisine_type}:")
    for restaurant in recommended_restaurants:
        print(f"- {restaurant}")

# User interaction
recommend_restaurants()