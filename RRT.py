#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Tue Oct 27 15:27:17 2015
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
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
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
    text='True',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxA = visual.TextStim(win=win, ori=0, name='falseBoxA',
    text='False',    font='Arial',
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
    text='True',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxA = visual.TextStim(win=win, ori=0, name='falseBoxA',
    text='False',    font='Arial',
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
    text='True',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxA = visual.TextStim(win=win, ori=0, name='falseBoxA',
    text='False',    font='Arial',
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
    text='True',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxB = visual.TextStim(win=win, ori=0, name='falseBoxB',
    text='False',    font='Arial',
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
    text='True',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseBoxB = visual.TextStim(win=win, ori=0, name='falseBoxB',
    text='False',    font='Arial',
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
    trialList=data.importConditions('instructions.xlsx', selection=u'0'),
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
    trialList=data.importConditions('stimuli.xlsx', selection=u'0:10'),
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
    
    #------Prepare to start Routine "trialsRuleA"-------
    t = 0
    trialsRuleAClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBoxA.setColor(stimulusColour, colorSpace='rgb')
    stimulusBoxA.setText(stimulus)
    requiredResponseKeyA = event.BuilderKeyResponse()  # create an object of type KeyResponse
    requiredResponseKeyA.status = NOT_STARTED
    feedbackResponseKeyA = event.BuilderKeyResponse()  # create an object of type KeyResponse
    feedbackResponseKeyA.status = NOT_STARTED
    
    # keep track of which components have finished
    trialsRuleAComponents = []
    trialsRuleAComponents.append(stimulusBoxA)
    trialsRuleAComponents.append(requiredResponseKeyA)
    trialsRuleAComponents.append(feedbackResponseKeyA)
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
        
        # *requiredResponseKeyA* updates
        if t >= 0.75 and requiredResponseKeyA.status == NOT_STARTED:
            # keep track of start time/frame for later
            requiredResponseKeyA.tStart = t  # underestimates by a little under one frame
            requiredResponseKeyA.frameNStart = frameN  # exact frame index
            requiredResponseKeyA.status = STARTED
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
            requiredResponseKeyA.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if requiredResponseKeyA.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if requiredResponseKeyA.keys == []:  # then this was the first keypress
                    requiredResponseKeyA.keys = theseKeys[0]  # just the first key pressed
                    requiredResponseKeyA.rt = requiredResponseKeyA.clock.getTime()
                    # was this 'correct'?
                    if (requiredResponseKeyA.keys == str(requiredResponseA)) or (requiredResponseKeyA.keys == requiredResponseA):
                        requiredResponseKeyA.corr = 1
                    else:
                        requiredResponseKeyA.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *feedbackResponseKeyA* updates
        if t >= 0.75 and feedbackResponseKeyA.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackResponseKeyA.tStart = t  # underestimates by a little under one frame
            feedbackResponseKeyA.frameNStart = frameN  # exact frame index
            feedbackResponseKeyA.status = STARTED
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
            feedbackResponseKeyA.clock.reset()  # now t=0
        if feedbackResponseKeyA.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if feedbackResponseKeyA.keys == []:  # then this was the first keypress
                    feedbackResponseKeyA.keys = theseKeys[0]  # just the first key pressed
                    feedbackResponseKeyA.rt = feedbackResponseKeyA.clock.getTime()
                    # was this 'correct'?
                    if (feedbackResponseKeyA.keys == str(feedbackResponseA)) or (feedbackResponseKeyA.keys == feedbackResponseA):
                        feedbackResponseKeyA.corr = 1
                    else:
                        feedbackResponseKeyA.corr = 0
        
        # *correctiveFeedbackA* updates
        if t >= 0.75 and correctiveFeedbackA.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackA.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackA.frameNStart = frameN  # exact frame index
            correctiveFeedbackA.setAutoDraw(True)
        if correctiveFeedbackA.status == STARTED:  # only update if being drawn
            correctiveFeedbackA.setText(msg, log=False)
        if len(feedbackResponseKeyA.keys)<1:
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
    if requiredResponseKeyA.keys in ['', [], None]:  # No response was made
       requiredResponseKeyA.keys=None
       # was no response the correct answer?!
       if str(requiredResponseA).lower() == 'none': requiredResponseKeyA.corr = 1  # correct non-response
       else: requiredResponseKeyA.corr = 0  # failed to respond (incorrectly)
    # store data for inducersLoop (TrialHandler)
    inducersLoop.addData('requiredResponseKeyA.keys',requiredResponseKeyA.keys)
    inducersLoop.addData('requiredResponseKeyA.corr', requiredResponseKeyA.corr)
    if requiredResponseKeyA.keys != None:  # we had a response
        inducersLoop.addData('requiredResponseKeyA.rt', requiredResponseKeyA.rt)
    # check responses
    if feedbackResponseKeyA.keys in ['', [], None]:  # No response was made
       feedbackResponseKeyA.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseA).lower() == 'none': feedbackResponseKeyA.corr = 1  # correct non-response
       else: feedbackResponseKeyA.corr = 0  # failed to respond (incorrectly)
    # store data for inducersLoop (TrialHandler)
    inducersLoop.addData('feedbackResponseKeyA.keys',feedbackResponseKeyA.keys)
    inducersLoop.addData('feedbackResponseKeyA.corr', feedbackResponseKeyA.corr)
    if feedbackResponseKeyA.keys != None:  # we had a response
        inducersLoop.addData('feedbackResponseKeyA.rt', feedbackResponseKeyA.rt)
    
    # the Routine "trialsRuleA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'inducersLoop'


# set up handler to look after randomisation of conditions etc
inst2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection=u'1'),
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
    trialList=data.importConditions('stimuli.xlsx', selection=u'10:30'),
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
    
    #------Prepare to start Routine "trialsRuleA"-------
    t = 0
    trialsRuleAClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBoxA.setColor(stimulusColour, colorSpace='rgb')
    stimulusBoxA.setText(stimulus)
    requiredResponseKeyA = event.BuilderKeyResponse()  # create an object of type KeyResponse
    requiredResponseKeyA.status = NOT_STARTED
    feedbackResponseKeyA = event.BuilderKeyResponse()  # create an object of type KeyResponse
    feedbackResponseKeyA.status = NOT_STARTED
    
    # keep track of which components have finished
    trialsRuleAComponents = []
    trialsRuleAComponents.append(stimulusBoxA)
    trialsRuleAComponents.append(requiredResponseKeyA)
    trialsRuleAComponents.append(feedbackResponseKeyA)
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
        
        # *requiredResponseKeyA* updates
        if t >= 0.75 and requiredResponseKeyA.status == NOT_STARTED:
            # keep track of start time/frame for later
            requiredResponseKeyA.tStart = t  # underestimates by a little under one frame
            requiredResponseKeyA.frameNStart = frameN  # exact frame index
            requiredResponseKeyA.status = STARTED
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
            requiredResponseKeyA.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if requiredResponseKeyA.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if requiredResponseKeyA.keys == []:  # then this was the first keypress
                    requiredResponseKeyA.keys = theseKeys[0]  # just the first key pressed
                    requiredResponseKeyA.rt = requiredResponseKeyA.clock.getTime()
                    # was this 'correct'?
                    if (requiredResponseKeyA.keys == str(requiredResponseA)) or (requiredResponseKeyA.keys == requiredResponseA):
                        requiredResponseKeyA.corr = 1
                    else:
                        requiredResponseKeyA.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *feedbackResponseKeyA* updates
        if t >= 0.75 and feedbackResponseKeyA.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackResponseKeyA.tStart = t  # underestimates by a little under one frame
            feedbackResponseKeyA.frameNStart = frameN  # exact frame index
            feedbackResponseKeyA.status = STARTED
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
            feedbackResponseKeyA.clock.reset()  # now t=0
        if feedbackResponseKeyA.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if feedbackResponseKeyA.keys == []:  # then this was the first keypress
                    feedbackResponseKeyA.keys = theseKeys[0]  # just the first key pressed
                    feedbackResponseKeyA.rt = feedbackResponseKeyA.clock.getTime()
                    # was this 'correct'?
                    if (feedbackResponseKeyA.keys == str(feedbackResponseA)) or (feedbackResponseKeyA.keys == feedbackResponseA):
                        feedbackResponseKeyA.corr = 1
                    else:
                        feedbackResponseKeyA.corr = 0
        
        # *correctiveFeedbackA* updates
        if t >= 0.75 and correctiveFeedbackA.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackA.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackA.frameNStart = frameN  # exact frame index
            correctiveFeedbackA.setAutoDraw(True)
        if correctiveFeedbackA.status == STARTED:  # only update if being drawn
            correctiveFeedbackA.setText(msg, log=False)
        if len(feedbackResponseKeyA.keys)<1:
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
    if requiredResponseKeyA.keys in ['', [], None]:  # No response was made
       requiredResponseKeyA.keys=None
       # was no response the correct answer?!
       if str(requiredResponseA).lower() == 'none': requiredResponseKeyA.corr = 1  # correct non-response
       else: requiredResponseKeyA.corr = 0  # failed to respond (incorrectly)
    # store data for stimuliRuleALoop (TrialHandler)
    stimuliRuleALoop.addData('requiredResponseKeyA.keys',requiredResponseKeyA.keys)
    stimuliRuleALoop.addData('requiredResponseKeyA.corr', requiredResponseKeyA.corr)
    if requiredResponseKeyA.keys != None:  # we had a response
        stimuliRuleALoop.addData('requiredResponseKeyA.rt', requiredResponseKeyA.rt)
    # check responses
    if feedbackResponseKeyA.keys in ['', [], None]:  # No response was made
       feedbackResponseKeyA.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseA).lower() == 'none': feedbackResponseKeyA.corr = 1  # correct non-response
       else: feedbackResponseKeyA.corr = 0  # failed to respond (incorrectly)
    # store data for stimuliRuleALoop (TrialHandler)
    stimuliRuleALoop.addData('feedbackResponseKeyA.keys',feedbackResponseKeyA.keys)
    stimuliRuleALoop.addData('feedbackResponseKeyA.corr', feedbackResponseKeyA.corr)
    if feedbackResponseKeyA.keys != None:  # we had a response
        stimuliRuleALoop.addData('feedbackResponseKeyA.rt', feedbackResponseKeyA.rt)
    
    # the Routine "trialsRuleA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'stimuliRuleALoop'


# set up handler to look after randomisation of conditions etc
inst3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection=u'2'),
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
    requiredResponseKeyA = event.BuilderKeyResponse()  # create an object of type KeyResponse
    requiredResponseKeyA.status = NOT_STARTED
    feedbackResponseKeyA = event.BuilderKeyResponse()  # create an object of type KeyResponse
    feedbackResponseKeyA.status = NOT_STARTED
    
    # keep track of which components have finished
    trialsRuleAComponents = []
    trialsRuleAComponents.append(stimulusBoxA)
    trialsRuleAComponents.append(requiredResponseKeyA)
    trialsRuleAComponents.append(feedbackResponseKeyA)
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
        
        # *requiredResponseKeyA* updates
        if t >= 0.75 and requiredResponseKeyA.status == NOT_STARTED:
            # keep track of start time/frame for later
            requiredResponseKeyA.tStart = t  # underestimates by a little under one frame
            requiredResponseKeyA.frameNStart = frameN  # exact frame index
            requiredResponseKeyA.status = STARTED
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
            requiredResponseKeyA.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if requiredResponseKeyA.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if requiredResponseKeyA.keys == []:  # then this was the first keypress
                    requiredResponseKeyA.keys = theseKeys[0]  # just the first key pressed
                    requiredResponseKeyA.rt = requiredResponseKeyA.clock.getTime()
                    # was this 'correct'?
                    if (requiredResponseKeyA.keys == str(requiredResponseA)) or (requiredResponseKeyA.keys == requiredResponseA):
                        requiredResponseKeyA.corr = 1
                    else:
                        requiredResponseKeyA.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *feedbackResponseKeyA* updates
        if t >= 0.75 and feedbackResponseKeyA.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackResponseKeyA.tStart = t  # underestimates by a little under one frame
            feedbackResponseKeyA.frameNStart = frameN  # exact frame index
            feedbackResponseKeyA.status = STARTED
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
            feedbackResponseKeyA.clock.reset()  # now t=0
        if feedbackResponseKeyA.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysA))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if feedbackResponseKeyA.keys == []:  # then this was the first keypress
                    feedbackResponseKeyA.keys = theseKeys[0]  # just the first key pressed
                    feedbackResponseKeyA.rt = feedbackResponseKeyA.clock.getTime()
                    # was this 'correct'?
                    if (feedbackResponseKeyA.keys == str(feedbackResponseA)) or (feedbackResponseKeyA.keys == feedbackResponseA):
                        feedbackResponseKeyA.corr = 1
                    else:
                        feedbackResponseKeyA.corr = 0
        
        # *correctiveFeedbackA* updates
        if t >= 0.75 and correctiveFeedbackA.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackA.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackA.frameNStart = frameN  # exact frame index
            correctiveFeedbackA.setAutoDraw(True)
        if correctiveFeedbackA.status == STARTED:  # only update if being drawn
            correctiveFeedbackA.setText(msg, log=False)
        if len(feedbackResponseKeyA.keys)<1:
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
    if requiredResponseKeyA.keys in ['', [], None]:  # No response was made
       requiredResponseKeyA.keys=None
       # was no response the correct answer?!
       if str(requiredResponseA).lower() == 'none': requiredResponseKeyA.corr = 1  # correct non-response
       else: requiredResponseKeyA.corr = 0  # failed to respond (incorrectly)
    # store data for inducersAndStimuliRuleALoop (TrialHandler)
    inducersAndStimuliRuleALoop.addData('requiredResponseKeyA.keys',requiredResponseKeyA.keys)
    inducersAndStimuliRuleALoop.addData('requiredResponseKeyA.corr', requiredResponseKeyA.corr)
    if requiredResponseKeyA.keys != None:  # we had a response
        inducersAndStimuliRuleALoop.addData('requiredResponseKeyA.rt', requiredResponseKeyA.rt)
    # check responses
    if feedbackResponseKeyA.keys in ['', [], None]:  # No response was made
       feedbackResponseKeyA.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseA).lower() == 'none': feedbackResponseKeyA.corr = 1  # correct non-response
       else: feedbackResponseKeyA.corr = 0  # failed to respond (incorrectly)
    # store data for inducersAndStimuliRuleALoop (TrialHandler)
    inducersAndStimuliRuleALoop.addData('feedbackResponseKeyA.keys',feedbackResponseKeyA.keys)
    inducersAndStimuliRuleALoop.addData('feedbackResponseKeyA.corr', feedbackResponseKeyA.corr)
    if feedbackResponseKeyA.keys != None:  # we had a response
        inducersAndStimuliRuleALoop.addData('feedbackResponseKeyA.rt', feedbackResponseKeyA.rt)
    
    # the Routine "trialsRuleA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'inducersAndStimuliRuleALoop'


