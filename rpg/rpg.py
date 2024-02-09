import time
import random
import pygame
class Player:
    def __init__(self,name,prof):
        self.name = name
        self.hp = 50
        self.power = 5
        self.iq = 60
        self.prof = prof
        self.day = 1
        self.energy = 7
        self.pts = 0

        self.create_hero()
        self.training()

    def create_hero(self):
        if self.prof == '1':
            self.hp *= 2
            self.power *= 2
            self.iq *= 0.5
            print(f'{self.name} готов. Атрибуты героя \nЗдоровье: {self.hp} \nСила: {self.power} \niq: {self.iq} ')
            time.sleep(1)
        elif self.prof == '2':
            self.hp *= 1.3
            self.power *= 1.3
            self.iq *= 2.5
            print(f'{self.name} готов. Атрибуты героя \nЗдоровье: {self.hp} \nСила: {self.power} \niq: {self.iq} ')
            time.sleep(1)

    def training(self):
        attack = random.randint(0, 6)
        go = True
        kind = input(f'Пора работать над собой у вас есть несколько вариантов: '
                     '\n1.Пойти в тренажерный зал '
                     '\n2.Пройти курс про успешный успех '
                     '\n3.Поиграть в доту 2 \n')
        if kind == '1':
            print(f'Вы пошли в зал')
            time.sleep(1)
            if attack == 6:
                self.fight()
            else:
                while go:
                    print('Вы начали тренироваться')
                    for i in range(5):
                        print('+power')
                        time.sleep(1)
                    self.power += 10
                    self.energy -= 2
                    print(f'Вы стали сильнее Сила: {self.power} \nОсталось энергии: {self.energy}')
                    if self.energy <= 0:
                        print('Вы переусердствовали и в итоге погибли. \nGAME OVER')
                        self.loose()
                    go = input('Еще? \n1.Да \n2.Нет,хватит \n')
                    if go == '2':
                        go = False
                choice = input('Что будем делать дальше? \n1.Улучшаться \n2.Отдыхать \n3.3.Убить дракона(очень силён) hp: 500 power: 25 ')
                if choice == '1':
                    self.training()
                elif choice == '2':
                    self.relax()
                elif choice == '3':
                    self.shop()

        elif kind == '2':
            print('Вы включили ноутбук и начали смотреть курс')
            print(attack)
            if attack == 6:
                self.meteor()
            else:
                for i in range(7):
                    print('+iq')
                    time.sleep(0.5)
            self.iq += 7
            self.energy -= 1
            if self.energy <= 0:
                print('Вы переусердствовали и в итоге погибли. \nGAME OVER')
                self.loose()
            print(f'Вы стали умнее iq: \n{self.iq} \nОсталось энергии: {self.energy}')
            choice = input('Что будем делать дальше? \n1.Улучшаться \n2.Отдыхать \n3.3.Убить дракона(очень силён) hp: 500 power: 25 ')
            if choice == '1':
                self.training()
            elif choice == '2':
                self.relax()
            elif choice == '3':
                self.shop()


        elif kind == '3':
            print('Вы включили ноутбук и начали деградировать ')
            if attack == 6:
                self.meteor()
            else:
                while go:
                    dota = [-25, +25]
                    result = random.choice(dota)
                    self.pts += result
                    print(f'{result} \nМмр: {self.pts} ')
                    time.sleep(0.5)
                    go = input('Еще? \n1.Да \n2.Нет,хватит \n')
                    self.energy -= 1
                    print(f'Осталось энергии: {self.energy}')
                    if go == '2':
                        go = False
                    if self.energy <= 0:
                        print('Вы переусердствовали и в итоге погибли. \nGAME OVER')
                        self.loose()
        choice = input('Что будем делать дальше? \n1.Улучшаться \n2.Отдыхать \n3.Убить дракона(очень силён) hp: 500 power: 25 ')
        if choice == '1':
            self.training()
        elif choice == '2':
            self.relax()
        elif choice == '3':
            self.shop()

    def relax(self):
        attack = random.randint(0,6)
        kind = input(f'Как будем отдыхать? \n1.Погулять в наушниках \n2.Покурить \n3.Лечь спать \n')
        if kind == '1':
            print('Вы вышли на прогулку')
            if attack == 6:
                self.fight()
            else:
                for i in range(5):
                    print('+энергия')
                    self.energy += 0.2
                    time.sleep(0.5)
                print(f'Вы немного востановились \nЭнергия: {self.energy}')
                choice = input('Что будем делать дальше? \n1.Улучшаться \n2.Отдыхать \n3.Убить дракона(очень силён) hp: 500 power: 25 ')
                if choice == '1':
                    self.training()
                elif choice == '2':
                    self.relax()
                elif choice == '3':
                    self.shop()

        elif kind == '2':
            print('Вы подожгли сигарету...')
            for i in range(5):
                print('+энергия \n-здоровье')
                self.hp -= 4
                self.energy += 0.1
                time.sleep(0.5)
            print(f'Вы немного востановились \nЭнергия: {self.energy} \nЗдоровье: {self.hp}')
            choice = input('Что будем делать дальше? \n1.Улучшаться \n2.Отдыхать \n3.Убить дракона(очень силён) hp: 500 power: 25 ')
            if choice == '1':
                self.training()
            elif choice == '2':
                self.relax()
            elif choice == '3':
                self.shop()

        elif kind == '3':
            print('Вы легли спать')
            for i in range(7):
                print('+энергия')
                time.sleep(0.5)
            self.energy += 7
            print(f'Вы  востановились \nЭнергия: {self.energy}')
            choice = input('Что будем делать дальше? \n1.Улучшаться \n2.Отдыхать \n3.Убить дракона(очень силён) hp: 500 power: 25 ')
            if choice == '1':
                self.training()
            elif choice == '2':
                self.relax()
            elif choice == '3':
                self.shop()

    def fight(self):
        print('На вас напали гопники. Придется драться')
        time.sleep(2)
        if self.power >= 15:
            print('Они оказались слишком слабы. -3 гопаря')
            choice = input('Что будем делать дальше? \n1.Улучшаться \n2.Отдыхать \n3.Убить дракона(очень силён) hp: 500 power: 25 ')
            if choice == '1':
                self.training()
            elif choice == '2':
                self.relax()
            elif choice == '3':
                self.shop()
        else:
            print('Вас избили, и вы погибли от кровотечения \n GAME OVER')
            self.loose()

    def meteor(self):
        print('Вы услышали объявление из новостей о том, что скоро упадет метеорит \nВы пытаетесь придумать, как вам выжить')
        time.sleep(3)
        if self.iq > 180:
            print('Так как вы довольно умны. Вы додумались убежать в бункер и выжили')
            choice = input('Что будем делать дальше? \n1.Улучшаться \n2.Отдыхать \n3.Убить дракона(очень силён) hp: 500 power: 25 ')
            if choice == '1':
                self.training()
            elif choice == '2':
                self.relax()
            elif choice == '3':
                self.shop()

        else:
            print('Вы слишком тупой и не додумались пойти в бунукер, а поэтому погибли. \nGAME OVER')
            self.loose()

    def shop(self):
        choice = input('Так как вы единственная надежда вам дают выбрать снаряжение \n1.Набор дракона(+50hp,+5power) \n2.Катана Сатори(+20power)')
        if choice == '1':
            self.hp += 50
            self.power += 5
        elif choice == '2':
            self.power += 20
        into = input('К дракону? '
                     '\n1.Да')
        if into == '1':
            self.final_fight()

    def final_fight(self):
        hp_drago = 500
        power_drago = 25
        print('Вы пошли в пещеру к дракону')
        time.sleep(2)
        print('Нашелся! ДРАКОН(300hp,25power) В бой!')
        while True:
            self.hp -= power_drago
            hp_drago -= self.power
            print(f'Ваше здоровье: {self.hp} \nЗдоровье дракона: {hp_drago}')
            time.sleep(1)
            if self.hp <= 0:
                print('Вы - никчемный герой.')
                self.loose()
            elif hp_drago <= 0:
                print('Вы стали героем и освободили мир от страданий. Теперь даже Джессика пойдет с вами на балл.')
                self.win()

    def win(self):
        background_colour = (234, 212, 252)
        screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('My game')
        screen.fill(background_colour)
        pygame.display.flip()
        img_win = pygame.image.load('win1.jpg')
        img_win_rect = img_win.get_rect(center=(250, 250))
        screen.blit(img_win, img_win_rect)
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        exit()

    def loose(self):
        background_colour = (234, 212, 252)
        screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('My game')
        screen.fill(background_colour)
        pygame.display.flip()
        img_win = pygame.image.load('loose1.png')
        img_win_rect = img_win.get_rect(center=(250, 250))
        screen.blit(img_win, img_win_rect)
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        exit()



myname = input('Как будут звать вашего героя?')
while True:
    print('Можно ввести только цифру "1" или "2"')
    prof = input('Выберите вид героя. Нажмите \n1.Тупой, но сильный. \n2.Умный, но слабый \n')
    if prof == '1' or prof == '2':
        break
if prof == '1' or prof == '2':
    print('Тип выбран, герой создается...')
    time.sleep(2)

hero = Player(myname,prof)

