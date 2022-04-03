from IPython.display import Image, display
from urllib.parse import urljoin
import requests
import random
import pypokedex

def getPokemon(name=None):
  if name == None:
    num = random.randint(1, 151)
    p = pypokedex.get(dex=num)
  else:
    p = pypokedex.get(name=name)

  url = urljoin("https://img.pokemondb.net/sprites/home/normal/", str(p.name)+".png")
  # display(Image(url))
  display(Image(requests.get(url).content))


  pdic = {}
  pdic['name'] = p.name
  types = p.types
  pdic['type'] = random.choice(types)
  pdic['hp'] = int(p.base_stats.hp)
 
  return pdic


def getPokemonImg(name=None):
  if name == None:
    num = random.randint(1, 151)
    p = pypokedex.get(dex=num)
  else:
    p = pypokedex.get(name=name)
  url = urljoin("https://img.pokemondb.net/sprites/home/normal/", str(p.name)+".png")
  display(Image(requests.get(url).content))


def simpleTypeCompare(poke1, poke2):

  type1 = poke1.get_type()
  type2 = poke2.get_type()

  if type1 == 'dragon' and type2 != 'dragon':
    return poke1
  elif type1 != 'dragon' and type2 == 'dragon':
    return poke2 
  
  if type1 == 'normal' and type2 != 'normal':
    return poke2
  elif type1 != 'normal' and type2 == 'normal':
    return poke1

  return 'fair'
