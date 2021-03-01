# Usage

## Setup

1. Get a bunch of word lists where each word is separated by line
   Then put your word lists in the folder `wordlists`
   inside of where you have installed `bruteforce`.
   
2. Put your keywords in a file named `keywords` without any file extensions _(optional)_
    In which that again, where words are separated by line.
    
    The keywords will be then used to create combinations of passwords together.

3. Create a folder called `result` where when successful, will extract files from the password-protected zip file.
    If you're only going to generate a list, then this is _optional_.
   
## Getting started

1. Run `main.py`
   
    If you're on Unix:
   ```
    python3 main.py
   ```
   
    If you're on Windows with the Python launcher installed:
    ```
    py main.py
    ```
   > If you want to generate a list only, add `--gen-only` at the end of your command

Then follow the prompts.

2. Enter the zip file name _(skipped if you want to generate a list only)_
3. Wait.
