# Taku Ito
# 10/09/2018

# Script requires workbench (wb_command), in addition to the below python packages
# Load dependencies
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os


#Setting the parcel files to be the 718 parcels (cortical + subcortical)
parcelCIFTIFile='CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dlabel.nii';

parcelTSFilename='Output_Atlas_CortSubcort.Parcels.LR.ptseries.nii';

#Set this to be your input fMRI data CIFTI file
#inputFile='Run1_fMRIData_Atlas.dtseries.nii'
inputFile='rfMRI_REST1_LR_Atlas_MSMAll.dtseries.nii'

# Load in dense array time series using nibabel
dtseries = np.squeeze(nib.load(inputFile).get_data())
# Find number of time points
n_timepoints = dtseries.shape[1]

# Parcellate dense time series using wb_command
os.system('wb_command -cifti-parcellate ' + inputFile + ' ' + parcelCIFTIFile + ' COLUMN ' + parcelTSFilename + ' -method MEAN')

# Load in parcellated data using nibabel
lr_parcellated = np.squeeze(nib.load(parcelTSFilename).get_data()).T

# Loading community ordering files
netassignments = np.loadtxt('cortex_subcortex_parcel_network_assignments.txt')
# need to subtract one to make it compatible for python indices
indsort = np.loadtxt('cortex_subcortex_community_order.txt',dtype=int) - 1 
indsort.shape = (len(indsort),1)
#netorder = np.loadtxt('network_labelfile.txt')


# Computing functional connectivity and visualizing the data (assuming preprocessing has already been done)
FCmat = np.corrcoef(lr_parcellated)
FCMat_sorted = FCmat[indsort,indsort.T]
plt.figure(figsize=(7,7))
plt.imshow(FCMat_sorted,origin='lower',cmap='gray_r')
plt.colorbar(fraction=0.046)
plt.title('Cortical-subcortical parcellation\nSorted FC Matrix',fontsize=24)
plt.tight_layout()
plt.show()

tseriesMatSubj = lr_parcellated

