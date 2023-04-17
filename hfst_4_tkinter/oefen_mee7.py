import tkinter as tk                                                                # Importeer tkinter als tk.

venster = tk.Tk()                                                                   # Variabele aanmaken voor de master.

label = tk.Label(master=venster, text="Geef naam op: ", width=15, height=2,         # Label aanmaken in de master 'venster' met de 
                 highlightthickness=2, highlightbackground="black")                 # aangegeven argumenten.
label.grid(row=0, column=0)                                                         # De plaats van het label bepalen.

veld = tk.Entry(master=venster, width=50, fg="red")                                 # Inputveld aanmaken in de master 'venster'.
veld.grid(row=0, column=1)                                                          # Plaats van het veld bepalen.

def display_naam():
    tekst = f"Hallo, mijn naam is {veld.get()}!"                                    # Functie, die als die wordt opgeroepen, de input uit het 
    label_naam = tk.Label(master=venster, text=tekst, width=50, height=2)           # inputveld haalt om deze uiteindelijk te tonen in een nieuw 
    label_naam.grid(row=2, column=0, columnspan=2)                                  # label waarvan de plaats bepaalt wordt door de functie grid().

knop = tk.Button(master=venster, command=display_naam, text="Voer in!", width=50)   # Variabele aanmaken voor de knop 'voer in!'.
knop.grid(row=1, column=0, columnspan=2)                                            # Plaats en grootte van de knop bepalen.

venster.mainloop()                                                                  # Maak de GUI zichtbaar op de pc.
