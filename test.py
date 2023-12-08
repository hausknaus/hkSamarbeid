class Karakter():
  '''Klasse som lar deg lage ein basic karakter'''
  
  def __init__(self, navn, hp, mp=0):
    self.navn = navn
    self.hp = hp
    self.mp = mp

  def __str__(self):
    return f"Karakteren {self.navn} har {self.hp} HP og {self.mp} MP."

helt = Karakter("Josefine", 100, 50)
print(helt)

fiende = Karakter("Troll", 50)
print(fiende)