# set up handler to look after randomisation of conditions etc
inst4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection=u'3'),
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
    trialList=data.importConditions('stimuli.xlsx', selection=u'10:30'),
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
    
    #------Prepare to start Routine "trialsRuleB"-------
    t = 0
    trialsRuleBClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBoxB.setColor(stimulusColour, colorSpace='rgb')
    stimulusBoxB.setText(stimulus)
    requiredResponseKeyB = event.BuilderKeyResponse()  # create an object of type KeyResponse
    requiredResponseKeyB.status = NOT_STARTED
    feedbackResponseKeyB = event.BuilderKeyResponse()  # create an object of type KeyResponse
    feedbackResponseKeyB.status = NOT_STARTED
    
    # keep track of which components have finished
    trialsRuleBComponents = []
    trialsRuleBComponents.append(stimulusBoxB)
    trialsRuleBComponents.append(requiredResponseKeyB)
    trialsRuleBComponents.append(feedbackResponseKeyB)
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
        if t >= 0.3 and stimulusBoxB.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusBoxB.tStart = t  # underestimates by a little under one frame
            stimulusBoxB.frameNStart = frameN  # exact frame index
            stimulusBoxB.setAutoDraw(True)
        
        # *requiredResponseKeyB* updates
        if t >= 0.3 and requiredResponseKeyB.status == NOT_STARTED:
            # keep track of start time/frame for later
            requiredResponseKeyB.tStart = t  # underestimates by a little under one frame
            requiredResponseKeyB.frameNStart = frameN  # exact frame index
            requiredResponseKeyB.status = STARTED
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
            requiredResponseKeyB.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if requiredResponseKeyB.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysB))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if requiredResponseKeyB.keys == []:  # then this was the first keypress
                    requiredResponseKeyB.keys = theseKeys[0]  # just the first key pressed
                    requiredResponseKeyB.rt = requiredResponseKeyB.clock.getTime()
                    # was this 'correct'?
                    if (requiredResponseKeyB.keys == str(requiredResponseB)) or (requiredResponseKeyB.keys == requiredResponseB):
                        requiredResponseKeyB.corr = 1
                    else:
                        requiredResponseKeyB.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *feedbackResponseKeyB* updates
        if t >= 0.3 and feedbackResponseKeyB.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackResponseKeyB.tStart = t  # underestimates by a little under one frame
            feedbackResponseKeyB.frameNStart = frameN  # exact frame index
            feedbackResponseKeyB.status = STARTED
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
            feedbackResponseKeyB.clock.reset()  # now t=0
        if feedbackResponseKeyB.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysB))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if feedbackResponseKeyB.keys == []:  # then this was the first keypress
                    feedbackResponseKeyB.keys = theseKeys[0]  # just the first key pressed
                    feedbackResponseKeyB.rt = feedbackResponseKeyB.clock.getTime()
                    # was this 'correct'?
                    if (feedbackResponseKeyB.keys == str(feedbackResponseB)) or (feedbackResponseKeyB.keys == feedbackResponseB):
                        feedbackResponseKeyB.corr = 1
                    else:
                        feedbackResponseKeyB.corr = 0
        
        # *correctiveFeedbackB* updates
        if t >= 0.3 and correctiveFeedbackB.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackB.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackB.frameNStart = frameN  # exact frame index
            correctiveFeedbackB.setAutoDraw(True)
        if correctiveFeedbackB.status == STARTED:  # only update if being drawn
            correctiveFeedbackB.setText(msg, log=False)
        if len(feedbackResponseKeyB.keys)<1:
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
    if requiredResponseKeyB.keys in ['', [], None]:  # No response was made
       requiredResponseKeyB.keys=None
       # was no response the correct answer?!
       if str(requiredResponseB).lower() == 'none': requiredResponseKeyB.corr = 1  # correct non-response
       else: requiredResponseKeyB.corr = 0  # failed to respond (incorrectly)
    # store data for stimuliRuleBLoop (TrialHandler)
    stimuliRuleBLoop.addData('requiredResponseKeyB.keys',requiredResponseKeyB.keys)
    stimuliRuleBLoop.addData('requiredResponseKeyB.corr', requiredResponseKeyB.corr)
    if requiredResponseKeyB.keys != None:  # we had a response
        stimuliRuleBLoop.addData('requiredResponseKeyB.rt', requiredResponseKeyB.rt)
    # check responses
    if feedbackResponseKeyB.keys in ['', [], None]:  # No response was made
       feedbackResponseKeyB.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseB).lower() == 'none': feedbackResponseKeyB.corr = 1  # correct non-response
       else: feedbackResponseKeyB.corr = 0  # failed to respond (incorrectly)
    # store data for stimuliRuleBLoop (TrialHandler)
    stimuliRuleBLoop.addData('feedbackResponseKeyB.keys',feedbackResponseKeyB.keys)
    stimuliRuleBLoop.addData('feedbackResponseKeyB.corr', feedbackResponseKeyB.corr)
    if feedbackResponseKeyB.keys != None:  # we had a response
        stimuliRuleBLoop.addData('feedbackResponseKeyB.rt', feedbackResponseKeyB.rt)
    
    # the Routine "trialsRuleB" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'stimuliRuleBLoop'


