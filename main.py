import ifcopenshell
import ifcopenshell.geom
from ifcopenshell.util.selector import Selector
#from Room import Room
from Classes import Face, Room, Geometry
import jsonpickle

ifc = ifcopenshell.open(r'C:\Users\satya\OneDrive\Desktop\TUM Lectures\Semester2\IFC\Lothar\querySample.ifc')
selector = Selector()
spaces = selector.parse(ifc, '.IfcSpace')
spaceBoundary = selector.parse(ifc, '.IfcRelSpaceBoundary')
faces=[]

for spaceBoundary in spaces[0].BoundedBy:
    element = spaceBoundary.RelatedBuildingElement
    surface = spaceBoundary.ConnectionGeometry.SurfaceOnRelatingElement
    points = []
    if "IfcSlab" in str(element):
        polyloop = surface.OuterBoundary
        for p in polyloop.Points:
            points.append([p.Coordinates[0], p.Coordinates[1], surface.BasisSurface.Position.Axis[0][2]])  # why indexing of 0?
        geometry=Geometry("Face3D",points)
        face = Face("Slab", "faces", geometry)
        faces.append(face)

    elif "IfcWallStandardCase" in str(element):
        polyloop=surface.SweptCurve.Curve
        for p in polyloop.Points:
            points.append([p.Coordinates[0], p.Coordinates[1], surface.ExtrudedDirection[0][2]])  # why indexing of 0?
        geometry = Geometry("Face3D", points)
        face = Face("Wall", "faces", geometry)
        faces.append(face)

    else:
        continue


room = Room("Room", faces)
test = jsonpickle.encode(room)
print(test)

