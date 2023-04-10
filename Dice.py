import random

class Dice():
    def __init__(self, ndice=1) -> None:
        self.throw(ndice)
    
    def throw(self, ndice=1) -> list:
        self.faceup: list = [random.randint(1, 6) for x in range(ndice)]
        self.dice_sum()
        self.is_same_faces()
        return self.faceup
    
    def dice_sum(self) -> int:
        self.result: int = sum(self.faceup)
        return self.result
    
    def is_same_faces(self) -> bool:
        if len(self.faceup) > 1:
            self.same_faces = all([1 if x == self.faceup[0] else 0 for x in self.faceup])
        else:
            self.same_faces = False
            
        return self.same_faces
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1].isdecimal():
            dice_quantity = int(sys.argv[1])
        else:
            print('Arg must be a interger')
    else:
        dice_quantity = 1

    dice_roll = Dice(dice_quantity)
    print(
        dice_roll.faceup,
        dice_roll.result,
        'lucky!' if dice_roll.same_faces else '')