from prompt_toolkit.shortcuts import PromptSession
from prompt_toolkit.eventloop.defaults import use_asyncio_event_loop
from prompt_toolkit.patch_stdout import patch_stdout

import asyncio
import dictlib

loop = asyncio.get_event_loop()


async def interactive_shell():

    # Create Prompt.
    session = PromptSession()

    nds = dictlib.DictSession()
    try:
        await nds.dblist()
    except ConnectionRefusedError as e:
        print(e)


    # Run echo loop. Read text from stdin, and reply it back.
    while True:
        try:
            input = await session.prompt('>',async_=True)
        except (EOFError, KeyboardInterrupt):
            return

        try:
            input = input.strip()
            inindex = input.index(" ")
            command = input[0:inindex]
            argument = input[inindex+1:]
            selection = None
            try:
               selection = int(argument)
            except Exception:
                print("argument must be an integer")

            if command == 'db' and selection <= nds.dblength:
                print ("setting database to {}".format(nds.dbs[selection-1][1]))
                nds.selected = selection
            else:
                print ("choose one of the database numbered between {} and {}".format(1,nds.dblength))
        except Exception:
            if input == 'db':
                await nds.showdb()
            elif nds.selected is None:
                print ('Select a database with db')
            else:
                #print ("{} is searched in {}".format(input, nds.dbs[nds.selected-1][1]))
                result = await nds.lookup(nds.dbs[nds.selected-1][0],input)
                for x in result[1:]:
                    print(x)
def main():
    # Tell prompt_toolkit to use the asyncio event loop.
   use_asyncio_event_loop()
   with patch_stdout():
    shell_task = asyncio.ensure_future(interactive_shell())
    loop.run_until_complete(shell_task)
    print('Quitting event loop. Bye.')


if __name__ == '__main__':
    main()
