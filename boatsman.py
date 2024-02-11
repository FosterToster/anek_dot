from anek.types import Moving, Dying, Emoting, Human, Place
from anek.types.core import IActor


sea = Place('море')

class Ship(IActor, Moving, Emoting, Dying):
    def __init__(self, *places: Place):
        super().__init__()
        print("На корабле есть", ", ".join(map(str, places)))
        self.places = list(places)

    @property
    def name(self):
        return 'корабль'
    
    def die(self):
        for plase in self.places:
            for member in plase.members:
                Dying.die_painful(member)
        super().die()


boatsman = Human('боцман')
captain = Human('капитан')

caps_cabin = Place('капитанская рубка')
machinery = Place('машинное отделение')

ship = Ship(caps_cabin, machinery)

ship.staying_at(sea)
boatsman.staying_at(caps_cabin)
captain.staying_at(caps_cabin)

crew = [Human('член экипажа') for _ in range(5)]
for man in crew:
    man.staying_at(machinery)

captain.say(boatsman, 'На нас идет торпеда, успокой команду')

boatsman.walkto(machinery)
boatsman.yall("Сейчас хуем по борту стукну, корабль развалится")

for man in crew:
    man.sceptic_to(boatsman)

boatsman.eqip('хуй')
boatsman.attack(ship)

ship.anger_to(boatsman)

boatsman.jumpto(sea)
captain.jumpto(sea)

ship.die_painful()

captain.yall("Дурак ты, боцман, торпеда мимо прошла")

