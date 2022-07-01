class Face:
  def __init__(self, _faceType=None, _type=None, _geometry=None,_boundary_condition=None,_properties=None,_apertures=None                                             ):
    self.faceType = _faceType
    self.type=_type
    self.geometry = _geometry
    self.boundary_condition=_boundary_condition
    self.properties=_properties
    self.apertures=_apertures

class Geometry:
  def __init__(self,_type=None,_boundary=None,_holes=None,_plane=None):
    self.type=_type
    self.boundary=_boundary
    self.holes=_holes
    self.plane=_plane


class Room:
  def __init__(self, _type=None, _faces=None):
    self.type=_type
    self.faces=_faces

class Properties:
  def __init__(self,_type=None, _energy=None, _radiance=None):
    self.type=_type
    self.energy=_energy
    self.radiance=_radiance

class Energy:
  def __init__(self,_type=None,_construction_set=None, _program_type=None,_hvac=None):
    self.type=_type
    self.construction_set=_construction_set
    self.program_type=_program_type
    self.hvac=_hvac

class Radiance:
  def __init__(self,_type=None,_modifier_set=None):
    self.type=_type
    self.modifier_set=_modifier_set
