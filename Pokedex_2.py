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
    
    else:
        print("\nEste Pokémon não existe... Tente novamente")
    
def caminho_erro():
    print("\nVerifique se digitou o numero corretamente\n")
                      

def caminhos(caminho):
    
    #caminho 1
    if int(caminho) == 1:
        for consulta in range(1,21):
            pokemon = get_pokemon_api(consulta)
            print('\n' + str(pokemon))
    
    #caminho 2
    elif int(caminho) == 2:
        while True:
            consulta = str(input("Qual Pokémon você quer consultar? :"))
            pokemon = get_pokemon_api(consulta)
            if pokemon != None:
                print('\n' + str(pokemon))
                next = input("Quer consultar mais Pokémons?[S/N]  :").lower()
                if next not in ['sim', 's', 'y', 'yes', '1', 'ok']:
                    break
                
    elif int(caminho) == 3:
        consulta1 = (input("Qual o início do intervalo desejado?  :"))
        consulta2 = (input("Qual é o final do intervalo desejado?  :"))
        
        if consulta1.isdigit() and consulta2.isdigit() and (consulta1 in list(range(0, 953, 1))) and (consulta2 in list(range(0, 953, 1))) and (int(consulta2) > int(consulta1)):     
            
            for i in list(range(int(consulta1), int(consulta2), 1)):
                pokemon = get_pokemon_api(i)
                print('\n' + str(pokemon))
        else:
            print("\nIntervalo inválido ou inexistente na Pokédex")     
        
    #caminho 4      
    else:
        print("\nAté a próxima treinador! Gotta Catch 'Em All!")
         

def main():


            caminho = input(
"""Como você gostaria de consultar os Pokémons?
                                
1- Os primeiros 20 Pokémons da Pokédex
2- O Pokémon da sua escolha
3- Pokémons dentro de um intervalo na Pokédex
4- Sair sem consultar
                                
Digite o número: """)
        
            
            if caminho.isdigit():
                
                if int(caminho) not in [1,2,3,4]:
                    caminho_erro()
                
                else:
                    caminhos(caminho)
                    
            else:
                caminho_erro()
            

if __name__ == '__main__':
    main()
    