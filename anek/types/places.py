from anek.types.core import IActor
from .core import IPlace

class Place(IPlace):
    def __init__(self, name: str, *, members: list[IActor] = None, places: list[IPlace] = None):
        self._name = name
        super().__init__(members=members, places=places)
    
    @property
    def name(self):
        return self._name