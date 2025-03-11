import string # importing the string module to get all the ascii lowercase

def high(x):
    letters = {l: i+1 for i, l in enumerate(string.ascii_lowercase)}
    words = x.split(' ')
    scores = {}
    for word in words:
        if word not in scores:
            scores[word] = sum([letters.get(l) for l in word])
    
    h = sorted(scores.items(), key=lambda x: x[1], reverse=True)[0][0]
    
    return h

if __name__ == '__main__':
    print(high("man i need a taxi up to ubud"))