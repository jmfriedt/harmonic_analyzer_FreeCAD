# import os
# os.chdir('/home/jmfriedt/freecad_motion')
# import harmonic
# ensuite pour recharger en cours de developpment : 
# import importlib
# importlib.reload(harmonic)
import FreeCAD
from PySide import QtCore
from math import sin, cos, radians

# retrieve the objects from the document: start typing FreeCAD.ActiveDocument and see completion
p1 = FreeCAD.ActiveDocument.getObject("Connect")
h1 = FreeCAD.ActiveDocument.getObject("Connect001")
c0 = FreeCAD.ActiveDocument.getObject("Cylinder")
c1 = FreeCAD.ActiveDocument.getObject("Cylinder001")
spring = FreeCAD.ActiveDocument.getObject("Box003")
i=0
p1init=p1.Placement
h1init=h1.Placement
springinit=spring.Placement
leninit=spring.Width


p12 = FreeCAD.ActiveDocument.getObject("Connect002")
h12 = FreeCAD.ActiveDocument.getObject("Connect003")
c02 = FreeCAD.ActiveDocument.getObject("Cylinder002")
c12 = FreeCAD.ActiveDocument.getObject("Cylinder003")
spring2 = FreeCAD.ActiveDocument.getObject("Box007")
i=0
p1init2=p12.Placement
h1init2=h12.Placement
springinit2=spring2.Placement
leninit2=spring2.Width


def update_harmonic():
  global i
  alpha = radians( i )
  y = c0.Radius*0.8*(sin( alpha ))
  p1.Placement = FreeCAD.Placement( p1init.Base , FreeCAD.Rotation ( FreeCAD.Vector( 0,0,1), i) )
  h1.Placement = FreeCAD.Placement( h1init.Base + FreeCAD.Vector( 0, y, 0 ) , h1init.Rotation )
  spring.Placement = FreeCAD.Placement( springinit.Base + FreeCAD.Vector( 0, y, 0 ) , h1init.Rotation )
  spring.Width=leninit-y
  
  alpha2 = radians(-2*i)
  y2 = c02.Radius*0.8*(sin( alpha2 ))
  p12.Placement = FreeCAD.Placement( p1init2.Base , FreeCAD.Rotation ( FreeCAD.Vector( 0,0,1), -i*2) )
  h12.Placement = FreeCAD.Placement( h1init2.Base + FreeCAD.Vector( 0, y2, 0 ) , h1init2.Rotation )
  spring2.Placement = FreeCAD.Placement( springinit2.Base + FreeCAD.Vector( 0, y2, 0 ) , h1init2.Rotation )
  spring2.Width=leninit2-y2
  
  FreeCAD.Gui.updateGui()
  # increase mechanism input position
  i += 1
  
  
# create a timer object
timer = QtCore.QTimer()
# connect timer event to function "update"
timer.timeout.connect( update_harmonic )
# start the timer by triggering "update" every 10 ms
timer.start( 10 )
