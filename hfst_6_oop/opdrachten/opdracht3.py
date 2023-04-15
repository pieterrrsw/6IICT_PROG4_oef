# # import modules.
# import RPi.GPIO as GPIO
# import time

# # Zet poort 5 als ingang.
# GPIO.setup(5, GPIO.IN)

# # Detecteer wijziging in stand van knop.
# vorige_stand = None
# while True:  
#   if (GPIO.input(5) != vorige_stand):
#     if GPIO.input(5) == GPIO.HIGH:
#       print("Knop 5 is aan")
#     else:
#       print("Knop 5 is uit") 
  
#   vorige_stand = GPIO.input(5)

class Button:
    def __init__(self, pin_nummer):
        GPIO.setup(pin_nummer, GPIO.IN)
        self.pin_nummer = pin_nummer
        self.vorige_stand = GPIO.LOW

    def detect_wijziging(self):
        if GPIO.input(5) != self.vorige_stand:
          self.vorige_stand = GPIO.input(5)

          if GPIO.input(5) == GPIO.HIGH:
            print("Knop 5 is aan")
            return "omhoog"
          else:
            print("Knop 5 is uit") 
            return "omlaag"
        return "geen_wijziging"
        
class Led:
    def __init__(self, pin_nummer):
        self.pin_nummer = pin_nummer
        GPIO.setup(self.pin_nummer, GPIO.OUT)

    def aan(self):
        GPIO.output(self.pin_nummer, GPIO.HIGH)
        
    def uit(self):
        GPIO.output(self.pin_nummer, GPIO.LOW)
        
# # Niveau 1
# # Maak een knop aan op pin 5
# knop_5 = Button(5)

# while True:
#    # Controleer of een wijziging is gebeurt TOV de vorige loop.
#    # Indien ja, print huidige stand van knop.
#    knop_5.detect_wijziging()

# # Niveau 2
# # Maak een knop op pin 5
# knop = Button(5)
# # Maak een led op pin 8 en 10
# led_8 = Led(8)
# led_10 = Led(10)

# while True:
#   # Controleer wat de toestand van de knop is:
#   #   "omhoog", "omlaag", "geen_wijziging"
#   toestand = knop.detect_wijziging()

#   # Als de knop is aangezet, schakel led 8 aan en 10 uit.
#   if toestand == "omhoog":
#     led_8.aan()
#     led_10.uit()
#   # Anders als de knop is uitgezet, schakel led 10 aan en 8 uit.
#   elif toestand == "omlaag":
#     led_8.uit()
#     led_10.aan()
#   # Anders als de toestand van de knop niet gewijzigd is, doe niets.
#   else:
#     pass
