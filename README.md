# Report for Assignment 1 resit

## Project Music Assistant

Name: Music Assistant - Server

URL: https://github.com/music-assistant/server

Number of lines of code and the tool used to count it: 35140

Programming language: Python

## Coverage measurement with existing tool

Tool: Coverage.py

URL: https://coverage.readthedocs.io/

Run: 

     pytest --cov=.

     coverage report -m
     
     coverage html

<img width="1422" alt="test-before-html-1" src="https://github.com/oykusen/music-assistant-test/assets/122273200/b49f8c65-929e-4f59-a737-663d195bd049">

<Show the coverage results provided by the existing tool with a screenshot>

## Coverage improvement

### Individual tests



#### Function 1: test_get_track():

URL: https://github.com/oykusen/music-assistant-test/blob/c80a6018c780aacd3c516c56370c52bea1f7e1e0/tests/client/test_music.py#L52

Old Result: (%0)

<img width="735" alt="function1-old-result" src="https://github.com/oykusen/music-assistant-test/assets/122273200/74930ee3-3560-4a18-92ad-5a3196ffce5a">

New Result: (%44)

<img width="750" alt="function1-new-result" src="https://github.com/oykusen/music-assistant-test/assets/122273200/1197f2eb-5a47-45ff-aa6f-36c0829b21e1">


Improvement Amount: %44

Why?: test_get_track function checks the parameters and return type of the get_track function. It also uses other variables and imports within the music.py file

#### Function 2: test_get_artist():

URL: https://github.com/oykusen/music-assistant-test/blob/c80a6018c780aacd3c516c56370c52bea1f7e1e0/tests/client/test_music.py#L69

Old Result: (%44)

<img width="750" alt="function2-old-result" src="https://github.com/oykusen/music-assistant-test/assets/122273200/41059bf9-3e2e-43fc-ae47-a5cfdad02764">

New Result: (%46)

<img width="743" alt="function2-new-result" src="https://github.com/oykusen/music-assistant-test/assets/122273200/7ded1d85-6e90-4b80-8a52-fcab30f157f5">

Why? test_get_artist function checks the get_artist functions return type and elibigle artist object's information.


### Overall

Old Result: (%12)

<img width="1422" alt="test-before-html-1" src="https://github.com/oykusen/music-assistant-test/assets/122273200/3a18858e-5fd8-4366-a7f9-13f12dcd246e">

New Result: (%14)

<img width="1422" alt="1" src="https://github.com/oykusen/music-assistant-test/assets/122273200/3e5ea6e1-4ad1-4672-b64a-63cc0ad48a6b">
