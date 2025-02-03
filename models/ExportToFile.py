import csv
from datetime import datetime

from models.Database import Database


file = 'game_leaderboard_v2.txt'

class ExportToFile:
    def __init__(self, model):
        self.db = Database()
        self.data = self.db.for_export()
        self.model = model

    def export(self):
        header = 'name;steps;quess;cheater;game_length;game_time' #päis
        with open (file, 'w', encoding='utf-8') as f:
            f.write(f'{header}\n')
            for row in self.data:
                formated_time = self.model.format_time(row[4])
                data = (f'{row[0]};{row[1]};{row[2]};{row[3]};{formated_time};{datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S').strftime("%d.%m.%Y %H:%M:%S")}')
                f.write(f'{data}\n')
