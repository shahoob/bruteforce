from tqdm import tqdm


def generate(charlist='', maxletters=3):
    passwords = []
    for current in range(maxletters):
        a = [i for i in charlist]
        for x in range(current):
            a = [y + i for i in charlist for y in a]
        passwords = passwords + a
    return passwords


from zipfile import ZipFile


def crack(passwords: list[str] or tqdm, file: ZipFile):
    currentPass = ''
    for password in passwords:
        try:
            file.setpassword(password.encode('ascii'))
            file.extractall(path='result')
            currentPass = password
            break
        except:
            pass
    if currentPass != '':
        print(f'Found: {currentPass}')
        print('Extracted files at folder \'result\'')
    else:
        print('not found')

'''
def leftpop(_list: list):
    __list = _list[:]
    __list.reverse()
    __list.pop()
    __list.reverse()
    _list = __list

def groupStr(list_to_fix: tuple[str] or list[str] or iter[str], seperator: str = ''):
    final: list_to_fix[str] = []
    queue = []
    queue_loop: list[str] = list_to_fix[:]
    for string in list_to_fix:
        if string == seperator or queue_loop.__len__() == 0:
            string_result = ''
            for s in queue:
                string_result += s
            queue = []
            final.append(string_result)
            string_result = ''
        queue.append(string)
        leftpop(queue_loop)
    return final
'''
