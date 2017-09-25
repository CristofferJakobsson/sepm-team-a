# SEPM, The A-team 

## Dependencies
* Python 3.6
* Pygame

## To generate documentation using pydocs
Generates automated documentation
* _Usage_: 
(from a specific _module_ directory) ```pydoc -w ./*.py; mv ./*.html ../../docs/;```
* _Note_:_ Have to remove infinite loops that are invoked e.g. ```while 1:
    ui.tic()```
* Documentation can then be viewed in the _docs_ directory as html files that can be viewed in the browser

## How to run
* Make sure you meet all required dependencies
* From the _user_interface_ directory, type: ```python3 user_interface.py``` in a terminal window