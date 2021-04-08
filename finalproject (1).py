from psychopy import visual, core, event  # import some libraries from PsychoPy
import random

def startExperiment():

    '''
    This is the first function to be called.
    
    Part 1: It will display instructions for the experiment.

    Part 2: Initializes word list for all sessions

    Part 3: Calls practice func for each of the sessions

    Part 4: Indicates end of experiment, waits 5 secs and closes the application
    '''

    # Part 1
    instructions = ['This is a test', 
    'you will now see a series of words',
    'press `->` for self and `<-` for other',
    'press any key to continue']
    pos = [[-9,8],[-4,6],[-4,4],[-6,2]]
    for i in range(len(instructions)):
        visual.TextStim(win=mywin, text=instructions[i], pos=pos[i], wrapWidth=500).draw()
    mywin.flip()
    thisResp=None
    while thisResp==None:
        allKeys=event.waitKeys()
        if len(allKeys) > 0:
            thisResp = allKeys[0]
    # Part 2
    sessions = [["Self","Other"]*3,["Joy", "Vomit"]*3,["Self", "Joy", "Other", "Vomit"]*3]
    sessions.append(sessions[1])
    sessions.append(sessions[2])

    # Part 3
    for i,current in enumerate(sessions):
        random.shuffle(current)
        practice(i+1,current)

    # Part 4
    visual.TextStim(win=mywin, text='End Of Experiment', pos=[0,0], wrapWidth=500).draw()
    mywin.flip()
    core.wait(5.0)
    
def practice(num,wordlist):

    '''
    This function is called from the start experiment func

    Part 1: Displays Practice number and waits for 1 sec

    Part 2: Displays each word in the wordlist, after displaying the word,
            calls recordTime func with currenttime, clears the screen and waits
            100 microsecs

    Part 3: Indicates end of practice session and waits for 1 sec
    '''

    # Part 1
    print(f"\nprinting info for Practice {num}: \n")
    visual.TextStim(win=mywin, text='Practice '+str(num), pos=[0,0]).draw()
    mywin.flip()
    core.wait(1)

    # Part 2
    for i in wordlist:
        visual.TextStim(win=mywin, text=i, pos=[0,0]).draw()
        mywin.flip()
        recordTime(i, timer.getTime())
        mywin.flip()
        core.wait(0.1)

    # Part 3
    visual.TextStim(win=mywin, text='End of practice '+str(num), pos=[0,0]).draw()
    mywin.flip()
    core.wait(1)
    
def recordTime(word, currentTime):

    '''
    This func is called from practice func

    Part 1: Waits for until user presses a key

    Part 2: looks thorough all the keys user press to check if they pressed
            left or right key if left/right key is pressed then gets the
            currentTime (as newTime) and calculates reaction time.

    Part 3: Prints word, keyPressed, and reaction time.
            Sets `thisResp` so the program doesn't wait
    '''

    # Part 1
    thisResp=None
    while thisResp==None:
        allKeys=event.waitKeys()
        for thisKey in allKeys:
            
            # Part 2
            if thisKey in ['right','left']:
                newTime = timer.getTime()
                reaction_time = newTime - currentTime

                # Part 3
                print(f"Current Word: {word} {thisKey} was pressed reaction time is {reaction_time}")
                thisResp = thisKey


timer = core.Clock() # Initializes timer

# Initialzes window for the experiment
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

startExperiment() #Calls startExperiment func
