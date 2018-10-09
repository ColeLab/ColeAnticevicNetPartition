
%Setting the parcel files to be the 718 parcels (cortical + subcortical)
L_parcelCIFTIFile='SeparateHemispheres/CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_L.dlabel.nii';
R_parcelCIFTIFile='SeparateHemispheres/CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_R.dlabel.nii';

L_parcelTSFilename='Output_Atlas.L.Parcels.32k_fs_LR.ptseries.nii';
R_parcelTSFilename='Output_Atlas.R.Parcels.32k_fs_LR.ptseries.nii';

%Set this to be your input fMRI data CIFTI file
inputFile='Run1_fMRIData_Atlas.dtseries.nii';

eval(['!wb_command -cifti-parcellate ' inputFile ' ' L_parcelCIFTIFile ' COLUMN ' L_parcelTSFilename ' -method MEAN'])
eval(['!wb_command -cifti-parcellate ' inputFile ' ' R_parcelCIFTIFile ' COLUMN ' R_parcelTSFilename ' -method MEAN'])

%Load parcellated data (requires the ciftiopen function from the HCP website, FieldTrip)
L_dat = ciftiopen(L_parcelTSFilename,'wb_command');
R_dat = ciftiopen(R_parcelTSFilename,'wb_command');

NUMPARCELS=718;
tseriesMatSubj=zeros(NUMPARCELS,size(L_dat.cdata,2));
tseriesMatSubj(1:359,:)=L_dat.cdata);
tseriesMatSubj(359:end,:)=R_dat.cdata);

%Loading other relevant files
load('cortex_subcortex_community_order.mat');
netorder=readtable('network_labelfile.txt','ReadVariableNames',false);
netassignments=table2array(readtable('cortex_subcortex_parcel_network_assignments.txt','ReadVariableNames',false));

%Computing Pearson correlation-based functional connectivity and vizualizing the data (assuming preprocessing has already been done)
FCmat=corrcoef(tseriesMatSubj');
FCmat_sorted=FCmat(indsort,indsort);
figure;imagesc(FCmat_sorted)
