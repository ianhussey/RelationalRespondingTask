#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Sun Nov  8 18:55:52 2015
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
expName = u'RRT'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'participant': u'', u'condition': u''}
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
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=1.6,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "inducerTrials"
inducerTrialsClock = core.Clock()
stimulusBoxInduc = visual.TextStim(win=win, ori=0, name='stimulusBoxInduc',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.6,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
correctiveFeedbackInduc = visual.TextStim(win=win, ori=0, name='correctiveFeedbackInduc',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-3.0)
msg=""
trueBoxInduc = visual.TextStim(win=win, ori=0, name='trueBoxInduc',
    text='default text',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxInduc = visual.TextStim(win=win, ori=0, name='falseBoxInduc',
    text='default text',    font='Arial',
    pos=[-0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=1.6,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "practiceTrialsRuleA"
practiceTrialsRuleAClock = core.Clock()
stimulusBoxAprac = visual.TextStim(win=win, ori=0, name='stimulusBoxAprac',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.6,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
correctiveFeedbackAprac = visual.TextStim(win=win, ori=0, name='correctiveFeedbackAprac',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-3.0)
msg=""
trueBoxAprac = visual.TextStim(win=win, ori=0, name='trueBoxAprac',
    text='default text',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxAprac = visual.TextStim(win=win, ori=0, name='falseBoxAprac',
    text='default text',    font='Arial',
    pos=[-0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=1.6,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trialsRuleA"
trialsRuleAClock = core.Clock()
stimulusBoxA = visual.TextStim(win=win, ori=0, name='stimulusBoxA',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.6,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
correctiveFeedbackA = visual.TextStim(win=win, ori=0, name='correctiveFeedbackA',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-3.0)
msg=""
trueBoxA = visual.TextStim(win=win, ori=0, name='trueBoxA',
    text='default text',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxA = visual.TextStim(win=win, ori=0, name='falseBoxA',
    text='default text',    font='Arial',
    pos=[-0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=1.6,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "practiceTrialsRuleB"
practiceTrialsRuleBClock = core.Clock()
stimulusBoxBprac = visual.TextStim(win=win, ori=0, name='stimulusBoxBprac',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.6,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
correctiveFeedbackBprac = visual.TextStim(win=win, ori=0, name='correctiveFeedbackBprac',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-3.0)
msg=""
trueBoxBprac = visual.TextStim(win=win, ori=0, name='trueBoxBprac',
    text='default text',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxBprac = visual.TextStim(win=win, ori=0, name='falseBoxBprac',
    text='default text',    font='Arial',
    pos=[-0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=1.6,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trialsRuleB"
trialsRuleBClock = core.Clock()
stimulusBoxB = visual.TextStim(win=win, ori=0, name='stimulusBoxB',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.6,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
correctiveFeedbackB = visual.TextStim(win=win, ori=0, name='correctiveFeedbackB',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-3.0)
msg=""
trueBoxB = visual.TextStim(win=win, ori=0, name='trueBoxB',
    text='default text',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxB = visual.TextStim(win=win, ori=0, name='falseBoxB',
    text='default text',    font='Arial',
    pos=[-0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=1.6,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
inst1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection='0'),
    seed=None, name='inst1')
thisExp.addLoop(inst1)  # add the loop to the experiment
thisInst1 = inst1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInst1.rgb)
if thisInst1 != None:
    for paramName in thisInst1.keys():
        exec(paramName + '= thisInst1.' + paramName)

for thisInst1 in inst1:
    currentLoop = inst1
    # abbreviate parameter names if possible (e.g. rgb = thisInst1.rgb)
    if thisInst1 != None:
        for paramName in thisInst1.keys():
            exec(paramName + '= thisInst1.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setText(instructions
)
    instructionsKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructionsKey.status = NOT_STARTED
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(instructionsKey)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 0.75 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *instructionsKey* updates
        if t >= 1.25 and instructionsKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsKey.tStart = t  # underestimates by a little under one frame
            instructionsKey.frameNStart = frameN  # exact frame index
            instructionsKey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructionsKey.status == STARTED:
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
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'inst1'


# set up handler to look after randomisation of conditions etc
inducersLoop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimuli.xlsx', selection='0:10'),
    seed=None, name='inducersLoop')
thisExp.addLoop(inducersLoop)  # add the loop to the experiment
thisInducersLoop = inducersLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInducersLoop.rgb)
if thisInducersLoop != None:
    for paramName in thisInducersLoop.keys():
        exec(paramName + '= thisInducersLoop.' + paramName)

for thisInducersLoop in inducersLoop:
    currentLoop = inducersLoop
    # abbreviate parameter names if possible (e.g. rgb = thisInducersLoop.rgb)
    if thisInducersLoop != None:
        for paramName in thisInducersLoop.keys():
            exec(paramName + '= thisInducersLoop.' + paramName)
    
    #------Prepare to start Routine "inducerTrials"-------
    t = 0
    inducerTrialsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBoxInduc.setColor(stimulusColour, colorSpace='rgb')
    stimulusBoxInduc.setText(stimulus)
    block1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block1.status = NOT_STARTED
    block1wrong = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block1wrong.status = NOT_STARTED
    
    trueBoxInduc.setText(trueLabel)
    falseBoxInduc.setText(falseLabel)
    # keep track of which components have finished
    inducerTrialsComponents = []
    inducerTrialsComponents.append(stimulusBoxInduc)
    inducerTrialsComponents.append(block1)
    inducerTrialsComponents.append(block1wrong)
    inducerTrialsComponents.append(correctiveFeedbackInduc)
    inducerTrialsComponents.append(trueBoxInduc)
    inducerTrialsComponents.append(falseBoxInduc)
    for thisComponent in inducerTrialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "inducerTrials"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = inducerTrialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusBoxInduc* updates
        if t >= 0.75 and stimulusBoxInduc.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusBoxInduc.tStart = t  # underestimates by a little under one frame
            stimulusBoxInduc.frameNStart = frameN  # exact frame index
            stimulusBoxInduc.setAutoDraw(True)
        
        # *block1* updates
        if t >= 0.75 and block1.status == NOT_STARTED:
            # keep track of start time/frame for later
            block1.tStart = t  # underestimates by a little under one frame
            block1.frameNStart = frameN  # exact frame index
            block1.status = STARTED
            # AllowedKeys looks like a variable named `requiredAllowedKeysA`
            if not 'requiredAllowedKeysA' in locals():
                logging.error('AllowedKeys variable `requiredAllowedKeysA` is not defined.')
                core.quit()
            if not type(requiredAllowedKeysA) in [list, tuple, np.ndarray]:
                if not isinstance(requiredAllowedKeysA, basestring):
                    logging.error('AllowedKeys variable `requiredAllowedKeysA` is not string- or list-like.')
                    core.quit()
                elif not ',' in requiredAllowedKeysA: requiredAllowedKeysA = (requiredAllowedKeysA,)
                else:  requiredAllowedKeysA = eval(requiredAllowedKeysA)
            # keyboard checking is just starting
            block1.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if block1.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block1.keys == []:  # then this was the first keypress
                    block1.keys = theseKeys[0]  # just the first key pressed
                    block1.rt = block1.clock.getTime()
                    # was this 'correct'?
                    if (block1.keys == str(requiredResponseA)) or (block1.keys == requiredResponseA):
                        block1.corr = 1
                    else:
                        block1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *block1wrong* updates
        if t >= 0.75 and block1wrong.status == NOT_STARTED:
            # keep track of start time/frame for later
            block1wrong.tStart = t  # underestimates by a little under one frame
            block1wrong.frameNStart = frameN  # exact frame index
            block1wrong.status = STARTED
            # AllowedKeys looks like a variable named `feedbackAllowedKeysA`
            if not 'feedbackAllowedKeysA' in locals():
                logging.error('AllowedKeys variable `feedbackAllowedKeysA` is not defined.')
                core.quit()
            if not type(feedbackAllowedKeysA) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackAllowedKeysA, basestring):
                    logging.error('AllowedKeys variable `feedbackAllowedKeysA` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackAllowedKeysA: feedbackAllowedKeysA = (feedbackAllowedKeysA,)
                else:  feedbackAllowedKeysA = eval(feedbackAllowedKeysA)
            # keyboard checking is just starting
            block1wrong.clock.reset()  # now t=0
        if block1wrong.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block1wrong.keys == []:  # then this was the first keypress
                    block1wrong.keys = theseKeys[0]  # just the first key pressed
                    block1wrong.rt = block1wrong.clock.getTime()
                    # was this 'correct'?
                    if (block1wrong.keys == str(feedbackResponseA)) or (block1wrong.keys == feedbackResponseA):
                        block1wrong.corr = 1
                    else:
                        block1wrong.corr = 0
        
        # *correctiveFeedbackInduc* updates
        if t >= 0.75 and correctiveFeedbackInduc.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackInduc.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackInduc.frameNStart = frameN  # exact frame index
            correctiveFeedbackInduc.setAutoDraw(True)
        if correctiveFeedbackInduc.status == STARTED:  # only update if being drawn
            correctiveFeedbackInduc.setText(msg, log=False)
        if len(block1wrong.keys)<1:
            msg=""
        else:
            msg="X"
        
        # *trueBoxInduc* updates
        if t >= 0 and trueBoxInduc.status == NOT_STARTED:
            # keep track of start time/frame for later
            trueBoxInduc.tStart = t  # underestimates by a little under one frame
            trueBoxInduc.frameNStart = frameN  # exact frame index
            trueBoxInduc.setAutoDraw(True)
        
        # *falseBoxInduc* updates
        if t >= 0 and falseBoxInduc.status == NOT_STARTED:
            # keep track of start time/frame for later
            falseBoxInduc.tStart = t  # underestimates by a little under one frame
            falseBoxInduc.frameNStart = frameN  # exact frame index
            falseBoxInduc.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inducerTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "inducerTrials"-------
    for thisComponent in inducerTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if block1.keys in ['', [], None]:  # No response was made
       block1.keys=None
       # was no response the correct answer?!
       if str(requiredResponseA).lower() == 'none': block1.corr = 1  # correct non-response
       else: block1.corr = 0  # failed to respond (incorrectly)
    # store data for inducersLoop (TrialHandler)
    inducersLoop.addData('block1.keys',block1.keys)
    inducersLoop.addData('block1.corr', block1.corr)
    if block1.keys != None:  # we had a response
        inducersLoop.addData('block1.rt', block1.rt)
    # check responses
    if block1wrong.keys in ['', [], None]:  # No response was made
       block1wrong.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseA).lower() == 'none': block1wrong.corr = 1  # correct non-response
       else: block1wrong.corr = 0  # failed to respond (incorrectly)
    # store data for inducersLoop (TrialHandler)
    inducersLoop.addData('block1wrong.keys',block1wrong.keys)
    inducersLoop.addData('block1wrong.corr', block1wrong.corr)
    if block1wrong.keys != None:  # we had a response
        inducersLoop.addData('block1wrong.rt', block1wrong.rt)
    
    # the Routine "inducerTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'inducersLoop'


# set up handler to look after randomisation of conditions etc
inst2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection='1'),
    seed=None, name='inst2')
thisExp.addLoop(inst2)  # add the loop to the experiment
thisInst2 = inst2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInst2.rgb)
if thisInst2 != None:
    for paramName in thisInst2.keys():
        exec(paramName + '= thisInst2.' + paramName)

for thisInst2 in inst2:
    currentLoop = inst2
    # abbreviate parameter names if possible (e.g. rgb = thisInst2.rgb)
    if thisInst2 != None:
        for paramName in thisInst2.keys():
            exec(paramName + '= thisInst2.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setText(instructions
)
    instructionsKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructionsKey.status = NOT_STARTED
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(instructionsKey)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 0.75 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *instructionsKey* updates
        if t >= 1.25 and instructionsKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsKey.tStart = t  # underestimates by a little under one frame
            instructionsKey.frameNStart = frameN  # exact frame index
            instructionsKey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructionsKey.status == STARTED:
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
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'inst2'


# set up handler to look after randomisation of conditions etc
stimuliRuleALoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimuli.xlsx', selection='10:30'),
    seed=None, name='stimuliRuleALoop')
thisExp.addLoop(stimuliRuleALoop)  # add the loop to the experiment
thisStimulusRuleALoop = stimuliRuleALoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisStimulusRuleALoop.rgb)
if thisStimulusRuleALoop != None:
    for paramName in thisStimulusRuleALoop.keys():
        exec(paramName + '= thisStimulusRuleALoop.' + paramName)

for thisStimulusRuleALoop in stimuliRuleALoop:
    currentLoop = stimuliRuleALoop
    # abbreviate parameter names if possible (e.g. rgb = thisStimulusRuleALoop.rgb)
    if thisStimulusRuleALoop != None:
        for paramName in thisStimulusRuleALoop.keys():
            exec(paramName + '= thisStimulusRuleALoop.' + paramName)
    
    #------Prepare to start Routine "practiceTrialsRuleA"-------
    t = 0
    practiceTrialsRuleAClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBoxAprac.setColor(stimulusColour, colorSpace='rgb')
    stimulusBoxAprac.setText(stimulus)
    block2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block2.status = NOT_STARTED
    block2wrong = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block2wrong.status = NOT_STARTED
    
    trueBoxAprac.setText(trueLabel)
    falseBoxAprac.setText(falseLabel)
    # keep track of which components have finished
    practiceTrialsRuleAComponents = []
    practiceTrialsRuleAComponents.append(stimulusBoxAprac)
    practiceTrialsRuleAComponents.append(block2)
    practiceTrialsRuleAComponents.append(block2wrong)
    practiceTrialsRuleAComponents.append(correctiveFeedbackAprac)
    practiceTrialsRuleAComponents.append(trueBoxAprac)
    practiceTrialsRuleAComponents.append(falseBoxAprac)
    for thisComponent in practiceTrialsRuleAComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practiceTrialsRuleA"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = practiceTrialsRuleAClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusBoxAprac* updates
        if t >= 0.75 and stimulusBoxAprac.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusBoxAprac.tStart = t  # underestimates by a little under one frame
            stimulusBoxAprac.frameNStart = frameN  # exact frame index
            stimulusBoxAprac.setAutoDraw(True)
        
        # *block2* updates
        if t >= 0.75 and block2.status == NOT_STARTED:
            # keep track of start time/frame for later
            block2.tStart = t  # underestimates by a little under one frame
            block2.frameNStart = frameN  # exact frame index
            block2.status = STARTED
            # AllowedKeys looks like a variable named `requiredAllowedKeysA`
            if not 'requiredAllowedKeysA' in locals():
                logging.error('AllowedKeys variable `requiredAllowedKeysA` is not defined.')
                core.quit()
            if not type(requiredAllowedKeysA) in [list, tuple, np.ndarray]:
                if not isinstance(requiredAllowedKeysA, basestring):
                    logging.error('AllowedKeys variable `requiredAllowedKeysA` is not string- or list-like.')
                    core.quit()
                elif not ',' in requiredAllowedKeysA: requiredAllowedKeysA = (requiredAllowedKeysA,)
                else:  requiredAllowedKeysA = eval(requiredAllowedKeysA)
            # keyboard checking is just starting
            block2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if block2.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block2.keys == []:  # then this was the first keypress
                    block2.keys = theseKeys[0]  # just the first key pressed
                    block2.rt = block2.clock.getTime()
                    # was this 'correct'?
                    if (block2.keys == str(requiredResponseA)) or (block2.keys == requiredResponseA):
                        block2.corr = 1
                    else:
                        block2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *block2wrong* updates
        if t >= 0.75 and block2wrong.status == NOT_STARTED:
            # keep track of start time/frame for later
            block2wrong.tStart = t  # underestimates by a little under one frame
            block2wrong.frameNStart = frameN  # exact frame index
            block2wrong.status = STARTED
            # AllowedKeys looks like a variable named `feedbackAllowedKeysA`
            if not 'feedbackAllowedKeysA' in locals():
                logging.error('AllowedKeys variable `feedbackAllowedKeysA` is not defined.')
                core.quit()
            if not type(feedbackAllowedKeysA) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackAllowedKeysA, basestring):
                    logging.error('AllowedKeys variable `feedbackAllowedKeysA` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackAllowedKeysA: feedbackAllowedKeysA = (feedbackAllowedKeysA,)
                else:  feedbackAllowedKeysA = eval(feedbackAllowedKeysA)
            # keyboard checking is just starting
            block2wrong.clock.reset()  # now t=0
        if block2wrong.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block2wrong.keys == []:  # then this was the first keypress
                    block2wrong.keys = theseKeys[0]  # just the first key pressed
                    block2wrong.rt = block2wrong.clock.getTime()
                    # was this 'correct'?
                    if (block2wrong.keys == str(feedbackResponseA)) or (block2wrong.keys == feedbackResponseA):
                        block2wrong.corr = 1
                    else:
                        block2wrong.corr = 0
        
        # *correctiveFeedbackAprac* updates
        if t >= 0.75 and correctiveFeedbackAprac.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackAprac.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackAprac.frameNStart = frameN  # exact frame index
            correctiveFeedbackAprac.setAutoDraw(True)
        if correctiveFeedbackAprac.status == STARTED:  # only update if being drawn
            correctiveFeedbackAprac.setText(msg, log=False)
        if len(block2wrong.keys)<1:
            msg=""
        else:
            msg="X"
        
        # *trueBoxAprac* updates
        if t >= 0 and trueBoxAprac.status == NOT_STARTED:
            # keep track of start time/frame for later
            trueBoxAprac.tStart = t  # underestimates by a little under one frame
            trueBoxAprac.frameNStart = frameN  # exact frame index
            trueBoxAprac.setAutoDraw(True)
        
        # *falseBoxAprac* updates
        if t >= 0 and falseBoxAprac.status == NOT_STARTED:
            # keep track of start time/frame for later
            falseBoxAprac.tStart = t  # underestimates by a little under one frame
            falseBoxAprac.frameNStart = frameN  # exact frame index
            falseBoxAprac.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceTrialsRuleAComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "practiceTrialsRuleA"-------
    for thisComponent in practiceTrialsRuleAComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if block2.keys in ['', [], None]:  # No response was made
       block2.keys=None
       # was no response the correct answer?!
       if str(requiredResponseA).lower() == 'none': block2.corr = 1  # correct non-response
       else: block2.corr = 0  # failed to respond (incorrectly)
    # store data for stimuliRuleALoop (TrialHandler)
    stimuliRuleALoop.addData('block2.keys',block2.keys)
    stimuliRuleALoop.addData('block2.corr', block2.corr)
    if block2.keys != None:  # we had a response
        stimuliRuleALoop.addData('block2.rt', block2.rt)
    # check responses
    if block2wrong.keys in ['', [], None]:  # No response was made
       block2wrong.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseA).lower() == 'none': block2wrong.corr = 1  # correct non-response
       else: block2wrong.corr = 0  # failed to respond (incorrectly)
    # store data for stimuliRuleALoop (TrialHandler)
    stimuliRuleALoop.addData('block2wrong.keys',block2wrong.keys)
    stimuliRuleALoop.addData('block2wrong.corr', block2wrong.corr)
    if block2wrong.keys != None:  # we had a response
        stimuliRuleALoop.addData('block2wrong.rt', block2wrong.rt)
    
    # the Routine "practiceTrialsRuleA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'stimuliRuleALoop'


# set up handler to look after randomisation of conditions etc
inst3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection='2'),
    seed=None, name='inst3')
thisExp.addLoop(inst3)  # add the loop to the experiment
thisInst3 = inst3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInst3.rgb)
if thisInst3 != None:
    for paramName in thisInst3.keys():
        exec(paramName + '= thisInst3.' + paramName)

for thisInst3 in inst3:
    currentLoop = inst3
    # abbreviate parameter names if possible (e.g. rgb = thisInst3.rgb)
    if thisInst3 != None:
        for paramName in thisInst3.keys():
            exec(paramName + '= thisInst3.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setText(instructions
)
    instructionsKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructionsKey.status = NOT_STARTED
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(instructionsKey)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 0.75 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *instructionsKey* updates
        if t >= 1.25 and instructionsKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsKey.tStart = t  # underestimates by a little under one frame
            instructionsKey.frameNStart = frameN  # exact frame index
            instructionsKey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructionsKey.status == STARTED:
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
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'inst3'


# set up handler to look after randomisation of conditions etc
inducersAndStimuliRuleALoop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimuli.xlsx'),
    seed=None, name='inducersAndStimuliRuleALoop')
thisExp.addLoop(inducersAndStimuliRuleALoop)  # add the loop to the experiment
thisInducersAndstimulusRuleALoop = inducersAndStimuliRuleALoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInducersAndstimulusRuleALoop.rgb)
if thisInducersAndstimulusRuleALoop != None:
    for paramName in thisInducersAndstimulusRuleALoop.keys():
        exec(paramName + '= thisInducersAndstimulusRuleALoop.' + paramName)

for thisInducersAndstimulusRuleALoop in inducersAndStimuliRuleALoop:
    currentLoop = inducersAndStimuliRuleALoop
    # abbreviate parameter names if possible (e.g. rgb = thisInducersAndstimulusRuleALoop.rgb)
    if thisInducersAndstimulusRuleALoop != None:
        for paramName in thisInducersAndstimulusRuleALoop.keys():
            exec(paramName + '= thisInducersAndstimulusRuleALoop.' + paramName)
    
    #------Prepare to start Routine "trialsRuleA"-------
    t = 0
    trialsRuleAClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBoxA.setColor(stimulusColour, colorSpace='rgb')
    stimulusBoxA.setText(stimulus)
    block3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block3.status = NOT_STARTED
    block3wrong = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block3wrong.status = NOT_STARTED
    
    trueBoxA.setText(trueLabel)
    falseBoxA.setText(falseLabel)
    # keep track of which components have finished
    trialsRuleAComponents = []
    trialsRuleAComponents.append(stimulusBoxA)
    trialsRuleAComponents.append(block3)
    trialsRuleAComponents.append(block3wrong)
    trialsRuleAComponents.append(correctiveFeedbackA)
    trialsRuleAComponents.append(trueBoxA)
    trialsRuleAComponents.append(falseBoxA)
    for thisComponent in trialsRuleAComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trialsRuleA"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialsRuleAClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusBoxA* updates
        if t >= 0.75 and stimulusBoxA.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusBoxA.tStart = t  # underestimates by a little under one frame
            stimulusBoxA.frameNStart = frameN  # exact frame index
            stimulusBoxA.setAutoDraw(True)
        
        # *block3* updates
        if t >= 0.75 and block3.status == NOT_STARTED:
            # keep track of start time/frame for later
            block3.tStart = t  # underestimates by a little under one frame
            block3.frameNStart = frameN  # exact frame index
            block3.status = STARTED
            # AllowedKeys looks like a variable named `requiredAllowedKeysA`
            if not 'requiredAllowedKeysA' in locals():
                logging.error('AllowedKeys variable `requiredAllowedKeysA` is not defined.')
                core.quit()
            if not type(requiredAllowedKeysA) in [list, tuple, np.ndarray]:
                if not isinstance(requiredAllowedKeysA, basestring):
                    logging.error('AllowedKeys variable `requiredAllowedKeysA` is not string- or list-like.')
                    core.quit()
                elif not ',' in requiredAllowedKeysA: requiredAllowedKeysA = (requiredAllowedKeysA,)
                else:  requiredAllowedKeysA = eval(requiredAllowedKeysA)
            # keyboard checking is just starting
            block3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if block3.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block3.keys == []:  # then this was the first keypress
                    block3.keys = theseKeys[0]  # just the first key pressed
                    block3.rt = block3.clock.getTime()
                    # was this 'correct'?
                    if (block3.keys == str(requiredResponseA)) or (block3.keys == requiredResponseA):
                        block3.corr = 1
                    else:
                        block3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *block3wrong* updates
        if t >= 0.75 and block3wrong.status == NOT_STARTED:
            # keep track of start time/frame for later
            block3wrong.tStart = t  # underestimates by a little under one frame
            block3wrong.frameNStart = frameN  # exact frame index
            block3wrong.status = STARTED
            # AllowedKeys looks like a variable named `feedbackAllowedKeysA`
            if not 'feedbackAllowedKeysA' in locals():
                logging.error('AllowedKeys variable `feedbackAllowedKeysA` is not defined.')
                core.quit()
            if not type(feedbackAllowedKeysA) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackAllowedKeysA, basestring):
                    logging.error('AllowedKeys variable `feedbackAllowedKeysA` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackAllowedKeysA: feedbackAllowedKeysA = (feedbackAllowedKeysA,)
                else:  feedbackAllowedKeysA = eval(feedbackAllowedKeysA)
            # keyboard checking is just starting
            block3wrong.clock.reset()  # now t=0
        if block3wrong.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block3wrong.keys == []:  # then this was the first keypress
                    block3wrong.keys = theseKeys[0]  # just the first key pressed
                    block3wrong.rt = block3wrong.clock.getTime()
                    # was this 'correct'?
                    if (block3wrong.keys == str(feedbackResponseA)) or (block3wrong.keys == feedbackResponseA):
                        block3wrong.corr = 1
                    else:
                        block3wrong.corr = 0
        
        # *correctiveFeedbackA* updates
        if t >= 0.75 and correctiveFeedbackA.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackA.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackA.frameNStart = frameN  # exact frame index
            correctiveFeedbackA.setAutoDraw(True)
        if correctiveFeedbackA.status == STARTED:  # only update if being drawn
            correctiveFeedbackA.setText(msg, log=False)
        if len(block3wrong.keys)<1:
            msg=""
        else:
            msg="X"
        
        # *trueBoxA* updates
        if t >= 0 and trueBoxA.status == NOT_STARTED:
            # keep track of start time/frame for later
            trueBoxA.tStart = t  # underestimates by a little under one frame
            trueBoxA.frameNStart = frameN  # exact frame index
            trueBoxA.setAutoDraw(True)
        
        # *falseBoxA* updates
        if t >= 0 and falseBoxA.status == NOT_STARTED:
            # keep track of start time/frame for later
            falseBoxA.tStart = t  # underestimates by a little under one frame
            falseBoxA.frameNStart = frameN  # exact frame index
            falseBoxA.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsRuleAComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trialsRuleA"-------
    for thisComponent in trialsRuleAComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if block3.keys in ['', [], None]:  # No response was made
       block3.keys=None
       # was no response the correct answer?!
       if str(requiredResponseA).lower() == 'none': block3.corr = 1  # correct non-response
       else: block3.corr = 0  # failed to respond (incorrectly)
    # store data for inducersAndStimuliRuleALoop (TrialHandler)
    inducersAndStimuliRuleALoop.addData('block3.keys',block3.keys)
    inducersAndStimuliRuleALoop.addData('block3.corr', block3.corr)
    if block3.keys != None:  # we had a response
        inducersAndStimuliRuleALoop.addData('block3.rt', block3.rt)
    # check responses
    if block3wrong.keys in ['', [], None]:  # No response was made
       block3wrong.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseA).lower() == 'none': block3wrong.corr = 1  # correct non-response
       else: block3wrong.corr = 0  # failed to respond (incorrectly)
    # store data for inducersAndStimuliRuleALoop (TrialHandler)
    inducersAndStimuliRuleALoop.addData('block3wrong.keys',block3wrong.keys)
    inducersAndStimuliRuleALoop.addData('block3wrong.corr', block3wrong.corr)
    if block3wrong.keys != None:  # we had a response
        inducersAndStimuliRuleALoop.addData('block3wrong.rt', block3wrong.rt)
    
    # the Routine "trialsRuleA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'inducersAndStimuliRuleALoop'


# set up handler to look after randomisation of conditions etc
inst4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection='3'),
    seed=None, name='inst4')
