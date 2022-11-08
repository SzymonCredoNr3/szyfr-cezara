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
    "m": ''
}
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

key = nsfw['k']
print(content, nsfw, CezarCode(content, key))