# harmonic analyzer simulator in FreeCAD

Inspired by B. Hammack's video on the harmonic analyzer entitled "An Old Mechanical Computer: The Harmonic Analyzer" 
[https://www.youtube.com/watch?v=GyYflzRVu6M] (accessed Dec. 2019) and J.G. Egas Ortuno's video entitled "FreeCAD animation 
how" at [https://www.youtube.com/watch?v=BHbnOlBvpLI] (accessed Dec. 2019)

<img src="20.png" width="300">

<img src="simulation.png" width="300">

# Running the simulation

When using a ready made FreeCAD mode:
1/ load the .FCStd model
2/ open the Python console (View → Panels → Python console menu) and type
```python
import os
os.chdir('/home/myuser/directory')
import script
```
assuming the program named script.py are located in the /home/myuser/directory directory
For re-loading the script (e.g. after modifying the Python program):
```python
import importlib
importlib.reload(script)
```

For the example creating the model in addition to running the simulation: Create an empty FreeCAD project, and
```python
import os
os.chdir('/home/myuser/directory')
import create
```
to run the create.py script. This script uses the nbharmonics (default value=20) to define how many harmonics are created.
