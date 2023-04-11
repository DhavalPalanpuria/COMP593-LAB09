import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_info(pokemon):
    pokemon = str(pokemon).strip().lower()

    if pokemon =='':
        print("Error: Entered Pokemon doesnit exist!")
        return

    print(f'Getting information for{pokemon}...', end='')
    url = POKE_API_URL + pokemon
    response_msg = requests.get(url)

    if response_msg == requests.codes.ok :
        print('Success.')
        return response_msg.json()
    else:
        print('Failure.')
        print(f'Response code: {response_msg.status_code} ({response_msg.reason})')
        return