import tkinter as tk                                                                # Importeer tkinter als tk

venster = tk.Tk()                                                                   # Variabele aanmaken voor de master

label = tk.Label(master=venster, text="Welke website wil je bezoeken?", height=2)   # Var. label voor het aanmaken van een label met 
label.grid(row=0, column=0, columnspan=2)                                           # de aangegeven argumenten op de aangegeven plaats

link_1 = tk.Entry(master=venster, width=33, font=("Helvetica",14),                  # 1e inputveld aanmaken met de aangegeven argumenten 
                  border=10, borderwidth=5)
link_1.grid(row=1, column=0)

link_2 = tk.Entry(master=venster, width=33, font=("Helvetica",14),                  # 2e inputveld aanmaken met de aangegeven argumenten
                  border=10, borderwidth=5)
link_2.grid(row=1, column=1)

def reset_links():                                                                  # Functie aanmaken voor het resetten van de inputs
    link_1.delete(0, 1)                                                             # Delete de eerste letter bij elke keer dat je het indrukt

    web_2 = link_2.get()                                                            # Variabele aanmaken voor het obtainen van de inhoud vd 2e link
    link_2.delete( 0, web_2.find(".")+1 )                                           # In die gekregen inhoud verwijder je alles wat voor het punt 
                                                                                    # komt alsook het punt zelf

knop = tk.Button(master=venster, command=reset_links,                               # Variabele aanmaken voor de knop 'reset input!'
                 text="Reset input!", width=50)
knop.grid(row=2, column=0, columnspan=2)                                            # Knop op de aangegeven plaats zetten

venster.mainloop()                                                                  # Maak de GUI zichtbaar op de pc