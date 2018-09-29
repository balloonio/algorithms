"""
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
Notes:

The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
The robot's initial position will always be in an accessible cell.
The initial direction of the robot will be facing up.
All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
Assume all four edges of the grid are all surrounded by wall.
"""

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    def __init__(self):
        self.robot = None
        self.visited = set()

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.traverse(0, 0, 0)

    # facing is 0: up, 1: right, 2: down, 3: left
    def traverse(self, thisx, thisy, facing):
        visited = self.visited
        robot = self.robot
        # robot is already here meaning this room is available
        # added room to visited and clean room
        visited.add((thisx, thisy))
        robot.clean()
        # loop through all facings starting from the current facing
        # visited the next room on the current facing if unvisted and available
        newfacing = facing
        for _ in range(4):
            nx, ny = self.get_next_room_facing(thisx, thisy, newfacing)
            # if next room visited or blocked, turn right to next facing
            if (nx, ny) in visited:
                newfacing = (newfacing + 1) % 4
                robot.turnRight()
                continue
            if not robot.move():
                newfacing = (newfacing + 1) % 4
                robot.turnRight()
                continue
            # already moved to the new room, dfs to next level
            self.traverse(nx, ny, newfacing)
            newfacing = (newfacing + 1) % 4
            robot.turnRight()
        # backtrack to the previous room with same facing as when it entered
        self.turn180()
        robot.move()
        self.turn180()

    def turn180(self):
        self.robot.turnRight()
        self.robot.turnRight()

    def get_next_room_facing(self, thisx, thisy, facing):
        delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dx, dy = delta[facing]
        return thisx + dx, thisy + dy


"""
My thoughs?
Dont be scared by the problems!
This is simply a backtrack DFS!
"""
