from abc import ABC, abstractproperty, abstractmethod

class IEntity(ABC):

    @abstractproperty
    def name(self):
        ...

    def __str__(self) -> str:
        return self.name
    

class IAction(IEntity):
    
    @abstractmethod
    def execute_by(self, actor: 'IActor'):
        ...


class IMovementAction(IAction):
    def __init__(self, place: 'IPlace'):
        self.place = place

    def execute_by(self, actor: 'IActor'):
        message_parts = [actor, self]
        if actor.being_at:
            message_parts.extend(['из', actor.being_at])
            actor.being_at.leave(actor)

        message_parts.extend(['в', self.place])
        actor.being_at = self.place
        self.place.enter(actor)
        
        print(' '.join(map(str, message_parts)))



class IActor(IEntity):
    
    def __init__(self):
        self.being_at: 'IPlace' = None
        self.equipped: str | None = None

    def do(self, action: IAction):
        action.execute_by(self)
    

class IPlace(IEntity):

    def __init__(self, *, members: list[IActor] = None, places: list['IPlace'] = None):
        self.members = members or []
        self.places = places or []
        
        for member in self.members:
            member.being_at = self        
    
    def enter(self, actor: IActor):
        self.members.append(actor)

    def leave(self, actor: IActor):
        self.members.remove(actor)