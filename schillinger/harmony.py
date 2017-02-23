import schillinger.pitch as SP

def harmonic_cicles(expansions, coef):
    '''
        *belongs to melody module*
        diatonic_cicles_with_coeficients(scale,[C3],[1]) for one scale
        diatonic_cicles_with_coeficients(test_scale,[C3,C5],*[2,1]*) for combinations
        warning:
        *[n!,n!]* must be the length of the expansions otherwise it produces scrap
        
    '''
    sum_arr = []
    #init & fill in first element
    last_element = expansions[0][0]
    sum_arr.append(last_element)
    last_element_idx = 0
    
    length = sum(coef)*len(expansions[0])
    count = 0
    i = 0
    for i in range(length):
        coef_iterator = i%len(coef)
        expansions_iterator = coef_iterator % len(expansions)
        for c in range(coef[coef_iterator]):
            last_element_idx = expansions[expansions_iterator].index(last_element)
            last_element = expansions[expansions_iterator][(last_element_idx+1)%len(expansions[0])]
            sum_arr.append(last_element)
            if count >= length-1:
                return sum_arr
            count += 1
        i += 1

def expansions(scale):
    SPG = SP.PitchGroup()
    scale_expansion = SPG.expansions(scale)
    return scale_expansion

def diatonic_cadences(expansions):
    cadences = []
    for e in expansions:
        cadences.append([e[0],e[1],e[-1],e[0]])
    return cadences
        
        
        
        
        
        
        