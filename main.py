import sys
# from filecmp import cmp
from itertools import permutations
from os import walk
from zipfile import ZipFile

import corefunctions

from tqdm import tqdm

if not sys.argv.__contains__('--gen-only'):
    filename = input('Zip file name: ')


passwords: set[str] = set()
temp_passwords: set[str] = set()

if not sys.argv.__contains__('--use-list-file'):
    print('Phase 1: Load word lists --------')
    for root, dirs, files, in walk('wordlists'):
        for file in files:
            print(f'Word list found: {file}')
            print('Loading...')
            _list = open(f'wordlists/{file}', 'r').read()
            print('Loaded')
            print('Preparing...')
            [temp_passwords.add(p) for p in _list.splitlines()]
            print('Prepared')
            del _list
    print('Phase 2: Keywords ---------------')
    try:
        keywords = open('keywords', 'r').read().splitlines()
        print('Putting all keywords into the list...')
        for keyword in tqdm(keywords, disable=False):
            temp_passwords.add(keyword)
        print('Combining...')
        temp_combinations = permutations(keywords, 2)
        [temp_passwords.add(i) for i in map(lambda x: x[0] + x[1], temp_combinations)]
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
passwords = temp_passwords.copy()
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
