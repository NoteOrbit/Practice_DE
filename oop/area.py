class area:
    
    
    def __init__(self,width:float,height:float) -> None:
        self.width = width
        self.height = height
        
    def getArea(self) -> None:
        return self.height * self.width
    
class color(area):
    def __init__(self, width: float, height: float,color:str) -> None:
        super().__init__(width, height)
        self.color = color

    def draw(self):
        return self.color
    

box = color(3,4,'Green')
print(box.getArea())
print(box.draw())

