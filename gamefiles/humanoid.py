from gamefiles.entity import Entity

class Humanoid(Entity):
	def __init__(self, entity, health, speed):
		super().__init__(entity.pos, (entity.width, entity.height), entity.color, entity.has_collision, entity.is_visible, entity.z_index)
		self.health = health
		self.speed = speed

	def get_hit(self, damage: int):
		pass
