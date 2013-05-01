directions = ('north', 'south', 'east')
verbs = ('go', 'kill', 'eat')
stops = ('the', 'in', 'of')
nouns = ('bear', 'princess')

def scan(sentence):
    action = []

    for word in sentence.split(' '):
        
        try:
            number = int(word)
            word_tuple = ('number', number)
            action.append(word_tuple)

        except ValueError:            

            if word in directions:
                word_tuple = ('direction', word)
                action.append(word_tuple)
            elif word in verbs:
                word_tuple = ('verb', word)
                action.append(word_tuple)
            elif word in stops:
                word_tuple =('stop', word)
                action.append(word_tuple)
            elif word in nouns:
                word_tuple = ('noun', word)
                action.append(word_tuple)   
            else:
                word_tuple = ('error', word)
                action.append(word_tuple) 

    return action

