from gamefiles.entity import Entity
from gamefiles.humanoid import Humanoid

class Enemy(Humanoid):
	def __init__(self, entity, health, damage, speed, worth):
		super().__init__(
			entity=Entity(entity.pos, (entity.width, entity.height), entity.color, entity.has_collision, entity.is_visible, entity.z_index), 
			health=health,
			speed=speed
		)
		self.damage = damage
		self.worth = worth
