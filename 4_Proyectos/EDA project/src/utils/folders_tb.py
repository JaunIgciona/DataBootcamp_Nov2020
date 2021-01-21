import pandas as pd
import json
import re

def json_prep(serie):
    ''' 
    Returns a pd.Series with json elements as a pd.Series with python elements
    '''
    try: 
        #If '' aren't replaced by "", python won't recognise the json file  
        serie = serie.str.replace("\'", "\"")

        #now every element of the series is legible by python   
        serie = serie.apply(json.loads)                  
        return serie
    except:
        #print(error)
        safe_word = input('Try to fix errors?(Yes/No):')
        if safe_word == 'No':
            return
        else:
            serie = serie.str.replace("\'", "\"")
            l = []

            for el in range(0,len(serie)):
                try:
                    a = json.loads(serie[el])
                except:
                    l.append(el)

            print('errors column positions:',l)

            for er in l:
                if type(serie[er]) != str:
                    serie[er] = "[]"
                else:
                    #Every " that doesn't correspond to an opening or clossing string quote mark, such as 
                    # apostrophes, are replaced by a space to not be confuse by json functions
                    a = re.sub(r'(?<=[^{, :])"(?=[^,:}])'," ",serie[er])
                    serie[er] = a

            return json_prep(serie)