directions = ('north', 'south', 'east', 'west')
verbs = ('go', 'kill', 'eat', 'sleep')
stops = ('the', 'in', 'of', 'out')
nouns = ('bear', 'princess', 'cave', 'castle')

def scan(sentence):
    action = []

    for word in sentence.split(' '):
        
        try:
            number = int(word)
            word_tuple = ('number', number)
            action.append(word_tuple)

        except ValueError:            

            if word.lower() in directions:
                word_tuple = ('direction',word)
                action.append(word_tuple)
            elif word.lower() in verbs:
                word_tuple = ('verb', word)
                action.append(word_tuple)
            elif word.lower() in stops:
                word_tuple =('stop', word)
                action.append(word_tuple)
            elif word.lower() in nouns:
                word_tuple = ('noun', word)
                action.append(word_tuple)   
            else:
                word_tuple = ('error', word)
                action.append(word_tuple) 

    return action

