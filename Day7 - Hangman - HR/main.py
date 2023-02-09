from hangman_art import logo
from hangman_word_list import word_list
from replit import clear


import random

# Nasumicna rijec
odabranaNasumicnaRijec = random.choice(word_list).lower()
duljinaNasumicneRijeci = len(odabranaNasumicnaRijec)

# Ispis logo igre
print(logo)
print(f"Rješenje je: {odabranaNasumicnaRijec}")

# Prazna slova
display = []
for _ in range(duljinaNasumicneRijeci):
  display += "_"

krajIgreHangman = False
# Broj zivota na raspolaganju
brojZivotaNaRaspolaganju = 6
  
# Ponavljanje petlje
while not krajIgreHangman:
  # Unos rijeci
  upisanoSlovo = input("\nUpiši jedno slovo: ").lower()

  clear()

  # ako je korisnik već upisao isto slovo
  if upisanoSlovo in display:
    print(f"Već ste upisalo slovo '{upisanoSlovo}'")
  
  # Provjera podudaranja
  for pozicijaSlovaNasumicneRijeci in range(duljinaNasumicneRijeci):
    # ovo je nova varijabla
    slovoNasumicneRijeci = odabranaNasumicnaRijec[pozicijaSlovaNasumicneRijeci]
    
    if upisanoSlovo == slovoNasumicneRijeci:
      display[pozicijaSlovaNasumicneRijeci] = slovoNasumicneRijeci

    # kraj for petlje

  if upisanoSlovo not in odabranaNasumicnaRijec:
    brojZivotaNaRaspolaganju -= 1

    print(f"\nUpisano slovo \'{upisanoSlovo}\' je neispravno.\nIzgubili ste jedan život.")
    
    if brojZivotaNaRaspolaganju == 0:
      krajIgreHangman = True
      print(f"\nUpisano slovo '{upisanoSlovo}' je neispravno.\n\nIgra je završena !!!\nIZGUBILI STE !!!")

  # Ispis pogođenih riječi na zaslon
  print("\n")
  print(f"{' '.join(display)}")

  # Ako više nema praznih slova
  if "_" not in display:
    krajIgreHangman = True
    print("\n\nČestitam. POBIJEDILI STE !!!")

  # Ispiši napredak korisnika ako pogriješi u upisu slova
  from hangman_art import fazeIgreHangman
  print(fazeIgreHangman[brojZivotaNaRaspolaganju])
