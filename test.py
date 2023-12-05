class Karakter():
  def __init__(self, navn, hp):
    self.navn = navn
    self.hp = hp

  def __str__(self):
    return f"Karakteren {self.navn} har {self.hp} HP"

helt = Karakter("Josefine", 100)
print(helt)