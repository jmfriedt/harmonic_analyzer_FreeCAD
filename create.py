# import os
# os.chdir('/home/jmfriedt/freecad_motion')
# os.chdir('c:/users/mariette/desktop/freecad_motion')
# import create
# ensuite pour recharger en cours de developpment : 
# import importlib
# importlib.reload(create)

import FreeCAD
from PySide import QtCore
from math import sin, cos, radians

nbharmonics=20
dt=1

harm=list()
roue=list()
rouepignon=list()
roue2=list()
spring=list()
harminit=list()
springinit=list()
i=0

def update_harmonic():
  global i
  global i
  yvar=0
  k=0
  for t in harm:
   angle=i*roue[0].Radius/roue[k].Radius
   y1 = roue[k].Radius*(sin(radians(angle)))
   rouepignon[k].Placement = FreeCAD.Placement( roueinit[k].Placement.Base , FreeCAD.Rotation ( FreeCAD.Vector( 0,0,1), angle) )
   harm[k].Placement.Base.y = y1.Value+harminit[k]
   spring[k].Placement.Base.y = springinit[k]+y1.Value
   yvar+=y1.Value    # yvar=(y1+y2+y3+y4) # square: la force de rappel est un terme constant -yrappel
   f.write(str(y1.Value)+" ")
   k += 1
  pen.Placement.Base.y=peninit.y+yvar
  for s in spring:
   s.Width=pen.Placement.Base.y-s.Placement.Base.y
  f.write(str(yvar)+"\n")
  f.flush()
  FreeCAD.Gui.updateGui()
  i += dt    # increase mechanism input position

pen=FreeCAD.ActiveDocument.addObject("Part::Box","Pen")
#pen.Length=600
pen.Height=1
pen.Width=1
pen.Placement.Base.y=480
pen.Placement.Base.x=-10
for k in range(nbharmonics):
 tmproue=FreeCAD.ActiveDocument.addObject("Part::Cylinder","Cylinder"+str(k))
 tmproue.Height=1
 tmproue.Radius=100/(2*k+1)
 tmproue.Placement.Base.z=-1
 pignon=FreeCAD.ActiveDocument.addObject("Part::Cylinder","Pignon"+str(k))
 pignon.Height=1
 pignon.Radius=0.5
 pignon.Placement.Base.x=tmproue.Radius.Value # -1
 tmprouepignon=FreeCAD.ActiveDocument.addObject("Part::MultiFuse","Fusion")
 tmprouepignon.Shapes = [tmproue,pignon]
 rouepignon.append(tmprouepignon)
 roueinter=FreeCAD.ActiveDocument.addObject("Part::Cylinder","Cylinder"+str(k))
 roueinter.Height=1
 roueinter.Radius=100/(2*k+1)
 roueinter.Placement.Base.z=-1
 tmpcube1=FreeCAD.ActiveDocument.addObject("Part::Box","Boxa"+str(k))
 tmpcube2=FreeCAD.ActiveDocument.addObject("Part::Box","Boxb"+str(k))
 tmpcube1.Length=tmproue.Radius*2;
 tmpcube2.Length=tmpcube1.Length.Value-1
 tmpcube1.Height=1
 tmpcube2.Height=1
 tmpcube1.Placement.Base.x=-tmproue.Radius
 tmpcube1.Width=2
 tmpcube1.Placement.Base.y=-1
 tmpcube2.Placement.Base.x=-tmproue.Radius.Value+0.5
 tmpcube2.Placement.Base.y=-0.5
 tmpcube2.Width=1
 axe1=FreeCAD.ActiveDocument.addObject("Part::Cut","Cut")
 axe1.Base=tmpcube1;  #FreeCAD.ActiveDocument.Cut.Base = tmpcube1
 axe1.Tool=tmpcube2
 axe2=FreeCAD.ActiveDocument.addObject("Part::Box","Boxa"+str(k))
 axe2.Height=1
 axe2.Width=300
 axe2.Length=2
 axe2.Placement.Base.x=-1
 axe2.Placement.Base.y=1
 T=FreeCAD.ActiveDocument.addObject("Part::MultiFuse","Fusion")
 T.Shapes = [axe1,axe2]
 roue.append(tmproue)
 harm.append(T)
 roue2.append(roueinter)
 springtmp=FreeCAD.ActiveDocument.addObject("Part::Box","Boxs"+str(k))
 springtmp.Height=1
 springtmp.Width=pen.Placement.Base.y-axe2.Width.Value-axe2.Placement.Base.y
 springtmp.Placement.Base.y=axe2.Placement.Base.y+axe2.Width.Value
 springtmp.Length=2
 springtmp.ViewObject.ShapeColor = (1.00,0.67,0.50)
 springtmp.ViewObject.LineColor = (1.00,0.67,0.50)
 spring.append(springtmp)

k=0
position=0
for r in roue:
 if k==0:
  position=r.Radius
 else:
  rouepignon[k].Placement.Base.x=position+r.Radius+2*r.Radius
  roue2[k].Placement.Base.x=position+r.Radius
  position=position+2*r.Radius+2*r.Radius
 k+=1
 
pen.Length=position.Value+10

k=0
for h in harm:
 h.Placement.Base.x=rouepignon[k].Placement.Base.x
 spring[k].Placement.Base.x=h.Placement.Base.x-1
 harminit.append(h.Placement.Base.y)
 springinit.append(spring[k].Placement.Base.y)
 k+=1

FreeCAD.ActiveDocument.recompute()
FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    
f=open("res","w+")
roueinit=rouepignon
peninit=pen.Placement.Base
timer = QtCore.QTimer()                  # create a timer object
timer.timeout.connect( update_harmonic ) # connect timer event to function "update"
timer.start( 10 )                        # start the timer by triggering "update" every 10 ms