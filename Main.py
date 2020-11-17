from tkinter import *
import csv
import re
from time import sleep
from tkinter import ttk
import pandas as pd
regex = re.compile('[0-9]+')
coutner= 0
header = []
formular = []
formulare = []
firma = ""
objekt = ""
anzahl = ""
kameras = ""
bereich = ""
auflosung = ""
aufzeichnung = ""
#Firma,Objekt,Anzahl Kameras,Bereich,Auflösung,Aufzeichnung



def main():

    def funct():

        with open('pending.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, quotechar='|')
            header = next(reader)
            firma, objek, anzahlKameras, bereich, auflosung, aufzeichnung = next(reader)
            firmaV.config(text = firma)

    button = Button(screen, text = "Nächstes", command = funct,cursor="closedhand").grid(row = 12, column = 4)



    screen.mainloop()




if __name__ == "__main__":
    notDone = []
    header = []
    with open('pending.csv',  newline='') as csvfile:
        reader = csv.reader(csvfile, quotechar='|')
        header = next(reader)
        with open('done.csv', 'w', newline='') as csvfileWrite:
            writeHeader = header + ["Preis"]
            csv_writer = csv.DictWriter(csvfileWrite, fieldnames= writeHeader)
            csv_writer.writeheader()

            #GUI
            screen = Tk()
            screen.geometry("500x500")
            screen.title("Formulare")

            #Static part
            firmaL = Label(screen ,text = "Firma :").grid(row = 0,column = 0)
            objektL = Label(screen ,text = "Objekt :").grid(row = 2,column = 0)
            anzahlL = Label(screen ,text = "Anzahl Kameras :").grid(row = 4,column = 0)
            bereicL = Label(screen ,text = "Bereich :").grid(row = 6,column = 0)
            auflosungL = Label(screen ,text = "Auflösung :").grid(row = 8,column = 0)
            aufzeichnungL = Label(screen ,text = "Aufzeichnung :").grid(row = 10,column = 0)
            leer = Label(screen ,text = "").grid(row = 12,column = 0)
            preis = Entry(screen)
            preis.grid(row = 14, column = 1)
            preisAngeben = Label(screen ,text = "Preis angeben:")
            preisAngeben.grid(row = 14,column = 0)


            #dynamica part
            values = next(reader)
            firmaV = Label(screen ,text = values[0])
            firmaV.grid(row = 0,column = 1)
            objekV = Label(screen ,text = values[1])
            objekV.grid(row = 2,column = 1)
            anzahlV = Label(screen ,text = values[2])
            anzahlV.grid(row = 4,column = 1)
            bereichV = Label(screen ,text = values[3])
            bereichV.grid(row = 6,column = 1)
            auflosungV = Label(screen ,text = f"{values[4]}Megapixel")
            auflosungV.grid(row = 8,column = 1)
            aufzeichnungV = Label(screen ,text = values[5])
            aufzeichnungV.grid(row = 10,column = 1)

            #button function
            def funct():
                priceV = preis.get()
                #no input, false input
                if not regex.match(priceV):
                    preisAngeben.config(text = "Bitte Preis angeben", fg = "Red")
                    preis.delete(0, END)
                    preis.insert(0, "")
                    return

                csv_writer.writerow({"Firma" : values[0], "Objekt" : values[1],
                                     "Anzahl Kameras" : values[2], "Bereich" : values[3],
                                     "Auflösung" : values[4], "Aufzeichnung" :values[5],
                                    "Preis" : priceV})


                # new csv row
                isthere = False
                for row in reader:
                    val = row
                    isthere = True
                    break

                if isthere:
                    firma, objekt, anzahlKameras, bereich, auflosung, aufzeichnung = val
                    firmaV.config(text = firma)
                    objekV.config(text = objekt)
                    anzahlV.config(text = anzahlKameras)
                    bereichV.config(text = bereich)
                    auflosungV.config(text = auflosung)
                    aufzeichnungV.config(text = aufzeichnung)
                    preis.delete(0, END)
                    preis.insert(0, "")
                    preisAngeben.config(text = "Preis angeben", fg = "Black")
                    values.clear()
                    values.extend(val)
                else:
                    csvfileWrite.close()
                    csvfile.close()
                    screen.destroy()


            button = Button(screen, text = "Speichern und Nächstes", command = funct,cursor="closedhand").grid(row = 14, column = 4)
            screen.mainloop()

            for row in reader:
                notDone.append(row)

    with open('pending.csv', "w+",  newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames= header)
        csv_writer.writeheader()

        for row in notDone:
            csv_writer.writerow({"Firma" : row[0], "Objekt" : row[1],
                                 "Anzahl Kameras" : row[2], "Bereich" : row[3],
                                 "Auflösung" : row[4], "Aufzeichnung" :row[5]})





