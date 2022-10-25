import pygame

class Node:

    def __init__(self, x, y, lenght):
        self.divided = False
        self.points = list()
        self.lenght = lenght # lenght equals to distance between center of square to edge of square
        self.capacity = 2
        self.x = x
        self.y = y

    def printInfo(self):
        print(f"x:{self.x}  y:{self.y}  divided:{self.divided}  pointCount:{len(self.points)}  lenght:{self.lenght}")
        if self.divided:
            self.leftUpChild.printInfo()
            self.rightUpChild.printInfo()
            self.leftDownChild.printInfo()
            self.rightDownChild.printInfo()

    def addPoint(self, point):
        if self.divided == True:
            self.addPointToChildren(point)
        elif self.contains(point):
            if len(self.points) == self.capacity:
                self.divide()
                self.addPointToChildren(point)
            else:
                self.points.append(point)

    def addPointToChildren(self, point):
        self.leftUpChild.addPoint(point)
        self.rightUpChild.addPoint(point)
        self.leftDownChild.addPoint(point)
        self.rightDownChild.addPoint(point)

    def contains(self, point):
        upEdge = self.y - self.lenght
        rightEdge = self.x + self.lenght
        downEdge = self.y + self.lenght
        leftEdge = self.x - self.lenght
        #print(upEdge, rightEdge, downEdge, leftEdge)
        return point.x > leftEdge and point.x < rightEdge and point.y < downEdge and point.y > upEdge
        
    def divide(self):
        x = self.x
        y = self.y
        newLenght = self.lenght / 2.0
        if self.divided == False:
            self.divided = True
            self.leftUpChild = Node(x - newLenght, y - newLenght, newLenght)
            self.rightUpChild = Node(x + newLenght, y - newLenght, newLenght)
            self.leftDownChild = Node(x - newLenght, y + newLenght, newLenght)
            self.rightDownChild = Node(x + newLenght, y + newLenght, newLenght)

            for p in self.points:
                self.addPointToChildren(p)
            
            self.points.clear()
    
    def draw(self, screen):
        if self.divided == True:
            self.leftUpChild.draw(screen)
            self.rightUpChild.draw(screen)
            self.leftDownChild.draw(screen)
            self.rightDownChild.draw(screen)
        else:
            pygame.draw.rect(screen, (255, 255, 255), [self.x - self.lenght, self.y - self.lenght, self.lenght * 2, self.lenght * 2], 1)
            for p in self.points:
                p.draw(screen)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), [self.x, self.y], 4.0)
