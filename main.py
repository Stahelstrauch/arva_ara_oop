from models.Database import Database
from models.Stopwatch import Stopwatch

if __name__ == '__main__':
    """stopper = Stopwatch() #Objekti loomine, sellega saime kontrollida, et stopper töötab
    stopper.start()
    input ("Oota..")
    stopper.stop()
    print(stopper.format_time())"""
    db = Database()
    data = db.read_records()
    if data:
        for record in data:
            print(record)
