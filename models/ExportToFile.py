import csv
from datetime import datetime
from time import strftime

from models.Database import Database

file = 'game_leaderboard_v2.txt'

class ExportToFile:
    db = Database()
    data = db.for_export()

    def __init__(self):
        self.export()

    def export(self):
        from models.Model import Model #Importisin modeli siin, kuna muidu andis errorit
        mo = Model()
        header = 'name;steps;quess;cheater;game_length;game_time' #päis
        with open (file, 'w', encoding='utf-8') as f:
            f.write(f'{header}\n')
            for row in self.data:
                data = (f'{row[0]};{row[1]};{row[2]};{row[3]};{mo.format_time(row[4])};{datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S').strftime("%d.%m.%Y %H:%M:%S")}')
                f.write(f'{data}\n')
