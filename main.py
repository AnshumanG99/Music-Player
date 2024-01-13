import time
import os
from replit import audio

#Define Functions

#Start Function; Creates main option menu
def starting():
  start = input("\033[38;2;0;0;255m" + "-------------Music-Bot---------------\nA. Play a note for me!\nB. Play a scale for me!\nC. I do not want to use the bot\nEnter a letter coresponding to the different options to continue: ")
  start = start.upper()

  #Checks what the user inputted, and sends corresponding output
  if start == "A":
    os.system('clear')
    note = input("\033[38;2;0;0;255m" + "-------------Music-Bot---------------\nWhat note would you like to hear? ")
    audio.play_tone(2, frequencies[notedic[note]], 1 )
    restart(2)
    
  elif start == "B":
    os.system('clear')
    scales_start()
  elif start == "C":
    print("Thanks!")

#Plays scale user wants
def scales_start():
  startingnote = input("\033[38;2;0;0;255m" + "-------------Music-Bot---------------\nWhat note would you like to start on? ")
  startingnote = startingnote.upper()
  scaletype = input("Would you like to hear a major or minor scale? ")
  arpeggio = input("Would you like to hear an arpeggio as well? ")

  #Checks if user entered a valid note, if not asks the user for another note
  if startingnote in notedic:
    pass
  else:
    startingnote = input("Make sure to type a valid note. ")

  #Plays scale that user asked for using half step patterns/intervals
  if scaletype.lower() == "major":
    scale(startingnote, [0, 2, 4, 5, 7, 9, 11, 12]) 
  #Checks if user asked for an arpeggio as well
  if (arpeggio.lower() == "yes") and (scaletype.lower() == "major"):
    print("\n")
    scale(startingnote, [0, 4, 7])
    restart(3)
  if scaletype.lower() == "minor":
    scale(startingnote, [0, 2, 3, 5, 7, 8, 10, 12])
  if (arpeggio.lower() == "yes") and (scaletype.lower() == "minor"):
    scale(startingnote, [0, 3, 7])
    restart(3)
  else:
    restart(2)
  
#Function to create a scale based off intervals
def scale(startingnote, intervals):
  #Checks length of intervals and prints dedicated statement
  if len(intervals) < 5:
    print("Here is the arpeggio!")
    intervals.append(intervals[1])
    intervals.append(intervals[0])
  elif len(intervals) > 7:
    print("Here is the scale!")

  #Loops code for every single value inside the parameter called intervals
  for interval in intervals:
    given_note_value = notedic[startingnote]+ interval
    #Prevents calling past the list range
    if (given_note_value) >= 12:
      given_note_value = given_note_value - 12
      #Makes notes go higher up when needed, notes would go lower than before without this 
      audio.play_tone(.5, (2 * frequencies[given_note_value]), 1)
    else:
      audio.play_tone(.5, (frequencies[given_note_value]), 1)
    #Prints the note that is being played by adding the list index of starting note with interval
    print(notes[given_note_value])
        #Makes sure that the code doesn't do all the playsounds instantly, causing no sound    
    time.sleep(.5)

#Function to restart code and clear system
def restart(x):
  time.sleep(x)
  os.system('clear')
  starting()

#Define variables

#Creates notes list and dictionary for available notes
notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
notedic = {}

#Adds notes to the dictionary
for i in range(len(notes)):
  notedic[notes[i]] = i

#Creates list of frequencies corresponding to notes
frequencies = [440, 466.16, 493.88, 523, 554, 587, 622, 659, 698, 740, 784, 831]

#Calling start function
starting()