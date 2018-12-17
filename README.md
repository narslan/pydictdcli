# pydictdcli
pydictdcli is an interactive command-line dictd client, built on
[prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)
and [wordbook](https://github.com/tomplus/wordbook)

## Usage
```
> $python dictdclient.py
```
Select a database then
```
   db   # show available dictd databases
   db 8 # select an available dictd database
        # WordNet is the 8.th dictionary on my localserver
```

Type in a word then press return  
```
   flask 
    flask
    n 1: bottle that has a narrow neck
    2: the quantity a flask will hold [syn: {flask}, {flaskful}]
```

## TODO
- [ ] colourising the returned definiton
- [ ] make to connect other dictd servers, not just to local one 


