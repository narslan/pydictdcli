import wordbook

class DictSession():
    
    
    def __init__(self):
       self.dbs = []
       self.dblength = 0
       self.selected = None
               
    async def showdb(self):
        dictb = wordbook.DictBase()
        await dictb.connect()
        await dictb.client('wordbook/server-status.py')
        info = await dictb.show_db()
        for i, line in enumerate(info):
            lineslice = line.index(" ")
            shortdesc = line[0:lineslice]
            longdesc = line[lineslice:]
            print('({}) => {} = {} '.format(i +1 , shortdesc, longdesc))

    async def dblist(self):
        dbstructure =[]
        dictb = wordbook.DictBase()
        await dictb.connect()
        await dictb.client('wordbook/server-status.py')
        info = await dictb.show_db()
        for i, line in enumerate(info):
            lineslice = line.index(" ")
            shortdesc = line[0:lineslice]
            longdesc = line[lineslice+1:]
            dbstructure.append([shortdesc,longdesc])
        self.dbs = dbstructure
        self.dblength = len(dbstructure)
    
    async def lookup(self, database, word):
        dictb = wordbook.DictBase()
        await dictb.connect()
        await dictb.client('wordbook/server-status.py')
        definition = await dictb.define(database,word)
        return definition
