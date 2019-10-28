import mimetypes
import os
from urllib.parse import urlparse
import cv2 
import numpy as np

import DetectChars
import DetectPlates
import PossiblePlate
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse



app = Flask(__name__)


GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"


@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():
    num_media = int(request.values.get("NumMedia"))
    media_files = []
    media_sid = ""
    file_extension = ""
    for idx in range(num_media):
        media_url = request.values.get(f'MediaUrl{idx}')
        mime_type = request.values.get(f'MediaContentType{idx}')
        media_files.append((media_url, mime_type))

        req = requests.get(media_url)
        file_extension = mimetypes.guess_extension(mime_type)
        media_sid = os.path.basename(urlparse(media_url).path)

        with open(f"app_data/{media_sid}{file_extension}", 'wb') as f:
            f.write(req.content)

    
    response = MessagingResponse()
    if not num_media:
        msg = response.message("Send us an image of the incident!")
    else:
        blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()         # attempt KNN training
        if blnKNNTrainingSuccessful == False:  
            msg = response.message("\nerror: KNN traning was not successful\n")                             # if KNN training was not successful
            return str(response)                                                         # and exit program
        # end if

        imgOriginalScene  = cv2.imread("app_data/"+media_sid+file_extension)               # open image

        if imgOriginalScene is None:   
            msg = response.message("\nerror: image not read from file +"+media_sid+file_extension)                         # if image was not read successfully
            return str(response)                                         # and exit program
        # end if

        listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates

        listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates

        if len(listOfPossiblePlates) == 0:  
            msg = response.message("\nno license plates were detected\n")                        # if no plates were found
        else:                                                       # else
                    # if we get in here list of possible plates has at leat one plate

                    # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
            listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                    # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
            licPlate = listOfPossiblePlates[0]

            if len(licPlate.strChars) == 0:
                msg = response.message("no characters were detected")                     # if no chars were found in the plate
                return str(response)                                       # and exit program
            # end if
           # mycursor.execute("INSERT INTO data VALUES (%s,%s,%s,%s,%s)", ("", "", "","",""))
           # mydb.commit()
            msg = response.message("We have recorded the incident. Could you please send us a location of the incident by clicking the following link? license plate read from image = " + licPlate.strChars )

    return str(response)


if __name__ == "__main__":
    app.run()
