
__all__ = [
        'Room',
        'TresureRoom',
        'FightRoom'
        ]

class Room(object):
    
    def __init__(self, name, directions)
        self.name = name
        self.directions = directions

    def get_name(self):
        return self.name

    def get_info(self):
        pass

    def go(self):
        return self.directions[self.choose()]

    def interact(self):
        pass

    def choose(self):
        for key, value in self.directions:
            print(key + ' - ' + value)
        return input()


class TresureRoom(Room):
    def __init__(self, name, directions, reward):
        super.__init__(name, directions)
        self.reward = reward

    def get_info(self):
        print("A tresure room. Here you can find some shiny stuff!")

    def interact(self):
        return self.reward


class FightRoom(Room):
    def __init__(self, name, directions, enemy, damage):
        super.__init__(name, directions)
        self.enemy = enemy
        self.damage = damage

    def get_info(self):
        print("A fight room. You are here to fight the boss!")
    
    def interact(self):
        self.enemy -= self.damage
        if self.enemy <= 0:
            print("You killed th boss")
            go()
