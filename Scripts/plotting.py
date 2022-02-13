#this script can be used for calculating and plotting of moment arms for different muscle groups with OpenSim Plotter
import os.path

#-------------------------------------specify the folder for saving data!!!---------------------------------------------
save_to = os.path.join("SOME_FOLDER")

#---------------------------------------use the active OpenSim model----------------------------------------------------
Model = getCurrentModel()

#------------------choose the name of the muscle group here, it would be used as a prefix-------------------------------
muscle_group = "deltoideus"
# muscle_group = "infraspinatus"
# muscle_group = "supraspinatus"
# muscle_group = "latdorsi"
# muscle_group = "subscapularis"
# muscle_group = "pecmajor"
# muscle_group = "teresmajmin"
# muscle_group = "for_picture"
# muscle_group = "all_for_diploma"

#----------------------------------------choose the set of muscles------------------------------------------------------
muscles = ["DeltoideusScapula_P", "DeltoideusScapula_M", "DeltoideusClavicle_A"]
# muscles = ["Infraspinatus_I", "Infraspinatus_S"]
# muscles = ["Supraspinatus_A", "Supraspinatus_P"]
# muscles = ["LatissimusDorsi_S", "LatissimusDorsi_M", "LatissimusDorsi_I"]
# muscles = ["Subscapularis_M", "Subscapularis_I", "Subscapularis_S"]
# muscles = ["PectoralisMajorClavicle_S", "PectoralisMajorThorax_I", "PectoralisMajorThorax_M"]
# muscles = ["TeresMajor", "TeresMinor"]
# muscles = ["DeltoideusScapula_P", "DeltoideusScapula_M", "DeltoideusClavicle_A", "Infraspinatus_I", "Infraspinatus_S", "Supraspinatus_A", "Supraspinatus_P", "Subscapularis_M", "Subscapularis_I", "Subscapularis_S", "TeresMajor", "TeresMinor"]

#------------------------------moment arms will be the functions of this coordinate-------------------------------------
coord = "shoulder_elv"

#----------------------------------creating of plotting panel for flexion-----------------------------------------------
plotterFlex = createPlotterPanel("Flexion")

#-------------------------setting plane_elv and axial_rot coordinates for flexion---------------------------------------
coord_handle = getCoordinate(Model, "plane_elv")
setCoordinateValueDegrees(coord_handle, 70.0)
coord_handle = getCoordinate(Model, "axial_rot")
setCoordinateValueDegrees(coord_handle, 0.0)

#-----------------------------------moment arms computation and plotting------------------------------------------------
crvFlex = []
for i, muscle in enumerate(muscles):
    crvFlex.append(addAnalysisCurve(plotterFlex, "momentarm." + coord, muscle, coord))

#---------------------------------------------exporting data------------------------------------------------------------
exportData(plotterFlex, save_to + muscle_group + "_flexion")

#----------------------------------creating of plotting panel for abduction---------------------------------------------
plotterAbd = createPlotterPanel("Abduction")

#-------------------------setting plane_elv and axial_rot coordinates for abduction-------------------------------------
coord_handle = getCoordinate(Model, "plane_elv")
setCoordinateValueDegrees(coord_handle, 0.0)

#-----------------------------------moment arms computation and plotting------------------------------------------------
crvAbd = []
for i, muscle in enumerate(muscles):
    crvAbd.append(addAnalysisCurve(plotterAbd, "momentarm." + coord, muscle, coord))
    crvAbd[i].setLegend(muscle)

#---------------------------------------------exporting data------------------------------------------------------------
exportData(plotterAbd, save_to + muscle_group + "_abduction")