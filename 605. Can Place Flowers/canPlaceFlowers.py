def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
            if n == 0 :
                return True
            else:
                if (i == 0) and (len(flowerbed) !=1):
                    if (flowerbed[i+1] == 0) and (flowerbed[i] != 1):
                        n -= 1
                        flowerbed[i] = 1
                elif i > 0 and i < len(flowerbed)-1:
                    if (flowerbed[i-1] == 0) and (flowerbed[i+1] == 0) and (flowerbed[i] != 1):
                        n -= 1
                        flowerbed[i] = 1
                else:
                    if (flowerbed[i-1] == 0) and (flowerbed[i] != 1):
                        n -= 1
                        flowerbed[i] = 1
    
    if n == 0 :
        return True
    else:
        return False
    
print(len([1]))
print(canPlaceFlowers([1], 1))