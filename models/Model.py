from random import randint

from models.Database import Database
from models.ExportToFile import ExportToFile
from models.Stopwatch import Stopwatch

"""Ülesanne:
1. Tehke meetod no_cheater() Database klassi, mis tagastab ainult ausad mängijad.
2. Näita edetabelis ainult ausaid mängijaid ning edetabelis näita nimi, äraarvatav number, sammude arv ja aeg (00:00:00) Ilusati :)
3. Nimest näita ainult 15 esimest tähte kui on pikem nimi."""


class Model:
    #Defineerime klassi muutujad
    pc_nr = randint(1,100) #Juhuslik number
    steps = 0 #Käikude arv
    game_over = False #Mäng ei ole läbi
    cheater = False #Mängija ei ole petja
    stopwatch = Stopwatch() #Loome stopperi objekti


    def __init__(self):
        """Konstruktor"""
        self.reset_game()

    def reset_game(self):
        """Teeb uue mängu"""
        self.pc_nr = randint(1,100)
        self.steps = 0
        self.game_over = False
        self.cheater = False
        self.stopwatch.reset() # Nullib stopperi
        #self.stopwatch.start() #Käivitab stopperi

    def ask(self):
        """Küsib numbrit ja kontrollib"""
        user_nr = int(input('Sisesta number: ')) #Küsi kasutajalt numbrit
        self.steps += 1 #Sammude arv kasvab ühe võrra

        if user_nr == 1000: #Tagauks
            self.cheater = True
            self.game_over = True #Mäng sai läbi
            self.stopwatch.stop() #Peata aeg
            print(f'Leidsid mu nõrga koha. Õige number oli {self.pc_nr}.')
        elif user_nr > self.pc_nr:
            print('Väiksem')
        elif user_nr < self.pc_nr:
            print('Suurem')
        elif user_nr == self.pc_nr:
            self.game_over = True
            self.stopwatch.stop()
            print(f'Leidsid õige numbri {self.steps} sammuga.')

    def lets_play(self):
        """Mängime mängu avalik meetod"""
        self.stopwatch.start() #Paneb stopperi käima
        while not self.game_over:
            self.ask()
        print(f'Mäng kestis {self.stopwatch.format_time()}')
        self.what_next() #Mis on järgmiseks #Nime küsimine ja kirje lisamine
        self.show_menu() #Näita mängu menüüd


    def what_next(self):
        """Küsime mängija nime ja lisame info andmebaasi"""
        name = self.ask_name()
        # print(name) #testisime kas küsib nime
        db = Database() #Loo andmebaasi objekt
        db.add_record(name, self.pc_nr, self.steps, self.cheater, self.stopwatch.seconds)


    @staticmethod
    def ask_name():
        """Küsib nime ja tagastab korrektse nime"""
        name = input('Kuidas on mängija nimi? ')
        if not name.strip():
            name = 'Teadmata'
        return name.strip()

    def show_menu(self):
        """Näita mängu menüüd"""
        print('1 - Mängima')
        print('2 - Edetabel')
        print('3 - Välju programmist')
        user_input = int(input('Sisesta number [1, 2 või 3]: '))
        if 1 <= user_input <= 3:
            if user_input == 1:
                self.reset_game() #Kõigepealt resetid selle mängu ära
                # self.stopwatch.start() #Käivita stopper
                self.lets_play() #Hakkad uuesti mängima
            elif user_input == 2:
                #self.show_leaderboard() #Näita edetabelit
                #self.show_no_cheater()
                #self.show_menu()#Näita menüüd
                etf = ExportToFile()
                etf.export()
                self.show_no_cheater()
                self.show_menu()
            elif user_input == 3:
                print('Bye, bye :)')
                exit() #Igasugune skripti töö lõpp
        else:
            self.show_menu()


    @staticmethod
    def show_leaderboard():
        """Näita edetabelit"""
        db = Database()
        data = db.read_records()
        if data:
            for record in data:
                print(record)  # name oleks record[1]

    def show_no_cheater(self):
        """Edetabel ausatele mängijatele"""
        db = Database()
        data = db.no_cheater()
        if data:
            #Vormindus funktsioon veerule
            #formatters = {'Mängu aeg': self.format_time}
            print() #Tühirida enne tabelit
            #self.print_table(data, formatters)
            self.manual_table(data)
            print()


    @staticmethod
    def format_time(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f'{hours:02}:{minutes:02}:{seconds:02}'

    def manual_table(self, data):
        print('Nimi             | Number | Sammud | Mängu aeg')
        for row in data:
            print('----------------------------------------------')
            print(f'{row[0][:15]:<16} | {row[1]:>6} | {row[2]:>6} | {self.format_time(row[3]):>9}')




