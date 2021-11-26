import requests

#lista vazia que será preenchida
lista_pokemons = []

#para os 20 primeiros pokemons (1,21)
for i in range(1,21):
    
    url = 'http://pokeapi.co/api/v2/pokemon/'+ str(i)
    response = requests.get(url)
    
    #condicional de sucesso
    if response.status_code == 200:
        
        dados = response.json()
        
        #criando a lista com os 20 pokemons
        nome_pokemon = dados.get('name')
        lista_pokemons += [nome_pokemon]
        print("O nome do pokemon n° %s é:" %i, nome_pokemon +'\n')
        

#criando classe
class Pokemon:
    
    def __init__(self, nome_pokemon, url, peso_pokemon,  habilidades, tipos):
        
        #molde para o pokemon
        self.nome_pokemon = nome_pokemon
        self.url = url
        self.peso_pokemon = peso_pokemon
        self.habilidades = habilidades
        self.tipos = tipos
        
        
    #representração da classe    
    def __repr__(self):
          return f'Pokemon({self.nome_pokemon}, {self.url}, {self.peso_pokemon}, {self.habilidades}, {self.tipos})'
        

def main():

    pokemon = str(input('Qual pokemon você gostaria de consultar? :'))

    #listas para serem preenchidas para cada pokemon
    habilidades=[]
    tipos=[]
    
    #url de cada pokemons
    url = 'http://pokeapi.co/api/v2/pokemon/'+ pokemon
    response = requests.get(url)
    
    #condicional de sucesso
    if response.status_code == 200:

        dados = response.json()

        #para pegar mais de 1 habilidade
        for i in range(0, len(dados['abilities'])):
            habilidades += [(dados['abilities'][i]['ability']['name'])]
        
        
        #para pegar mais de 1 habilidade
        for i in range(0, len(dados['types'])):
            tipos += [(dados['types'][i]['type']['name'])]
            
    pokemons = [Pokemon(dados.get('name'), url, dados.get('weight'), habilidades, tipos)]
    print('\n' + str(pokemons))
  
    next = input("Quer consultar mais pokemons?  :").lower()
    if next in ['sim', 's', 'y', 'yes', '1']:
        (main())
    
if __name__ == '__main__':
    main()