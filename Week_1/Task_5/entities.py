

from dataclasses import dataclass

@dataclass
class Entity:
    name: str
    position: str 

    def interact(self):
        pass

@dataclass
class Player(Entity):
    health: int = 100

    def interact(self):
        print(f"Player '{self.name}' at {self.position} is ready for action. Health: {self.health}HP.")

@dataclass
class NPC(Entity):
    role: str = "Villager"

    def interact(self):
        print(f"NPC '{self.name}' at {self.position} says: 'Greetings! I am a {self.role}.'")

@dataclass
class Object(Entity):
    object_type: str = "Obstacle"

    def interact(self):
        print(f"Object '{self.name}' at {self.position} is a {self.object_type}. It does not respond.")
