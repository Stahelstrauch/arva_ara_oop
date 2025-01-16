import time

from models.Database import Database
from models.Model import Model
from models.Stopwatch import Stopwatch

if __name__ == '__main__':
    model = Model()
    model.show_menu() # kui see on esimene ilma lets_playta, siis näed esimesena menüüd
    #TODO Järgnev rida oli enne show_menu osa
    #model.lets_play()

    """stopper = Stopwatch() #Objekti loomine, sellega saime kontrollida, et stopper töötab
    stopper.start()
    input ("Oota..")
    stopper.stop()
    print(stopper.format_time())"""
    """db = Database() #Kontrollisime sellega, et ühendus andmebaasiga on olemas ja saab andmed kätte sealt
    data = db.read_records()
    if data:
        for record in data:
            print(record)"""


    """print(f'Väljasta juhuslik number: {model.pc_nr}') #Arvuti mõeldud number, käivitati ka stopper
    time.sleep(2) #Oota 2 sekundit
    model.stopwatch.stop() #Jäta stopper seisma
    print(model.stopwatch.format_time())"""

