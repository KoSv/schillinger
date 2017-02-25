import random



def diatonic_cadences(expansions):
    cadences = []
    for e in expansions:
        cadences.append([e[0],e[1],e[-1],e[0]])
    return cadences


def chordify_scale(scala, voices):
    '''
            chordify_scale(['C', 'E-', 'G', 'B-', 'D', 'F', 'A-'],4)
            >>> [['C', 'E-', 'G', 'B-'], ['E-', 'G', 'B-', 'D'], ['G', 'B-', 'D', 'F'], ...]
    '''
    new_list=[]
    for r in range(len(scala)):
        l = []
        for d in range(voices):
            l.append(scala[(r+d)%len(scala)])
        new_list.append(l)
    return new_list

def harmonize_note(note, chordified_scale, reference_note_coefs, randomized=False):
    ''' 
        
        harmonize([C], [['C', 'E-', 'G', 'B-'],['E-', 'G', 'B-', 'D']], 0, randomized=False) 
        >>> 
    '''
    array = []
    
    #for i, note in enumerate(note_seq):
    temp_cord = []
    for chord in chordified_scale:
        if randomized:
            if note in chord:
                    temp_cord.append(chord)
            
        else:
            if note == chord[reference_note_coefs]:
                temp_cord.append(chord)
                break
    array.append(random.choice(temp_cord))
    return array[0]

##

def clean_harmony(harmonized_part):
    cleaned_list = []
    for i,p in enumerate(harmonized_part):
        cl = []
        for l in p[1]:
            if l != p[0]:
                cl.append(l)
        cleaned_list.append([p[0],cl])
    return cleaned_list
        
        
        
        
        