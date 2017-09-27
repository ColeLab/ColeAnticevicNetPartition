# Cole-Anticevic Labs Network Partition info

## Authors
Marjolein Spronk, Jie Lisa Ji, Kaustubh Kulkarni, Grega Repovs, Alan Anticevic, and Michael W. Cole
Cole Neurocognition Lab, http://www.colelab.org/
Anticevic Lab, http://anticeviclab.yale.edu/

**Version 1**: July 19th, 2017

Available from: https://github.com/ColeLab/ColeAnticevicNetPartition/

Cite as: tba
and https://github.com/ColeLab/ColeAnticevicNetPartition/

## OVERVIEW

This network partition was created using the Glasser 2016 parcels [Glasser MF, Coalson TS, Robinson EC, Hacker CD, Harwell J, Yacoub E, Ugurbil K, Andersson J, Beckmann CF, Jenkinson M, Smith SM, Van Essen DC (2016) A multi-modal parcellation of human cerebral cortex. Nature. PMID: 27437579 http://doi.org/10.1038/nature18933], along with data of 337 unrelated healthy volunteers from the WashU-Minn Human Connectome Project (HCP) [https://www.humanconnectome.org/]. Resting-state fMRI data were used (across all 4 resting-state fMRI runs per subject). ICA+FIX was used for denoising and MSMAll for registration (along with standard HCP minimal preprocessing). Pearson correlations between time series were then calculated between all parcels/regions, and network communities were identified using the general Louvain algorithm.

The cortical network partition was extended into subcortex. Briefly, this was accomplished by labeling each subcortical voxel with the cortical network with the strongest average Pearson correlation.

See the main paper reporting on this partition for more information [citation].


The Glasser2016 parcels are available here: https://balsa.wustl.edu/sceneFile/show/lLMz

## QUICK START

Open Connectome Workbench (https://www.humanconnectome.org/software/connectome-workbench). Load the ColeAnticevicNetPartition_v1.wb.spec file. Open the associated scene file (ColeAnticevicNetPartition_MainScene_v1.wb.scene) and select one of the scenes of interest. This will allow you to view the network partition and parcels.

### Caption for "cortex_Illustration_ColeLabNetpartition_v1.pdf":
Left: Illustration of the network partition with the Glasser parcels. The colors correspond to the colors labeled in the network matrix (to the right).
Right: Network matrix with Pearson correlation-based functional connectivity, sorted based on community affiliation according to the network partition. A dataset of 337 subjects from the WashU-Minn Human Connectome Project (HCP) was used [https://www.humanconnectome.org/], with 4 runs for each subject. See [citation] for more information.

### Caption for "cortex_Illustration_ColeLabNetpartition_splithalfvalidation_v1.pdf":
Illustration of the split-half validation of the network partition. Network detection was repeated with two groups (N=168 and N=169) matched on age, gender, handedness and education. Analysis was done in exactly the same way as the analysis for the main partition. See [citation] for more information.


## INCLUDED FILES

- cortex_community_order.mat - The order the Glasser parcels should be in to reveal the community structure identified by this network partition. Note that this file assumes you have the left hemisphere Glasser parcellation regions first, followed by the right hemisphere regions. This can be accomplished, for instance, by merging the hemispheres with this command (where $leftHemi and $rightHemi are the left and right hemisphere parcel CIFTI files, respectively):
wb_command -cifti-merge-dense COLUMN Q1-Q6_RelatedParcellation210.LR.CorticalAreas_dil_Colors.32k_fs_LR.dlabel.nii -cifti $leftHemi -cifti $rightHemi
- cortex_community_order.txt - Same as the previous file, but in text format.
- cortex_Illustration_ColeLabNetpartition_v1.pdf - An illustration of the network partition.
- cortex_Illustration_ColeLabNetpartition_splithalfvalidation_v1.pdf - An illustration of the split half validation results.
- L_ColeLab_NetPartition_GlasserParcels.label.gii - A GIFTI file that can be loaded into Connectome Workbench to visualize the partition (left hemisphere)
- network_labelfile.txt - The labels for each network, along with color information (RGBA value).
Format is:
<Partition Name>
<Partition Number> <R> <G> <B> <A>
Example:
Visual
1 0 0 255 255
- parcel_network_assignments.mat - A vector of numbers, one per parcel, indicating which network that parcel was assigned to in the network partition. (Parcel order: L first, R second.)
parcel_network_assignments.txt - Same as the previous file, but in text format.
- Q1-Q6_RelatedParcellation210.L.CorticalAreas_dil_Black.32k_fs_LR.border - The left-hemisphere borders of the Glasser parcels (useful for use with L_ColeLab_NetPartition_GlasserParcels.label.gii for visualizing the partition)
- Q1-Q6_RelatedParcellation210.R.CorticalAreas_dil_Black.32k_fs_LR.border - The right-hemisphere borders of the Glasser parcels (useful for use with R_ColeLab_NetPartition_GlasserParcels.label.gii for visualizing the partition)
- R_ColeLab_NetPartition_GlasserParcels.label.gii - A GIFTI file that can be loaded into Connectome Workbench to visualize the partition (right hemisphere)
- README.md - This file
- *SeparateHemispheres* directory - Files with each hemisphere separate. This can be useful for ensuring that parcels from each hemisphere are in the correct order by loading each hemisphere separately (e.g., in MATLAB).
  - cortex_ColeAnticevic_NetPartition_GlasserParcels_v1_L.label.gii - Left hemisphere cortex-only partition
	- cortex_ColeAnticevic_NetPartition_GlasserParcels_v1_R.label.gii - Right hemisphere cortex-only partition
	- CortexSubcortex_ColeAnticevic_NetPartition_netassignments_v1_L.dlabel.nii - Left hemisphere cortex+subcortex network assignments for each parcel
	- CortexSubcortex_ColeAnticevic_NetPartition_netassignments_v1_R.dlabel.nii - Right hemisphere cortex+subcortex network assignments for each parcel
	- CortexSubcortex_ColeAnticevic_NetPartition_parcels_v1_L.dlabel.nii - Left hemisphere cortex+subcortex list of parcels, with a label for each parcel.
	- CortexSubcortex_ColeAnticevic_NetPartition_parcels_v1_R.dlabel.nii - Right hemisphere cortex+subcortex list of parcels, with a label for each parcel.
