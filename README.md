FaceTag - Seamless Transportation
===

## Pitch

https://youtu.be/aBXFRKyUbwY

## Project Description

In today's increasingly populated world, it has become increasingly difficult to travel using public transports due to the bottlenecks it consists when people are moving in and out of the system.  We are focusing on building a solution for bottlenecked gateways in the daily commute; one such location would be the entry and exit points at metro stations. The idea is to use Azure's Cognitive API (facial recognition) to have an automated payment system for public transports (using an online wallet). Imagine FastTag-based tollways for human faces without the need for any hardware / physical cards. You can simply walk in; we'll scan the face and deduct the costs from your wallet.  This enables the people to just walk in, without any additional hardware (and/or RFID cards) and move through the public transport system without any wait times or unnecessary issues.

## Instructions to run

* Install python dependencies by running ```pip install -r requirements.txt```

* Execute ```python3 app.py``` to start the app

* Head over to localhost, you will be prompted with a signup page, enter any username and password. You may be required to login using these later on.

* Look into the camera, and register your face with the system.

* Head over to ```localhost/camera-in```, the url for any camera at the check in stage in the public transport system. Once you're recognised, close the tab.

* Open ```localhost/camera-out``` and repeat the process. You will be showed as checked-out in the system and money will be deducted from your wallet.

* Check ```localhost/dashboard``` to see the updated balance.



## Libraries Used

### facial recognition
1. Azure Face API module - for better and easy face recognition
2. OpenCV
3. Flask server
4. Python


User story
---
```gherkin=
Feature: Facial Recognition

  # The first example has two steps
  Scenario: User enters into X metro station
    Then the facial recognition platform looks for the user in database.
    Then An api is called for the transection of blockchain contract to init
    

  # The second example has three steps
  Scenario: User Exits from Y metro station
    Then The facial recognition looks for the user in database
    Then it calculates the fare for the distance travelled 
    Then An api is called for the deduction of fare from the wallet
```

Future Additions
---
```gherkin=
Density check in a station

  # Future addition would be to add density check of people using azure object detection
    in all metro stations to help with the wait time of the metro in a perticular station 
    at a perticular time based on the density and azure analitics

```

######  `Made in HackCBS hackathon`
