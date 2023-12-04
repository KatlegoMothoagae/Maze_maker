import pygame
import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    maze_len = int(sys.argv[1])
else:
    maze_len = 10

pygame.init()

GRID_SIZE = 2
GRID_WIDTH = 19
GRID_HEIGHT = 19
GRID_GAP = 1
WINDOW_WIDTH = maze_len*20
WINDOW_HEIGHT = maze_len*20 
FPS = 60


GREEN = (0, 255, 0)
RED = (255, 0, 0)
colors = [RED, GREEN]

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Clicker")



def grid():
    grid = []
    for row in range(maze_len):
        for col in range(maze_len):
            grid.append([pygame.Rect(col * (GRID_WIDTH + GRID_GAP), row * (GRID_HEIGHT + GRID_GAP),GRID_WIDTH, GRID_HEIGHT),0])
    return grid

def maze_coordinates(rects):
    maze = []
    coordinates = []
    for row in range(maze_len):
        r = []
        for col in range(maze_len):
            if rects[row*maze_len + col][1] == 1:
                r.append(".")
                coordinates.append(f"({row},{col})")
            else:
                r.append("*")
                
        maze.append(r)
    return maze,coordinates
                
def draw_grid(rects):
    for rect in rects:
        pygame.draw.rect(window,colors[rect[1]],rect[0])

def save_maze(maze,filename):
    with open(f"{filename}.txt","w") as file:
        for row in range(len(maze[0])):
            for col in range(len(maze[0][row])):
            
                file.write(maze[0][row][col])
            file.write("\n")
    save_maze_coordinates(maze[1],f"{filename}_coordinates.txt")


def save_maze_coordinates(coordinates,filename):
    with open(f"{filename}.txt","w") as file:
        for c in coordinates:
            file.write(f"{c}\n")

clock = pygame.time.Clock()

def collision(rects, point):
    for rect in rects:
        
        if rect[0].collidepoint(point):
            rect[1] = 1 - rect[1]
rects = grid()
a_key_pressed = False

while True:
    maze_coordinates(rects)
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            collision(rects, event.pos)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and not a_key_pressed:
       
            save_maze(maze_coordinates(rects), "maze")
            a_key_pressed = True
        elif not keys[pygame.K_a]:
            a_key_pressed = False
        
    window.fill((0, 0, 0))

    draw_grid(rects)
    pygame.display.flip()
    clock.tick(FPS)
