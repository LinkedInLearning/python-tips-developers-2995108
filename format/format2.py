netto = 7.91
brutto = netto * 1.19
bezahlt = 20
retour = bezahlt - brutto


print('Das Produkt kostet € {:<6} brutto bzw. € {:<6} netto.\nBezahlt habe ich € {:<6}. Wechselgeld ist € {:<6}.'
.format(brutto,netto, bezahlt, retour))
print("-"*50)
print('Das Produkt kostet € {0:<6} brutto bzw. € {1:<6} netto.\nBezahlt habe ich € {2:<6}. Wechselgeld ist € {3:<6}.'
.format(brutto,netto, bezahlt, retour))
print("-"*50)


