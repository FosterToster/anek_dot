from anek.types.core import IActor
from ..core import IAction

class Die(IAction):
    @property
    def name(self):
        return 'умирает'

    def execute_by(self, actor: IActor):
        if actor.being_at:
            actor.being_at.leave(actor)
            actor.being_at = None
        print(actor, self.name)


class Say(IAction):
    def __init__(self, say_to: IActor, phrase: str):
        self.say_to = say_to
        self.phrase = phrase
    
    @property
    def name(self):
        return 'говорит'
    
    def execute_by(self, actor: IActor):
        print(actor, self.name, self.say_to, f'"{self.phrase}"')


class Yall(IAction):
    def __init__(self, phrase: str):
        self.phrase = phrase
    
    @property
    def name(self):
        return 'кричит'
    
    def execute_by(self, actor: IActor):
        print(actor, self.name, f'"{self.phrase}"', end='')
        if actor.being_at:
            print(' это слышат:', ", ".join(map(str, [member for member in actor.being_at.members if member is not actor])))
        else:
            print()


class Emote(IAction):
    def __init__(self, to: IActor) -> None:
        self.to = to

    def execute_by(self, actor: IActor):
        print(actor, 'испытывает', self.name, end='')
        if self.to:
            print(' к', 'себе' if actor is self.to else self.to)
        else:
            print()


class Scepsis(Emote):
    @property
    def name(self):
        return 'скепсис'
    

class Anger(Emote):
    @property
    def name(self):
        return 'гнев'


class Pain(Emote):
    def __init__(self) -> None:
        super().__init__(None)

    @property
    def name(self):
        return 'боль'
    

class Equip(IAction):
    def __init__(self, what: str | None) -> None:
        self.what = what

    @property
    def name(self):
        return 'экипирует'
    
    def execute_by(self, actor: IActor):
        actor.equipped = self.what
        print(actor, self.name, 'ничего' if self.what is None else self.what)


class Attack(IAction):
    def __init__(self, who: IActor) -> None:
        self.who = who

    @property
    def name(self):
        return 'атакует'
    
    def execute_by(self, actor: IActor):
        print(actor, self.name, self.who, end='')
        if actor.equipped:
            print('с помощью', actor.equipped)
        else:
            print()

