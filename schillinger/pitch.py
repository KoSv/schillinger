'''
    Schillinger System
    Book II - Pitch
    c. Konstantin Svechtarov 2017
    
'''
import numpy as np
import itertools
import random

class PitchGroup:
    
    def __init__(self):
        pass
    
    def melodic_forms_definition(self, units):
        return list(itertools.permutations(units))
    
    def melodic_forms_combination(self, units):
        return list(itertools.permutations(units))
    
    def clock_rotation(self, units):
        # Rotate Lists
        def rotate(l, x):
          return l[-x % len(l):] + l[:-x % len(l)]
        #clock
        l = []
        for i,e in enumerate(units):
            l.append(rotate(units, i))
            #print(rotate(units, i))
        return l
    def counter_clock_rotation(self, units):
        # Rotate Lists
        def rotate(l, x):
          return l[-x % len(l):] + l[:-x % len(l)]
        l = []
        #counterclock
        for i,e in enumerate(units):
            l.append(rotate(units, -i))
            #print(rotate(units, -i))
        return l
    
    def max_coefficients_of_reccurence(self, coeficients, mel_form):
        #get the higher number and iterate over both lists whith %
        max_num = max(len(coeficients), len(mel_form))
        temp = []
        for i in range(max_num):
            temp.append(mel_form[i%len(mel_form)]*coeficients[i%len(coeficients)])
        return temp

    def coefficients_of_reccurence(self, coeficients, mel_form):
        temp = []
        for i,e in enumerate(coeficients):
            temp.append([mel_form[i%len(mel_form)]]*e)

        return temp

    def convert_to_1D(self, sequence, levels_of_depth):
        for i in range(levels_of_depth):
            sequence = list(itertools.chain(*sequence))
        return sequence
    
    def convert_to_note_sequence(self, tone_sequence, attacks):
        new_seq = []
        for i in range(attacks):
            new_seq.append(tone_sequence[i%len(tone_sequence)])
        return new_seq
    
    # EXPANSIONS
    def expansions(self,units):
        expansions_len = len(units)
        expansion_array = []
        for l in range(1,expansions_len):
            temp = []
            for i,e in enumerate(units):
                x = (i*l)%len(units)
                u = units[x]
                if u in temp:
                    x = (x+1)%expansions_len
                    u = units[x]
                    temp.append(u)
                else:
                    temp.append(u)
            expansion_array.append(temp)      
        return expansion_array

    #ex = expansions([0,1,2,3,4,5,6])   
    #print(ex)

    def translate_notes_to_expansions(self, notes, scale):
        expansion_variables = []
        exp = self.expansions([x for x in range(len(scale))]) 
        for e in exp:
            new_notes = []
            for n in notes:
                index = scale.index(n)
                expansion_index = e[index]
                new_notes.append(scale[expansion_index])

            expansion_variables.append(new_notes)
        return expansion_variables
    
    def chordify_scale(self, scala, voices):
        new_list=[]
        for r in range(len(scala)):
            l = []
            for d in range(voices):
                l.append(scala[(r+d)%len(scala)])
            new_list.append(l)
        return new_list
    
    def harmonize(self, note_seq, chordified_scale):
        # erstma mit choice
        array = []
        for i, note in enumerate(note_seq):
            temp_cord = []
            for chord in chordified_scale:
                if note in chord:
                    temp_cord.append(chord)
            array.append([note,random.choice(temp_cord)])
        return array
    
    def harmonize_canonical(self, note_seq, chordified_scale):
        # only top note chooses harmony
        array = []
        for i, note in enumerate(note_seq):
            temp_cord = []
            for chord in chordified_scale:
                if note == chord[-1]:
                    temp_cord.append(chord)
            array.append([note,random.choice(temp_cord)])
        return array
    
    def clean_harmony(self,harmonized_part):
        cleaned_list = []
        for i,p in enumerate(harmonized_part):
            cl = []
            for l in p[1]:
                if l != p[0]:
                    cl.append(l)
            cleaned_list.append([p[0],cl])
        return cleaned_list

