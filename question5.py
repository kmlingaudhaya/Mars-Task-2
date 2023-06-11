class RobotWorkspace:
    def __init__(self, width, height, robot_position):
        self.width = width
        self.height = height
        self.robot_position = robot_position
        self.workspace = [[1 for _ in range(width)] for _ in range(height)]

    def insert_obstacle(self, x, y):
        self.workspace[x][y] = 0

    def move_robot(self, direction):
        x, y = self.robot_position
        if direction == "up" and x-1 < 0:
            print("!!OOPS!! Out of workspace, out of workspace")
        elif direction == "down" and x+1 > self.height - 1:
            print("!!OOPS!! Out of workspace, out of workspace")
        elif direction == "left" and y-1 < 0:
            print("!!OOPS!! Out of workspace, out of workspace")
        elif direction == "right" and y+1 > self.width - 1:
            print("!!OOPS!! Out of workspace, out of workspace")

        elif direction == "up" and y > 0 and self.workspace[x-1][y] == 0:
            # self.robot_position = (x-1, y)
            print("Obstacle ahead, please reroute")
        elif direction == "down" and y <= self.height - 1 and self.workspace[x+1][y] == 0:
            # self.robot_position = (x+1, y)
            print("Obstacle ahead, please reroute")
        elif direction == "left" and x > 0 and self.workspace[x][y-1] == 0:
            # self.robot_position = (x, y-1)
            print("Obstacle ahead, please reroute")
        elif direction == "right" and x <= self.width - 1 and self.workspace[x][y+1] == 0:
            # self.robot_position = (x, y+1)
            print("Obstacle ahead, please reroute")

        elif direction == "up" and y >= 0 and self.workspace[x-1][y] != 0:
            self.robot_position = (x-1, y)
        elif direction == "down" and y <= self.height - 1 and self.workspace[x+1][y] != 0:
            self.robot_position = (x+1, y)
        elif direction == "left" and x >= 0 and self.workspace[x][y-1] != 0:
            self.robot_position = (x, y-1)
        elif direction == "right" and x <= self.width - 1 and self.workspace[x][y+1] != 0:
            self.robot_position = (x, y+1)

    def visualize_workspace(self):
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) == self.robot_position:
                    print("R", end=" ")
                else:
                    print(self.workspace[x][y], end=" ")
            print()


# Example usage
workspace = RobotWorkspace(5, 5, (2, 2))
workspace.insert_obstacle(1, 2)
workspace.insert_obstacle(4, 2)

print("Current position of the BOT")
# Move the robot
while True:
    workspace.visualize_workspace()
    direction = input("Enter direction (up/down/left/right) or 'exit' to quit: ")
    if direction == "exit":
        break
    workspace.move_robot(direction)
