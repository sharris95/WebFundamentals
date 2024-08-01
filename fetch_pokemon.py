import requests

def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    data = response.json()
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    weight = data['weight']
    return name, abilities, weight

# Fetch data for each Pokémon
pokemon_data = [fetch_pokemon_data(name) for name in ["pikachu", "bulbasaur", "charmander"]]

# Print name and abilities
for name, abilities, _ in pokemon_data:
    print(f"Name: {name}")
    print(f"Abilities: {', '.join(abilities)}")

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon[2] for pokemon in pokemon_list)  # The weight is the third element in the tuple
    return total_weight / len(pokemon_list)

# Calculate and print the average weight
average_weight = calculate_average_weight(pokemon_data)
print(f"Average weight: {average_weight}")