'''
    Schillinger System
    Book I - Rhythm
    c. Konstantin Svechtarov 2017
    
'''
import numpy as np
from fractions import Fraction
import random


def slice_list(result):
    if len(result) % 2 == 0:
        
        firstpart, secondpart = result[:int(len(result)/2)], result[int(len(result)/2):]
    else:
        firstpart, secondpart = result[:int(len(result)/2)+1], result[int(len(result)/2):]
        
    return [firstpart,secondpart]

def slice_by_fraction(result, fraction):
    
    if len(result) % 2 == 0:
        
        firstpart, secondpart = result[:int(len(result)*fraction)], result[int(len(result)*fraction):]
    else:
        firstpart, secondpart = result[:int(len(result)*fraction)], result[int(len(result)*fraction):]
        
    return [firstpart,secondpart]

def get_random_attack_combination(attack_sequence):
    
    devisible_list = []
    sum_sr = sum(attack_sequence)
    for i in range(1,sum_sr):
        if sum_sr % i == 0:
            devisible_list.append(i)
    
    return_attack_array = []
    while sum(return_attack_array) <= sum_sr:
        random_num = random.choice(devisible_list)
        return_attack_array.append(random_num)
        for i in devisible_list:
            if sum(return_attack_array) + i > sum_sr:
                devisible_list.remove(i)
        if sum(return_attack_array) >= sum_sr:
            return return_attack_array


class Type_I:
    '''
    
    Schillinger Rhythm Type I: 
        takes a list of fractions f.e [a,b] or [a,b,c]
    stores lists of:
        [common_product], [[generators]], [resultant]
    and the complementary results:
        [[complementary_generators]], [complementary_resultant]
        
    '''
    common_product = []
    generators = []
    resultant = []

    complementary_generators = []
    complementary_resultant = []

    def __init__(self, fraction):
        self.common_product = []
        self.generators = []
        self.resultant = []
        self.complementary_generators = []
        self.complementary_resultant = []

        self.binary_syncronisation(fraction)

    def binary_syncronisation_result(self, fraction, seq_len):
        result = []
        count = 1
        flag = True
        for i in range(1, seq_len):
            for m in fraction:
                if i % m == 0:
                    flag = True
                    break
                else:
                    flag = False
            if flag:
                result.append(count)
                count = 1
            else:
                count += 1
        result.append(count)
        return result

    def binary_syncronisation(self, fraction):
        seq_len = np.prod(fraction)
        # fill in lists
        # print(seq_len)
        self.common_product = [1] * seq_len
        complementary_fraction = []
        for generator in fraction:
            num = int(seq_len / generator)
            self.generators.append([generator] * num)
            # complementary
            com_num = int(seq_len / num)
            complementary_fraction.append(num)
            self.complementary_generators.append([num] * com_num)

        self.resultant = self.binary_syncronisation_result(fraction, seq_len)
        self.complementary_resultant = self.binary_syncronisation_result(complementary_fraction, seq_len)


##schillinger II

class Type_II:
    '''
    
    Schillinger Rhythm Type II: 
        takes a list of a fraction f.e [a,b]
            where a > b!
    stores lists of:
        [common_product], [major_generator], [[minor_generators]], [resultant]
        
    '''
    common_product = []
    major_generator = []
    minor_generators = []
    resultant = []
    
    def __init__(self, fraction):
        
        if len(fraction) > 2:
            raise ValueError('only one fraction! f.e [3,2]')
        if fraction[1] > fraction[0]:
            raise ValueError('for Type II fraction a must be greater then b!')
            
        self.common_product = []
        self.major_generator = []
        self.minor_generators = []
        self.resultant = []
        
        self.binary_syncronisation(fraction)

    def binary_syncronisation(self, fraction):
        
        a = fraction[0]
        b = fraction[1]
        
        N = a - b + 1
        length = a * a
        
        self.common_product = [1]*length
        
        self.major_generator= [a]*a
        
        for n in range(N):
            self.minor_generators.append([b] * a)
            
        binary_list = [0] * length
        for i in range(0, a):
            binary_list[i*a] = 1
        
        major_places = [x*a for x in range(0, a)]
        
        for i, e in enumerate(self.minor_generators):
            pointer = major_places[i]
            for x in range(0, a):
                binary_list[(x*b)+pointer] = 1
        
        result_list = []
        counter = 1
        for i in range(1,len(binary_list)):
            if binary_list[i] == 1:
                result_list.append(counter)
                counter = 1
            else:
                counter += 1
        result_list.append(counter)
        self.resultant = result_list

# Grouping



# Grouping by pairs
# Balance 



