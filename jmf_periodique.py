# os.chdir('c:/users/mariette/Desktop/freecad_motion')
# import importlib
# importlib.reload(jmf_periodique)
import FreeCAD
from PySide import QtCore
from math import sin, cos, radians

# retrieve the objects from the document: start typing FreeCAD.ActiveDocument and see completion
cubemobile = FreeCAD.ActiveDocument.getObject("Box")
cubefixe = FreeCAD.ActiveDocument.getObject("Box001")
slider = FreeCAD.ActiveDocument.getObject("Cylinder")
cubefixe_init=cubefixe.Placement.Base;
i=0

def update():
  global i
  alpha = radians( i )
  z = slider.Height/20*(cos( alpha )+1.5)
  cubefixe.Placement = FreeCAD.Placement( cubefixe_init + FreeCAD.Vector( 0, 0, z ), cubefixe.Placement.Rotation )
  cubemobile.Placement.Base.z=cubefixe.Placement.Base.z/2
  FreeCAD.Gui.updateGui()
  # increase mechanism input position
  i += 1
  
  
# create a timer object
timer = QtCore.QTimer()
# connect timer event to function "update"
timer.timeout.connect( update )
# start the timer by triggering "update" every 10 ms
timer.start( 10 )
