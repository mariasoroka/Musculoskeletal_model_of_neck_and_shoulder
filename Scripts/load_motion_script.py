#this is a simple script for loading several motion files in OpenSim

import os.path

#-----------------------------------specify the folder with motions!!!--------------------------------------------------
motion_folder = os.path.join("SOME_FOLDER")

#----------------------------------------specify the needed motions-----------------------------------------------------
motions = ["IK_abd_all", "IK_flx_all", "IK_shr_all"]

#---------------------------------------use the active OpenSim model----------------------------------------------------
Model = getCurrentModel()

#----------------------------------------------motion loading-----------------------------------------------------------
for motion in motions:
    loadMotion(motion_folder + motion + ".mot")