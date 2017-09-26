Cole-Anticevic Labs Network Partition info

Authors: Marjolein Spronk <marjoleinspronk@gmail.com>, Jie Lisa Ji, Kaustubh Kulkarni <kulkarni.bio@gmail.com>, Grega Repovs, Alan Anticevic, and Michael W. Cole <mwcole@mwcole.net>
Cole Neurocognition Lab, http://www.colelab.org/
Anticevic Lab, http://anticeviclab.yale.edu/

Final version: July 19th, 2017

Available at: https://github.com/ColeLab/ColeAnticevicNetPartition/

Cite as: tba
and https://github.com/ColeLab/ColeAnticevicNetPartition/

------------------------------------------------------------------------------------------------------------------------
OLD VERSION...

OVERVIEW:
This network partition was created using the Glasser 2016 parcels [Glasser MF, Coalson TS, Robinson EC, Hacker CD, Harwell J, Yacoub E, Ugurbil K, Andersson J, Beckmann CF, Jenkinson M, Smith SM, Van Essen DC (2016) A multi-modal parcellation of human cerebral cortex. Nature. PMID: 27437579 http://doi.org/10.1038/nature18933], along with data of 337 healthy volunteers from the WashU-Minn Human Connectome Project (HCP) [https://www.humanconnectome.org/]. Resting-state fMRI data were used (across all 4 resting-state fMRI runs per subject). <add precise preprocessing steps> ICA+FIX was used for denoising and MSMAll for registration. Pearson correlations were then calculated between all parcels/regions, and communities were estimated using the general Louvain algorithm.

Note that the partition assumes you have the left hemisphere Glasser parcellation regions first, followed by the right hemisphere regions. This can be accomplished, for instance, by merging the hemispheres with this command (where $leftHemi and $rightHemi are the left and right hemisphere parcel CIFTI files, respectively):
wb_command -cifti-merge-dense COLUMN Q1-Q6_RelatedParcellation210.LR.CorticalAreas_dil_Colors.32k_fs_LR.dlabel.nii -cifti $leftHemi -cifti $rightHemi

The Glasser2016 parcels are available here: https://balsa.wustl.edu/sceneFile/show/lLMz

Caption for "Illustration_ColeLabNetPartition_finalversion.pdf":
Left: Illustration of the network partition with the Glasser parcels. The colors correspond to the colors labeled in the network matrix (to the right).
Right: Network matrix with Pearson correlation-based functional connectivity, sorted based on community affiliation according to the network partition. A dataset of 337 subjects from the WashU-Minn Human Connectome Project (HCP) was used [https://www.humanconnectome.org/], with 4 runs for each subject. Preprocessing: HCP minimal preprocessing pipeline, ICA+FIX, MSMAll… KK?

Caption for "Illustration_ColeLabNetPartition_finalversion.pdf": Illustration of the split-half validation of the network partition. Network detection was repeated with two groups (N=168 and N=169) matched on age, gender, handedness and education. Analysis was done in exactly the same way as the analysis for the main partition.


INCLUDED FILES:

community_order.mat - The order the Glasser parcels should be in to reveal the community structure identified by this network partition.
community_order.txt - Same as the previous file, but in text format.
gamma1.295_partition_before_reassignment.mat - A vector of numbers, one per parcel, indicating which network that parcel was assigned to in the network partition before reassignment of certain regions (see “reassigned_regions.txt” in this folder). (Parcel order: L first, R second.)
Illustration_ColeLabNetPartition_final.pdf - An illustration of the network partition.
Illustration_ColeLabNetPartition_final.pdf - An illustration of the split half validation results.
L_ColeLab_NetPartition_GlasserParcels.label.gii - A GIFTI file that can be loaded into Connectome Workbench to visualize the partition (left hemisphere)
network_labelfile.txt - The labels for each network, along with color information (RGBA value).
Format is:
<Partition Name>
<Partition Number> <R> <G> <B> <A>
Example:
Visual
1 0 0 255 255
parcel_network_assignments.mat - A vector of numbers, one per parcel, indicating which network that parcel was assigned to in the network partition. (Parcel order: L first, R second.)
parcel_network_assignments.txt - Same as the previous file, but in text format.
Q1-Q6_RelatedParcellation210.L.CorticalAreas_dil_Black.32k_fs_LR.border - The left-hemisphere borders of the Glasser parcels (useful for use with L_ColeLab_NetPartition_GlasserParcels.label.gii for visualizing the partition)
Q1-Q6_RelatedParcellation210.R.CorticalAreas_dil_Black.32k_fs_LR.border - The right-hemisphere borders of the Glasser parcels (useful for use with R_ColeLab_NetPartition_GlasserParcels.label.gii for visualizing the partition)
R_ColeLab_NetPartition_GlasserParcels.label.gii - A GIFTI file that can be loaded into Connectome Workbench to visualize the partition (right hemisphere)
README.txt - This file
reassigned_regions.txt - Parcel numbers of reassigned regions. Compare “gamma1.295_partition_before_reassignment.mat” and “parcel_network_assignments.mat” to find old and new partition assignments for these regions.


-------------------------------------------------------------------------------------------------------------------------
SPLIT HALF RESULTS

The results are in /projects2/NetworkDetection/data/results/anticevic_analysis/Lisa_analysis/April_2017_GSR_noGSR/noGSR/split_half/

The spreadsheet with matched subjects is in the NetworkDetection folder in the Google Drive NetworkDetection folder under experimentfiles/
-------------------------------------------------------------------------------------------------------------------------
