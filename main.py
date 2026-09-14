from PIL import Image
import os

def FindDistanceBetweenTwoColors(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

def FindDistanceBetweenTwoPoints(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def DrawMap(MapArray):
    middleY = int(len(MapArray) / 2)
    middleX = int(len(MapArray[0]) / 2)
    CounterY = 0
    for i in MapArray:
        CounterX = 0
        for e in i:
            if e == "#":
                if FindDistanceBetweenTwoPoints((CounterX, CounterY), (middleX, middleY)) < middleY:
                    print(e, end="")
                else:
                    print(" ", end="")
            else:
                print(e, end="")
            CounterX+=1
        print("")
        CounterY+=1

def ClearTerminal():
    os.system("cls")

def PushGlobe(MapArray, speedX):
    sizeX = len(MapArray[0])
    sizeY = len(MapArray)

    for _ in range(speedX):
        lastItem = MapArray[sizeY - 1]
        MapArray.pop(sizeY - 1)
        MapArray.insert(0, lastItem)

    for i in range(len(MapArray)):
        for _ in range(int(speedX * 2.3)):
            lastItem = MapArray[i][sizeX - 1]
            MapArray[i].pop(sizeX - 1)
            MapArray[i].insert(0, lastItem)

def FixMap(MapArray, ImageName, EmptyColor, BlockColor, ImgSize):
    WorldMap = Image.open(ImageName)
    LoadedMapPixels = WorldMap.load()

    x, y = WorldMap.size

    for i in range(int(y / ImgSize)):
        MapArray.append([])
        for e in range(int(x / ImgSize)):
            px = LoadedMapPixels[int((e + 0.5) * ImgSize), int((i + 0.5) * ImgSize)]
            EmptyPercent = FindDistanceBetweenTwoColors(EmptyColor, px)
            BlockPercent = FindDistanceBetweenTwoColors(BlockColor, px)

            if EmptyPercent == 0 or EmptyPercent < BlockPercent:
                MapArray[i].append(" ")
            else:
                MapArray[i].append("#")

ImgSize = int(input("Image Quality: "))
speed = int(input("Rotation Speed: "))
MapArray = []
FixMap(MapArray, "WorldMap.jpg", (9, 48, 81), (116, 187, 231), ImgSize)
while True:
    DrawMap(MapArray)
    PushGlobe(MapArray, speed)
    ClearTerminal()