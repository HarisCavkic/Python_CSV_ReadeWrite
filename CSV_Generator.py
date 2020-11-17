from random import Random
import csv


firma = ["JA", "NEIN"]
objekt = ["Privatobjekt","Gewerbeobjekt"] ### 0 - Privatobjekt        1 - Gewerbeobjekt
anzahlKameras = [i for i in range(1,20)] + [i for i in range(1,11)] + [i for i in range(1,11)]
bereich = ["Innenbereich","Außenbereich"] ### 0-Innenbereich      1-Außenbereich
auflosung = [1,2,4,8] + 5 * [2,4,8] ### in Megapixel 1=> Andere
aufzeichnung = ["JA","NEIN"]
fields = ["Firma","Objekt", "Anzahl Kameras", "Bereich", "Auflösung", "Aufzeichnung"]
random = Random()





with open('pending.csv', 'w', newline='') as csvfile:
    i = 0
    csv_writer = csv.DictWriter(csvfile, fieldnames= fields)
    csv_writer.writeheader()

    while i<100:
        firmaV = firma[random.randrange(0,len(firma),1)]
        objektV = objekt[random.randrange(0,len(objekt),1)]
        anzahlKamerasV = anzahlKameras[random.randrange(0,len(anzahlKameras),1)]
        bereichV = bereich[random.randrange(0,len(bereich),1)]
        auflosungV = auflosung[random.randrange(0,len(auflosung),1)]
        aufzeichnungV  = aufzeichnung[random.randrange(0,len(aufzeichnung),1)]
        csv_writer.writerow({"Firma" : firmaV, "Objekt" : objektV,
                             "Anzahl Kameras" : anzahlKamerasV, "Bereich" : bereichV,
                             "Auflösung" : auflosungV, "Aufzeichnung" :aufzeichnungV})
        i+=1


