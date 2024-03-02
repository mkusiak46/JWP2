import math


class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self):
        return f"Vector3D({self.__x},{self.__y},{self.__z})"

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    def norm(self):
        return math.sqrt(math.pow(self.__x, 2) + math.pow(self.__y, 2) + math.pow(self.__z, 2))

    def __add__(self, other):
        self.__x = self.__x + other.getX()
        self.__y = self.__y + other.getY()
        self.__z = self.__z + other.getZ()

    def __sub__(self, other):
        self.__x = self.__x - other.getX()
        self.__y = self.__y - other.getY()
        self.__z = self.__z - other.getZ()

    def __mul__(self, other):
        self.__x = self.__x * other
        self.__y = self.__y * other
        self.__z = self.__z * other

    def dot(self,other):
        print(self.__x*other.getX() + self.__y*other.getY() + self.__z * other.getZ())
        return self.__x*other.getX() + self.__y*other.getY() + self.__z * other.getZ()

    def cross(self,other):
        temp_vector = Vector3D()
        temp_vector.__x = self.__y * other.getZ() - self.__z * other.getY()

        temp_vector.__y = self.__z * other.getX() - self.__x * other.getZ()
        temp_vector.__z = self.__x * other.getY() - self.__y * other.getX()
        return temp_vector

    def are_orthogonal(self,other):
        if self.dot(other) == 0:
            return True
        return False

wektor1 = Vector3D(3,4,5)
wektor2 = Vector3D(6,2,1)
wektor1.__add__(wektor2)
print(wektor1)
wektor1.__sub__(wektor2)
print(wektor1)
wektor1.__mul__(5)
print(wektor1)

wektor3 = wektor1.cross(wektor2)
print(wektor3)

wektor4 = Vector3D(0,0,0)
wektor5 = Vector3D(0,0,0)

print(wektor1.are_orthogonal(wektor2))

