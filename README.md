# DeeP Western BoUndary Current Flux and Forcing MechanIsms iN ECCO (PUFFIN)  
Lilli Enders - ECCO Summer School, May 2025

## Organization of this project folder: 
* **`notebooks/`**
<br> Notebooks contain most of the core workflow, pulling from the routines in /scripts 
* **`scripts/`**
<br> Functions and subroutines for plotting and analysis live here 
* **`Figures/`**
<br> (Some) output from notebooks is saved here

## Project Overview

The equatorward flowing Deep Western Boundary Current (DWBC) bifurcates as it interacts with the shallow topography and dynamical complexity of the Tail of the Grand Banks (TGB) south of Newfoundland. Some portion of the DWBC is thought to continue onto the Scotian Shelf, eventually influencing the shelf circulation (and potentially the Gulf Stream). It’s not clear whether variability in the transport of the DWBC onto the Scotian Shelf is inherited from the DWBC further North (i.e., in the Labrador Sea), or whether it is a result of local processes at the TGB. In this project, I investigate the representation of the DWBC near the TGB (in both the mean and anomalous senses) using ECCOv4r4. The goals of the project are: 
  1. Understand how much of the variability of DWBC flux onto the Scotian Shelf (across the East Face) is explained by the variability of the DWBC flux upstream of the TGB
  2. Identify mechanisms that drive the variability in DWBC volume transport, and investigate whether they differ between the north and south faces
A schematic representation of the circulation near the TGB is shown below. In this project, I focus on the DWBC that makes it to the Scotian Shelf through route (1):
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/bb249b29-4c93-4eb8-ad1c-91ad8e434d0c" />

## Data and Methods

### Data & Tools

* **ECCO v4r4 outputs:** Fields of variabiles including U,V,UMASS,VMASS, T & S

* **ECCO EMU:** Adjoint, attribution, forward gradient

* **Other Tools:** OSS Tutorials, ecco_v4_py

I access the ECCOv4r4 data via the AWS cloud system, and rely (heavily) on the ecco_v4_py pacakge and related tutorials (https://ecco-v4-python-tutorial.readthedocs.io/).

### Background Reading
* **Interior pathways of the North Atlantic meridional overturning circulation (Bower et al., 2009)**
* Water mass components of the North Atlantic deep western boundary current (Pickart, 1992)
* Deep Western Boundary Current variability at Cape Hatteras (Pickart & Watts, 1990)
* Changes in the Deep Western Boundary Current at 53°N (Myers & Kulan, 2012)
* The Deep Western Boundary Current in the Labrador Sea From Observations and a High-Resolution Model (Handmann et al., 2018)
* Float trajectories in the deep western boundary current and deep equatorial jets of the tropical Atlantic (Richardson & Fratantoni, 1999)

### Proposed Workflow
1. Identify a control volume around the Tail of Grand Banks, where the DWBC is thought to bifurcate
2. Visualize velocity sections across the North and East edges of the control volume. The North face will reflect the 'total' inflow of DWBC into the control volume, and the East face will reflect the portion of the 'total' DWBC that arrives on the Scotian Shelf.
3. Identify the climatological position of the DWBC across each face (North and East). Using this climatological position, create a mask for each face.
4. Calculate the volume flux of DWBC through each face using masks. Compute statistical quantities (correlation, wavelets, spectra) to understand the variability of the flux in each case.
5. Using the flux across each face as the cost function, use EMU attribution to assess the relative influences of wind/heat flux/fresh water flux/etc on flux. Compare between two faces.
6. Compute model adjoint, using flux across each face as cost functions to diagnose the spatial patterns associated with flux forcings. 

## Project goals and tasks

### Project goals

List the specific project goals or research questions you want to answer. Think about what outcomes or deliverables you'd like to create (e.g. a series of tutorial notebooks demonstrating how to work with a dataset, results of an anaysis to answer a science question, an example of applying a new analysis method, or a new python package).

* Goal 1
* Goal 2
* ...

### Tasks

What are the individual tasks or steps that need to be taken to achieve each of the project goals identified above? What are the skills that participants will need or will learn and practice to complete each of these tasks? Think about which tasks are dependent on prior tasks, or which tasks can be performed in parallel.

* Task 1 (all team members will learn to use GitHub)
* Task 2 (team members will use the scikit-learn python library)
  * Task 2a (assigned to team member A)
  * Task 2b (assigned to team member B)
* Task 3
* ...

## Project Results

Use this section to briefly summarize your project results. This could take the form of describing the progress your team made to answering a research question, developing a tool or tutorial, interesting things found in exploring a new dataset, lessons learned for applying a new method, personal accomplishments of each team member, or anything else the team wants to share.

You could include figures or images here, links to notebooks or code elsewhere in the repository (such as in the [notebooks](notebooks/) folder), and information on how others can run your notebooks or code.
