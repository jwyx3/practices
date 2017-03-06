"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    def draw(self):
        print "  /\  "
        print " /  \ "
        print "/____\\"


class Rectangle(Shape):
    def draw(self):
        print " ---- "
        print "|    |"
        print " ----"


class Square(Shape):
    def draw(self):
        print " ---- "
        print "|    |"
        print "|    |"
        print " ---- "


class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        klass = {'Square': Square, 'Rectangle': Rectangle, 'Triangle': Triangle}
        return klass[shapeType]()


