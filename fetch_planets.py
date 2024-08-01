import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    return [
        {
            'name': planet['englishName'],
            'mass': planet.get('mass', {}).get('massValue', 'Unknown'),
            'orbit_period': planet.get('sideralOrbit', 'Unknown')
        }
        for planet in planets if planet['isPlanet']
    ]

planets = fetch_planet_data()
for planet in planets:
    print(f"Planet: {planet['name']}, Mass: {planet['mass']}, Orbit Period: {planet['orbit_period']} days")
def find_heaviest_planet(planets):
    return max(planets, key=lambda planet: planet['mass'])

heaviest_planet = find_heaviest_planet(planets)
print(f"The award for heaviest planet goes to {heaviest_planet['name']} with a mass of {heaviest_planet['mass']} kg.")
