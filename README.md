# SEPM, The A-team 


### Pydocs
Generates automated documentation
* _Usage_: 
(from a specific _module_ directory) ```pydoc -w ./*.py; mv ./*.html ../../docs/;```
* _Note_:_ Have to remove infinite loops that are invoked e.g. ```while 1:
    ui.tic()```