# --*--coding:utf-8
# Author:cnn
import pygame
from com.solar.solar_tools import *
import sys


# 创建时钟对象
clock = pygame.time.Clock()


class SolarMain(Sprite):
    pygame.init()

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_RECT.width, SCREEN_RECT.height))
        self.__create_sprites()

    def __create_sprites(self):
        # 创建背景图片精灵
        background = Background()
        # print(background.rect)
        self.background_group = pygame.sprite.Group()
        self.background_group.add(background)
        #创建太阳
        self.solar=Solar()
        self.solar_group=pygame.sprite.Group()
        self.solar_group.add(self.solar)
        #创建地球
        self.earth = EarthPlanet(self.solar,self.solar.rect.y/2,self.solar.rect.x/3)
        self.earth_group = pygame.sprite.Group()
        self.earth_group.add(self.earth)
        #创建Jupiter
        self.jupiter = JupiterPlanet(self.solar, self.solar.rect.y / 3, self.solar.rect.x / 4)
        self.jupiter_group = pygame.sprite.Group()
        self.jupiter_group.add(self.jupiter)
        #创建Neptune
        self.neptune = NeptunePlanet(self.solar, self.solar.rect.y/4, self.solar.rect.x/5)
        self.neptune_group = pygame.sprite.Group()
        self.neptune_group.add(self.neptune)
    def start(self):
        """
        循环
        :return:
        """
        while True:
            clock.tick(60)
            self.check_event()
            self.update_sprite()
            self.move()


    def check_event(self):
        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.over()

    def update_sprite(self):
        """更新精灵"""
        self.background_group.update()
        self.background_group.draw(self.screen)
        self.solar_group.update()
        self.solar_group.draw(self.screen)
        self.earth.update()
        self.earth_group.draw(self.screen)
        self.jupiter_group.update()
        self.jupiter_group.draw(self.screen)
        self.neptune_group.update()
        self.neptune_group.draw(self.screen)
        pygame.display.update()

    def move(self):
        """
        精灵移动
        :return:
        """
        self.earth.move(self.screen)
        self.jupiter.move(self.screen)
        self.neptune.move(self.screen)

    def over(self):
        """点击x停止"""
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    solar_main = SolarMain()
    solar_main.start()
