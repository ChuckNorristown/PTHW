directions = ('north', 'south', 'east')
verbs = ('go', 'kill', 'eat')
nouns = ('the', 'in', 'of')
nouns = ('bear', 'princess')

def scan(sentence):
    action = []

    for word in sentence.split(' '):
        word = word.lower()
        try:
            if word in directions:
                action.append('directions', word)
            elif word in verbs:
                action.append('verbs', word)
            elif word in stops:
                action.append('stops', word)
            elif word in nouns:
                action.append('nouns', word)
            elif word.isdigit():
                action.append('number', int(word))
        except ValueError:
            actions.append('error', word)
        else:
            return (ERROR, word)