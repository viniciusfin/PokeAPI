import requests
from classe_pokemon import Pokemon

url_base = 'https://pokeapi.co/api/v2/'
url_base_pokemon = url_base + 'pokemon/'


def get_pokemon_api(identificador):
    url = url_base_pokemon + str(identificador)
    
    r = requests.get(url)    
    
    if r.status_code == 200:
        dados = r.json()
        
        nome = dados['name']
        peso = float(dados['weight'])
        habilidades = [x['ability']['name'] for x in dados['abilities']]
        tipos = [x['type']['name'] for x in dados['types']]

        
        pokemon = Pokemon(nome, url, peso, habilidades, tipos)
        return pokemon
    
        
def main():
    for i in range(1,21):
        pokemon = get_pokemon_api(i)
        print('\n' + str(pokemon))
        


if __name__ == '__main__':
    main()