class Grouping:
    '''
    
    Grouping:
    for resultant of Type I use:
        type_I_*
    for resultant of Type II use:
        type_II_*
    returns [measures, tones]:
        where measures a the total number of bars and tones are the units per bar.

    '''
    balance = []
    expansion = []
    contraction = []
    
    def __init__(self):
        
        self.balance = []
        self.expansion = []
        self.contraction = []
        
    # for Type I
    
    # returns -> [measures, tones]
    def type_I_grouping_by_ab(self, a,b):
        group_ab = [a*b,a*b]
        measures = int(group_ab[0]/group_ab[1])
        tones = int(a*b/measures)
        return [measures, tones]
    
    def type_I_grouping_by_a(self, a,b):
        group_a = [a*b,a]
        measures = int(group_a[0]/group_a[1])
        tones = int(a*b/measures)
        return [measures, tones]
    
    def type_I_grouping_by_b(self, a,b):
        group_b = [a*b,b]
        measures = int(group_b[0]/group_b[1])
        tones = int(a*b/measures)
        return [measures, tones]
    
    # for Type II
    
    def type_II_grouping_by_a(self, a,b):
        group = [a*a, a]
        measures = group[0]/group[1]
        tones = int(a*a)
        return [measures, int(tones/measures)]
    
    def type_II_grouping_by_aa(self, a,b):
        group = [a*a, a*a]
        measures = group[0]/group[1]
        tones = int(a*a)
        return [measures, int(tones/measures)]
    
    def type_II_grouping_by_b(self, a,b):
        group = [a*a, b]
        measures = group[0]/group[1]
        tones = int(a*a)
        return [measures, int(tones/measures)]
    
    ## Pairs
    
    def grouping_by_pairs(self, r, r_, a, b):
        
        #Balance
        #if a > 2*b or 3*b
        if a > b*2:
            divisor = a//b
            sum_r = sum(r)
            sum_r_ = sum(r_)
            sd = sum_r*divisor
            rest = sum_r_ - sd
            rr = r*2
            self.balance = r_ + rr + [rest]
            pass
        else:
            self.balance = r_ + r + [a*(a-b)]

        #Expansion
        self.expansion = r + r_
        #print(expansion)

        #Contraction
        self.contraction = r_ + r
        #print(contraction)
    
class CTS:
    '''
        schillinger coordination of time structures
        inputs [parts(or instruments)] [part order] [attack_pattern] [durations_pattern] 
            -> f.e. (4, [0,1,2,3], [1,3,1], [3,2,1,1,2,3])
        get_values()
            returns [pattern lenght(not needed with music21)] [[rhythm pattern arrays]] [[bar measures as fraction]]
        
    '''
    return_values = []

    def __init__(self, parts, order_of_parts, attack_pattern, durations_pattern):
        
        self.parts = parts
        self.order_of_parts = order_of_parts


        self.aa = attack_pattern
        self.PLi = parts
        self.PLa = len(self.aa)
        self.Nip = len(durations_pattern)*sum(attack_pattern)
        self.A = [self.aa]*self.PLi

        self.instrument_parts = [[] for x in range(len(self.A))]
        count = 0
        for i,e in enumerate(self.A):
            for r in e:
                self.instrument_parts[count%len(self.A)].append(r)
                count+=1

        self.durations_array = []
        for i in range(self.Nip):
            self.durations_array.append(durations_pattern[i%len(durations_pattern)])
            pass
        
        ##
        ar = self.generate_binary_test()
        fa = self.brainfuck_algo(ar[1])

        bars = int(len(self.durations_array)/len(durations_pattern))
        
        f = Fraction(bars,4)
        
        pattern_len  = sum(durations_pattern) # not needed
        
        self.return_values = [pattern_len, fa, [f.numerator,f.denominator]]
    
    def get_values(self):
        return self.return_values
        
    def generate_binary_test(self):
        binary_array = [[0 for x in range(self.Nip)] for x in range(self.PLi)]
        attacks_array = [[0 for x in range(self.Nip)] for x in range(self.PLi)]
        count = 0
        while count < self.Nip:
            for r in range(self.PLa):
                for x in range(self.PLi):
                    for y in range(self.instrument_parts[x][r]):
                        binary_array[self.order_of_parts[x]][count] = 1
                        attacks_array[self.order_of_parts[x]][count] = self.durations_array[count]
                        if count >= self.Nip-1:
                            return [binary_array, attacks_array]
                        count+=1
        return [binary_array, attacks_array]

    

    def brainfuck_algo(self,ata):
        flag = False
        test_array = [[] for x in range(self.PLi)]
        for op in self.order_of_parts:

            start_point = 0
            summe = 0
            for i, o in enumerate(ata[op]):

                if o is 0:
                    if not flag:
                        start_point = i-1
                        summe = 0
                        flag = True
                    for p in range(self.PLi):
                        p = (p + op)%self.PLi
                        summe += ata[p][i]
                else:
                    if flag:
                        flag = False
                        test_array[op].append(ata[op][start_point] + summe)
                    else:
                        if i > 0:
                            test_array[op].append(ata[op][i-1])

            ## end fill up
            if flag:
                test_array[op].append(ata[op][start_point] + summe)
            else:
                test_array[op].append(ata[op][i])

        return test_array
    