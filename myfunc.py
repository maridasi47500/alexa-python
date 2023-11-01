import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    print("hi")
    try:
        shouldendsessions=False
        myexpr = event["request"]["type"]
        myhash=None
        print(myexpr)
        match myexpr:
            case "LaunchRequest":
                speak = "régiment garde a vous "
                speak += "<audio src=\"%s\"></audio>" % 'https://armymusic.s3.amazonaws.com/legav.mp3'

            case _:
                myotherexpr = event["request"]["intent"]["name"]
                match myotherexpr:
                    case "AMAZON.StopIntent":
                        shouldendsessions=True
                        speak = "ok ! si tu dois partir maintenant, à bientôt!"
                    case "AMAZON.HelpIntent":
                        speak = "parlons d'emploi, de travail ou de ce que tu veux !!"
                    case "AMAZON.CancelIntent":
                        speak = "ok"
                    case "garde_a_vous":
                        speak = "<audio src=\"%s\"></audio>" % 'https://armymusic.s3.amazonaws.com/legav.mp3'

                    case "ouvrez_le_banc":
                        speak = "<audio src=\"%s\"></audio>" % 'https://armymusic.s3.amazonaws.com/leban.mp3'
                    case "au_drapeau":
                        speak = "<audio src=\"%s\"></audio>" % 'https://armymusic.s3.amazonaws.com/ledrapeau.mp3'

                    case "entre_terre_et_mer":
                        speak = "<audio src=\"%s\"></audio>" % 'https://armymusic.s3.amazonaws.com/entreterreetmer.mp3'

    except:
        speak = "Désolée , il y a eu une erreur "+e.message
    if not myhash:
    	myhash= {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>"+speak+"</speak>"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "SSML",
                    "ssml": "<speak>J'ai pas compris, comment ?</speak>"
                }
            },
            "shouldEndSession": shouldendsessions
        },
        "userAgent": "ask-node/2.3.0 Node/v8.10.0",
        "sessionAttributes": {}
    	}
    return myhash
