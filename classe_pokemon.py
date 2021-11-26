class Pokemon:
    
   def __init__(self, nome, url, peso, habilidades, tipo):
       
       self.name = nome
       self.url = url
       self.weight = peso
       self.ability = habilidades
       self.type = tipo    
       
    #representração da classe    
   def __repr__(self):
      return f'Pokemon({self.name}, {self.url}, {self.weight}, {self.ability}, {self.type})'