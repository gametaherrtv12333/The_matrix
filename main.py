import pygame as pg
import random
import keyboard


class MatrixLetters:
    def __init__(self, app):
        self.app = app
        self.letters = "01"
        self.font_size = 23
        self.font = pg.font.SysFont('ms mincho', self.font_size, bold=False)
        self.columns = app.WIDTH // self.font_size
        self.drops = [1 for i in range(0, self.columns)]
    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False,(random.randint(133, 136), random.randint(210, 250), random.randint(12, 36)))
            pos = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self.app.surface.blit(char_render, pos)
            if self.drops[i] * self.font_size > app.HEIGHT and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1
            def randomize_font_scale():
                self.font_size = random.randint(24, 140)
            keyboard.add_hotkey("alt", lambda: randomize_font_scale())

    def run(self):
        self.draw()


class MatrixApp:
    def __init__(self):  # init programm
        self.RES = self.WIDTH, self.HEIGHT = 1300, 840
        pg.init()
        self.screen = pg.display.set_mode(self.RES)  # Screen
        self.surface = pg.Surface(self.RES, pg.SRCALPHA) #Surface
        self.clock = pg.time.Clock()  # To track time
        self.matrixLetters = MatrixLetters(self)  # Symbols

    def draw(self):
        self.surface.fill((0, 0, 0, 10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0, 0))

    def run(self):  # Main loop
        while True:
            self.draw()  # Riding the screen
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()  # Update Screen
            self.clock.tick(30)  # Char drop Speed


if __name__ == '__main__':
    app = MatrixApp()
    app.run()
