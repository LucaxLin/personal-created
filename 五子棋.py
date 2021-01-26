import pygame


def draw_circle(pos, count):
    if count // 2 == count / 2:
        pygame.draw.circle(window, 'white', pos, 20)
    else:
        pygame.draw.circle(window, 'black', pos, 20)


def aux_circle(pos):
    pygame.draw.circle(window, 'red', pos, 20)


def check_win(current_x, current_y, chess_board):
    connected_vertices = 1
    # horizontal
    for i in range(current_x - 1, -1, -1):
        if chess_board[current_x][current_y] == chess_board[i][current_y]:
            connected_vertices += 1
        else:
            break
    for i in range(current_x + 1, len(chess_board)):
        if chess_board[current_x][current_y] == chess_board[i][current_y]:
            connected_vertices += 1
        else:
            break
    if connected_vertices >= 5:
        return True
    else:
        connected_vertices = 1
    # vertical
    for i in range(current_y - 1, -1, -1):
        if chess_board[current_x][current_y] == chess_board[current_x][i]:
            connected_vertices += 1
        else:
            break
    for i in range(current_y + 1, len(chess_board)):
        if chess_board[current_x][current_y] == chess_board[current_x][i]:
            connected_vertices += 1
        else:
            break
    if connected_vertices >= 5:
        return True
    else:
        connected_vertices = 1
    # left diagonal
    left_top = min(current_x, current_y) + 1
    right_bottom = len(chess_board) - max(current_x, current_y)
    for i in range(1, left_top):
        if chess_board[current_x][current_y] == chess_board[current_x - i][current_y - i]:
            connected_vertices += 1
        else:
            break
    for i in range(1, right_bottom):
        if chess_board[current_x][current_y] == chess_board[current_x + i][current_y + i]:
            connected_vertices += 1
        else:
            break
    if connected_vertices >= 5:
        return True
    else:
        connected_vertices = 1
    # right diagonal
    left_bottom = len(chess_board) - max(len(chess_board) - current_x - 1, current_y)
    right_top = len(chess_board) - max(current_x, len(chess_board) - current_y - 1)
    for i in range(1, left_bottom):
        if chess_board[current_x][current_y] == chess_board[current_x - i][current_y + i]:
            connected_vertices += 1
        else:
            break
    for i in range(1, right_top):
        if chess_board[current_x][current_y] == chess_board[current_x + i][current_y - i]:
            connected_vertices += 1
        else:
            break
    if connected_vertices >= 5:
        return True
    return False


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.width, self.height])
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(self.text, True, (255, 0, 0))
        window.blit(text,
                    (self.x + (self.width / 2 - text.get_width() / 2),
                     self.y + (self.height / 2 - text.get_height() / 2)))

    def isoverPos(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


board_width = 750
board_height = 750
window_width = 1000
window_height = 1000
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
window.fill('gray')
replay_button = button('white', 800, 100, 150, 75, text='replay')
aux_button = button('black', 800, 100, 150, 75, text='replay')
replay_button.draw(window)
chess_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               ]
for i in range(1, 16):
    pygame.draw.line(window, 'black', (50, 50 * i), (board_width, 50 * i))
    pygame.draw.line(window, 'black', (50 * i, 50), (50 * i, board_height))
pygame.draw.circle(window, 'black', (400, 400), 5)
pygame.display.update()
run = True
count = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        pos = pygame.mouse.get_pos()
        pos_x, pos_y = pos[0], pos[1]
        valid_x = False
        valid_y = False
        for i in range(1, 16):
            if i * 50 - 20 < pos_x < 50 * i + 20:
                pos_x = 50 * i
                valid_x = True
                break
        for i in range(1, 16):
            if i * 50 - 20 < pos_y < 50 * i + 20:
                pos_y = 50 * i
                valid_y = True
                break
        if valid_x and valid_y:
            row_index = pos_x // 50 - 1
            col_index = pos_y // 50 - 1
            if chess_board[row_index][col_index] == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    draw_circle([pos_x, pos_y], count)
                    if count / 2 != count // 2:
                        chess_board[row_index][col_index] = 1
                    else:
                        chess_board[row_index][col_index] = 2
                    count += 1
                    pygame.display.update()
                    if check_win(row_index, col_index, chess_board):
                        font = pygame.font.SysFont('comicsans', 60)
                        text = font.render('YOU WIN', True, (255, 0, 0))
                        window.blit(text, (50, 850))
                        pygame.display.update()
        if replay_button.isoverPos(pygame.mouse.get_pos()):
            aux_button.draw(window)
            pygame.display.update()
        else:
            replay_button.draw(window)
            pygame.display.update()
        if replay_button.isoverPos(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                window.fill('gray')
                for i in range(1, 16):
                    pygame.draw.line(window, 'black', (50, 50 * i), (board_width, 50 * i))
                    pygame.draw.line(window, 'black', (50 * i, 50), (50 * i, board_height))
                pygame.draw.circle(window, 'black', (400, 400), 5)
                replay_button.draw(window)
                pygame.display.update()
                count = 1
                chess_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               ]
