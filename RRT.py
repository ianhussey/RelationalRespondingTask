#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Sun May  1 16:04:58 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'RRT'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
# Dependencies
import itertools  # for flattening lists of lists into lists
import random

# Import stimuli exemplars
exemplars_filename = 'stimuli.xlsx'
exemplars = data.importConditions(exemplars_filename)# Import stimuli exemplars

# Trial generation function
def generate_trials(trial_type_column, multiplier):
    """Generate a shuffled list of stimuli exemplars from a column in an excel stimuli file""" 
    a = dict()  # declare a dict to be populated
    for i in range(len(exemplars)):
        a[i] = [exemplars[i][trial_type_column]] * multiplier  # populate the dict from vertical reads of the conditions
    a = a.values()  # extract only values (and not keys) from the list of dicts
    a = list(itertools.chain(*a))  # flatten the list of dicts into a list
    random.shuffle(a)  # shuffle this list, so that it can be drawn from by the trials
    return a
instructions_box = visual.TextStim(win=win, ori=0, name='instructions_box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.6,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
msg=""
stimulus_box = visual.TextStim(win=win, ori=0, name='stimulus_box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-3.0)
feedback = visual.TextStim(win=win, ori=0, name='feedback',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
true_text = visual.TextStim(win=win, ori=0, name='true_text',
    text='default text',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
false_text = visual.TextStim(win=win, ori=0, name='false_text',
    text='default text',    font='Arial',
    pos=[-0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "end"
endClock = core.Clock()
end_box = visual.TextStim(win=win, ori=0, name='end_box',
    text='End of the task',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    #------Prepare to start Routine "instruction"-------
    t = 0
    instructionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # Determine block repeats and which trial rows are used in each block
    if blocks.thisN == 0:
        trial_rows = "0:2" 
        n_block_repeats = 10   #2*10 = 20 trials
    elif blocks.thisN == 1:
        trial_rows = "2:6" 
        n_block_repeats = 5   #4*5 = 20 trials
    elif blocks.thisN == 2:
        trial_rows = "0:6" 
        n_block_repeats = 10   #6*10 = 60 trials
    elif blocks.thisN == 3:
        trial_rows = "2:6" 
        n_block_repeats = 5   #4*5 = 20 trials
    elif blocks.thisN == 4:
        trial_rows = "0:6" 
        n_block_repeats = 10   #6*10 = 60 trials
    
    # Generate list of stimuli for the block
    trial_type_1_trials = generate_trials('trial_type_1_exemplars', 2)
    trial_type_2_trials = generate_trials('trial_type_2_exemplars', 2)
    trial_type_3_trials = generate_trials('trial_type_3_exemplars', 2)
    trial_type_4_trials = generate_trials('trial_type_4_exemplars', 2)
    trial_type_5_trials = generate_trials('trial_type_5_exemplars', 2)
    trial_type_6_trials = generate_trials('trial_type_6_exemplars', 2)
    
    instructions_box.setText(instructions)
    instructions_key = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructions_key.status = NOT_STARTED
    # keep track of which components have finished
    instructionComponents = []
    instructionComponents.append(instructions_box)
    instructionComponents.append(instructions_key)
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instruction"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *instructions_box* updates
        if t >= 1 and instructions_box.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_box.tStart = t  # underestimates by a little under one frame
            instructions_box.frameNStart = frameN  # exact frame index
            instructions_box.setAutoDraw(True)
        
        # *instructions_key* updates
        if t >= 2 and instructions_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_key.tStart = t  # underestimates by a little under one frame
            instructions_key.frameNStart = frameN  # exact frame index
            instructions_key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructions_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=n_block_repeats, method='fullRandom', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('block_layout.xlsx', selection=trial_rows),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        # choose a random exemplar from the appropriate trial type list
        if trial_type == 1:
            stimulus = trial_type_1_trials.pop()
        elif trial_type == 2:
            stimulus = trial_type_2_trials.pop()
        elif trial_type == 3:
            stimulus = trial_type_3_trials.pop()
        elif trial_type == 4:
            stimulus = trial_type_4_trials.pop()
        elif trial_type == 5:
            stimulus = trial_type_5_trials.pop()
        elif trial_type == 6:
            stimulus = trial_type_6_trials.pop()
        
        # stimulus colors 
        if trial_type == 1 or trial_type == 2:
             stimulus_color = "orange" 
        elif trial_type >2:
             stimulus_color = "cyan"
        
        # correct and incorrect answers for each trialtype in each block
        if trial_type == 1: #true
            required_allowed = "i"
            required_correct = "i"
            feedback_allowed = "e"
            feedback_correct = "e"
        elif trial_type == 2: #false
            required_allowed = "e"
            required_correct = "e"
            feedback_allowed = "i"
            feedback_correct = "i"
        if blocks.thisN <= 2:
            if trial_type == 3: #self pos
                required_allowed = "i"
                required_correct = "i"
                feedback_allowed = "e"
                feedback_correct = "e"
            elif trial_type == 4: #self neg
                required_allowed = "e"
                required_correct = "e"
                feedback_allowed = "i"
                feedback_correct = "i"
            elif trial_type == 5: #self not pos
                required_allowed = "e"
                required_correct = "e"
                feedback_allowed = "i"
                feedback_correct = "i"
            elif trial_type == 6: #self not neg
                required_allowed = "i"
                required_correct = "i"
                feedback_allowed = "e"
                feedback_correct = "e"
        elif blocks.thisN >= 3:
            if trial_type == 3: #self pos
                required_allowed = "e"
                required_correct = "e"
                feedback_allowed = "i"
                feedback_correct = "i"
            elif trial_type == 4: #self neg
                required_allowed = "i"
                required_correct = "i"
                feedback_allowed = "e"
                feedback_correct = "e"
            elif trial_type == 5: #self not pos
                required_allowed = "i"
                required_correct = "i"
                feedback_allowed = "e"
                feedback_correct = "e"
            elif trial_type == 6: #self not neg
                required_allowed = "e"
                required_correct = "e"
                feedback_allowed = "i"
                feedback_correct = "i"
        required_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        required_response.status = NOT_STARTED
        feedback_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        feedback_response.status = NOT_STARTED
        stimulus_box.setColor(stimulus_color, colorSpace='rgb')
        stimulus_box.setText(stimulus)
        true_text.setText(true_label)
        false_text.setText(false_label)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(required_response)
        trialComponents.append(feedback_response)
        trialComponents.append(stimulus_box)
        trialComponents.append(feedback)
        trialComponents.append(true_text)
        trialComponents.append(false_text)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if len(feedback_response.keys)<1:
                msg=""
            else:
                msg="X"
            
            # *required_response* updates
            if t >= 0.3 and required_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                required_response.tStart = t  # underestimates by a little under one frame
                required_response.frameNStart = frameN  # exact frame index
                required_response.status = STARTED
                # AllowedKeys looks like a variable named `required_allowed`
                if not 'required_allowed' in locals():
                    logging.error('AllowedKeys variable `required_allowed` is not defined.')
                    core.quit()
                if not type(required_allowed) in [list, tuple, np.ndarray]:
                    if not isinstance(required_allowed, basestring):
                        logging.error('AllowedKeys variable `required_allowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in required_allowed: required_allowed = (required_allowed,)
                    else:  required_allowed = eval(required_allowed)
                # keyboard checking is just starting
                required_response.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if required_response.status == STARTED:
                theseKeys = event.getKeys(keyList=list(required_allowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if required_response.keys == []:  # then this was the first keypress
                        required_response.keys = theseKeys[0]  # just the first key pressed
                        required_response.rt = required_response.clock.getTime()
                        # was this 'correct'?
                        if (required_response.keys == str(required_correct )) or (required_response.keys == required_correct ):
                            required_response.corr = 1
                        else:
                            required_response.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *feedback_response* updates
            if t >= .3 and feedback_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_response.tStart = t  # underestimates by a little under one frame
                feedback_response.frameNStart = frameN  # exact frame index
                feedback_response.status = STARTED
                # AllowedKeys looks like a variable named `feedback_allowed`
                if not 'feedback_allowed' in locals():
                    logging.error('AllowedKeys variable `feedback_allowed` is not defined.')
                    core.quit()
                if not type(feedback_allowed) in [list, tuple, np.ndarray]:
                    if not isinstance(feedback_allowed, basestring):
                        logging.error('AllowedKeys variable `feedback_allowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in feedback_allowed: feedback_allowed = (feedback_allowed,)
                    else:  feedback_allowed = eval(feedback_allowed)
                # keyboard checking is just starting
                feedback_response.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if feedback_response.status == STARTED:
                theseKeys = event.getKeys(keyList=list(feedback_allowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if feedback_response.keys == []:  # then this was the first keypress
                        feedback_response.keys = theseKeys[0]  # just the first key pressed
                        feedback_response.rt = feedback_response.clock.getTime()
                        # was this 'correct'?
                        if (feedback_response.keys == str(feedback_correct )) or (feedback_response.keys == feedback_correct ):
                            feedback_response.corr = 1
                        else:
                            feedback_response.corr = 0
            
            # *stimulus_box* updates
            if t >= 0.3 and stimulus_box.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulus_box.tStart = t  # underestimates by a little under one frame
                stimulus_box.frameNStart = frameN  # exact frame index
                stimulus_box.setAutoDraw(True)
            
            # *feedback* updates
            if t >= .3 and feedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback.tStart = t  # underestimates by a little under one frame
                feedback.frameNStart = frameN  # exact frame index
                feedback.setAutoDraw(True)
            if feedback.status == STARTED:  # only update if being drawn
                feedback.setText(msg, log=False)
            
            # *true_text* updates
            if t >= 0 and true_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                true_text.tStart = t  # underestimates by a little under one frame
                true_text.frameNStart = frameN  # exact frame index
                true_text.setAutoDraw(True)
            
            # *false_text* updates
            if t >= 0.0 and false_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                false_text.tStart = t  # underestimates by a little under one frame
                false_text.frameNStart = frameN  # exact frame index
                false_text.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if required_response.keys in ['', [], None]:  # No response was made
           required_response.keys=None
           # was no response the correct answer?!
           if str(required_correct ).lower() == 'none': required_response.corr = 1  # correct non-response
           else: required_response.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('required_response.keys',required_response.keys)
        trials.addData('required_response.corr', required_response.corr)
        if required_response.keys != None:  # we had a response
            trials.addData('required_response.rt', required_response.rt)
        # check responses
        if feedback_response.keys in ['', [], None]:  # No response was made
           feedback_response.keys=None
           # was no response the correct answer?!
           if str(feedback_correct ).lower() == 'none': feedback_response.corr = 1  # correct non-response
           else: feedback_response.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('feedback_response.keys',feedback_response.keys)
        trials.addData('feedback_response.corr', feedback_response.corr)
        if feedback_response.keys != None:  # we had a response
            trials.addData('feedback_response.rt', feedback_response.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed n_block_repeats repeats of 'trials'
    
# completed 1 repeats of 'blocks'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(3.750000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(end_box)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_box* updates
    if t >= 0.75 and end_box.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_box.tStart = t  # underestimates by a little under one frame
        end_box.frameNStart = frameN  # exact frame index
        end_box.setAutoDraw(True)
    if end_box.status == STARTED and t >= (0.75 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        end_box.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


win.close()
core.quit()
