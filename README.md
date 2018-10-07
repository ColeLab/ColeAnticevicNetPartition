# The Cole-Anticevic Brain-wide Network Partition (CAB-NP)

## Authors
Jie Lisa Ji, Marjolein Spronk, Kaustubh Kulkarni, Grega Repovs, Alan Anticevic, and Michael W. Cole

Cole Neurocognition Lab, http://www.colelab.org/

Anticevic Lab, http://anticeviclab.yale.edu/

## Version Info and Acknowledgements

**Version 1.0.3**: October 7, 2018, filenames changed for simplicity and consistency.

**Version 1.0.2**: October 4, 2018, changed subcortical parcellation with global signal regression (GSR) applied as a preprocessing to be the primary version. This is based on results reported in the final version of the article accepted for publication after peer review.

**Version 1.0.1**: January 17, 2018, added a version of the subcortical parcellation with GSR applied as a preprocess step. This was included due to concern over extensive assignment of subcortical voxels to the visual networks (which GSR reduced). A version of the parcellation based on the conjunction of the GSR and non-GSR versions is included, for those who wish to only use subcortical voxels with assignments consistent with and without GSR.

**Version 1.0**: September 27, 2017


Available from: https://github.com/ColeLab/ColeAnticevicNetPartition/

**Cite as**: Ji JL, Spronk M, Kulkarni K, Repovs G, Anticevic A, Cole MW (In Press) "Mapping the human brain's cortical-subcortical functional network organization". NeuroImage. https://doi.org/10.1016/j.neuroimage.2018.10.006
and https://github.com/ColeLab/ColeAnticevicNetPartition/

Scientific article also available as a bioRxiv preprint: http://doi.org/10.1101/206292

Data were provided by the Human Connectome Project, WU-Minn Consortium (Principal Investigators: David Van Essen and Kamil Ugurbil; 1U54MH091657) funded by the 16 NIH Institutes and Centers that support the NIH Blueprint for Neuroscience Research; and by the McDonnell Center for Systems Neuroscience at Washington University. This work was supported by the NIH via awards K99/R00-MH096801 (Cole), DP5-OD012109 (Anticevic), R01-MH109520 (Cole), R01-MH108590 (Anticevic), R01-AG055556 (Cole), and R01-MH112189 (Anticevic), as well as the Brain and Behavior Foundation (NARSAD) Independent Investigator grant (Anticevic) and ARRS J7-6829 (Repovs).

## Overview

