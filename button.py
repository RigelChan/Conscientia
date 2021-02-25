class Button:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height

        def isOver(self, pos):
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
                
            return False
