# this script can be used directly from OpenSim GUI to change the optimal fiber lengths and tendon slack length

#---------------------------------------use the active OpenSim model----------------------------------------------------
oldModel = getCurrentModel()

#-------------------------this code is needed to have access to muscle parameters---------------------------------------
myModel = modeling.Model(oldModel)

#-----------------------------------------get the current model state---------------------------------------------------
myState = myModel.initSystem()

#------------------------------------------setting new model name-------------------------------------------------------
oldName = oldModel.getName()
myModel.setName(oldName+"_muscles_changed")

#-----------------------parameter that is used to change the optimal fiber length---------------------------------------
mult_by = 1.02

#---------------------------------------list of muscles to change-------------------------------------------------------
muscles_to_change = ["DeltoideusScapula_P", "TeresMinor", "levator_scap", "trap_acr"]

#--------------------------muscles for the left side have to be changed symmetrically-----------------------------------
left_muscles = ["levator_scap_L", "trap_acr_L"]

new_values_dict = {}

#-------------------------------a loop over all the muscles in the model------------------------------------------------
for i in range(myModel.getMuscles().getSize()):
    currentMuscle = myModel.getMuscles().get(i)
    if currentMuscle.getName() in muscles_to_change:
        fiber_length = currentMuscle.getOptimalFiberLength()
        tendon_length = currentMuscle.getTendonSlackLength()
        summ = fiber_length + tendon_length
        new_fiber_length = fiber_length * mult_by
        new_tendon_length = summ - new_fiber_length
        currentMuscle.setOptimalFiberLength(new_fiber_length)
        currentMuscle.setTendonSlackLength(new_tendon_length)
        new_values_dict[currentMuscle.getName()] = [new_fiber_length, new_tendon_length]
        print("Changed " + currentMuscle.getName() + ": old_f_length = " + str(fiber_length) + ", old_t_length = " + str(tendon_length) + ", new_f_length = " + str(new_fiber_length) + ", new_t_length = " + str(new_tendon_length))
    elif currentMuscle.getName() in left_muscles:
        fiber_length = currentMuscle.getOptimalFiberLength()
        tendon_length = currentMuscle.getTendonSlackLength()
        right_muscle_name = currentMuscle.getName()[0:-2]
        currentMuscle.setOptimalFiberLength(new_values_dict[right_muscle_name][0])
        currentMuscle.setTendonSlackLength(new_values_dict[right_muscle_name][1])
        print("Changed " + currentMuscle.getName() + ": old_f_length = " + str(fiber_length) + ", old_t_length = " + str(tendon_length) + ", new_f_length = " + str(new_values_dict[right_muscle_name][0]) + ", new_t_length = " + str(new_values_dict[right_muscle_name][1]))
fullPathName = oldModel.getInputFileName()
newPathName = fullPathName.replace('.osim', '_1.osim')
myModel.print(newPathName)

#----------------------------------add model to GUI if it is needed-----------------------------------------------------
loadModel(newPathName)
        