thisExp.addLoop(inst4)  # add the loop to the experiment
thisInst4 = inst4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInst4.rgb)
if thisInst4 != None:
    for paramName in thisInst4.keys():
        exec(paramName + '= thisInst4.' + paramName)

for thisInst4 in inst4:
    currentLoop = inst4
    # abbreviate parameter names if possible (e.g. rgb = thisInst4.rgb)
    if thisInst4 != None:
        for paramName in thisInst4.keys():
            exec(paramName + '= thisInst4.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setText(instructions
)
    instructionsKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructionsKey.status = NOT_STARTED
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(instructionsKey)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 0.75 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *instructionsKey* updates
        if t >= 1.25 and instructionsKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsKey.tStart = t  # underestimates by a little under one frame
            instructionsKey.frameNStart = frameN  # exact frame index
            instructionsKey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructionsKey.status == STARTED:
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
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'inst4'


# set up handler to look after randomisation of conditions etc
stimuliRuleBLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimuli.xlsx', selection='10:30'),
    seed=None, name='stimuliRuleBLoop')
thisExp.addLoop(stimuliRuleBLoop)  # add the loop to the experiment
thisStimulusRuleBLoop = stimuliRuleBLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisStimulusRuleBLoop.rgb)
if thisStimulusRuleBLoop != None:
    for paramName in thisStimulusRuleBLoop.keys():
        exec(paramName + '= thisStimulusRuleBLoop.' + paramName)

