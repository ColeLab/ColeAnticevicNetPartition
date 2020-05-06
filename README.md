# The Cole-Anticevic Brain-wide Network Partition (CAB-NP)

## Authors
Jie Lisa Ji, Marjolein Spronk, Kaustubh Kulkarni, Grega Repovs, Alan Anticevic, and Michael W. Cole

Cole Neurocognition Lab, http://www.colelab.org/

Anticevic Lab, http://anticeviclab.yale.edu/

## Version Info and Acknowledgements

**Version 1.1.1**: May 1, 2020, added Glasser360Indices_LR.dscalar.nii. This file can be loaded into Connectome Workbench, such that clicking a parcel will indicate which parcel number it is within the cortical Glasser parcellation. Tip: Turn off Display Borders to speed up Connectome Workbench.

**Version 1.1.0**: July 8, 2019, updated all files with cortical parcels from the HCP1200 release; updated and standardized naming of parcels; added LabelKey.txt showing mappings for the wSubcorGSR and woSubcorGSR parcellations between: Index; KeyValue; Label; Red; Green; Blue; Alpha; Hemisphere; Network; NetworkKey; NetworkSortedOrder

**Version 1.0.5**: October 10, 2018, first public release.

**Version 1.0.4**: October 9, 2018, added cortex+subcortex parcel order files and dscalar versions of CIFTI files.

**Version 1.0.3**: October 7, 2018, filenames changed for simplicity and consistency.

**Version 1.0.2**: October 4, 2018, changed subcortical parcellation with global signal regression (GSR) applied as a preprocessing to be the primary version. This is based on results reported in the final version of the article accepted for publication after peer review.

**Version 1.0.1**: January 17, 2018, added a version of the subcortical parcellation with GSR applied as a preprocess step. This was included due to concern over extensive assignment of subcortical voxels to the visual networks (which GSR reduced). A version of the parcellation based on the conjunction of the GSR and non-GSR versions is included, for those who wish to only use subcortical voxels with assignments consistent with and without GSR.

**Version 1.0.0**: September 27, 2017


**Cite as**: Ji JL*, Spronk M*, Kulkarni K, Repovs G, Anticevic A**, Cole MW** (2019). "Mapping the human brain's cortical-subcortical functional network organization". NeuroImage. 185:35–57. doi:10.1016/j.neuroimage.2018.10.006 [* = equal contribution; ** = senior authors] https://doi.org/10.1016/j.neuroimage.2018.10.006
and https://github.com/ColeLab/ColeAnticevicNetPartition/

Interactive versions of the figures from the paper are available here: https://balsa.wustl.edu/study/show/wZML

Scientific article also available as an open access bioRxiv preprint: http://doi.org/10.1101/206292

Data were provided by the Human Connectome Project, WU-Minn Consortium (Principal Investigators: David Van Essen and Kamil Ugurbil; 1U54MH091657) funded by the 16 NIH Institutes and Centers that support the NIH Blueprint for Neuroscience Research; and by the McDonnell Center for Systems Neuroscience at Washington University. This work was supported by the NIH via awards K99/R00-MH096801 (Cole), DP5-OD012109 (Anticevic), R01-MH109520 (Cole), R01-MH108590 (Anticevic), R01-AG055556 (Cole), and R01-MH112189 (Anticevic), as well as the Brain and Behavior Foundation (NARSAD) Independent Investigator grant (Anticevic) and ARRS J7-6829 (Repovs).

## Overview