This network partition was created using the Glasser 2016 parcels [Glasser MF, Coalson TS, Robinson EC, Hacker CD, Harwell J, Yacoub E, Ugurbil K, Andersson J, Beckmann CF, Jenkinson M, Smith SM, Van Essen DC (2016) A multi-modal parcellation of human cerebral cortex. Nature. http://doi.org/10.1038/nature18933], along with data of 337 unrelated healthy volunteers from the WashU-Minn Human Connectome Project (HCP) [https://www.humanconnectome.org/]. Resting-state fMRI data were used (across all 4 resting-state fMRI runs per subject). ICA+FIX was used for denoising and MSMAll for registration (along with standard HCP minimal preprocessing). Pearson correlations between time series were then calculated between all parcels/regions, and network communities were identified using the general Louvain algorithm.

The cortical network partition was extended into subcortex. This was accomplished by labeling each subcortical voxel with the cortical network with the strongest average Pearson correlation.

See the main publication reporting this partition for more information: Ji JL, Spronk M, Kulkarni K, Repovs G, Anticevic A, Cole MW (In Press) "Mapping the human brain's cortical-subcortical functional network organization". NeuroImage. https://doi.org/10.1016/j.neuroimage.2018.10.006 [Open access preprint: http://doi.org/10.1101/206292]

The Glasser2016 parcels are available here: https://balsa.wustl.edu/sceneFile/show/lLMz

## Quick Start

Download and open Connectome Workbench (https://www.humanconnectome.org/software/connectome-workbench). Load the ColeAnticevicNetPartition.wb.spec file. Click the "Load Scenes" button, select one of the scenes of interest, and click the "Show" button. This will allow you to view and interact with the network partition and parcels.

## The Network Partition

![Alt text](images/Figure1.jpg?raw=true "Illustration of ColeAnticevicNetPartition_v1")
*Top Left*: Illustration of the network partition with the Glasser parcels. The colors correspond to the colors labeled in the network matrix (to the right).
*Top Right*: Axial slices illustrating the subcortical extension of the cortical network partition. Each voxel was assigned to the network that it had the highest mean resting-state functional connectivity with. See Ji et al. (In Press) for more information.
*Bottom Left*: Network matrix with Pearson correlation-based resting-state functional connectivity, sorted based on community affiliation according to the network partition. An fMRI dataset of 337 subjects from the WashU-Minn Human Connectome Project (HCP) was used (https://www.humanconnectome.org/), with 4 runs for each subject. See Ji et al. (In Press) for more information.
*Bottom Right*: Same as bottom left, but now also including subcortical parcels.


![Alt text](images/ColeAnticevicHumanNetPartition_animation.gif?raw=true "Animation of ColeAnticevicNetPartition_v1")

The partition across transaxial slices of the S1200 HCP average T1 image.


## Included Files

- ColeAnticevicNetPartition.wb.spec - Main Connectome Workbench file, specifying network partition visualization files. Load this file with wb_view to visualize and interact with the network partition.
- ColeAnticevicNetPartition_MainScene.wb.scene - The main Connectome Workbench scene file.
- ColeAnticevicNetPartition_OtherScenes.wb.scene - Alternative scenes for use with Connectome Workbench. These were separated from the main scene file to accommodate computers with low amounts of RAM.
- cortex_community_order.mat - The order the Glasser parcels should be in to reveal the community structure identified by this network partition, in MATLAB format. Note that this file assumes you have the left hemisphere Glasser parcellation regions first, followed by the right hemisphere regions.
- cortex_community_order.txt - Same as the previous file, but in text format.
- [LoadParcellatedDataInMatlab_Example.m](LoadParcellatedDataInMatlab_Example.m) - Example of how to parcellate CIFTI fMRI data and load it into MATLAB
- [LoadParcellatedDataInMatlab_Example_cortexonly.m](LoadParcellatedDataInMatlab_Example_cortexonly.m) - Example of how to parcellate CIFTI fMRI data and load it into MATLAB, using cortical parcels only (no subcortical parcels)
- network_labelfile.txt - The labels for each network, along with color information (RGBA value).
- cortex_parcel_network_assignments.mat - A vector of numbers, one per parcel, indicating which network that parcel was assigned to in the network partition (in MATLAB format). (Parcel order: L first, R second.)
- cortex_parcel_network_assignments.txt - Same as the previous file, but in text format.
-  CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_netassignments_LR.dlabel.nii - Cortex + subcortex (whole-brain) network assignments. Global signal regression (GSR) applied to subcortical voxels as a preprocessing step.
- CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dlabel.nii - Same as above, but at the parcel level (rather than the network assignment level).
- Q1-Q6_RelatedParcellation210.L.CorticalAreas_dil_Black.32k_fs_LR.border - The left-hemisphere borders of the Glasser parcels
- Q1-Q6_RelatedParcellation210.R.CorticalAreas_dil_Black.32k_fs_LR.border - The right-hemisphere borders of the Glasser parcels
- README.md - This file
- S1200_AverageT1w_restore.nii.gz - The average of 1096 subjects from the HCP dataset, from the S1200 release. From HCP_S1200_GroupAvg_v1.zip. For more info visit http://www.humanconnectome.org/documentation/S1200 and https://www.humanconnectome.org/study/hcp-young-adult/article/s1200-group-average-data-release. Before using data from HCP you must agree to the HCP Open Access Data Use Terms at http://humanconnectome.org/data/data-use-terms/DataUseTerms-HCP-Open-Access-26Apr2013.pdf
- S1200.L.inflated_MSMAll.32k_fs_LR.surf.gii - Left hemisphere inflated cortical surface
- S1200.L.midthickness_MSMAll.32k_fs_LR.surf.gii - Left hemisphere midthickness cortical surface
- S1200.L.pial_MSMAll.32k_fs_LR.surf.gii - Left hemisphere pial cortical surface
- S1200.L.very_inflated_MSMAll.32k_fs_LR.surf.gii - Left hemisphere very inflated cortical surface
- S1200.R.inflated_MSMAll.32k_fs_LR.surf.gii - Right hemisphere inflated cortical surface
- S1200.R.midthickness_MSMAll.32k_fs_LR.surf.gii - Right hemisphere midthickness cortical surface
- S1200.R.pial_MSMAll.32k_fs_LR.surf.gii - Right hemisphere pial cortical surface
- S1200.R.very_inflated_MSMAll.32k_fs_LR.surf.gii - Right hemisphere very inflated cortical surface
- S1200.sulc_MSMAll.32k_fs_LR.dscalar.nii -  Cortical surface sulcus pattern for visualization of cortical surface
- *SeparateHemispheres* directory - Files with each hemisphere separated. This can be useful for ensuring that parcels from each hemisphere are in the correct order by loading each hemisphere separately (e.g., in MATLAB).
  - cortex_ColeAnticevic_NetPartition_GlasserParcels_L.label.gii - Left hemisphere cortex-only partition
  - cortex_ColeAnticevic_NetPartition_GlasserParcels_R.label.gii - Right hemisphere cortex-only partition
  - CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_netassignments_L.dlabel.nii - Left hemisphere cortex+subcortex network assignments for each parcel
  - CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_netassignments_R.dlabel.nii - Right hemisphere cortex+subcortex network assignments for each parcel
  - CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_L.dlabel.nii - Left hemisphere cortex+subcortex list of parcels, with a label for each parcel.
  - CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_R.dlabel.nii - Right hemisphere cortex+subcortex list of parcels, with a label for each parcel.
  - Q1-Q6_RelatedParcellation210.L.CorticalAreas_dil_Colors.32k_fs_LR.dlabel.nii - Glasser2016 cortical parcels, left hemisphere
  - Q1-Q6_RelatedParcellation210.R.CorticalAreas_dil_Colors.32k_fs_LR.dlabel.nii - Glasser2016 cortical parcels, right hemisphere
  - subcortex_atlas_GSR_L.nii - Left hemisphere subcortex-only network partition
  - subcortex_atlas_GSR_R.nii - Right hemisphere subcortex-only network partition
  - subcortex_atlas_GSR_parcels_L.nii - Left hemisphere subcortex-only network parcellation (each parcel separated)
  - subcortex_atlas_GSR_parcels_R.nii - Right hemisphere subcortex-only network parcellation (each parcel separated)
- *images* directory
  - [Figure1.jpg](images/Figure1.jpg) - An illustration of the network partition.
  - [cortex_Illustration_ColeAnticevicNetpartition_splithalfvalidation_v1.pdf](images/cortex_Illustration_ColeAnticevicNetpartition_splithalfvalidation_v1.pdf) - An illustration of the split half validation results.
  - [ColeAnticevicHumanNetPartition_animation.gif](images/ColeAnticevicHumanNetPartition_animation.gif) - An animated GIF illustrating the partition across transaxial slices of the S1200 HCP average T1 image.
- *NoGSRSubcortex* directory
	- CortexSubcortex_ColeAnticevic_NetPartition_woSubcorGSR_parcels_LR.dlabel.nii - Subcortical parcellation without global signal regression (GSR) applied to subcortical voxels as a preprocessing step. Cortex is also included.
	-  CortexSubcortex_ColeAnticevic_NetPartition_woSubcorGSR_netassignments_LR.dlabel.nii - Same as above, but at the network assignment level (rather than level of individual parcels).
	- subcortex_atlas_ConjunctionGSRnoGSR_n.dlabel.nii - A version of the parcellation based on the conjunction of the GSR and non-GSR versions, for those who wish to only use subcortical voxels with assignments consistent with and without GSR.
	- *SeparateHemispheres* directory - Files with hemispheres separated, for subcortical parcellation without global signal regression (GSR) applied to subcortical voxels as a preprocessing step.
- *data* directory
	- cortex_fc_avg.pconn.nii - Correlation matrix used for creating the cortical partition. Formatted for visualization in Workbench.
	- meanFCMatSorted.csv - Same correlation matrix, formatted as a comma separated value file.
	- meanFCMatSorted.mat - Same correlation matrix, formatted as a MATLAB file.