for thisStimulusRuleBLoop in stimuliRuleBLoop:
    currentLoop = stimuliRuleBLoop
    # abbreviate parameter names if possible (e.g. rgb = thisStimulusRuleBLoop.rgb)
    if thisStimulusRuleBLoop != None:
        for paramName in thisStimulusRuleBLoop.keys():
            exec(paramName + '= thisStimulusRuleBLoop.' + paramName)
    
    #------Prepare to start Routine "practiceTrialsRuleB"-------
    t = 0
    practiceTrialsRuleBClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBoxBprac.setColor(stimulusColour, colorSpace='rgb')
    stimulusBoxBprac.setText(stimulus)
    block4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block4.status = NOT_STARTED
    block4wrong = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block4wrong.status = NOT_STARTED
    
    trueBoxBprac.setText(trueLabel)
    falseBoxBprac.setText(falseLabel)
    # keep track of which components have finished
    practiceTrialsRuleBComponents = []
    practiceTrialsRuleBComponents.append(stimulusBoxBprac)
    practiceTrialsRuleBComponents.append(block4)
    practiceTrialsRuleBComponents.append(block4wrong)
    practiceTrialsRuleBComponents.append(correctiveFeedbackBprac)
    practiceTrialsRuleBComponents.append(trueBoxBprac)
    practiceTrialsRuleBComponents.append(falseBoxBprac)
    for thisComponent in practiceTrialsRuleBComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practiceTrialsRuleB"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = practiceTrialsRuleBClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusBoxBprac* updates
        if t >= 0.75 and stimulusBoxBprac.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusBoxBprac.tStart = t  # underestimates by a little under one frame
            stimulusBoxBprac.frameNStart = frameN  # exact frame index
            stimulusBoxBprac.setAutoDraw(True)
        
        # *block4* updates
        if t >= 0.75 and block4.status == NOT_STARTED:
            # keep track of start time/frame for later
            block4.tStart = t  # underestimates by a little under one frame
            block4.frameNStart = frameN  # exact frame index
            block4.status = STARTED
            # AllowedKeys looks like a variable named `requiredAllowedKeysB`
            if not 'requiredAllowedKeysB' in locals():
                logging.error('AllowedKeys variable `requiredAllowedKeysB` is not defined.')
                core.quit()
            if not type(requiredAllowedKeysB) in [list, tuple, np.ndarray]:
                if not isinstance(requiredAllowedKeysB, basestring):
                    logging.error('AllowedKeys variable `requiredAllowedKeysB` is not string- or list-like.')
                    core.quit()
                elif not ',' in requiredAllowedKeysB: requiredAllowedKeysB = (requiredAllowedKeysB,)
                else:  requiredAllowedKeysB = eval(requiredAllowedKeysB)
            # keyboard checking is just starting
            block4.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if block4.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysB))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block4.keys == []:  # then this was the first keypress
                    block4.keys = theseKeys[0]  # just the first key pressed
                    block4.rt = block4.clock.getTime()
                    # was this 'correct'?
                    if (block4.keys == str(requiredResponseB)) or (block4.keys == requiredResponseB):
                        block4.corr = 1
                    else:
                        block4.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *block4wrong* updates
        if t >= 0.75 and block4wrong.status == NOT_STARTED:
            # keep track of start time/frame for later
            block4wrong.tStart = t  # underestimates by a little under one frame
            block4wrong.frameNStart = frameN  # exact frame index
            block4wrong.status = STARTED
            # AllowedKeys looks like a variable named `feedbackAllowedKeysB`
            if not 'feedbackAllowedKeysB' in locals():
                logging.error('AllowedKeys variable `feedbackAllowedKeysB` is not defined.')
                core.quit()
            if not type(feedbackAllowedKeysB) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackAllowedKeysB, basestring):
                    logging.error('AllowedKeys variable `feedbackAllowedKeysB` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackAllowedKeysB: feedbackAllowedKeysB = (feedbackAllowedKeysB,)
                else:  feedbackAllowedKeysB = eval(feedbackAllowedKeysB)
            # keyboard checking is just starting
            block4wrong.clock.reset()  # now t=0
        if block4wrong.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysB))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block4wrong.keys == []:  # then this was the first keypress
                    block4wrong.keys = theseKeys[0]  # just the first key pressed
                    block4wrong.rt = block4wrong.clock.getTime()
                    # was this 'correct'?
                    if (block4wrong.keys == str(feedbackResponseB)) or (block4wrong.keys == feedbackResponseB):
                        block4wrong.corr = 1
                    else:
                        block4wrong.corr = 0
        
        # *correctiveFeedbackBprac* updates
        if t >= 0.75 and correctiveFeedbackBprac.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackBprac.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackBprac.frameNStart = frameN  # exact frame index
            correctiveFeedbackBprac.setAutoDraw(True)
        if correctiveFeedbackBprac.status == STARTED:  # only update if being drawn
            correctiveFeedbackBprac.setText(msg, log=False)
        if len(block4wrong.keys)<1:
            msg=""
        else:
            msg="X"
        
        # *trueBoxBprac* updates
        if t >= 0 and trueBoxBprac.status == NOT_STARTED:
            # keep track of start time/frame for later
            trueBoxBprac.tStart = t  # underestimates by a little under one frame
            trueBoxBprac.frameNStart = frameN  # exact frame index
            trueBoxBprac.setAutoDraw(True)
        
        # *falseBoxBprac* updates
        if t >= 0 and falseBoxBprac.status == NOT_STARTED:
            # keep track of start time/frame for later
            falseBoxBprac.tStart = t  # underestimates by a little under one frame
            falseBoxBprac.frameNStart = frameN  # exact frame index
            falseBoxBprac.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceTrialsRuleBComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "practiceTrialsRuleB"-------
    for thisComponent in practiceTrialsRuleBComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if block4.keys in ['', [], None]:  # No response was made
       block4.keys=None
       # was no response the correct answer?!
       if str(requiredResponseB).lower() == 'none': block4.corr = 1  # correct non-response
       else: block4.corr = 0  # failed to respond (incorrectly)
    # store data for stimuliRuleBLoop (TrialHandler)
    stimuliRuleBLoop.addData('block4.keys',block4.keys)
    stimuliRuleBLoop.addData('block4.corr', block4.corr)
    if block4.keys != None:  # we had a response
        stimuliRuleBLoop.addData('block4.rt', block4.rt)
    # check responses
    if block4wrong.keys in ['', [], None]:  # No response was made
       block4wrong.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseB).lower() == 'none': block4wrong.corr = 1  # correct non-response
       else: block4wrong.corr = 0  # failed to respond (incorrectly)
    # store data for stimuliRuleBLoop (TrialHandler)
    stimuliRuleBLoop.addData('block4wrong.keys',block4wrong.keys)
    stimuliRuleBLoop.addData('block4wrong.corr', block4wrong.corr)
    if block4wrong.keys != None:  # we had a response
        stimuliRuleBLoop.addData('block4wrong.rt', block4wrong.rt)
    
    # the Routine "practiceTrialsRuleB" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'stimuliRuleBLoop'


