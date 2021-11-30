# PokeAPI -- Gotta Catch 'Em All!! #

## Este é um projeto que irá utilizar a PokéAPI. ##


Existem 3 arquivos que podem ser baixados:

1- Pokédex: Uma versão mais básica e uma Pokédex, que vai listar os primeiros 20 pokémons.
<br />
2- Pokédex_v2: Uma versão um pouco mais trabalhada da Pokedéx, possuindo um "menu" com mais funções de consulta.
<br />
3- classe_pokemon: Um arquivo do qual é importada a classe "Pokemon" que é utilizada nos scripts acima.


A consulta do Pokémon é feita através da PokeAPI : "https://pokeapi.co/"
de onde as informações são retirada para então fazzer o preenchimento da classe.

As informações de cada Pokémon fornecidas são, respectivamente:

- Nome;
- Url cada acesso aos dados detalhados;
- Peso;
- Habilidades;
- Tipo

<br />
<br />
<br />
<br />
Então como um exemplo, para melhor entendimento, segue abaixo o pokémon n°1:


Pokemon(bulbasaur, https://pokeapi.co/api/v2/pokemon/1, 69.0, ['overgrow', 'chlorophyll'], ['grass', 'poison'])

- Nome: bulbasaur
- Url: https://pokeapi.co/api/v2/pokemon/1
- Peso: 69.0
- Habilidades: overgrow e chlorophyll
- Tipo: grass e poison
