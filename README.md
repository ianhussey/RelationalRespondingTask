# Created by
Ian Hussey (ian.hussey@ugent.be)

# Last change
8/11/2015

# Version number
0.9.7.4
#### This is still in beta - I have not had this code reviewed to guarantee that it functions as intended.


# Notes
- NB written in PsychoPy 1.82.01. Bugs may crop up if you're using a different version.
- The escape key quits the task at any time. E, I, or the return key ends the task properly once it’s complete.
- You can run either the psyexp file or the py file inside psychopy. The py file should have greater cross platform support; if you run into errors with the psyexp file use the py instead.
- psydat and csv files are produced for each participant. csv file alone is sufficient to most analyses (e.g., calculation of D scores).
- All stimuli and instructions can be altered by editing the excel files. However, if the number of exemplars of inducers and/or target stimuli are changed, then so too must be the “selected rows” variables be changed in the psychopy builder. These can be found in the “inducersLoop”, “stimuliRuleALoop” and  “stimuliRuleBLoop” loops. Setting this to “0:20” results in 20 trials starting from the first row after the header in the stimulus file. Row numbers start with zero and don’t include the latter number, i.e., “include from rows 0 up to but not including 20” to get 20 trials.
- ITI is set to 750 ms, as in the original publication.


# Block layout
The current version follows’s Sean Hughes’ (unpublished) block layout design rather than Niclas Heider’s design (as used in De Houwer et al., 2015). The key difference between these is that Sean’s design lowers the number of training trials and the ratio of inducers to target trials in the test blocks. Effects are therefore calculated on the same total number of test trials, but the task length is shortened by about 30% (from 10 mins to 7 mins)

## 1. Niclas’s original block layout:

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

## 2. Sean’s block layout (current implementation):

1:2 ratio of inducers to targets
10 target RT pairs per trial-type (40 total)
280 total trials
Estimated 7 min completion time inc 1 min reading instructions

10 inducer stimuli = 5 exemplars for true and 5 for false
20 target stimuli = 4 trial-types with 5 exemplars each

* Block 1 (Inducer) 20 Trials (2 loops of 10 inducers)
* Block 2 (Target) 20 Trials (1 loop of 20 targets)
* Block 3 (Rule 1) 60 Trials (2 loops of 10 inducers plus 20 targets)
* Block 4 (R Target) 20 Trials (1 loop of 20 targets)
* Block 5 (Rule 2) 60 Trials (2 loops of 10 inducers plus 20 targets)


# Known issues
1. If duplicate stimuli are entered in the stimuli file then participants can be presented with two identical exemplars one after another. This is not easy to overcome within the confines of the Psychopy builder. However, the included stimulus file does not repeat stimuli, thus if a similar pattern is followed this issue will not arise.

2. If participants get 100% of trials correct on a given block then the incorrect response RT column will not be created for that block for that participant. This is not a problem if you process files based on column header matching (e.g., using r's `rbind()` command). However, it can be problematic if your data processing workflow relies on column ORDER rather than column header NAME, e.g., a SPSS script using a GET command.

# Changelog
0.9.5 Corrected trials per block in Block 1.

0.9.6 reordered and relabelled trial-types in the stimuli.xlsx file. Before, trial-types 1-4 were, respectively, "i am +", "i am not +", "i am -", "I am not -". Not the order is "I am +", "I am -", "I am not +", "I am not -". Although the difference does not constitute an error, the old order did not conform to the numbering convention used in the IRAP and may have caused confusion.

0.9.7 Significant reorganization of the instructions blocks and loops to make the output easier to analyze.

0.9.7.1 ITI was 300 ms on ruleB blocks: corrected to 750 ms throughout task.

0.9.7.2 Created separate blocks for inducers, practice and test blocks for even easier analysis. Columns now contain only info for a single block, so you can mean() or sd() the whole column. Also changed the names of the keyboard components to blockX and blockXwrong. A future R script will therefore be easier to interpret, as it will sample blockX.rt and blockX.corr variables.

0.9.7.3 Changed True and False labels into variables that are in the stimuli.xlsx file. All text within the task is now changeable via the instrucitons and stimuli files, thereby aiding easier translations.

0.9.7.4 Addition a condition variable to the the pre experiment popup