# set up handler to look after randomisation of conditions etc
inst5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection='4'),
    seed=None, name='inst5')
thisExp.addLoop(inst5)  # add the loop to the experiment
thisInst5 = inst5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInst5.rgb)
if thisInst5 != None:
    for paramName in thisInst5.keys():
        exec(paramName + '= thisInst5.' + paramName)

for thisInst5 in inst5:
    currentLoop = inst5
    # abbreviate parameter names if possible (e.g. rgb = thisInst5.rgb)
    if thisInst5 != None:
        for paramName in thisInst5.keys():
            exec(paramName + '= thisInst5.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setText(instructions
)
    instructionsKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructionsKey.status = NOT_STARTED
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(instructionsKey)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 0.75 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *instructionsKey* updates
        if t >= 1.25 and instructionsKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsKey.tStart = t  # underestimates by a little under one frame
            instructionsKey.frameNStart = frameN  # exact frame index
            instructionsKey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructionsKey.status == STARTED:
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
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'inst5'


# set up handler to look after randomisation of conditions etc
inducersAndStimuliRuleBLoop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimuli.xlsx'),
    seed=None, name='inducersAndStimuliRuleBLoop')
thisExp.addLoop(inducersAndStimuliRuleBLoop)  # add the loop to the experiment
thisInducersAndstimulusRuleBLoop = inducersAndStimuliRuleBLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInducersAndstimulusRuleBLoop.rgb)
if thisInducersAndstimulusRuleBLoop != None:
    for paramName in thisInducersAndstimulusRuleBLoop.keys():
        exec(paramName + '= thisInducersAndstimulusRuleBLoop.' + paramName)

