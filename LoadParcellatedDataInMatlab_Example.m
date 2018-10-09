%Make sure to have this in your shell path:
%wb_command

addpath('code/')
addpath('code/gifti-1.6/')

%Setting the parcel files to be the 718 parcels (cortical + subcortical)
parcelCIFTIFile='CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dlabel.nii';

parcelTSFilename='Output_Atlas_CortSubcort.Parcels.LR.ptseries.nii';

%Set this to be your input fMRI data CIFTI file
%inputFile='Run1_fMRIData_Atlas.dtseries.nii';
inputFile='rfMRI_REST1_LR_Atlas_MSMAll.dtseries.nii';

eval(['!wb_command -cifti-parcellate ' inputFile ' ' parcelCIFTIFile ' COLUMN ' parcelTSFilename ' -method MEAN'])

%Load parcellated data (requires the ciftiopen function from the HCP website, FieldTrip)
LR_dat = ciftiopen(parcelTSFilename,'wb_command');

NUMPARCELS=718;
tseriesMatSubj=LR_dat.cdata;

%Loading other relevant files
load('cortex_subcortex_community_order.mat');
netorder=readtable('network_labelfile.txt','ReadVariableNames',false);
netassignments=table2array(readtable('cortex_subcortex_parcel_network_assignments.txt','ReadVariableNames',false));

%Computing Pearson correlation-based functional connectivity and vizualizing the data (assuming preprocessing has already been done)
FCmat=corrcoef(tseriesMatSubj');
FCmat_sorted=FCmat(indsort,indsort);
figure;imagesc(FCmat_sorted)
