import sys
# from filecmp import cmp
from itertools import permutations
from os import walk
from zipfile import ZipFile

import corefunctions

from tqdm import tqdm

if not sys.argv.__contains__('--gen-only'):
    filename = input('Zip file name: ')

'''
charLists = [
    'abcdefghijklmnopqrstuvwxyz!@#$%^&*()-=_+?><":{}|\][;\',./0123456789',
    'abcdefghijklmnopqrstuvwxyz!@#0123456789'
]
charListName = ''
'''
passwords: list[str] = []
'''
maxletters = int(input('Number of max letters: '))
filename = input('Zip file name: ')
currentCharList = ''
chosenCharList = input('Which character list: Complex (0, default), Simple (1), or Custom (custom)?: ')
if chosenCharList == 'custom':
    charListName = input('Name of custom character list (leave blank to not save the list): ')
    fCharListFileName = f'{charListName}.charlist.bruteforce'
    if isfile(fCharListFileName):
        print('Loading custom character list...')
        currentCharList = open(fCharListFileName, 'r').read()
        print('Loaded')
    else:
        currentCharList = input('Enter characters: ')
        if charListName != '':
            print('Saving custom character list...')
            with open(fCharListFileName, 'w') as f:
                f.write(currentCharList)
                f.close()
            print(f'Saved custom character list as {fCharListFileName}')
else:
    i = 0
    if chosenCharList != '': i = int(chosenCharList)
    currentCharList = charLists[i]

fListFileName = f'{maxletters}.list.bruteforce'

if isfile(fListFileName):
    print('Loading cached list...')
    temp_passwords = []
    with open(fListFileName, 'r') as f:
        for line in f: temp_passwords.append(line)
    print('Loaded')
    print('Preparing...')
    for password in tqdm(temp_passwords):
        passwords.append(password.rstrip('\n'))
    print('Prepared')
else:
    print('Generating list...')
    \'\'\'
    for current in range(maxletters):
        a = [i for i in currentCharList]
        for x in range(current):
            a = [y + i for i in currentCharList for y in a]
        passwords = passwords + a
    \'\'\'
    passwords = corefunctions.generate(charlist=currentCharList, maxletters=maxletters)
    print('Generated list')
    print('Saving list...')
    with open(fListFileName, 'w') as f:
        for password in tqdm(passwords):
            f.write(password)
            f.write('\n')
        f.close()
    print(f'List saved as {fListFileName}')
'''
temp_passwords: list[str] = []

if not sys.argv.__contains__('--use-list-file'):
    print('Phase 1: Load word lists --------')
    for root, dirs, files, in walk('wordlists'):
        for file in files:
            print(f'Word list found: {file}')
            print('Loading...')
            _list = open(f'wordlists/{file}', 'r').read()
            print('Loaded')
            print('Preparing...')
            _list = _list.splitlines()
            temp_passwords.extend(_list)
            print('Prepared')
            del _list
    print('Phase 2: Keywords ---------------')
    try:
        keywords = open('keywords', 'r').read().splitlines()
        print('Putting all keywords into the list...')
        for keyword in tqdm(keywords, disable=False):
            temp_passwords.append(keyword)
        print('Combining...')
        temp_combinations = permutations(keywords, 2)
        temp_passwords.extend(map(lambda x: x[0] + x[1], temp_combinations))
        print('Combined')
    except FileNotFoundError:
        print('keywords file not found, skipping...')
else:
    list_path = input('Path pointing to the list to load: ')
    print(f'Loading \'{list_path}\'...')
    _list = open(list_path, 'r').read()
    print('Loaded')
    print('Preparing...')
    _list = _list.splitlines()
    temp_passwords.extend(_list)
    print('Prepared')
    del _list

print('Final phase: Finalization -------')
print('Finalizing...')
for password in tqdm(temp_passwords):
    passwords.append(password)
print('Finalized')
del temp_passwords


if not sys.argv.__contains__('--gen-only'):
    print(f'pickLock(\'lock.zip\', passwords=passwords)')
    file = ZipFile(filename)

    print('Picking...')
    corefunctions.crack(tqdm(passwords), file)
else:
    list_path = input('Path to save list: ')
    print('Saving list...')
    with open(list_path, 'w') as f:
        for password in tqdm(passwords):
            f.write(password + '\n')
    print(f'List saved at {list_path}')
