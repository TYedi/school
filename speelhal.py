toegangsticket_per_persoon = 7.45
aantal_personen = 4

prijs_per_5_min = 0.37
vr_tijd_in_minuten = 45

kosten_toegang = toegangsticket_per_persoon * aantal_personen
kosten_vr = (vr_tijd_in_minuten / 5) * prijs_per_5_min * aantal_personen

totale_kosten = kosten_toegang + kosten_vr

print(f"De totale kosten voor de speelhal zijn: €{totale_kosten:.2f}")