for thisInducersAndstimulusRuleBLoop in inducersAndStimuliRuleBLoop:
    currentLoop = inducersAndStimuliRuleBLoop
    # abbreviate parameter names if possible (e.g. rgb = thisInducersAndstimulusRuleBLoop.rgb)
    if thisInducersAndstimulusRuleBLoop != None:
        for paramName in thisInducersAndstimulusRuleBLoop.keys():
            exec(paramName + '= thisInducersAndstimulusRuleBLoop.' + paramName)
    
    #------Prepare to start Routine "trialsRuleB"-------
    t = 0
    trialsRuleBClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBoxB.setColor(stimulusColour, colorSpace='rgb')
    stimulusBoxB.setText(stimulus)
    block5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block5.status = NOT_STARTED
    block5wrong = event.BuilderKeyResponse()  # create an object of type KeyResponse
    block5wrong.status = NOT_STARTED
    
    trueBoxB.setText(trueLabel)
    falseBoxB.setText(falseLabel)
    # keep track of which components have finished
    trialsRuleBComponents = []
    trialsRuleBComponents.append(stimulusBoxB)
    trialsRuleBComponents.append(block5)
    trialsRuleBComponents.append(block5wrong)
    trialsRuleBComponents.append(correctiveFeedbackB)
    trialsRuleBComponents.append(trueBoxB)
    trialsRuleBComponents.append(falseBoxB)
    for thisComponent in trialsRuleBComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trialsRuleB"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialsRuleBClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusBoxB* updates
        if t >= 0.75 and stimulusBoxB.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusBoxB.tStart = t  # underestimates by a little under one frame
            stimulusBoxB.frameNStart = frameN  # exact frame index
            stimulusBoxB.setAutoDraw(True)
        
        # *block5* updates
        if t >= 0.75 and block5.status == NOT_STARTED:
            # keep track of start time/frame for later
            block5.tStart = t  # underestimates by a little under one frame
            block5.frameNStart = frameN  # exact frame index
            block5.status = STARTED
            # AllowedKeys looks like a variable named `requiredAllowedKeysB`
            if not 'requiredAllowedKeysB' in locals():
                logging.error('AllowedKeys variable `requiredAllowedKeysB` is not defined.')
                core.quit()
            if not type(requiredAllowedKeysB) in [list, tuple, np.ndarray]:
                if not isinstance(requiredAllowedKeysB, basestring):
                    logging.error('AllowedKeys variable `requiredAllowedKeysB` is not string- or list-like.')
                    core.quit()
                elif not ',' in requiredAllowedKeysB: requiredAllowedKeysB = (requiredAllowedKeysB,)
                else:  requiredAllowedKeysB = eval(requiredAllowedKeysB)
            # keyboard checking is just starting
            block5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if block5.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysB))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block5.keys == []:  # then this was the first keypress
                    block5.keys = theseKeys[0]  # just the first key pressed
                    block5.rt = block5.clock.getTime()
                    # was this 'correct'?
                    if (block5.keys == str(requiredResponseB)) or (block5.keys == requiredResponseB):
                        block5.corr = 1
                    else:
                        block5.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *block5wrong* updates
        if t >= 0.75 and block5wrong.status == NOT_STARTED:
            # keep track of start time/frame for later
            block5wrong.tStart = t  # underestimates by a little under one frame
            block5wrong.frameNStart = frameN  # exact frame index
            block5wrong.status = STARTED
            # AllowedKeys looks like a variable named `feedbackAllowedKeysB`
            if not 'feedbackAllowedKeysB' in locals():
                logging.error('AllowedKeys variable `feedbackAllowedKeysB` is not defined.')
                core.quit()
            if not type(feedbackAllowedKeysB) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackAllowedKeysB, basestring):
                    logging.error('AllowedKeys variable `feedbackAllowedKeysB` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackAllowedKeysB: feedbackAllowedKeysB = (feedbackAllowedKeysB,)
                else:  feedbackAllowedKeysB = eval(feedbackAllowedKeysB)
            # keyboard checking is just starting
            block5wrong.clock.reset()  # now t=0
        if block5wrong.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysB))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if block5wrong.keys == []:  # then this was the first keypress
                    block5wrong.keys = theseKeys[0]  # just the first key pressed
                    block5wrong.rt = block5wrong.clock.getTime()
                    # was this 'correct'?
                    if (block5wrong.keys == str(feedbackResponseB)) or (block5wrong.keys == feedbackResponseB):
                        block5wrong.corr = 1
                    else:
                        block5wrong.corr = 0
        
        # *correctiveFeedbackB* updates
        if t >= 0.75 and correctiveFeedbackB.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackB.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackB.frameNStart = frameN  # exact frame index
            correctiveFeedbackB.setAutoDraw(True)
        if correctiveFeedbackB.status == STARTED:  # only update if being drawn
            correctiveFeedbackB.setText(msg, log=False)
        if len(block5wrong.keys)<1:
            msg=""
        else:
            msg="X"
        
        # *trueBoxB* updates
        if t >= 0 and trueBoxB.status == NOT_STARTED:
            # keep track of start time/frame for later
            trueBoxB.tStart = t  # underestimates by a little under one frame
            trueBoxB.frameNStart = frameN  # exact frame index
            trueBoxB.setAutoDraw(True)
        
        # *falseBoxB* updates
        if t >= 0 and falseBoxB.status == NOT_STARTED:
            # keep track of start time/frame for later
            falseBoxB.tStart = t  # underestimates by a little under one frame
            falseBoxB.frameNStart = frameN  # exact frame index
            falseBoxB.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsRuleBComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trialsRuleB"-------
    for thisComponent in trialsRuleBComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if block5.keys in ['', [], None]:  # No response was made
       block5.keys=None
       # was no response the correct answer?!
       if str(requiredResponseB).lower() == 'none': block5.corr = 1  # correct non-response
       else: block5.corr = 0  # failed to respond (incorrectly)
    # store data for inducersAndStimuliRuleBLoop (TrialHandler)
    inducersAndStimuliRuleBLoop.addData('block5.keys',block5.keys)
    inducersAndStimuliRuleBLoop.addData('block5.corr', block5.corr)
    if block5.keys != None:  # we had a response
        inducersAndStimuliRuleBLoop.addData('block5.rt', block5.rt)
    # check responses
    if block5wrong.keys in ['', [], None]:  # No response was made
       block5wrong.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseB).lower() == 'none': block5wrong.corr = 1  # correct non-response
       else: block5wrong.corr = 0  # failed to respond (incorrectly)
    # store data for inducersAndStimuliRuleBLoop (TrialHandler)
    inducersAndStimuliRuleBLoop.addData('block5wrong.keys',block5wrong.keys)
    inducersAndStimuliRuleBLoop.addData('block5wrong.corr', block5wrong.corr)
    if block5wrong.keys != None:  # we had a response
        inducersAndStimuliRuleBLoop.addData('block5wrong.rt', block5wrong.rt)
    
    # the Routine "trialsRuleB" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'inducersAndStimuliRuleBLoop'


# set up handler to look after randomisation of conditions etc
instEnd = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection='5'),
    seed=None, name='instEnd')
thisExp.addLoop(instEnd)  # add the loop to the experiment
thisInstEnd = instEnd.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstEnd.rgb)
if thisInstEnd != None:
    for paramName in thisInstEnd.keys():
        exec(paramName + '= thisInstEnd.' + paramName)

for thisInstEnd in instEnd:
    currentLoop = instEnd
    # abbreviate parameter names if possible (e.g. rgb = thisInstEnd.rgb)
    if thisInstEnd != None:
        for paramName in thisInstEnd.keys():
            exec(paramName + '= thisInstEnd.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setText(instructions
)
    instructionsKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructionsKey.status = NOT_STARTED
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(instructionsKey)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 0.75 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *instructionsKey* updates
        if t >= 1.25 and instructionsKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsKey.tStart = t  # underestimates by a little under one frame
            instructionsKey.frameNStart = frameN  # exact frame index
            instructionsKey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructionsKey.status == STARTED:
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
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instEnd'






win.close()
core.quit()
