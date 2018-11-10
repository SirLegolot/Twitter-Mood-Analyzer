from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2018-11-09',
    iam_apikey='LsOj4gKV9nj5tk9nEv08fqu6k1-qhYOmzUJO3v_rqHn8',
    url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api'
)

def analyzeToneRaw(tweet):
    text = tweet
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json', False
    ).get_result()
    return tone_analysis
    

def analyzeTone(tweet):
    raw = analyzeToneRaw(tweet)
    tones = raw["document_tone"]["tones"]
    if len(tones)==0:
        return "Neutral"
    elif len(tones)==1:
        return tones[0]["tone_name"]
    else:
        emotions = []
        for tone in tones:
            emotions.append(tone["tone_name"])
        return emotions
    
# print(analyzeTone("I hate this one kid. It is making me very sad."))
