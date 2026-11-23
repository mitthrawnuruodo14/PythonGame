from gamefiles.entity import Entity
from gamefiles.world import World

class Humanoid(Entity):
	def __init__(self, entity, health, speed):
		super().__init__(entity.pos, (entity.width, entity.height), entity.color, entity.has_collision, entity.is_visible, entity.z_index)
		self.max_health = health
		self.health = self.max_health
		self.speed = speed

	def get_hit(self, damage: int, world: World):
		pass
