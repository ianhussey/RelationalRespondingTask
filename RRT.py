#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Mon Nov  9 22:57:03 2015
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
    monitor=u'testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
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
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimulusBox = visual.TextStim(win=win, ori=0, name='stimulusBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg=""
feedback = visual.TextStim(win=win, ori=0, name='feedback',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
trueText = visual.TextStim(win=win, ori=0, name='trueText',
    text='default text',    font='Arial',
    pos=[0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
falseText = visual.TextStim(win=win, ori=0, name='falseText',
    text='default text',    font='Arial',
    pos=[-0.75, 0.75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "end"
endClock = core.Clock()
endBox = visual.TextStim(win=win, ori=0, name='endBox',
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
    instructionsBox.setText(instructions)
    instructionsKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructionsKey.status = NOT_STARTED
    # keep track of which components have finished
    instructionComponents = []
    instructionComponents.append(instructionsBox)
    instructionComponents.append(instructionsKey)
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
    trials = data.TrialHandler(nReps=nBlockRepetitions, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(stimulusFile),
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
        stimulusBox.setColor(stimulusColour, colorSpace='rgb')
        stimulusBox.setText(stimulus)
        requiredResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        requiredResponse.status = NOT_STARTED
        feedbackResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        feedbackResponse.status = NOT_STARTED
        
        trueText.setText(trueLabel)
        falseText.setText(falseLabel)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(stimulusBox)
        trialComponents.append(requiredResponse)
        trialComponents.append(feedbackResponse)
        trialComponents.append(feedback)
        trialComponents.append(trueText)
        trialComponents.append(falseText)
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
            
            # *stimulusBox* updates
            if t >= 0.75 and stimulusBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusBox.tStart = t  # underestimates by a little under one frame
                stimulusBox.frameNStart = frameN  # exact frame index
                stimulusBox.setAutoDraw(True)
            
            # *requiredResponse* updates
            if t >= 0.75 and requiredResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                requiredResponse.tStart = t  # underestimates by a little under one frame
                requiredResponse.frameNStart = frameN  # exact frame index
                requiredResponse.status = STARTED
                # AllowedKeys looks like a variable named `requiredResponseAllowed`
                if not 'requiredResponseAllowed' in locals():
                    logging.error('AllowedKeys variable `requiredResponseAllowed` is not defined.')
                    core.quit()
                if not type(requiredResponseAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(requiredResponseAllowed, basestring):
                        logging.error('AllowedKeys variable `requiredResponseAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in requiredResponseAllowed: requiredResponseAllowed = (requiredResponseAllowed,)
                    else:  requiredResponseAllowed = eval(requiredResponseAllowed)
                # keyboard checking is just starting
                requiredResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if requiredResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(requiredResponseAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if requiredResponse.keys == []:  # then this was the first keypress
                        requiredResponse.keys = theseKeys[0]  # just the first key pressed
                        requiredResponse.rt = requiredResponse.clock.getTime()
                        # was this 'correct'?
                        if (requiredResponse.keys == str(requiredResponseCorrect )) or (requiredResponse.keys == requiredResponseCorrect ):
                            requiredResponse.corr = 1
                        else:
                            requiredResponse.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *feedbackResponse* updates
            if t >= .75 and feedbackResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackResponse.tStart = t  # underestimates by a little under one frame
                feedbackResponse.frameNStart = frameN  # exact frame index
                feedbackResponse.status = STARTED
                # AllowedKeys looks like a variable named `feedbackResponseAllowed`
                if not 'feedbackResponseAllowed' in locals():
                    logging.error('AllowedKeys variable `feedbackResponseAllowed` is not defined.')
                    core.quit()
                if not type(feedbackResponseAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(feedbackResponseAllowed, basestring):
                        logging.error('AllowedKeys variable `feedbackResponseAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in feedbackResponseAllowed: feedbackResponseAllowed = (feedbackResponseAllowed,)
                    else:  feedbackResponseAllowed = eval(feedbackResponseAllowed)
                # keyboard checking is just starting
                feedbackResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if feedbackResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(feedbackResponseAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if feedbackResponse.keys == []:  # then this was the first keypress
                        feedbackResponse.keys = theseKeys[0]  # just the first key pressed
                        feedbackResponse.rt = feedbackResponse.clock.getTime()
                        # was this 'correct'?
                        if (feedbackResponse.keys == str(feedbackResponseCorrect )) or (feedbackResponse.keys == feedbackResponseCorrect ):
                            feedbackResponse.corr = 1
                        else:
                            feedbackResponse.corr = 0
            if len(feedbackResponse.keys)<1:
                msg=""
            else:
                msg="X"
            
            # *feedback* updates
            if t >= .75 and feedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback.tStart = t  # underestimates by a little under one frame
                feedback.frameNStart = frameN  # exact frame index
                feedback.setAutoDraw(True)
            if feedback.status == STARTED:  # only update if being drawn
                feedback.setText(msg, log=False)
            
            # *trueText* updates
            if t >= 0 and trueText.status == NOT_STARTED:
                # keep track of start time/frame for later
                trueText.tStart = t  # underestimates by a little under one frame
                trueText.frameNStart = frameN  # exact frame index
                trueText.setAutoDraw(True)
            
            # *falseText* updates
            if t >= 0.0 and falseText.status == NOT_STARTED:
                # keep track of start time/frame for later
                falseText.tStart = t  # underestimates by a little under one frame
                falseText.frameNStart = frameN  # exact frame index
                falseText.setAutoDraw(True)
            
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
        if requiredResponse.keys in ['', [], None]:  # No response was made
           requiredResponse.keys=None
           # was no response the correct answer?!
           if str(requiredResponseCorrect ).lower() == 'none': requiredResponse.corr = 1  # correct non-response
           else: requiredResponse.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('requiredResponse.keys',requiredResponse.keys)
        trials.addData('requiredResponse.corr', requiredResponse.corr)
        if requiredResponse.keys != None:  # we had a response
            trials.addData('requiredResponse.rt', requiredResponse.rt)
        # check responses
        if feedbackResponse.keys in ['', [], None]:  # No response was made
           feedbackResponse.keys=None
           # was no response the correct answer?!
           if str(feedbackResponseCorrect ).lower() == 'none': feedbackResponse.corr = 1  # correct non-response
           else: feedbackResponse.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('feedbackResponse.keys',feedbackResponse.keys)
        trials.addData('feedbackResponse.corr', feedbackResponse.corr)
        if feedbackResponse.keys != None:  # we had a response
            trials.addData('feedbackResponse.rt', feedbackResponse.rt)
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nBlockRepetitions repeats of 'trials'
    
# completed 1 repeats of 'blocks'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(3.750000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(endBox)
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
    
    # *endBox* updates
    if t >= 0.75 and endBox.status == NOT_STARTED:
        # keep track of start time/frame for later
        endBox.tStart = t  # underestimates by a little under one frame
        endBox.frameNStart = frameN  # exact frame index
        endBox.setAutoDraw(True)
    if endBox.status == STARTED and t >= (0.75 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        endBox.setAutoDraw(False)
    
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
