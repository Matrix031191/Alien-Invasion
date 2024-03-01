import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
                                      ai_settings.screen_height))
    pygame.display.set_caption("Napad vanzemaljaca")
    
    ship = Ship(ai_settings, screen)
    #make a group to store bullets in
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")
    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    while True:
        
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        

run_game()