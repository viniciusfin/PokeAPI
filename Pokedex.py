import requests

url_base = 'http://pokeapi.co/api/v2/'
url_base_pokemon = url_base + 'pokemon/'


#criando classe
class Pokemon:
    
    def __init__(self, nome, url, peso,  habilidades, tipos):
        
        #molde para o pokemon
        self.nome = nome
        self.url = url
        self.peso = peso
        self.habilidades = habilidades
        self.tipos = tipos
         
       
    #representração da classe    
    def __str__(self):
          return f'Pokemon({self.nome}, {self.url}, {self.peso}, {self.habilidades}, {self.tipos})'

         
def get_pokemon(identificador):
     
    url = url_base_pokemon + str(identificador)
    response = requests.get(url)
    
    if response.status_code == 200:

        dados = response.json()
        name_pokemon = dados['name']

        
        weight_pokemon = float(dados['weight'])
        
        
        abilities=[x['ability']['name'] for x in dados['abilities']]
   
        tipos=[x['type']['name'] for x in dados['types']]
        
        pokemon = Pokemon(name_pokemon, url, weight_pokemon, abilities, tipos)
        
        return pokemon
        
    else:
        return None
        

def main():
    
    for i in range(1,21):
        pokemon = get_pokemon(i) 
        print(str(pokemon)+'\n')

    while True:
        identificador = str(input('Qual pokemon você gostaria de consultar? :'))
            
            
        pokemon = get_pokemon(identificador)
        
        if pokemon != None:
            print('\n' + str(pokemon))
            
        else:
            print("\nErro, verifique se digitou corretamente")
            
      
        next = input("Quer consultar mais pokemons?[S/N]  :").lower()
        if next not in ['sim', 's', 'y', 'yes', '1', 'ok']:
            break
    
if __name__ == '__main__':
    main()