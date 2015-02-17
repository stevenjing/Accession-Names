#Accession Names Code (Ch. 8, pg. 172)

for acc in accs:
    if re.search(r"d[arp]$", acc):
        print("\t" + acc)
