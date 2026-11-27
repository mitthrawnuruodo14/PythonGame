import math
import time
import random
from copy import copy
import pygame  # type: ignore

from gamefiles.world import World
from gamefiles.settings import *  # type: ignore
from gamefiles.player import *  # type: ignore
from gamefiles.camera import Camera
from gamefiles.menu import *
from gamefiles.controls import *
from gamefiles.level import *
from gamefiles.game import GameState
from gamefiles.enemy import Enemy
from gamefiles.enemies.zombie import Zombie
from gamefiles.enemies.skeleton import Skeleton
from gamefiles.enemies.splitter import Splitter
from gamefiles.enemies.rammer import Rammer
from gamefiles.leaderboard import *


def get_spawn_interval(time_survived: float) -> float:
    initial_interval = 2.5
    min_interval = 0.4
    growth_factor = 0.02

    return min_interval + (initial_interval - min_interval) * math.exp(-growth_factor * time_survived)

screen = pygame.display.set_mode(RESOLUTION, pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()

camera = Camera(screen)
world = World(Player(0, 0))
menu = Menu(screen)

game_state = GameState.MENU
inputs: list = []

build_level(screen, world.entities)
world.update_draw_order()

enemies = [
    Zombie(50, 50),
    Skeleton(700, 500),
    Splitter(-50, -400, 100, 3, 40),
    Rammer(600, 200)
]

upgrade_active = False

button_width = 220
button_height = 100
button_gap = 20

total_width = button_width * 5 + button_gap * 4
start_x = (screen.get_width() - total_width) // 2

upgrade_buttons = [
    pygame.Rect(
        start_x + i * (button_width + button_gap),
        50,
        button_width,
        button_height
    )
    for i in range(5)
]

pen_pick_required_count = 2
pen_pick_count = 0
split_pick_required_count = 2
split_pick_count = 0
upgrade_names = [
    "More damage",
    "Heal",
    "Move speed",
    "Penetration",
    "Split level"
]

last_spawned_enemy_timestamp = 0
next_upgrade_points = 100
upgrade_step = 1000
upgrade_counter = 0
time_passed = 0
upgrade_just_appeared = False

is_game_running = True
while is_game_running:
    delta_time = clock.tick(120) / 1000.0

    for event in pygame.event.get(pygame.QUIT):
        is_game_running = False

    get_inputs(inputs)

    if game_state == GameState.MENU:
        game_state = menu.update(game_state, inputs)
        menu.draw(screen)

    elif game_state == GameState.IN_LEVEL:
        if upgrade_active:
            if Input.MOUSE_LEFT in inputs:
                for i, button in enumerate(upgrade_buttons):
                    if button.collidepoint(inputs[Input.MOUSE_POS_IDX]):
                        if i == 0:
                            world.player.damage += 10
                        elif i == 1:
                            world.player.health = world.player.max_health
                        elif i == 2:
                            world.player.speed += 50
                        elif i == 3:
                            if (pen_pick_count >= pen_pick_required_count - 1):
                                world.player.penetration += 1
                                pen_pick_count = 0
                            else:
                                pen_pick_count += 1
                        elif i == 4:
                            if (split_pick_count >= split_pick_required_count - 1):
                                world.player.split_upgrade_level += 1
                                split_pick_count = 0
                            else:
                                split_pick_count += 1

                        upgrade_active = False
                        next_upgrade_points += upgrade_step * (1 + upgrade_counter * 0.25)
                        upgrade_counter += 1

        if not upgrade_active:
            time_passed += delta_time

        if not bool(max(0, world.player.health)):
            name = menu.player_name if menu.player_name != "" else "Unbekannt"
            with open("gamefiles/leaderboard.txt", "a", encoding="utf-8") as datei:
                datei.write(f"{world.player.points}:{name}\n")
            menu = Menu(screen)

            world.entities = [
                entity for entity in world.entities
                if not isinstance(entity, Enemy)
            ]

            world.player.health = world.player.max_health
            world.player.speed = world.player.speed_base
            world.player.damage = world.player.damage_base
            world.player.penetration = world.player.penetration_base
            world.player.split_upgrade_level = world.player.split_upgrade_level_base
            world.player.points = 0
            world.player.pos = pygame.Vector2(0, 0)

            time_passed = 0
            last_spawned_enemy_timestamp = 0
            next_upgrade_points = 100
            upgrade_active = False

            game_state = GameState.MENU

        if min(time_passed - last_spawned_enemy_timestamp, get_spawn_interval(time_passed)) == get_spawn_interval(time_passed):
            enemy = copy(random.choice(enemies))
            enemy_pos = world.player.pos

            while (enemy_pos - world.player.pos).length() != 800 and abs((enemy_pos - world.player.pos).length() - 800) == 800 - (enemy_pos - world.player.pos).length():
                enemy_pos = pygame.Vector2(
                    random.randint(-710, 700),
                    random.randint(-710, 700)
                )

            enemy.pos = enemy_pos
            world.entities.append(enemy)

            last_spawned_enemy_timestamp = time_passed

        if min(world.player.points, next_upgrade_points) == next_upgrade_points and not upgrade_active:
            upgrade_active = True
            upgrade_just_appeared = True

        if not upgrade_active:
            world.update_entities(screen, inputs, delta_time)


        for entity in world.entities:
            if entity.has_collision:
                for _entity in world.entities:
                    if entity.has_collision and _entity != entity and isinstance(_entity, Humanoid):
                        _entity.uncollide(entity)

                world.player.uncollide(entity)

        camera.update(world.player)

        screen.fill((28, 32, 38))

        world.draw_screen(camera, screen)

        health_bar_width = 250
        health_bar_height = 25

        pygame.draw.rect(screen, "red", pygame.Rect(12, 12, health_bar_width, health_bar_height))

        player_health_ratio = world.player.health / world.player.max_health

        pygame.draw.rect(screen, "green", pygame.Rect(12, 12, health_bar_width * player_health_ratio, health_bar_height))

        health_text = FONT_36.render(f"{world.player.health}/{world.player.max_health}", True, (255, 255, 255))

        screen.blit(health_text, (90, 12))

        points_text = FONT_36.render(f"{world.player.points}", True, (255, 255, 255))

        screen.blit(points_text, (screen.get_rect().width//2 - 20, 12))

        if upgrade_active:
            for i, button in enumerate(upgrade_buttons):
                mouse_pos = pygame.mouse.get_pos()

                color = ((80, 140, 220) if button.collidepoint(mouse_pos) else (50, 100, 180))

                pygame.draw.rect(screen, color, button, border_radius=0)

                if i == 3:
                    text = FONT_36.render(f"penentration ({pen_pick_count}/{pen_pick_required_count})", True, (255, 255, 255))
                elif i == 4:
                    text = FONT_36.render(f"Split level ({split_pick_count}/{split_pick_required_count})", True, (255, 255, 255))
                else:
                    text = FONT_36.render(upgrade_names[i], True, (255, 255, 255))

                text_rect = text.get_rect(center=button.center)
                screen.blit(text, text_rect)

    pygame.display.flip()

    if upgrade_just_appeared:
        time.sleep(0.5)
        upgrade_just_appeared = False


pygame.quit()
