#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Sat Oct 17 23:13:28 2015
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
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
instructions1box = visual.TextStim(win=win, ori=0, name='instructions1box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trialsRuleA"
trialsRuleAClock = core.Clock()
stimulusBoxA = visual.TextStim(win=win, ori=0, name='stimulusBoxA',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
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

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instructions2box = visual.TextStim(win=win, ori=0, name='instructions2box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trialsRuleA"
trialsRuleAClock = core.Clock()
stimulusBoxA = visual.TextStim(win=win, ori=0, name='stimulusBoxA',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
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

# Initialize components for Routine "instructions3"
instructions3Clock = core.Clock()
instructions3box = visual.TextStim(win=win, ori=0, name='instructions3box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trialsRuleA"
trialsRuleAClock = core.Clock()
stimulusBoxA = visual.TextStim(win=win, ori=0, name='stimulusBoxA',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
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

# Initialize components for Routine "instructions4"
instructions4Clock = core.Clock()
instructions4box = visual.TextStim(win=win, ori=0, name='instructions4box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trialsRuleB"
trialsRuleBClock = core.Clock()
stimulusBoxB = visual.TextStim(win=win, ori=0, name='stimulusBoxB',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
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

# Initialize components for Routine "instructions5"
instructions5Clock = core.Clock()
instructions5box = visual.TextStim(win=win, ori=0, name='instructions5box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trialsRuleB"
trialsRuleBClock = core.Clock()
stimulusBoxB = visual.TextStim(win=win, ori=0, name='stimulusBoxB',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
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

# Initialize components for Routine "instructionsEnd"
instructionsEndClock = core.Clock()
instructionsEndBox = visual.TextStim(win=win, ori=0, name='instructionsEndBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructionsLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx'),
    seed=None, name='instructionsLoop')
thisExp.addLoop(instructionsLoop)  # add the loop to the experiment
thisInstructionsLoop = instructionsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstructionsLoop.rgb)
if thisInstructionsLoop != None:
    for paramName in thisInstructionsLoop.keys():
        exec(paramName + '= thisInstructionsLoop.' + paramName)

for thisInstructionsLoop in instructionsLoop:
    currentLoop = instructionsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop.rgb)
    if thisInstructionsLoop != None:
        for paramName in thisInstructionsLoop.keys():
            exec(paramName + '= thisInstructionsLoop.' + paramName)
    
    #------Prepare to start Routine "instructions1"-------
    t = 0
    instructions1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructions1box.setText(instructions1
)
    instructions1key = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructions1key.status = NOT_STARTED
    # keep track of which components have finished
    instructions1Components = []
    instructions1Components.append(instructions1box)
    instructions1Components.append(instructions1key)
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions1box* updates
        if t >= 0.75 and instructions1box.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions1box.tStart = t  # underestimates by a little under one frame
            instructions1box.frameNStart = frameN  # exact frame index
            instructions1box.setAutoDraw(True)
        
        # *instructions1key* updates
        if t >= 1.25 and instructions1key.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions1key.tStart = t  # underestimates by a little under one frame
            instructions1key.frameNStart = frameN  # exact frame index
            instructions1key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructions1key.status == STARTED:
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
        for thisComponent in instructions1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions1"-------
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    
    
    #------Prepare to start Routine "instructions2"-------
    t = 0
    instructions2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructions2box.setText(instructions2)
    instructions2key = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructions2key.status = NOT_STARTED
    # keep track of which components have finished
    instructions2Components = []
    instructions2Components.append(instructions2box)
    instructions2Components.append(instructions2key)
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions2box* updates
        if t >= 0.75 and instructions2box.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions2box.tStart = t  # underestimates by a little under one frame
            instructions2box.frameNStart = frameN  # exact frame index
            instructions2box.setAutoDraw(True)
        
        # *instructions2key* updates
        if t >= 1.25 and instructions2key.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions2key.tStart = t  # underestimates by a little under one frame
            instructions2key.frameNStart = frameN  # exact frame index
            instructions2key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructions2key.status == STARTED:
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
        for thisComponent in instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions2"-------
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    
    
    #------Prepare to start Routine "instructions3"-------
    t = 0
    instructions3Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructions3box.setText(instructions3
)
    instructions3key = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructions3key.status = NOT_STARTED
    # keep track of which components have finished
    instructions3Components = []
    instructions3Components.append(instructions3box)
    instructions3Components.append(instructions3key)
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions3"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions3box* updates
        if t >= 0.75 and instructions3box.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions3box.tStart = t  # underestimates by a little under one frame
            instructions3box.frameNStart = frameN  # exact frame index
            instructions3box.setAutoDraw(True)
        
        # *instructions3key* updates
        if t >= 1.25 and instructions3key.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions3key.tStart = t  # underestimates by a little under one frame
            instructions3key.frameNStart = frameN  # exact frame index
            instructions3key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructions3key.status == STARTED:
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
        for thisComponent in instructions3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions3"-------
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    
    
    #------Prepare to start Routine "instructions4"-------
    t = 0
    instructions4Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructions4box.setText(instructions4
)
    instructions4key = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructions4key.status = NOT_STARTED
    # keep track of which components have finished
    instructions4Components = []
    instructions4Components.append(instructions4box)
    instructions4Components.append(instructions4key)
    for thisComponent in instructions4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions4"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions4box* updates
        if t >= 0.75 and instructions4box.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions4box.tStart = t  # underestimates by a little under one frame
            instructions4box.frameNStart = frameN  # exact frame index
            instructions4box.setAutoDraw(True)
        
        # *instructions4key* updates
        if t >= 1.25 and instructions4key.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions4key.tStart = t  # underestimates by a little under one frame
            instructions4key.frameNStart = frameN  # exact frame index
            instructions4key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructions4key.status == STARTED:
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
        for thisComponent in instructions4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions4"-------
    for thisComponent in instructions4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    
    
    #------Prepare to start Routine "instructions5"-------
    t = 0
    instructions5Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructions5box.setText(instructions5

)
    instructions5key = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructions5key.status = NOT_STARTED
    # keep track of which components have finished
    instructions5Components = []
    instructions5Components.append(instructions5box)
    instructions5Components.append(instructions5key)
    for thisComponent in instructions5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions5"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions5box* updates
        if t >= 0.75 and instructions5box.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions5box.tStart = t  # underestimates by a little under one frame
            instructions5box.frameNStart = frameN  # exact frame index
            instructions5box.setAutoDraw(True)
        
        # *instructions5key* updates
        if t >= 1.25 and instructions5key.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions5key.tStart = t  # underestimates by a little under one frame
            instructions5key.frameNStart = frameN  # exact frame index
            instructions5key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructions5key.status == STARTED:
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
        for thisComponent in instructions5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions5"-------
    for thisComponent in instructions5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    
    
    #------Prepare to start Routine "instructionsEnd"-------
    t = 0
    instructionsEndClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsEndBox.setText(instructionsEnd
)
    instructionsEndkey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructionsEndkey.status = NOT_STARTED
    # keep track of which components have finished
    instructionsEndComponents = []
    instructionsEndComponents.append(instructionsEndBox)
    instructionsEndComponents.append(instructionsEndkey)
    for thisComponent in instructionsEndComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructionsEnd"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsEndClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsEndBox* updates
        if t >= 0.75 and instructionsEndBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsEndBox.tStart = t  # underestimates by a little under one frame
            instructionsEndBox.frameNStart = frameN  # exact frame index
            instructionsEndBox.setAutoDraw(True)
        
        # *instructionsEndkey* updates
        if t >= 1.25 and instructionsEndkey.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsEndkey.tStart = t  # underestimates by a little under one frame
            instructionsEndkey.frameNStart = frameN  # exact frame index
            instructionsEndkey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructionsEndkey.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i', 'return'])
            
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
        for thisComponent in instructionsEndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructionsEnd"-------
    for thisComponent in instructionsEndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructionsEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructionsLoop'






win.close()
core.quit()