# set up handler to look after randomisation of conditions etc
inst5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection=u'4'),
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
    requiredResponseKeyB = event.BuilderKeyResponse()  # create an object of type KeyResponse
    requiredResponseKeyB.status = NOT_STARTED
    feedbackResponseKeyB = event.BuilderKeyResponse()  # create an object of type KeyResponse
    feedbackResponseKeyB.status = NOT_STARTED
    
    # keep track of which components have finished
    trialsRuleBComponents = []
    trialsRuleBComponents.append(stimulusBoxB)
    trialsRuleBComponents.append(requiredResponseKeyB)
    trialsRuleBComponents.append(feedbackResponseKeyB)
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
        if t >= 0.3 and stimulusBoxB.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusBoxB.tStart = t  # underestimates by a little under one frame
            stimulusBoxB.frameNStart = frameN  # exact frame index
            stimulusBoxB.setAutoDraw(True)
        
        # *requiredResponseKeyB* updates
        if t >= 0.3 and requiredResponseKeyB.status == NOT_STARTED:
            # keep track of start time/frame for later
            requiredResponseKeyB.tStart = t  # underestimates by a little under one frame
            requiredResponseKeyB.frameNStart = frameN  # exact frame index
            requiredResponseKeyB.status = STARTED
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
            requiredResponseKeyB.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if requiredResponseKeyB.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowedKeysB))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if requiredResponseKeyB.keys == []:  # then this was the first keypress
                    requiredResponseKeyB.keys = theseKeys[0]  # just the first key pressed
                    requiredResponseKeyB.rt = requiredResponseKeyB.clock.getTime()
                    # was this 'correct'?
                    if (requiredResponseKeyB.keys == str(requiredResponseB)) or (requiredResponseKeyB.keys == requiredResponseB):
                        requiredResponseKeyB.corr = 1
                    else:
                        requiredResponseKeyB.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *feedbackResponseKeyB* updates
        if t >= 0.3 and feedbackResponseKeyB.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackResponseKeyB.tStart = t  # underestimates by a little under one frame
            feedbackResponseKeyB.frameNStart = frameN  # exact frame index
            feedbackResponseKeyB.status = STARTED
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
            feedbackResponseKeyB.clock.reset()  # now t=0
        if feedbackResponseKeyB.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowedKeysB))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if feedbackResponseKeyB.keys == []:  # then this was the first keypress
                    feedbackResponseKeyB.keys = theseKeys[0]  # just the first key pressed
                    feedbackResponseKeyB.rt = feedbackResponseKeyB.clock.getTime()
                    # was this 'correct'?
                    if (feedbackResponseKeyB.keys == str(feedbackResponseB)) or (feedbackResponseKeyB.keys == feedbackResponseB):
                        feedbackResponseKeyB.corr = 1
                    else:
                        feedbackResponseKeyB.corr = 0
        
        # *correctiveFeedbackB* updates
        if t >= 0.3 and correctiveFeedbackB.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctiveFeedbackB.tStart = t  # underestimates by a little under one frame
            correctiveFeedbackB.frameNStart = frameN  # exact frame index
            correctiveFeedbackB.setAutoDraw(True)
        if correctiveFeedbackB.status == STARTED:  # only update if being drawn
            correctiveFeedbackB.setText(msg, log=False)
        if len(feedbackResponseKeyB.keys)<1:
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
    if requiredResponseKeyB.keys in ['', [], None]:  # No response was made
       requiredResponseKeyB.keys=None
       # was no response the correct answer?!
       if str(requiredResponseB).lower() == 'none': requiredResponseKeyB.corr = 1  # correct non-response
       else: requiredResponseKeyB.corr = 0  # failed to respond (incorrectly)
    # store data for inducersAndStimuliRuleBLoop (TrialHandler)
    inducersAndStimuliRuleBLoop.addData('requiredResponseKeyB.keys',requiredResponseKeyB.keys)
    inducersAndStimuliRuleBLoop.addData('requiredResponseKeyB.corr', requiredResponseKeyB.corr)
    if requiredResponseKeyB.keys != None:  # we had a response
        inducersAndStimuliRuleBLoop.addData('requiredResponseKeyB.rt', requiredResponseKeyB.rt)
    # check responses
    if feedbackResponseKeyB.keys in ['', [], None]:  # No response was made
       feedbackResponseKeyB.keys=None
       # was no response the correct answer?!
       if str(feedbackResponseB).lower() == 'none': feedbackResponseKeyB.corr = 1  # correct non-response
       else: feedbackResponseKeyB.corr = 0  # failed to respond (incorrectly)
    # store data for inducersAndStimuliRuleBLoop (TrialHandler)
    inducersAndStimuliRuleBLoop.addData('feedbackResponseKeyB.keys',feedbackResponseKeyB.keys)
    inducersAndStimuliRuleBLoop.addData('feedbackResponseKeyB.corr', feedbackResponseKeyB.corr)
    if feedbackResponseKeyB.keys != None:  # we had a response
        inducersAndStimuliRuleBLoop.addData('feedbackResponseKeyB.rt', feedbackResponseKeyB.rt)
    
    # the Routine "trialsRuleB" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'inducersAndStimuliRuleBLoop'


# set up handler to look after randomisation of conditions etc
instEnd = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx', selection=u'5'),
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
