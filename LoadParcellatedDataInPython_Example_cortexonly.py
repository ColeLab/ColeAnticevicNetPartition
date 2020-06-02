# Taku Ito
# 10/09/2018

# Script requires workbench (wb_command), in addition to the below python packages
# Load dependencies
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os

#Setting the parcel files to be the 360 Glasser2016 cortical parcels
L_parcelCIFTIFile='SeparateHemispheres/Q1-Q6_RelatedValidation210.L.CorticalAreas_dil_Final_Final_Areas_Group_Colors.32k_fs_LR.dlabel.nii'
R_parcelCIFTIFile='SeparateHemispheres/Q1-Q6_RelatedValidation210.R.CorticalAreas_dil_Final_Final_Areas_Group_Colors.32k_fs_LR.dlabel.nii'

L_parcelTSFilename='Output_Atlas.L.Parcels.32k_fs_LR.ptseries.nii'
R_parcelTSFilename='Output_Atlas.R.Parcels.32k_fs_LR.ptseries.nii'

#Set this to be your input fMRI data CIFTI file
inputFile='Run1_fMRIData_Atlas.dtseries.nii';

# Load in dense array time series using nibabel
dtseries = np.squeeze(nib.load(inputFile).get_data())
# Find time points
n_timepoints = dtseries.shape[1]

# Parcellate dense time series using wb_command for left and right hemispheres
os.system('wb_command -cifti-parcellate ' + inputFile + ' ' + L_parcelCIFTIFile + ' COLUMN ' + L_parcelTSFilename + ' -method MEAN')
os.system('wb_command -cifti-parcellate ' + inputFile + ' ' + R_parcelCIFTIFile + ' COLUMN ' + R_parcelTSFilename + ' -method MEAN')

# Load in parcellated data using nibabel
l_parcellated = np.squeeze(nib.load(L_parcelTSFilename).get_data()).T
r_parcellated = np.squeeze(nib.load(R_parcelTSFilename).get_data()).T

# Stack left and right hemispheres
lr_parcellated = np.vstack((l_parcellated,r_parcellated))


# Loading community ordering files
netassignments = np.loadtxt('cortex_parcel_network_assignments.txt')
# need to subtract one to make it compatible for python indices
indsort = np.loadtxt('cortex_community_order.txt',dtype=int) - 1 
indsort.shape = (len(indsort),1)
#netorder = np.loadtxt('network_labelfile.txt')


# Computing functional connectivity and visualizing the data (assuming preprocessing has already been done)
FCmat = np.corrcoef(lr_parcellated)
FCMat_sorted = FCmat[indsort,indsort.T]
plt.figure(figsize=(7,7))
plt.imshow(FCMat_sorted,origin='lower',cmap='gray_r')
plt.colorbar(fraction=0.046)
plt.title('Sorted FC Matrix',fontsize=24)
plt.show()

tseriesMatSubj = lr_parcellated