This network partition was created using the Glasser 2016 parcels [Glasser MF, Coalson TS, Robinson EC, Hacker CD, Harwell J, Yacoub E, Ugurbil K, Andersson J, Beckmann CF, Jenkinson M, Smith SM, Van Essen DC (2016) A multi-modal parcellation of human cerebral cortex. Nature. http://doi.org/10.1038/nature18933], along with data of 337 unrelated healthy volunteers from the WashU-Minn Human Connectome Project (HCP) [https://www.humanconnectome.org/]. Resting-state fMRI data were used (across all 4 resting-state fMRI runs per subject). ICA+FIX was used for denoising and MSMAll for registration (along with standard HCP minimal preprocessing). Pearson correlations between time series were then calculated between all parcels/regions, and network communities were identified using the general Louvain algorithm.

The cortical network partition was extended into subcortex. This was accomplished by labeling each subcortical voxel with the cortical network with the strongest average Pearson correlation.

See the main publication reporting this partition for more information: Ji JL*, Spronk M*, Kulkarni K, Repovs G, Anticevic A**, Cole MW** (2019). "Mapping the human brain's cortical-subcortical functional network organization". NeuroImage. 185:35–57. doi:10.1016/j.neuroimage.2018.10.006 [* = equal contribution; ** = senior authors] https://doi.org/10.1016/j.neuroimage.2018.10.006 [Open access preprint: http://doi.org/10.1101/206292]

The Glasser2016 parcels are available here: https://balsa.wustl.edu/study/show/RVVG

More info on the cortical parcels is available in the main and supplemental documents released as part of the main Glasser2016 publication (e.g., details in Table 1 of the Supplementary Neuroanatomical Results document, page 81):
Glasser, Matthew F, Timothy S Coalson, Emma C Robinson, Carl D Hacker, John Harwell, Essa Yacoub, Kamil Ugurbil, et al. (2016). "A Multi-Modal Parcellation of Human Cerebral Cortex." Nature, July. doi:10.1038/nature18933. http://www.nature.com/doifinder/10.1038/nature18933

Evidence that the CIFTI format used here (combining cortical surface with subcortical volume data) is superior to prior methods:
Coalson, T.S., Van Essen, D.C., Glasser, M.F., 2018. The impact of traditional neuroimaging methods on the spatial localization of cortical areas. Proc Natl Acad Sci USA 115, E6356–E6365. https://doi.org/10.1073/pnas.1801582115

Software versions this release was tested on:
Connectome Workbench 1.3.2, MATLAB R2014b, and Python 2.7

Many features are available in Connectome Workbench's wb_command (https://www.humanconnectome.org/software/workbench-command) for interfacing with CAB-NP.


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
- cortex_subcortex_community_order.mat - The order of all 718 regions (cortex+subcortex), sorted by network affiliation, in MATLAB format.
- cortex_subcortex_community_order.txt - The order of all 718 regions (cortex+subcortex), sorted by network affiliation, in plain text format.
- cortex_subcortex_parcel_network_assignments.mat - A vector of numbers, one per cortex+subcortex parcel, indicating which network that parcel was assigned to in the network partition (in MATLAB format). (Parcel order: L first, R second.)
- cortex_subcortex_parcel_network_assignments.txt - Same as the previous file, but in text format.
- [LoadParcellatedDataInMatlab_Example.m](LoadParcellatedDataInMatlab_Example.m) - Example of how to parcellate CIFTI fMRI data and load it into MATLAB
- [LoadParcellatedDataInMatlab_Example_cortexonly.m](LoadParcellatedDataInMatlab_Example_cortexonly.m) - Example of how to parcellate CIFTI fMRI data and load it into MATLAB, using cortical parcels only (no subcortical parcels)
- [LoadParcellatedDataInPython_Example.py](LoadParcellatedDataInPython_Example.py) - Example of how to parcellate CIFTI fMRI data and load it into Python
- [LoadParcellatedDataInPython_Example_cortexonly.py](LoadParcellatedDataInPython_Example_cortexonly.py) - Example of how to parcellate CIFTI fMRI data and load it into Python, using cortical parcels only (no subcortical parcels)
- network_labelfile.txt - The labels for each network, along with color information (RGBA value).
- cortex_parcel_network_assignments.mat - A vector of numbers, one per cortical parcel, indicating which network that parcel was assigned to in the network partition (in MATLAB format). (Parcel order: L first, R second.)
- cortex_parcel_network_assignments.txt - Same as the previous file, but in text format.
- CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_netassignments_LR.dlabel.nii - Cortex + subcortex (whole-brain) network assignments. Global signal regression (GSR) applied to subcortical voxels as a preprocessing step.
- CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dlabel.nii - Same as above, but at the parcel level (rather than the network assignment level).
- CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_v1.1_LR.txt - Label text file for CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dlabel.nii
- Glasser360Indices_LR.dscalar.nii - Indicates the parcel number (ordered left hemisphere, then right hemisphere) for each cortical parcel. This is especially useful when loaded into Connectome Workbench along with the main scene file, since simply clicking on a parcel will indicate the parcel number for that parcel. Tip: Turn off Display Borders to speed up Connectome Workbench.
- Q1-Q6_RelatedParcellation210.L.CorticalAreas_dil_Black.32k_fs_LR.border - The left-hemisphere borders of the Glasser parcels
- Q1-Q6_RelatedParcellation210.R.CorticalAreas_dil_Black.32k_fs_LR.border - The right-hemisphere borders of the Glasser parcels
- Q1-Q6_RelatedValidation210.L.CorticalAreas_dil_Final_Final_Areas_Group.32k_fs_LR.border - The updated (HCP Phase 2) left-hemisphere borders of the Glasser parcels
- Q1-Q6_RelatedValidation210.R.CorticalAreas_dil_Final_Final_Areas_Group.32k_fs_LR.border - The updated (HCP Phase 2) right-hemisphere borders of the Glasser parcels
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
- CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR_ReorderedByNetworks.dlabel.nii - The parcels (same as in CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dlabel.nii) sorted by network according to cortex_subcortex_parcel_network_assignments.txt
- CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR_LabelKey.txt - Legend text file showing all mappings for the wSubcorGSR parcellation between: Index; KeyValue; Label; Red; Green; Blue; Alpha; Hemisphere; Network; NetworkKey; NetworkSortedOrder
- *SeparateHemispheres* directory - Files with each hemisphere separated. This can be useful for ensuring that parcels from each hemisphere are in the correct order by loading each hemisphere separately (e.g., in MATLAB).
  - cortex_ColeAnticevic_NetPartition_GlasserParcels_L.label.gii - Left hemisphere cortex-only partition
  - cortex_ColeAnticevic_NetPartition_GlasserParcels_R.label.gii - Right hemisphere cortex-only partition
  - CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_netassignments_L.dlabel.nii - Left hemisphere cortex+subcortex network assignments for each parcel
  - CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_netassignments_R.dlabel.nii - Right hemisphere cortex+subcortex network assignments for each parcel
  - CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_L.dlabel.nii - Left hemisphere cortex+subcortex list of parcels, with a label for each parcel. Note that some midline subcortical parcels were split to create this left-hemisphere-only version, such that combining both hemispheres results in 758 parcels (rather than 718).
  - CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_R.dlabel.nii - Right hemisphere cortex+subcortex list of parcels, with a label for each parcel. Note that some midline subcortical parcels were split to create this right-hemisphere-only version, such that combining both hemispheres results in 758 parcels (rather than 718).
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
	- CortexSubcortex_ColeAnticevic_NetPartition_woSubcorGSR_netassignments_LR.dscalar.nii - Dscalar version of network assignments.
	- CortexSubcortex_ColeAnticevic_NetPartition_woSubcorGSR_parcels_LR.dscalar.nii - Dscalar version of parcel-level network assignments.
	- CortexSubcortex_ColeAnticevic_NetPartition_woSubcorGSR_parcels_LR_LabelKey.txt - Legend text file showing all mappings for the woSubcorGSR parcellation between: Index; KeyValue; Label; Red; Green; Blue; Alpha; Hemisphere; Network; NetworkKey; NetworkSortedOrder
	- *SeparateHemispheres* directory - Files with hemispheres separated, for subcortical parcellation without global signal regression (GSR) applied to subcortical voxels as a preprocessing step.
- *data* directory
	- cortex_fc_avg.pconn.nii - Correlation matrix used for creating the cortical partition. Formatted for visualization in Workbench.
	- meanFCMatSorted.csv - Same correlation matrix, formatted as a comma separated value file.
	- meanFCMatSorted.mat - Same correlation matrix, formatted as a MATLAB file.
	- cortex_gamma1.295_partition_before_reassignment.mat - Network assignment for the cortical parcels prior to the clean up (reassignment) step.
	- CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_netassignments_LR.dscalar.nii - Dscalar version of network assignments.
	- CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dscalar.nii - Dscalar version of parcel-level network assignments.

### Network Order Information and Examples for Re-ordering CIFTI Outputs

Note that the file `CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dlabel.nii` is ordered by cortical then subcortical parcels. Also, note that the subcortex is ordered in L/R order instead of by network (refer to *_LabelKey.txt for label mappings). The key reason for this choice was to provide a clear distinction between cortical and subcortical parcels. Here is an example:

![Alt text](images/ExampleCortexSubcortexMatrix.jpg?raw=true "Illustration of example correlation matrix from data parcellated with ColeAnticevicNetPartition_v1")


For most people this result may not be the preferred choice, especially if you wish to publish an ordered matrix by network:

![Alt text](images/ExampleNetworkReorderedMatrix.jpg?raw=true "Illustration of example correlation matrix from data parcellated with ColeAnticevicNetPartition_v1, ordered by Network")


Therefore, if you would like to run an analysis such that your order is ordered by network, then the following file should be used on the front end of your analysis:
```
CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR_ReorderedByNetworks.dlabel.nii
```

If you already ran an analysis that was parcellated with `CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dlabel.nii` and wish to reorder your result by network then follow the following steps for a `ptseries` or `pscalar` file types:
```
wb_command -cifti-reorder <yourfile>.ptseries.nii COLUMN ColeAnticevicNetPartition/cortex_subcortex_community_order.txt <yourfile>.ptseries.nii
```

---

If you already ran an analysis that was parcellated with `CortexSubcortex_ColeAnticevic_NetPartition_wSubcorGSR_parcels_LR.dlabel.nii` and wish to reorder your result by network then follow the following steps for a `pconn` file type:
* Note -- you will have to re-order the file twice: once by COLUMN and once by ROW

```
wb_command -cifti-reorder <yourfile>.pconn.nii COLUMN ColeAnticevicNetPartition/cortex_subcortex_community_order.txt <yourfile>.pconn.nii

wb_command -cifti-reorder <yourfile>.pconn.nii ROW ColeAnticevicNetPartition/cortex_subcortex_community_order.txt <yourfile>.pconn.nii
```
[//]: # (This is tracking code for keeping track of visits to the repo; MWC)
[![Analytics](https://ga-beacon.appspot.com/UA-158202396-1/CABNP/readme?pixel)](https://github.com/igrigorik/ga-beacon)

### Volume version of the Glasser surface parcels

We have been receiving many inquiries into using our network partition with volume (rather than CIFTI) data. We defer to the creators of the Glasser et al. (2016) cortical parcellation (https://balsa.wustl.edu/study/show/RVVG) in saying that using a volume version is not recommended. See here for more info on this recommendation: https://www.mail-archive.com/hcp-users@humanconnectome.org/msg03398.html

That said, there are several options for those willing to take the risk in using a volume version of the Glasser cortical parcellation. As recommended previously (https://www.mail-archive.com/hcp-users@humanconnectome.org/msg03398.html) the best option is to use Connectome Workbench to map the group-level cortical surface label file to each subject's individual volume:
1) Use wb_command -cifti-separate to make GIFTI label files
2) Use wb_command -label-to-volume-mapping to map GIFTI label files to the volume

Less ideal but still possible, there are also several options for versions of the Glasser cortical parcellation mapped to group-level volume space. Use with caution.
Examples:
* https://cjneurolab.org/2016/11/22/hcp-mmp1-0-volumetric-nifti-masks-in-native-structural-space/
* https://neurovault.org/collections/1549/
* https://figshare.com/articles/HCP-MMP1_0_projected_on_MNI2009a_GM_volumetric_in_NIfTI_format/3501911
* Apparently AFNI now comes with a volume version of the Glasser cortical parcellation, as described here: https://openwetware.org/wiki/Beauchamp:CorticalSurfaceHCP


