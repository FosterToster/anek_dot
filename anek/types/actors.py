from typing import Any
from .core import IActor, IPlace
from .actions.movement import Walkto, BeingAt, SweemTo, JumpTo
from .actions.life_functions import Die, Say, Yall, Scepsis, Pain, Anger, Equip, Attack

class Moving:
    def walkto(self, place: IPlace):
        self.do(Walkto(place))

    def staying_at(self, place: IPlace):
        self.do(BeingAt(place))

    def sweemto(self, place: IPlace):
        self.do(SweemTo(place))

    def jumpto(self, place: IPlace):
        self.do(JumpTo(place))

class Dying:
    def die(self):
        self.do(Die())

    def die_painful(self):
        self.do(Pain())
        self.die()

class Emoting:
    def sceptic_to(self, who: IActor):
        self.do(Scepsis(who))

    def anger_to(self, actor: IActor):
        self.do(Anger(actor))


class Saying:
    def say(self, to: IActor, phrase: str):
        self.do(Say(to, phrase))

    def yall(self, phrase: str):
        self.do(Yall(phrase))

class Human(IActor, Moving, Dying, Emoting, Saying):
    
    def __init__(self, name: str):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    def eqip(self, what: str):
        self.do(Equip(what))

    def attack(self, actor: IActor):
        self.do(Attack(actor))