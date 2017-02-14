import numpy as np

class SchillingerRythm_I:

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

class SchillingerRythm_II:
    
    common_product = []
    major_generator = []
    minor_generators = []
    resultant = []
    
    def __init__(self, fraction):
        
        if len(fraction) > 2:
            raise ValueError('only 2 fractions!')
        if fraction[1] > fraction[0]:
            raise ValueError('for Type II fraction 1 must be greater!')
            
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

balance = []
expansion = []
contraction = []

class Grouping:
    
    def __init__(self):
        pass
    
    # Type I
    
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
    
    # Type II
    
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
            devisor = a//b
            sum_r = sum(r)
            sum_r_ = sum(r_)
            sd = sum_r*devisor
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
    
    
    