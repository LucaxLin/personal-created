import pygame


pygame.init()
win = pygame.display.set_mode((500, 600))
win.fill((255, 255, 255))


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.width, self.height])
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(self.text, True, (255, 0, 0))
        win.blit(text,
                 (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isoverPos(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


def redrawWin():
    win.fill((255, 255, 255))
    stopButton.draw(win)
    contButton.draw(win)


run = True
stopButton = button((200, 200, 200), 140, 300, 250, 100, text='STOP')
contButton = button((200, 200, 200), 140, 450, 250, 100, text='CONTINUE')
scroll = True
while run:
    for i in range(1, 51):
        redrawWin()
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render(str(i), True, (255, 0, 0))
        if scroll:
            win.blit(text, (220, 180))
            pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and scroll:
                if stopButton.isoverPos(pos):
                    scroll = False
            if event.type == pygame.MOUSEBUTTONDOWN and not scroll:
                if contButton.isoverPos(pos):
                    scroll = True
