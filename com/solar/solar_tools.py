# --*--coding:utf-8
# Author:cnn
import pygame
from pygame.sprite import Sprite
import os
import math

# 屏幕信息常量
SCREEN_RECT = pygame.Rect(0, 0, 800, 600)
# 路径
OBJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# 椭圆弧线的颜色
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Basic(Sprite):
    """
    基类
    """

    # object_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    def __init__(self, img_path, speed=0):
        # 当继承的不是object的时候,需要显示调用父类的__init__()
        super().__init__()
        # 图片
        self.image = pygame.image.load(img_path)
        # 速度
        self.speed = speed
        # 坐标
        self.rect = self.image.get_rect()


class Background(Basic):
    """
    背景图片类
    """

    def __init__(self):
        super().__init__(OBJECT_PATH + "/images/bg.jpg")

    def update(self):
        pass


class Solar(Basic):
    """太阳类"""

    def __init__(self):
        super().__init__(OBJECT_PATH + "/images/sun.jpg", speed=1)
        # self.rect.x=SCREEN_RECT.centerx
        self.rect.center = SCREEN_RECT.center


class Planet(Basic):
    """行星类基类"""

    def __init__(self, center, longAxis, shortAxis, img_path, speed=1.0):
        super().__init__(img_path, speed)
        # 行星运行的角度
        self.degree = 3.14 / 3
        self.center = center  # 某个Star对象
        self.rect.y = self.center.rect.y  # 行星的y坐标是中心的y坐标轴, 行星与中心Star在同一水平线上初始时
        self.rect.x = self.center.rect.x + longAxis  # 行星的x坐标是中心的x坐标 + 长轴
        self.longAxis = longAxis
        self.shortAxis = shortAxis
        self.ovalWidth = 2 * self.longAxis  # 椭圆的宽为2倍长轴的长度
        self.ovalHeight = 2 * self.shortAxis
        self.ovalX = self.center.rect.x + self.center.rect.width / 2 - self.longAxis
        self.ovalY = self.center.rect.y + self.center.rect.height / 2 - self.shortAxis

    # def move(self, screen):
    #     self.move_trace(screen)
    #     self.rect.x += self.speed
    #     self.rect.y += self.speed

    def move_trace(self, screen):
        # 画弧线
        pygame.draw.ellipse(screen, BLUE, (self.ovalX, self.ovalY, self.ovalWidth, self.ovalHeight), 1)
        # pygame.draw.ellipse(screen, GREEN, (100, 100, 400, 400), 1)
        # 刷新图
        pygame.display.flip()

    def move(self, screen):
        # self.rect.x = self.rect.x + (solor.rect.centerx) * math.cos(self.degree)
        # self.rect.y = self.rect.y + (solor.rect.centery) * math.sin(self.degree)
        # self.degree += 0.1
        self.move_trace(screen)
        # 行星围绕center的中心飞, 为了精确要加上图片宽度的一半
        self.rect.x = self.center.rect.x + self.center.rect.width / 2 + self.longAxis * math.cos(self.degree)
        self.rect.y = self.center.rect.y + self.center.rect.height / 2 + self.shortAxis * math.sin(self.degree)
        self.degree += self.speed


class EarthPlanet(Planet):
    def __init__(self, center, longAxis, shortAxis):
        super().__init__(center, longAxis, shortAxis, OBJECT_PATH + "/images/earth.jpg", speed=0.5)

        # def move(self, screen):
        #     # self.rect.x = self.rect.x + (solor.rect.centerx) * math.cos(self.degree)
        #     # self.rect.y = self.rect.y + (solor.rect.centery) * math.sin(self.degree)
        #     # self.degree += 0.1
        #     super().move_trace(screen)
        #     # 行星围绕center的中心飞, 为了精确要加上图片宽度的一半
        #     self.rect.x = self.center.rect.x + self.center.rect.width / 2 + self.longAxis * math.cos(self.degree)
        #     self.rect.y = self.center.rect.y + self.center.rect.height / 2 + self.shortAxis * math.sin(self.degree)
        #     self.degree += self.speed


class JupiterPlanet(Planet):
    def __init__(self, center, longAxis, shortAxis):
        super().__init__(center, longAxis, shortAxis, OBJECT_PATH + "/images/Jupiter.jpg", speed=0.25)


class NeptunePlanet(Planet):
    def __init__(self, center, longAxis, shortAxis):
        super().__init__(center, longAxis, shortAxis, OBJECT_PATH + "/images/Neptune.jpg", speed=0.3)
