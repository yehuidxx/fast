import random
import pygame
from pygame.locals import *
from sys import exit

# 常量定义
PANEL_WIDTH = 1920
PANEL_HEIGHT = 1200

# 初始化Pygame
pygame.init()
screen = pygame.display.set_mode((PANEL_WIDTH, PANEL_HEIGHT), FULLSCREEN, 28)
pygame.display.set_caption("Chinese Digital Rain")

# 使用支持中文的字体（需确保系统有该字体）
font = pygame.font.SysFont("simhei", 20)  # 改为黑体
FONT_PX = font.size('雨')[0]  # 用中文字符计算宽度
COLUMNS = PANEL_WIDTH // FONT_PX  # 重新计算列数

# 透明层（用于拖尾效果）
trail_surface = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT), pygame.SRCALPHA)

# 生成中文常用字符集（可自行扩展）
chinese_chars = [
    '坚持 努力 冷静'
]
chars = ''.join(chinese_chars)

# 初始化下落位置和颜色
drops = [
    {
        'pos': 0,  # 下落位置
        'hue': random.randint(0, 360),  # 随机初始色相
        'speed': random.uniform(1, 6),  # 颜色变化速度
        'char_index': random.randint(0, len(chars)-1)  # 当前字符索引
    }
    for _ in range(COLUMNS)
]

while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            exit()

    # 添加拖尾效果
    trail_surface.fill(pygame.Color(0, 0, 0, 20))
    screen.blit(trail_surface, (0, 0))

    # 更新字符位置和颜色
    for i in range(COLUMNS):
        # 颜色变化
        drops[i]['hue'] = (drops[i]['hue'] + drops[i]['speed']) % 360
        current_color = pygame.Color(0)
        current_color.hsva = (drops[i]['hue'], 100, 100, 100)

        # 获取当前字符（使用索引实现连续变化）
        current_char = chars[drops[i]['char_index']]
        text = font.render(current_char, True, current_color)

        x_pos = i * FONT_PX
        y_pos = drops[i]['pos'] * FONT_PX

        # 绘制字符
        screen.blit(text, (x_pos, y_pos))

        # 重置位置条件
        if y_pos > PANEL_HEIGHT or random.random() > 0.95:
            drops[i]['pos'] = 0
            drops[i]['hue'] = random.randint(0, 360)
            drops[i]['speed'] = random.uniform(1, 6)
            drops[i]['char_index'] = random.randint(0, len(chars)-1)
        else:
            drops[i]['pos'] += 1
            # 字符渐变变化（每3帧切换一次）
            if pygame.time.get_ticks() % 3 == 0:
                drops[i]['char_index'] = (drops[i]['char_index'] + 1) % len(chars)

    pygame.display.flip()
    pygame.time.delay(44)