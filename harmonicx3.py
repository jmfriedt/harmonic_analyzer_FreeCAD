# import os
# os.chdir('/home/jmfriedt/freecad_motion')
# os.chdir('c:/users/mariette/desktop/freecad_motion')
# import harmonicx3
# ensuite pour recharger en cours de developpment : 
# import importlib
# importlib.reload(harmonicx3)
import FreeCAD
from PySide import QtCore
from math import sin, cos, radians

# retrieve the objects from the document: start typing FreeCAD.ActiveDocument and see completion
# first wheel
p1 = FreeCAD.ActiveDocument.getObject("Connect")
h1 = FreeCAD.ActiveDocument.getObject("Connect001")
c0 = FreeCAD.ActiveDocument.getObject("Cylinder")
c1 = FreeCAD.ActiveDocument.getObject("Cylinder001")
spring1 = FreeCAD.ActiveDocument.getObject("Box003")
p1init1=p1.Placement
h1init1=h1.Placement
springinit1=spring1.Placement
leninit1=spring1.Width

# second wheel
p13 = FreeCAD.ActiveDocument.getObject("Connect002")
h13 = FreeCAD.ActiveDocument.getObject("Connect003")
c03 = FreeCAD.ActiveDocument.getObject("Cylinder002")
c13 = FreeCAD.ActiveDocument.getObject("Cylinder003")
spring3 = FreeCAD.ActiveDocument.getObject("Box007")

p1init3=p13.Placement
h1init3=h13.Placement
springinit3=spring3.Placement
leninit3=spring3.Width

# third wheel
p12 = FreeCAD.ActiveDocument.getObject("Connect004")
h12 = FreeCAD.ActiveDocument.getObject("Connect005")
c02 = FreeCAD.ActiveDocument.getObject("Cylinder004")
c12 = FreeCAD.ActiveDocument.getObject("Cylinder005")
spring2 = FreeCAD.ActiveDocument.getObject("Box010")
p1init2=p12.Placement
h1init2=h12.Placement
springinit2=spring2.Placement
leninit2=spring2.Width

pen=FreeCAD.ActiveDocument.getObject("Box012")
peninit=pen.Placement.Base

i=0
f=open("res","w+")

def update_harmonic():
  global i
  alpha = radians( i )
  y1 = c1.Placement.Base.x*(sin( alpha ))
  p1.Placement = FreeCAD.Placement( p1init1.Base , FreeCAD.Rotation ( FreeCAD.Vector( 0,0,1), i) )
  h1.Placement = FreeCAD.Placement( h1init1.Base + FreeCAD.Vector( 0, y1, 0 ) , h1init1.Rotation )
  spring1.Placement = FreeCAD.Placement( springinit1.Base + FreeCAD.Vector( 0, y1, 0 ) , h1init1.Rotation )
  #spring.Width=leninit.Value-y1
  
  # il FAUT inserer une roue intermediaire sinon on a -3i qui tourne dans le mauvais sens ! 
  alpha3 = radians(3*i)
  y3 = c13.Placement.Base.x*(sin( alpha3 ))
  p13.Placement = FreeCAD.Placement( p1init3.Base , FreeCAD.Rotation ( FreeCAD.Vector( 0,0,1), 3*i) )
  h13.Placement = FreeCAD.Placement( h1init3.Base + FreeCAD.Vector( 0, y3, 0 ) , h1init2.Rotation )
  spring3.Placement = FreeCAD.Placement( springinit3.Base + FreeCAD.Vector( 0, y3, 0 ) , h1init2.Rotation )
  #spring3.Width=leninit3.Value-y3
  
  alpha2 = radians(5*i)
  y2 = c12.Placement.Base.x*(sin( alpha2 ))
  p12.Placement = FreeCAD.Placement( p1init2.Base , FreeCAD.Rotation ( FreeCAD.Vector( 0,0,1), i*5) )
  h12.Placement = FreeCAD.Placement( h1init2.Base + FreeCAD.Vector( 0, y2, 0 ) , h1init2.Rotation )
  spring2.Placement = FreeCAD.Placement( springinit2.Base + FreeCAD.Vector( 0, y2, 0 ) , h1init2.Rotation )
  #spring2.Width=leninit2.Value-y2
  
  yvar=(y1+y2/5+y3/3)/2  # triangle
  yvar=(y1+y2+y3)/2      # square: la force de rappel est un terme constant -yrappel
  spring1.Width=leninit1.Value-y1+yvar
  spring2.Width=leninit2.Value-y2+yvar
  spring3.Width=leninit3.Value-y3+yvar
  pen.Placement.Base.y=peninit.y+yvar
  FreeCAD.Gui.updateGui()
  f.write(str(yvar)+"\n")
  f.flush()
  # increase mechanism input position
  i += 1
 
# create a timer object
timer = QtCore.QTimer()
# connect timer event to function "update"
timer.timeout.connect( update_harmonic )
# start the timer by triggering "update" every 10 ms
timer.start( 10 )
