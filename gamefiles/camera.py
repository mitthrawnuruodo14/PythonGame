class Camera:
    def __init__(self, screen):
        self.offset_x = 0
        self.offset_y = 0
        self.screen = screen

    def update(self, player_centerx, player_centery):
        self.offset_x = player_centerx - self.screen.get_width() // 2
        self.offset_y = player_centery - self.screen.get_height() // 2

    def apply(self, rect):
        return rect.move(-self.offset_x, -self.offset_y)
