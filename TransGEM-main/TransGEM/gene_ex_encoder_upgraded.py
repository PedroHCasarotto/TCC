import numpy as np

def value(gene_e: list, decimal_points: int=1) -> np.array:
        out=[]
        for sample in gene_e:
            sample = float(f"%.{decimal_points}f" % sample)
            vector=[sample]
            out.append(vector)
        return np.array(out)

def one_hot(gene_e: list, decimal_points: int=1, max_int: int=10, numbers_size: int=9) -> np.array:
        out=[]
        for sample in gene_e:
             bit = (1+max_int+numbers_size*decimal_points+1)
             sample = float(f"%.{decimal_points}f" % sample)
             vector = [0]*bit

             if sample > 0:
                 vector[0] = 1
             else:
                  sample = -sample

             vector[abs(int(sample)-max_int)+1] = 1

             for decimal in range(1, decimal_points+1):
                    if sample*decimal - int(sample*decimal) != 0:
                       value = int(int(sample*10**decimal) - int(sample*10**(decimal-1))*10)
                       if (value != 10) & (value != 0):
                        index = 1+max_int+numbers_size*(decimal-1)+value
                        vector[index] = 1
             out.append(vector)

        return np.array(out)


def binary(gene_e: list, decimal_points: int = 6, max_int: int = 10) -> np.array:
    out = []
    scale = 10 ** decimal_points  # Scaling factor to preserve decimal precision
    
    for sample in gene_e:

        scaled_sample = int(sample * scale)

        integer_part = scaled_sample // scale

        fractional_part = scaled_sample % scale

        bit = 1 + max_int.bit_length() + decimal_points * 4
        vector = [0] * bit

        # Handle the sign bit (first bit)
        if sample >= 0:
            vector[0] = 1
        else:
            scaled_sample = -scaled_sample
            integer_part = -integer_part

        integer_bin = bin(integer_part)[2:]
        value = [int(j) for j in integer_bin]
        vector[1 + max_int.bit_length() - len(integer_bin):1 + max_int.bit_length()] = value

        for i in range(decimal_points):
            fractional_digit = (fractional_part // (10 ** (decimal_points - 1 - i))) % 10
            binary_value = bin(fractional_digit)[2:].zfill(4)
            index_begin = 1 + max_int.bit_length() + 4 * i
            vector[index_begin:index_begin + 4] = [int(b) for b in binary_value]

        out.append(vector)

    return np.array(out)


def tenfold_binary(gene_e: list, decimal_points: int=1, max_int: int=10, decimals_to_int: int=None) -> np.array:
        if decimals_to_int == None: decimals_to_int = decimal_points
        decimal_points = decimal_points - decimals_to_int
        out=[]
        for sample in gene_e:
            sample = sample * 10**decimals_to_int
            sample=float(f"%.{decimal_points}f" % sample)
            int_lenth = len(bin(max_int*(10**decimals_to_int))[2:]) if max_int != 0 else len(bin(10**decimals_to_int)[2:])
            bit = 1+int_lenth+4*(decimal_points)
            vector= [0] * bit
            
            if sample > 0:
                vector[0] = 1
            else:
                sample = -sample
            
            vector[1+int_lenth-len(bin(int(sample))[2:]):int_lenth+1] = [int(j) for j in (bin(int(sample))[2:])]

            
            for decimal in range(1, decimal_points+1):
                if sample*decimal - int(sample*decimal) != 0:
                    value = int(int(sample*10**decimal) - int(sample*10**(decimal-1))*10)
                    index_begin = (1+int_lenth+4*decimal) - len(bin(value)[2:])
                    index_end = (1+int_lenth+4*decimal)
                    vector[index_begin:index_end] = [int(j) for j in (bin(int(value))[2:])]

            out.append(vector)
        return np.array(out)