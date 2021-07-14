netto = 7.91
brutto = netto * 1.19
bezahlt = 20
retour = bezahlt - brutto

print('Das Produkt kostet {} € brutto bzw. {} € netto.\nBezahlt habe ich {} €. Wechselgeld ist {} €.'
.format(brutto,netto, bezahlt, retour))


print('Das Produkt kostet {0} € brutto bzw. {1} € netto.\nBezahlt habe ich {2} €. Wechselgeld ist {3} €.'
.format(brutto,netto, bezahlt, retour))