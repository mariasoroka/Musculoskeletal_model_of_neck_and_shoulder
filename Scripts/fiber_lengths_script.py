#this sript can be used from OpenSim GUI to print in the specified file optimal fiber lengths for current model

#---------------------------------------use the active OpenSim model----------------------------------------------------
oldModel = getCurrentModel()

#-------------------------this code is needed to have access to muscle parameters---------------------------------------
myModel = modeling.Model(oldModel)

#-----------------------------------specify the file where to print!!!--------------------------------------------------
file_name = "SOME_FILE.csv"
my_file = open(file_name, "w")

#-------------------------------a loop over all the muscles in the model------------------------------------------------
for i in range(myModel.getMuscles().getSize()):
	currentMuscle = myModel.getMuscles().get(i)
	my_file.write(currentMuscle.getName() + ";" +  str(currentMuscle.getOptimalFiberLength()) + "\n")
my_file.close()
