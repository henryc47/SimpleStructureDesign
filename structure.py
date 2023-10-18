#program to determine structure geometry and design

#this a point in the structural geometry, has x (left-right), y (up-down), z (in/out of screen = vertical in real world)
class Geo_Point():
    def __init__(self,x : float,y : float,z : float):
        self.x :float  = x
        self.y : float = y
        self.z : float = z

#this is a surface in the roof geometry, parent of both triangle and quad classes
#note there are three types of structures. Floors, Roofs and Walls. 
# Floors have all points at the same z position. 
# Roofs have a lower and upper z level. 
# Walls have a lower and upper z levels, with matching x/y axis between upper and lower floors. Z levels must match for same level
# At the moment, the end user must define whether structure is wall, floor or roof (though we may try and add automatic detection later on)
class Geo_Surface():
    def __init__():
        pass

#represents a triangle in the structure geometry
#note  by convention for roofs and walls, A and C must have the same z position which must be lower than B's z position
#A and C represent the "base" of the triangle, and B represents the "peak" of the triangle
class Geo_Triangle(Geo_Surface):
    #create the triangle
    def __init__(self,point_A : Geo_Point,point_B : Geo_Point,point_C : Geo_Point, type : str):
        #store the points that make up the triangle
        self.A : Geo_Point = point_A
        self.B : Geo_Point = point_B
        self.C : Geo_Point = point_C
        self.type : str = type
        meets_convention,error_message : tuple[bool,str] = self.check_convention() #check if the triangle meets conventional norms based on type
        if(meets_convention==False):
            print(error_message)
            return False #creation of triangle failed
        else:
            return True #creation of triangle successful 

    #check the triangle is conventional depending on the type
    def check_convention(self) -> "tuple[bool,str]":
        meets_convention : bool = False
        error_message : str = "structure type " + self.type + " is not a valid type, valid types are 'wall', 'floor', and 'roof'"
        if(self.type=='wall'):
            meets_convention,error_message = self.check_convention_wall() #check if the triangle meets conventional norms for the wall type
        if(self.type=='floor'):
            meets_convention,error_message : tuple[bool,str] = self.check_convention_floor() #check if the triangle meets conventional norms for the floor type
        if(self.type=='roof'):
            meets_convention,error_message : tuple[bool,str] = self.check_convention_roof() #check if the triangle meets conventional norms for the roof type
        return meets_convention,error_message

    #check if the triangle meets conventional norms for the wall type
    def check_convention_wall(self) -> "tuple[bool,str]":
        meets_convention : bool = False
        error_message : str = "not a valid wall : "
        if (self.A.z==self.C.Z):#do we have a clear lower level
            if(self.A.z<self.B.z): #is the lower level below the upper level
                #now check upper level on same line as lower level (0.1% tolerance)
                distance_AC : float = (self.A.x-self.C.x)**2 + (self.A.y-self.C.y)**2
                distance_AB : float = (self.A.x-self.B.x)**2 + (self.A.y-self.B.y)**2
                distance_BC : float = (self.B.x-self.C.x)**2 + (self.C.y-self.C.y)**2
                ratio_distance : float = (distance_AB+distance_BC)/distance_AC
                if(ratio_distance>1.0001): #0.01% tolerance for point misalignment
                    meets_convention = True
                    error_message = "correct wall"
                else:
                    meets_convention = False
                    error_message += "point B not along line from A to C, perhaps it should be a roof?"
            else:
                error_message += "lower level between point A and C not below above level at point B"

        else:
            error_message += "point A and C are not on same elevation"
        return meets_convention,error_message
    

    #check if the triangle meets conventional norms for the roof type
    def check_convention_roof(self) -> "tuple[bool,str]":
        meets_convention : bool = False   
        error_message : str = "not a valid roof : "
        if (self.A.z==self.C.Z):#do we have a clear lower level
            if(self.B.z>self.A.z): #is the peak higher than the lower level
                meets_convention = True
                error_message = "correct roof"
            else:
                error_message += "lower level between point A and C not below above level at point B"
        else:
            error_message += "we do not have a consistent lower level, elevation of point A and C not equal "
        return meets_convention,error_message
    
    def check_convention_floor(self) -> "tuple[bool,str]":
        meets_convention : bool = False
        error_message : str = "not a valid floor : "
        if (self.A.z==self.B.z) and (self.B.z==self.C.z): #check all points at same height
            meets_convention = True
            error_message = "correct floor"
        else:
            error_message += "Points do not all have the same elevation "
        return meets_convention,error_message
            

#represents a quadrilateral in the structure geometry
#note  by convention (we may change this later), the A/D and B/C point pairs must have the same z position, with A/D lower than B/C
#A and D represent the "lower base" of the quadrilateral and B and C represents the "upper base" of the triangle
class Geo_Quad(Geo_Surface):
    def __init__(self,point_A : Geo_Point,point_B : Geo_Point,point_C : Geo_Point,point_D : Geo_Point,type : str):
        #store the points that make up the quadrangle
        self.A : Geo_Point = point_A
        self.B : Geo_Point = point_B
        self.C : Geo_Point = point_C
        self.D : Geo_Point = point_D
        self.type : str = type 



