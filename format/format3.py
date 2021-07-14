netto = 7.91
brutto = netto * 1.19
bezahlt = 20
retour = bezahlt - brutto


print('Das Produkt kostet {0:,.2f} € brutto bzw. {1:,.2f} € netto.\nBezahlt habe ich {2:,.2f} €. Wechselgeld ist {3:,.2f} €.'
.format(brutto,netto, bezahlt, retour))
print("-"*50)
print('Das Produkt kostet {0:,.3f} € brutto bzw. {1:,.3f} € netto.\nBezahlt habe ich {2:,.3f} €. Wechselgeld ist {3:,.3f} €.'
.format(brutto,netto, bezahlt, retour))
print("-"*50)
