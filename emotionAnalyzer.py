from twitterFns import getTweets, getTweetsFast
from watsonFns import analyzeTone
from graphics import runDrawing

def emotionAnalyzer(username, num):
    emotions = []
    tweets = getTweetsFast(username, num)
    i=0
    for tweet in tweets:
        tone = analyzeTone(tweet)
        emotions.append(tone)
        i+=1
    return emotions

# print(emotionAnalyzer("PidiBuster", 20))

def flatten(lst):
    # base case returns the empty list if the lst is empty
    if len(lst)==0:
        return []
    else:
        # if the first element is a list, runs the function recursively on
        # that element and runs a rescursion on the remaining elements
        if isinstance(lst[0], list):
            return flatten(lst[0]) + flatten(lst[1:])
        else:
            # adds the list of the element to the rest of the recursively
            # flattened list
            return [lst[0]] + flatten(lst[1:])

def countEmotions(lst):
    lst = flatten(lst)
    anger = lst.count("Anger")
    joy = lst.count("Joy")
    fear = lst.count("Fear")
    analytical = lst.count("Analytical")
    tentative = lst.count("Tentative")
    sadness = lst.count("Sadness")
    return [("Anger", anger), ("Analytical", analytical), ("Joy", joy), ("Fear", fear),  ("Tentative", tentative), ("Sadness", sadness)]
    
def emotionAnalyzerRaw(username, num):
    emotions = emotionAnalyzer(username, num)
    countedEmotions = countEmotions(emotions)
    return countedEmotions

# runDrawing(username, countedEmotions)
# print(emotionAnalyzer("elonmusk", 20))

# emotionAnalyzerGraphics("ye", 20)
