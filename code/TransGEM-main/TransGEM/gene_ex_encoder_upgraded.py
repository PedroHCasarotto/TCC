import numpy as np

def value(gene_e: list, decimal_points: int=1) -> np.array:
        out=[]
        for sample in gene_e:
            sample = float(f"%.{decimal_points}f" % sample)
            vector=[sample]
            out.append(vector)
        return np.array(out)

def one_hot(gene_e: list, decimal_points: int=1, max_int_size: int=15, numbers_size: int=9) -> np.array:
        out=[]
        for sample in gene_e:
             bit = (1+15+numbers_size*decimal_points+1)
             sample = float(f"%.{decimal_points}f" % sample)
             vector = [0]*bit

             if sample > 0:
                 vector[0] = 1
             else:
                  sample = -sample

             vector[abs(int(sample)-max_int_size)+1] = 1

             for decimal in range(1, decimal_points+1):
                    if sample*decimal - int(sample*decimal) != 0:
                       if (sample*10**decimal - int(sample*10**decimal) >= 0.99):
                          value = int(round(sample*10**decimal) - round(sample*10**(decimal-1))*10)
                       else:
                          value = int(int(sample*10**decimal) - int(sample*10**(decimal-1))*10)
                       if value != 10:
                        index = 1+max_int_size+numbers_size*(decimal-1)+value
                        vector[index] = 1

             out.append(vector)

        return np.array(out)



def binary(gene_e: list, decimal_points: int=1) -> np.array:
        out=[]
        for sample in gene_e:
            sample=float(f"%.{decimal_points}f" % sample)
            bit = (1+5+4*decimal_points)
            vector= [0] * bit
            
            if sample > 0:
                vector[0] = 1
            else:
                sample = -sample
            
            vector[6-len(bin(int(sample))[2:]):6] = [int(j) for j in bin(int(sample))[2:]]

            
            for decimal in range(1, decimal_points+1):
                if sample*decimal - int(sample*decimal) != 0:
                    value = int(int(sample*10**decimal) - int(sample*10**(decimal-1))*10)
                    index_begin = (6+4*decimal) - len(bin(value)[2:])
                    index_end = (6+4*decimal)
                    vector[index_begin:index_end] = [int(j) for j in bin(int(value))[2:]]

            out.append(vector)
        return np.array(out)


def tenfold_binary(gene_e: list, decimal_points: int=1, max_int: int=15, decimals_to_int: int=1) -> np.array:
        decimal_points = decimal_points - decimals_to_int
        out=[]
        for sample in gene_e:
            sample = sample * 10**decimals_to_int
            sample=float(f"%.{decimal_points}f" % sample)
            int_lenth = len(bin(max_int*(10**decimals_to_int))[2:])
            bit = 1+int_lenth+4*(decimal_points)
            vector= [0] * bit
            
            if sample > 0:
                vector[0] = 1
            else:
                sample = -sample
            
            vector[1+int_lenth-len(bin(int(sample))[2:]):int_lenth+1] = [int(j) for j in bin(int(sample))[2:]]

            
            for decimal in range(1, decimal_points+1):
                if sample*decimal - int(sample*decimal) != 0:
                    value = int(int(sample*10**decimal) - int(sample*10**(decimal-1))*10)
                    index_begin = (1+int_lenth+4*decimal) - len(bin(value)[2:])
                    index_end = (1+int_lenth+4*decimal)
                    vector[index_begin:index_end] = [int(j) for j in bin(int(value))[2:]]

            out.append(vector)
        return np.array(out)