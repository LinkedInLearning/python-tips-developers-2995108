netto = 7.91
brutto = netto * 1.19
bezahlt = 20
retour = bezahlt - brutto


print('Das Produkt kostet {:+f} € brutto bzw. {:+f} € netto.\nBezahlt habe ich {:+f} €. Wechselgeld ist {:+f} €.'
.format(brutto,netto, bezahlt, retour))
print("-"*50)

print('Das Produkt kostet {:+.2f} € brutto bzw. {:+.2f} € netto.\nBezahlt habe ich {:+.2f} €. Wechselgeld ist {:+.2f} €.'
.format(brutto,netto, bezahlt, retour))
print("-"*50)

