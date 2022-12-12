import sys
import re
import pandas as pd
line = sys.stdin.readline()
ab= ['i.e.','etc', 'e.g']

def tokenize(line, ab):
    line = re.sub(r'([\(\)”?:!;])', r' \g<1> ', line)
    line = re.sub(r'([^0-9]),', r'\g<1> ,', line)
    line = re.sub(r',([^0-9])', r', \g<1>', line)
    line = re.sub(r'([0-9]), ', r'\g<1> ,', line)
    line = re.sub(r'  +', ' ', line)

    output=[]
    for token in line.split(' '):
        if token == ' ':
            continue
        if token[-1] == '.' and token not in ab:
            token = token[:-1] + '.'
        output.append(token)

    return output

def tokenizer_print(i_d, line, ab):
    form = tokenize(line, ab)
    df = pd.DataFrame({'Form': form})
    df['LEMMA'] = '-'
    df['MISC'] = '-'
    df['UPOS'] = '-'
    df['XPOS'] = '-'
    df['FEATS'] = '-'
    df['HEAD'] = '-'
    df['DEPREL'] ='-'
    df['DEPS'] = '-'
    print('# sent_id', i_d)
    print('# text =', line)
    print(df)

i_d = 1
while line:
    line = tokenize_and_print(i, line, abbr)
    i += 1
    sys.stdout.write(line)
    line = sys.stdin.readline()

