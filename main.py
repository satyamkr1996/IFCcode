import ifcopenshell
import ifcopenshell.geom
from ifcopenshell.util.selector import Selector
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
            points.append([p.Coordinates[0], p.Coordinates[1], surface.BasisSurface.Position.Axis[0][2]])
        geometry=Geometry("Face3D",points)
        face = Face("Slab", "faces", geometry)
        faces.append(face)

    elif "IfcWallStandardCase" in str(element):
        polyloop=surface.SweptCurve.Curve
        for p in polyloop.Points:
            points.append([p.Coordinates[0], p.Coordinates[1], surface.ExtrudedDirection[0][2]])  # (1.) Just like slabs, I tried to find out coordinates (x and y) of the wall but there is only 2 coordinates present. How to find the other 2 coordinates? Also, the z-component is 1.0 for all walls in IfcAxis.
        geometry = Geometry("Face3D", points)                                                      # coordinates for walls are still quite confusing
        face = Face("Wall", "faces", geometry)
        faces.append(face)

    else:
        continue


room = Room("Room", faces)                                      # (2.)Is it okay to put classtype as "Room" manually or do we have to find it from IFC file? Similar doubt for other classtypes like "Wall", "Face3D" in lines 30 and 26 respectively.
test = jsonpickle.encode(room)
print(test)

#(3.) How to proceed further as further classes need more energy related data like sunexposure,windexposure, radiance etc which are hard to find in IFC file.
