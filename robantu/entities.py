""" TODO """


class Entity(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        pass

    def handle_key_press(self, symbol, modifiers):
        pass

    def handle_key_release(self, symbol, modifiers):
        pass