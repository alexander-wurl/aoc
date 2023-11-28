#!/usr/bin/env python

import helper

def get_valid_tickets(tickets: list, notes: list):

    validTickets = []

    for ticket in tickets:

        valid = True

        for value in ticket:
            
            if (valid == False):
                break

            val = {}

            for note in notes:

                check = check_validity(value, note)
                val[str(note)] = check

            if (True in val.values()):
                valid = True
            else:
                valid = False
                break

        if (valid):
            validTickets.append(ticket)

    return validTickets

# check single value (for one note)
def check_validity(value: int, note: list) -> bool:
    valid = False

    if (((value >= note[0]) and (value <= note[1])) or ((value >= note[2]) and (value <= note[3]))):
        valid = True

    return valid

# check multiple values (for one note), one mismatch means column is not valid for given note
def check_validities(values: list, note: list) -> bool:
    valid = True

    for i in values:
        if not (((i >= note[0]) and (i <= note[1])) or ((i >= note[2]) and (i <= note[3]))):
            valid = False

    return valid

def part1():

    data = helper.getData("16")

    notes = []
    tickets = []

    # read notes
    for e in data[0:20]:
        temp = e.split(":")[1].replace("or", "-").replace(" ", "").split("-")
        notes.append(list([int(value) for value in temp]))

    # read tickets
    for e in data[26:]:
        temp = e.split(",")
        tickets.append([int(value) for value in temp])


    validity = {}

    # scanning error rate
    ser = 0

    # all tickets
    for ticket in tickets:

        # all values
        for value in ticket:

            # all notes
            for note in notes:
                validity[str(note)] = check_validity(value, note)

            # check validity
            if not True in validity.values():
                ser += value
     
            validity.clear

    print("Solution for part 1 is: {}".format(ser))

def get_matching_note_with_value_1(matchingNotes, notes):

    for note in matchingNotes:

        ret = matchingNotes[note]
        if (len(ret) == 1):
            return note
        
def delete_matching_note_in_matching_notes(matchingNote, matchingNotes, notes):

    ret = matchingNotes[matchingNote]
    del matchingNotes[matchingNote]
    return (matchingNotes, ret)

def remove_column_value_in_matching_notes(columnValue, matchingNotes, notes):

    s = int(columnValue[0])

    for note in matchingNotes:

        if (s in matchingNotes[note]):

            matchingNotes[note].remove(s)

    return matchingNotes

def part2():

    data = helper.getData("16")

    notes = []
    tickets = []
    myticket = []
    
    # read notes
    for e in data[0:20]:
       temp = e.split(":")[1].replace("or", "-").replace(" ", "").split("-")
       notes.append(list([int(value) for value in temp]))

    # read tickets
    for e in data[25:]:
       temp = e.split(",")
       tickets.append(list([int(value) for value in temp]))

    # read my ticket
    for e in data[22:23]:
       temp = e.split(",")
       myticket.append(list([int(value) for value in temp]))

    validTickets = get_valid_tickets(tickets, notes)
    

    matchingNotes = {}

    # process valid tickets
    for note in notes:

        matchingNotes[str(note)] = []

        for columnIndex in range(0, len(validTickets[0])):

            column = [t[columnIndex] for t in validTickets]

            if (check_validities(column, note)):
                #print("Note {}: matches with column {}".format(note, columnIndex))
                matchingNotes[str(note)].append(columnIndex) 

    # process matching notes
    
    finalNotes = {}
    tempColumn = 0

    while ( not(len(finalNotes) == 6) ):

        # get matchingNote with value 1
        matchingNote = get_matching_note_with_value_1(matchingNotes, notes)

        if (matchingNote):
           # remove that note and return it's column value
            (matchingNotes, columnValue) = delete_matching_note_in_matching_notes(matchingNote, matchingNotes, notes)
            
            # remove all 'columnValue' from matchingNotes
            matchingNotes = remove_column_value_in_matching_notes(columnValue, matchingNotes, notes)
        else:
            columnValue = tempColumn
            matchingNotes = remove_column_value_in_matching_notes(columnValue, matchingNotes, notes)

        try:
            if ( (len(matchingNotes[str(notes[0])]) == 1) ):
                finalNotes[str(notes[0])] = matchingNotes[str(notes[0])]
                tempColumn = matchingNotes[str(notes[0])]
                del matchingNotes[str(notes[0])]
        except:
            pass
        try:
            if ( (len(matchingNotes[str(notes[1])]) == 1) ):
                finalNotes[str(notes[1])] = matchingNotes[str(notes[1])]
                tempColumn = matchingNotes[str(notes[1])]
                del matchingNotes[str(notes[1])]
        except:
            pass
        try:
            if ( (len(matchingNotes[str(notes[2])]) == 1) ):
                finalNotes[str(notes[2])] = matchingNotes[str(notes[2])]
                tempColumn = matchingNotes[str(notes[2])]
                del matchingNotes[str(notes[2])]
        except:
            pass
        try:
            if ( (len(matchingNotes[str(notes[3])]) == 1) ):
                finalNotes[str(notes[3])] = matchingNotes[str(notes[3])]
                tempColumn = matchingNotes[str(notes[3])]
                del matchingNotes[str(notes[3])]
        except:
            pass
        try:
            if ( (len(matchingNotes[str(notes[4])]) == 1) ):
                finalNotes[str(notes[4])] = matchingNotes[str(notes[4])]
                tempColumn = matchingNotes[str(notes[4])]
                del matchingNotes[str(notes[4])]
        except:
            pass
        try:
            if ( (len(matchingNotes[str(notes[5])]) == 1) ):
                finalNotes[str(notes[5])] = matchingNotes[str(notes[5])]
                tempColumn = matchingNotes[str(notes[5])]
                del matchingNotes[str(notes[5])]
        except:
            pass

    # process final notes

    solution2 = 1

    for fn in finalNotes:
        x = int(finalNotes[fn][0])
        solution2 *= myticket[0][x]

    print("Solution for part 2 is: {}".format(solution2))


# main

part1()
part2()
