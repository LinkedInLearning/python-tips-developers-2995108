netto = 7.91
brutto = netto * 1.19
bezahlt = 20
retour = bezahlt - brutto


print('Das Produkt kostet {0:,.2f} €.\nZurück bekam ich {2:,.2f} €, da ich {1:,.2f} € bezahlt habe.'
.format(brutto, bezahlt, retour))