# docs: https://docs.google.com/document/d/1_ITk4WFkY3zLkIEg80tKjag6hkRaRX-PbLUHKrf5U6U/edit
def count_decodings(string): 
    def count_decodings_rec(string, count):
        if string == '':
            return 1

        count = count_decodings_rec(string[1:], count) # 111

        # if len(string) == 2:
        #     return 1
        if len(string) >= 2 and (
                string[0] == '1' and '0' <= string[1] <= '9' or
                string[0] == '2' and '0' <= string[1] <= '6'
        ): # 111
            count += count_decodings_rec(string[2:], count) # 1
        
        return count

    return 0 if string == '' else count_decodings_rec(string, 0) # | 

assert count_decodings('') == 0
assert count_decodings('1') == 1
assert count_decodings('11') == 2
assert count_decodings('111') == 3
assert count_decodings('1111') == 5
assert count_decodings('11161') == 5
assert count_decodings('12161') == 5
assert count_decodings('13161') == 4
assert count_decodings('111') == 3
