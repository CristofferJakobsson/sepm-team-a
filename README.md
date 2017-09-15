# SEPM, The A-team 


### Pydocs
Generates automated documentation
* _Usage_: 
(from the docs directory) ```pydoc -w ../src/module/*.py```
* _Example_: ```pydoc -w ../src/user_interface/*.py```
* _Note_:_ Have to remove infinite loops that are invoked e.g. ```while 1:
    ui.tic()```