import math
import pygame #type: ignore
from gamefiles.settings import * #type: ignore
from gamefiles.entity import Entity
from gamefiles.controls import *
from gamefiles.bullet import Bullet
from gamefiles.humanoid import Humanoid

class Player(Humanoid):
    def __init__(self, x: int, y: int):
        super().__init__(
            entity=Entity(
                pos=pygame.Vector2(x, y),
                size=(60, 60),
                color=(255, 255, 255),
                has_collision=True,
                is_visible=True,
                z_index=0,
            ),
            health=100,
            speed=200
        )
        self.health = 100
        self.hit_indicator_duration = 0.125
        self.active_hit_indicator_duration = 0.0
        self.shoot_cooldown = 0.3
        self.active_shoot_cooldown = 0.0
        
    def update(self, world, screen, inputs: list, delta_time):
        self.color = RED if self.active_hit_indicator_duration > 0.0 else WHITE

        self.active_hit_indicator_duration -= delta_time
        self.active_shoot_cooldown -= delta_time
        self.active_hit_indicator_duration = pygame.math.clamp(self.active_hit_indicator_duration, 0.0, self.hit_indicator_duration)
        self.active_shoot_cooldown = pygame.math.clamp(self.active_shoot_cooldown, 0.0, self.hit_indicator_duration)

        if Input.D in inputs:
            self.pos.x += 200 * delta_time
        if Input.A in inputs:
            self.pos.x -= 200 * delta_time
        if Input.W in inputs:
            self.pos.y -= 200 * delta_time
        if Input.S in inputs:
            self.pos.y += 200 * delta_time
        if Input.MOUSE_LEFT in inputs:
            if self.active_shoot_cooldown == 0.0:
                mouse_pos = pygame.Vector2(inputs[Input.MOUSE_POS_IDX])
                direction = mouse_pos - pygame.Vector2(screen.get_rect().width/2, screen.get_rect().height/2)
                angle = math.atan2(direction.y, direction.x)
                
                bullet_pos = pygame.Vector2(self.pos.x + self.width/2, self.pos.y + self.height/2)
                world.entities.append(Bullet(self, bullet_pos, (10, 10), angle, 1200, 10, 10))

                self.active_shoot_cooldown = self.shoot_cooldown

    def get_hit(self, damage: int):
        self.health -= damage
        self.active_hit_indicator_duration = self.hit_indicator_duration
