prijs_croissant = 0.39
aantal_croissant = 17

prijs_stokbrood = 2.78
aantal_stokbroden = 2

korting_per_bon = 0.50
aantal_kortingsbonnen = 3

totale_kosten = (prijs_croissant * aantal_croissant) + (prijs_stokbrood * aantal_stokbroden)

totale_korting = (korting_per_bon * aantal_kortingsbonnen)

te_betalen = totale_kosten - totale_korting

print(f"Het te betalen bedrag is: €{te_betalen:.2f}")