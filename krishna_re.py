def substitute(Pattern,replace_value,arg):
    string=""
    
    for i in arg:
        if i not in Pattern:
            string=string+i
        else:
            string=string+replace_value        
    print(string)