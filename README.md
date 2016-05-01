# Relational Responding Task (RRT) written in PsychoPy
## LicenceCopyright Ian Hussey (ian.hussey@ugent.be)

Distributed under the MIT licence
## Version1.0 (1/5/2016)
Written in PsychoPy 1.82.01
## Notes- NB written in PsychoPy 1.82.01. Bugs may crop up if you run this script in a different version of PsychoPy.- The escape key quits the task at any time. E, I, or the return key ends the task properly once it’s complete.- You can run either the psyexp file or the py file inside psychopy. The py file should have greater cross platform support; if you run into errors with the psyexp file use the py instead.- psydat and csv files are produced for each participant. csv file alone is sufficient to most analyses (e.g., calculation of D scores).- All stimuli and instructions can be altered by editing the excel files. However, there must be 5 exemplars per target stimulus category for the current code implimentation to function correctly, and for it to retain the block layout specified below.- The block length is the number of rows per stimulus file multiplied by the nBlockReptitions variable for that iteration of the blocks loop, which is specified in the instructions file. I've done it this way (rather than simply duplicating the rows in a given stimulus file) so that the same stimulus cannot appear on two consecutive trials. 
- ITI is set to 300 ms (700 in the original publication).

## Block layout
The current version follows’s Sean Hughes’ (unpublished) block layout design rather than Niclas Heider’s design (as used in De Houwer et al., 2015). The key difference between these is that Sean’s design lowers the number of training trials and the ratio of inducers to target trials in the test blocks. Effects are therefore calculated on the same total number of test trials, but the task length is shortened by about 30% (from c.10 mins to c.7 mins)

### 1. Niclas Heider’s original block layout:

1:1 ratio of inducers to targets
10 target RT pairs per trial-type (40 total)
280 total trials
Estimated 10 min completion time inc 1 min reading instructions

10 inducer stimuli = 5 exemplars for true and 5 for false
20 target stimuli = 4 trial-types with 5 exemplars each

* Block 1 (Inducer) 40 Trials (4 loops of 10 inducers)
* Block 2 (Target) 40 Trials (2 loops of 20 targets)
* Block 3 (Rule 1) 80 Trials (4 loops of 10 inducers plus 2 loops of 20 targets)
* Block 4 (R Target) 40 Trials (2 loops of 20 targets)
* Block 5 (Rule 2) 80 Trials (4 loops of 10 inducers plus 2 loops of 20 targets)

### 2. Sean Hughes’ block layout (current implementation):

1:2 ratio of inducers to targets
10 target RT pairs per trial-type (40 total)
280 total trials
Estimated 7 min completion time inc 1 min reading instructions

10 inducer stimuli = 5 exemplars for true and 5 for false.
20 target stimuli = 4 trial-types with 5 exemplars each.

* Block 1 (Inducer) 20 Trials (2 loops of 10 inducers)
* Block 2 (Target) 20 Trials (1 loop of 20 targets)
* Block 3 (Rule 1) 60 Trials (2 loops of 10 inducers plus 20 targets)
* Block 4 (R Target) 20 Trials (1 loop of 20 targets)
* Block 5 (Rule 2) 60 Trials (2 loops of 10 inducers plus 20 targets)

## Known issues
1. If duplicate stimuli are entered in the stimuli file then participants can be presented with two identical exemplars one after another. This is not easy to overcome within the confines of the Psychopy builder. However, the included stimulus file does not repeat stimuli, thus if a similar pattern is followed this issue will not arise.

2. If participants get 100% of trials correct throughout the whole task then the feedbackResponse columns will not be created that participant. This is both highly unlikely, and also not a problem if your data processing workflow processes files based on column name (e.g., using plyr's `rbind.fill()` function) rather than column position (e.g., an SPSS script using a GET command - although some R solutions do assume all files have equal dimensions too). 

3. Because the stimulus file conflates block order with the exemplars, the task requires exactly 5 exemplars per category. My psychopy IRAP implimentation has a method to separate these out, but it hasn't been implimented here yet.  

4. Flemmish language instructions need updating now that english instructions have been simplified. 

5. Number of critical RT pairs is relativley low for trial-type level analyses. Think about doubling the lengths of blocks 3 and 5 to 120 trials (or including additonal test blocks in order to give people a break) - this would give you roughtly the same number as in a standard IRAP.

## Changelog
### 1.0
- Log file added.
- Variable names changed to meet PEP8 standard.
- Used in an experiment, no apparent issues.
- R script included, but needs testing against manual calculations.

### 0.10 
- Additional code components added: only a single stimulus file needed. Correct and incorrect answer for each trial defined in code. 
- ITI changed to 300ms. It's 700ms in the original publication, but it feels slow. Usage with participants doesn't suggest any decreased accuracy with the lower ITI.

### 0.9.8 
- Completely rewritten from scratch. Yeah, go figure. After reading Hadley Wickham's "Tidy Data" while in the process of writing a dplyr script to calculate D scores, I realised that the block layout of the task was a shambles. 
- With some thought, and the idea that I could use an excel file and loop to specify which excel file the loop below should pull from, I managed to reduce the builder flow from many routines to just three. Similarly, the py script went from 1850 lines to 450, and is also much more readable. 
- This is not just code aesthetics however: the data file now has no empty cells. This is in line with the Tidy Data concept that each variable should form a single column. For example, previously, a given RT column contained the reaction times *but also* specified which block they were from, making it harder to analyse the data. Instead, a second variable (e.g., blocks.thisRepN) now specifies the block. This makes analysis easier.

### 0.9.7.4 
Addition a condition variable to the the pre experiment popup

### 0.9.7.3 
Changed True and False labels into variables that are in the stimuli.xlsx file. All text within the task is now changeable via the instrucitons and stimuli files, thereby aiding easier translations.

### 0.9.7.2 
Created separate blocks for inducers, practice and test blocks for even easier analysis. Columns now contain only info for a single block, so you can mean() or sd() the whole column. Also changed the names of the keyboard components to blockX and blockXwrong. A future R script will therefore be easier to interpret, as it will sample blockX.rt and blockX.corr variables.

### 0.9.7.1 
ITI was 300 ms on ruleB blocks: corrected to 750 ms throughout task.

### 0.9.7 
Significant reorganization of the instructions blocks and loops to make the output easier to analyze.

### 0.9.6 
Reordered and relabelled trial-types in the stimuli.xlsx file. Before, trial-types 1-4 were, respectively, "i am +", "i am not +", "i am -", "I am not -". Not the order is "I am +", "I am -", "I am not +", "I am not -". Although the difference does not constitute an error, the old order did not conform to the numbering convention used in the IRAP and may have caused confusion.

### 0.9.5 
Corrected trials per block in Block 1.


