lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun',
    '1234': 'number',
    '3': 'number',
    '91234': 'number',
    'ASDFADFASDF': 'error',
    'IAS': 'error',
}

def scan(sentence):
    words = sentence.split()
    result = []

    for word in words:
        pair = (lexicon[word], word)
        result.append(pair)
    
    return result
