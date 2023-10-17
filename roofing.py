#program to determine roof geometry and design

#this a point in the roof geometry, has x (left-right), y (up-down), z (in/out of screen = vertical in real world)
class Geo_Point():
    def __init__(self,x : float,y : float,z : float):
        self.x :float  = x
        self.y : float = y
        self.z : float = z

#this is a surface in the roof geometry, parent of both triangle and quad classes
class Geo_Surface():
    def __init__():
        pass

#represents a triangle in the roof geometry
#note  by convention (we may change this later), A and C must have the same z position which must be lower than B's z position
#A and C represent the "base" of the triangle, and B represents the "peak" of the triangle
class Geo_Triangle():
    #create the triangle
    def __init__(self,point_A : Geo_Point,point_B : Geo_Point,point_C : Geo_Point):
        #store the points that make up the triangle
        self.A : Geo_Point = point_A
        self.B : Geo_Point = point_B
        self.C : Geo_Point = point_C
        

    #check the triangle is conventional
    def check_convention(self):
        lower_base_conventional : bool = self.check_lower_base_convention()
        if(lower_base_conventional==False):
            return False #convention violated
        else:
            upper_peak_convention : bool = self.check_upper_base_convention()


    def check_lower_base_convention(self):
        lower_base_conventional : bool = (self.A.z==self.C.z)
        if(lower_base_conventional):
            self.lower_base_height = self.A.z
            return True
        else:
            return False

    def check_upper_base_convention(self):
        upper_base_conventional : bool = (self.B.z>self.C.z)
            

#represents a quadrilateral in the roof geometry
#note  by convention (we may change this later), the A/D and B/C point pairs must have the same z position, with A/D lower than B/C
#A and D represent the "lower base" of the quadrilateral and B and C represents the "upper base" of the triangle
class Geo_Quad():
    def __init__(self,point_A : Geo_Point,point_B : Geo_Point,point_C : Geo_Point,point_D : Geo_Point):
        #store the points that make up the quadrangle
        self.A : Geo_Point = point_A
        self.B : Geo_Point = point_B
        self.C : Geo_Point = point_C
        self.D : Geo_Point = point_D



