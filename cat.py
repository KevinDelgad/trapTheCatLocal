class Cat:

    movePaths = {}    

    def __init__(self, validSpaces):
        self.locationX = "5"
        self.locationY = "5"
        for elems in validSpaces:
            y = elems.split('x')[0]
            x = elems.split('x')[1]
            possibleTiles = []
            if(x == '0' or x == '10' or y == '0' or y == '10'):
                continue
            
            possibleTiles.append(str(int(y) - 1) + 'x' + x)
            possibleTiles.append(str(int(y) - 1) + 'x' + str(int(x) + 1))

            possibleTiles.append(y + 'x' + str(int(x) - 1))
            possibleTiles.append(y + 'x' + str(int(x) + 1))

            possibleTiles.append(str(int(y) + 1) + 'x' + x)
            possibleTiles.append(str(int(y) + 1) + 'x' + str(int(x) + 1))            

            self.movePaths[elems] = possibleTiles

        print(self.movePaths)

    def calculateNextMove(self, validSpaces):
        print(self.locationX)
        print(self.locationY)

    def checkTrapped(self, validSpaces):
        pass

    def checkWon(self):
        pass