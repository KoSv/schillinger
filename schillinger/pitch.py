'''
    Schillinger System
    Book II - Pitch
    c. Konstantin Svechtarov 2017
    
'''
import numpy as np
import itertools
import random


def diatonic_cicles_with_coeficients(scale, cycles, coef):
    '''
        *belongs to melody module*
        diatonic_cicles_with_coeficients(scale,[C3],[1]) for one scale
        diatonic_cicles_with_coeficients(test_scale,[C3,C5],*[2,1]*) for combinations
        warning:
        *[n!,n!]* must be the length of the cycles otherwise it produces scrap
        
    '''
    sum_arr = []
    #init & fill in first element
    last_element = scale[0]
    sum_arr.append(last_element)
    last_element_idx = 0
    
    length = sum(coef)*len(scale)
    count = 0
    i = 0
    for i in range(length):
        coef_iterator = i%len(coef)
        cycles_iterator = coef_iterator % len(cycles)
        for c in range(coef[coef_iterator]):
            last_element_idx = cycles[cycles_iterator].index(last_element)
            last_element = cycles[cycles_iterator][(last_element_idx+1)%len(scale)]
            sum_arr.append(last_element)
            #print(coef_iterator, cycles_iterator, last_element_idx, last_element, cycles[cycles_iterator] )
            if count >= length-1:
                return sum_arr
            count += 1
        i += 1

def get_whole_sequence(melody_notes, init_scales, voices, theme_expansion, scale_expansion_amount):
    '''
        convert multiple note sequences plus the corresponding scales to harmonized stream
        
        gets a [[melody_notes]] [[init_scales]] int(voices) int(theme_expansion) int(scale_expansion_amount default=1!)
        returns hatmonizes array [[melody1[chords1]] [melody2[chords2]] ... [melodyN[chordsN]]]
    '''
    SPG = PitchGroup()
    harmonized_note_sequence_array = []
    
    for i in range(len(melody_notes)):
        
        note_sequence_all_expansions = SPG.translate_notes_to_expansions(melody_notes[i], init_scales[i])

        scale_expansion = SPG.expansions(init_scales[i])

        scale_ = scale_expansion[scale_expansion_amount] 

        chordified_scale = SPG.chordify_scale(scale_, voices)

        note_sequence = note_sequence_all_expansions[theme_expansion%len(note_sequence_all_expansions)]

        harmonized_note_sequence = SPG.harmonize(note_sequence, chordified_scale)
        
        cleaned_sequence = SPG.clean_harmony(harmonized_note_sequence)
        
        harmonized_note_sequence_array.append(cleaned_sequence)   
        
    return harmonized_note_sequence_array

def get_whole_sequence_canonical(melody_notes, init_scales, voices, theme_expansion, scale_expansion_amount):
    '''
        convert multiple note seqeunces plus scales to a harmonized stream
        
        gets a [[melody_notes]] [[init_scales]] int(voices) int(theme_expansion) int(scale_expansion_amount default=1!)
        returns hatmonizes array [[melody1[chords1]] [melody2[chords2]] ... [melodyN[chordsN]]]
    '''
    SPG = PitchGroup()
    harmonized_note_sequence_array = []
    
    for i in range(len(melody_notes)):
        
        note_sequence_all_expansions = SPG.translate_notes_to_expansions(melody_notes[i], init_scales[i])

        scale_expansion = SPG.expansions(init_scales[i])

        scale_ = scale_expansion[scale_expansion_amount] 

        chordified_scale = SPG.chordify_scale(scale_, voices)

        note_sequence = note_sequence_all_expansions[theme_expansion%len(note_sequence_all_expansions)]

        harmonized_note_sequence = SPG.harmonize_canonical(note_sequence, chordified_scale)
        
        cleaned_sequence = SPG.clean_harmony(harmonized_note_sequence)
        
        harmonized_note_sequence_array.append(cleaned_sequence)   
        
    return harmonized_note_sequence_array

def get_whole_sequence_bass(melody_notes, init_scales, voices, theme_expansion, scale_expansion_amount):
    '''
        convert multiple note sequences plus the corresponding scales to harmonized stream
        
        gets a [[melody_notes]] [[init_scales]] int(voices) int(theme_expansion) int(scale_expansion_amount default=1!)
        returns hatmonizes array [[melody1[chords1]] [melody2[chords2]] ... [melodyN[chordsN]]]
    '''
    SPG = PitchGroup()
    harmonized_note_sequence_array = []
    
    for i in range(len(melody_notes)):
        try:
        
            note_sequence_all_expansions = SPG.translate_notes_to_expansions(melody_notes[i], init_scales[i])
        

            scale_expansion = SPG.expansions(init_scales[i])

            scale_ = scale_expansion[scale_expansion_amount] 

            chordified_scale = SPG.chordify_scale(scale_, voices)

            note_sequence = note_sequence_all_expansions[theme_expansion%len(note_sequence_all_expansions)]

            harmonized_note_sequence = SPG.harmonize_bass(note_sequence, chordified_scale)

            cleaned_sequence = SPG.clean_harmony(harmonized_note_sequence)

            harmonized_note_sequence_array.append(cleaned_sequence)   
        except:
            scale_expansion = SPG.expansions(init_scales[i])
            print("note skipped not in scale!", melody_notes[i],scale_expansion)
        
    return harmonized_note_sequence_array


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
    
    def harmonize_bass(self, note_seq, chordified_scale):
        array = []
        for i, note in enumerate(note_seq):
            temp_cord = []
            #print(note)
            for chord in chordified_scale:
                if note == chord[0]:
                    #print(note, chord)
                    temp_cord.append(chord)
                    array.append([note,random.choice(temp_cord)])
                    break
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

