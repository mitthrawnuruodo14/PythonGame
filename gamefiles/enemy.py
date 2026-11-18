import pygame
from gamefiles.entity import Entity
from gamefiles.player import Player
from gamefiles.world import World

class Enemy(Entity):
	def __init__(self, entity: Entity, health: int, damage: int, speed: int):
		super().__init__(entity.rect, entity.color, entity.has_collision, entity.is_visible)
		self.health = health
		self.damage = damage
		self.speed = speed
