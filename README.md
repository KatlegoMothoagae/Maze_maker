### Maze Clicker

This Python script utilizes the Pygame library to create a simple maze clicker . The goal of the game is to click on grid cells to toggle their state between two colors (RED and GREEN). Additionally, the script allows the user to save the current maze configuration and coordinates of clicked cells.

### Usage:

#    Installation of Dependencies:
        Ensure you have Python installed on your system.
        Install Pygame library using: pip install pygame

#    Run the Script:
        Execute the script in the terminal by providing an optional command-line argument for the maze size: python script_name.py [maze_size].
        If no size is provided, the default maze size is set to 10.

#    Game Controls:
        Left Click: Toggle the state of a grid cell between RED and GREEN.
        Key 's': Save the current maze configuration and coordinates to files ("maze.txt" and "maze_coordinates.txt" respectively).

#    Grid Representation:
        The grid is represented by a matrix of cells, each having a width and height of 19 pixels with a gap of 1 pixel in between.
        The maze is initialized with a default size of 10x10 cells, which can be adjusted using the command-line argument.

#    File Saving:
        The save_maze function saves the maze configuration to a text file named "maze.txt".
        The save_maze_coordinates function saves the coordinates of clicked cells to a text file named "maze_coordinates.txt".

#    Exiting the Game:
        Click the close button on the window to exit the game gracefully.

### Example Usage:

bash

> python maze_clicker.py 15

This will run the script with a maze size of 15x15 cells.
### Notes:

    The game window will display a grid of cells, and you can interact with it using mouse clicks and the 's' key.

    The maze configuration and clicked cell coordinates are saved when the 's' key is pressed.

    Adjust the GRID_SIZE, GRID_WIDTH, and GRID_HEIGHT constants to modify the appearance of the grid.

Feel free to experiment with different maze sizes and grid configurations!