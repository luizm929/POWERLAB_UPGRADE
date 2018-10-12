
Power Laboratory Upgrade App

#--------------Please Read This First------------------------------------
This is part of a big project (smart grids). All parts work together however they are installed in different
systems. The files in this folder are supposed to be installed on the main server as well as in all
substation systems and there are prompts to start on substation mode or main-server mode.
The main-server mode need a password and the substation mode does not. Main-server mode needs password
because it can control all devices on all substations of the smart-grid.


The main GUI's in this folder are

LoadBanksV2.py            <-- Working!
Power_Lab_GUI_Main.py     <-- Needs to be redesigned

Communication files are. Real communication code is not included.

simplerun.py
simplerun2.py

The GUI's is not yet password protected thus the modes are still not available.


#--------------- Things that need to be fixed/implemented--------------------------------------

1. Power_Lab_GUI_Main.py needs to be redesigned to include controls for P and Q.
2. Password protection for different modes.
