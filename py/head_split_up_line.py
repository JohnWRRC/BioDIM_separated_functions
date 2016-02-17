def head_split_up_line(line):
    line = line.split(' ')
    clean_line={}
    clean_line[line[0]]=line[len(line)-1]
    return clean_line