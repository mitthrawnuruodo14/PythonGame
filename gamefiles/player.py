import math
import pygame #type: ignore
from gamefiles.settings import * #type: ignore
from gamefiles.entity import Entity
from gamefiles.controls import *
from gamefiles.bullet import Bullet
from gamefiles.humanoid import Humanoid

class Player(Humanoid):
    def __init__(self, x: float, y: float):
        super().__init__(
            entity=Entity(
                pos=pygame.Vector2(x, y),
                size=(40, 40),
                color=(255, 255, 255),
                has_collision=True,
                is_visible=True,
                z_index=0,
            ),
            health=100,
            speed=200
        )
        self.max_health = 100
        self.health = self.max_health
        self.damage_base = 20
        self.damage = self.damage_base
        self.speed_base = 200
        self.speed = self.speed_base
        self.penetration_base = 1
        self.penetration = self.penetration_base
        self.hit_indicator_duration = 0.125
        self.active_hit_indicator_duration = 0
        self.shoot_cooldown = 0.3
        self.active_shoot_cooldown = 0
        self.dash_cooldown = 4
        self.active_dash_cooldown = 0
        self.dash_speed = 800
        self.remaining_dash_distance = 0
        self.dash_distance = 400
        self.direction = pygame.Vector2(0, 0)
        self.move_state = "normal"
        self.kill_count = 0
        self.split_upgrade_level_base = 0
        self.split_upgrade_level = self.split_upgrade_level_base
        
    def update(self, world, screen, inputs: list, delta_time):
        self.color = RED if self.active_hit_indicator_duration > 0.0 else WHITE

        self.active_hit_indicator_duration -= delta_time
        self.active_shoot_cooldown -= delta_time
        self.active_dash_cooldown -= delta_time
        self.active_hit_indicator_duration = pygame.math.clamp(self.active_hit_indicator_duration, 0.0, self.hit_indicator_duration)
        self.active_shoot_cooldown = pygame.math.clamp(self.active_shoot_cooldown, 0.0, self.shoot_cooldown)
        self.active_dash_cooldown = pygame.math.clamp(self.active_dash_cooldown, 0.0, self.dash_cooldown)

        if self.move_state == "normal":
            self.direction = pygame.Vector2(0, 0)
            if Input.D in inputs:
                self.pos.x += self.speed * delta_time
                self.direction.x += 1
            if Input.A in inputs:
                self.pos.x -= self.speed * delta_time
                self.direction.x -= 1
            if Input.W in inputs:
                self.pos.y -= self.speed * delta_time
                self.direction.y -= 1
            if Input.S in inputs:
                self.pos.y += self.speed * delta_time
                self.direction.y += 1
            if Input.SPACE in inputs:
                if self.active_dash_cooldown == 0.0 and self.direction != pygame.Vector2(0, 0):
                    self.move_state = "dashing"
                    self.remaining_dash_distance = self.dash_distance
                    self.active_dash_cooldown = self.dash_cooldown
        else:
            self.pos += self.direction * self.dash_speed * delta_time
    
            self.remaining_dash_distance -= self.dash_speed * delta_time

            if self.remaining_dash_distance <= 0:
                self.move_state = "normal"

        if Input.MOUSE_LEFT in inputs:
            if self.active_shoot_cooldown == 0.0:
                mouse_pos = pygame.Vector2(inputs[Input.MOUSE_POS_IDX])
                direction = mouse_pos - pygame.Vector2(screen.get_rect().width/2, screen.get_rect().height/2)
                angle = math.atan2(direction.y, direction.x)
                
                bullet_pos = pygame.Vector2(self.pos.x + self.width/2, self.pos.y + self.height/2)
                world.entities.append(Bullet(self, bullet_pos, (10, 10), angle, 1200, self.damage, self.penetration, self.split_upgrade_level))

                self.active_shoot_cooldown = self.shoot_cooldown

    def get_hit(self, damage: int, world):
        self.health -= damage
        self.active_hit_indicator_duration = self.hit_indicator_duration
