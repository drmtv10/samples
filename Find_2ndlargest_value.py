#!/bin/python

# Implement a function to find second largest value from a file.
# each line in the file is 32-bit integer and file has at least 2 lines
# file may be up to 100 million lines as well, so
# solution needs to scale.

# generator / yield based implementation desired?  How?

def process_file(fname, mxval):
    #mxval = list()
    print fname
    with open(fname, 'r') as fobj:
        counter = 0
        for line in fobj:
            print counter, line
            value_in = int(line)
            if counter == 0 :
                mxval.append(value_in)
            elif counter == 1 :
                if mxval[0] < value_in:
                    mxval.append(mxval[0])
                    mxval[0] = value_in
                else:
                    mxval.append(value_in)
            elif counter > 1 :
                if mxval[0] < value_in:
                    mxval[1] = mxval[0] # prev max - 2nd max
                    mxval[0] = value_in # max
                elif mxval[1] < value_in:
                    mxval[1] = value_in
            print counter, mxval
            counter += 1
    return

def process_val(val, mxval):
    if len(mxval) < 1:
        mxval.append(val)
    elif len(mxval) < 2:
        if mxval[0] < val:
            mxval.append(mxval[0])
            mxval[0] = val
        else:
            mxval.append(val)
    elif mxval[0] < val:
        mxval[1] = mxval[0] # prev max - 2nd max
        mxval[0] = val      # max
    elif mxval[1] < val:
        mxval[1] = val

def process_using_generator(fobj, mxval):
    for line in fobj:
        value_in = int(line)
        yield value_in
     
def process_file_using_generator(fname, mxval):
    print fname
    with open(fname, 'r') as fobj:
        for val in process_using_generator(fobj, mxval):
            process_val(val, mxval)
        print mxval
    return

if __name__ == '__main__':
    filename = raw_input('Enter file name:')
    filename.rstrip()
    max_val = list()
    process_file_using_generator(filename, max_val)
    if len(max_val) == 2:
        print 'Processed file: {} for 2nd largest value {}'.format( filename, max_val[1])
    else:
        print 'failed to process file:', filename
