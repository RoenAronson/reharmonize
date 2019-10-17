#!/usr/bin/python
# -*- coding: utf-8 -*-
import AutumnLeaves
# from pychord import *

simpleNotes = ["A", "B", "C", "D", "E", "F", "G"]
complexNotes = []

extensions = ["-", "7", "-7", "ø7", "°", "maj7", "7b13", "-6"]
chords = []

twoFives = []

for note in simpleNotes:
    a = note + "b"
    b = note
    c = note + "#"
    complexNotes.append(a)
    complexNotes.append(b)
    complexNotes.append(c)

for note in complexNotes:
    for extension in extensions:
        a = note + extension
        chords.append(a)

# Remove the yucky stuff
complexNotes.remove("B#")
complexNotes.remove("Cb")
complexNotes.remove("E#")
complexNotes.remove("Fb")

circleOfFifths = ["A", "E", "B", "F#", "C#", "G#", "D#", "A#", "F", "C", "G", "D", "A"]

def getFifth(note):
    if (note == "Bb"):
        return "F"
    if (note == "B"):
        return "F#"
    if (note == "Eb"):
        return "Bb"
    if (note ==  "E"):
        return "B"
    if (complexNotes.index(note) < (len(complexNotes) - 12)):
        a = complexNotes.index(note) + 10
    else:
        a = complexNotes.index(note) - 7
    return complexNotes[a]

def getSecond(note):
    if (note == "Bb"):
        return "C"
    if (note == "Eb"):
        return "F"
    if (note ==  "E"):
        return "F#"
    if (note == "B"):
        return "C#"
    if (complexNotes.index(note) < (len(complexNotes) - 3)):
        a = complexNotes.index(note) + 3
    else:
        a = complexNotes.index(note) - 14
    return complexNotes[a]

def getTritone(note):
    if (note == "Bb"):
        return "E"
    if (note == "B"):
        return "F"
    if (note == "Eb"):
        return "A"
    if (note ==  "E"):
        return "Bb"
    if (note == "Gb"):
        return "C"
    if (note == "Ab"):
        return "D"
    if (note == "Db"):
        return "G"
    if (complexNotes.index(note) < (len(complexNotes) - 9)):
        a = complexNotes.index(note) + 9
    else:
        a = complexNotes.index(note) - 8
    return complexNotes[a]

# print(complexNotes)
def printIntervals():
    print("Seconds: ")
    for note in complexNotes:
        print(note + " " + getSecond(note))
    print("Fifths: ")
    for note in complexNotes:
        print(note + " " + getFifth(note))
    print("Tritones: ")
    for note in complexNotes:
        print(note + " " + getTritone(note))

# printIntervals()

#Song Identification


def printChanges():
    for i in range(len(AutumnLeaves.changes)):
        for j in range(2):
            print(AutumnLeaves.changes[i][j])

# Identify 2-5's
def identifyTwoFive():

    changes = AutumnLeaves.changes

    for i in range(len(changes)-2):
        if (i % 2 == 0):

            # Get the chord
            relativeTwo = changes[i][0]

            # In order to get the correct note, we need to check if the chord is sharp or flat.
            if (relativeTwo[1] == "#" or relativeTwo[1] == "b"):
                chord = relativeTwo[0:2]
            else:
                chord = relativeTwo[0]

            # Doing the same for the "root" chord , which we assume the relative chord is the 2 of
            relativeRoot = changes[i+2][0]
            if (relativeRoot[1] == "#" or relativeRoot[1] == "b"):
                root = relativeRoot[0:2]
            else:
                root = relativeRoot[0]

            # Find the 5th
            relativeFifth = changes[i+1][0]
            if (relativeFifth[1] == "#" or relativeFifth[1] == "b"):
                fifth = relativeFifth[0:2]
            else:
                fifth = relativeFifth[0]

            # If both are true, this is a 2-5
            if (chord == getSecond(root) and fifth == getFifth(root)):
                print("We have ourselves a 2-5: " + relativeTwo + " " + relativeFifth + " " + relativeRoot)
                twoFives.append([relativeTwo, relativeFifth])

def mutateFives():
    for i in range(len(twoFives)):
        chord = twoFives[i][1]
        if (chord[1] == "#" or chord[1] == "b"):
            fifth = chord[0:2]
            extension = chord[3:]
        else:
            fifth = chord[0]
            extension = chord[1:]
        twoFives[i][1] = getTritone(fifth) + extension

identifyTwoFive()
print(twoFives)
mutateFives()
print(twoFives)