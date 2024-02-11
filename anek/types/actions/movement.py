from anek.types.core import IActor
from ..core import IMovementAction

class Walkto(IMovementAction):
    @property
    def name(self):
        return 'идет'
    
class BeingAt(IMovementAction):
    @property
    def name(self):
        return 'находится'
    
    def execute_by(self, actor: IActor):
        if actor.being_at:
            raise ValueError(f'{actor} уже находится в {actor.being_at}')
        
        return super().execute_by(actor)
    

class SweemTo(IMovementAction):
    @property
    def name(self):
        return 'плывет'
    

class JumpTo(IMovementAction):
    @property
    def name(self):
        return 'прыгает'