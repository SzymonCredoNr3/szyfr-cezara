import sys

class CezarCode:
    key: int
    content: str
    def __init__(self, content, imp_key):
        self.content = ""
        key = int(imp_key) % 26
        for char in content:
            new_char_code = ord(char) + key
            if 65 <= ord(char) <= 90:  # duże litery
                if new_char_code < 65:
                    new_char_code += 26
                elif new_char_code > 90:
                    new_char_code -= 26
            elif 97 <= ord(char) <= 122:  # małe litery
                if new_char_code < 97:
                    new_char_code += 26
                elif new_char_code > 122:
                    new_char_code -= 26
            else:
                new_char_code = ord(char)

            new_char = chr(new_char_code)
            self.content+= new_char

    def __repr__(self):
        return self.content
nsfw = {
    "k": 0,
    "m": '',
    'o': None
}
content = None
for arg in sys.argv[1:]:
    if arg[0] == '-':
        try:
            nsfw[arg[1]] = arg[3:]
        except IndexError:
            raise AttributeError("This program dose not have a argument " + arg[1:2])
    else:
        content = arg
if content is None:
    raise AttributeError("content not defined")
key = int(nsfw['k'])
def code():
    global key
    print(CezarCode(content, key))
def decode():
    global key
    print(CezarCode(content, key*-1))
def file():
    global content, key
    with open(content, mode='r') as file:
        content = file.read()
    return content
def file_code():
    global key, nsfw
    out = CezarCode(file(), key*-1)
    print(out)
    if nsfw['o'] is not None:
        with open(nsfw['0'], 'w') as fife:
            fife.write(out)
def file_decode():
    global key
    out = CezarCode(file(), key*-1)
    print(out)
    if nsfw['o'] is not None:
        with open(nsfw['0'], 'w') as fife:
            fife.write(out)
mode_nsfw = {
    '': code,
    'code': code,
    'decode': decode,
    'file-code': file_code,
    'file-decode': file_decode
}

try:
    mode_nsfw[nsfw['m']]()
except IndexError:
    raise AttributeError("This mode is invalid")