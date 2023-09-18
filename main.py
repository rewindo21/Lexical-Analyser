import re

keyword_list = ["False", "class", "from", "or", "None", "continue", "global", "pass", "break",
                "True", "def", "if", "raise", "and", "del", "import", "return", "for", "input"
                "as", "elif", "in", "try", "assert", "else", "is", "while", "not", "print",
                "async", "except", "lambda", "with", "await", "finally", "nonlocal", "yield", "self"]
# help("keywords")

operator_list = ["+", "-", "*", "/", "**", "//", "%",
                 "=", "+=", "-=", "*=", "/=", "%=", "**=", "//=", "&=", "|=", "^=", ">>=", "<<=", 
                 "==", "!=", "<", ">", "<=", ">=",
                 "&", "|", "^", "~", "<<", ">>"]

symbol_list  = [",", ":", "(", ")", "[", "]", "{", "}", "\\"]


# Remove singel-line comments
def slc_remover(words):
    while '#' in words:
        a = words.index('#')
        b = words.index('\n', a)
        del words[a:b+1]
    return list


# Remove multi-line comments
def mlc_remover(words):
    c = 0
    for w in words:
        if words[c] == "'" and words[c+1] == "'" and words[c+2] == "'":
            d = words.index("'", c+3)
            del words[c:d+3]
            c += 1
        else:
            c += 1
    return list


# Remove new lines
def nl_remover(words):
    while '\n' in words:
        e = words.index('\n')
        del words[e]
    return list


def analyser(words):
    inner_code = 1
    f = 0
    print('----------------------------')
    print('< ' + 'CODE' + ' | ' + '  DATA' + '  |  ' + 'TYPE' + '   >')
    print('----------------------------')
    for w in words:
        if w == "\'" or w == "\"":
            print('< ' + str(inner_code).center(4) + ' | ' + w.center(7) + ' | ' + 'SYMBOL'.center(7) + ' >')
            f += 1
        if f % 2 != 0 and (w != "\'" and w != "\""):
            print('< ' + str(inner_code).center(4) + ' | ' + w.center(7) + ' | ' + 'STR'.center(7) + ' >')
        else:
            if w in keyword_list:
                print('< ' + str(inner_code).center(4) + ' | ' + w.center(7) + ' | ' + 'KEYWORD'.center(7) + ' >')
            else:
                if w in operator_list:
                    print('< ' + str(inner_code).center(4) + ' | ' + w.center(7) + ' | ' + 'OPERATOR'.center(7) + ' >')
                else:
                    if w in symbol_list:
                        print('< ' + str(inner_code).center(4) + ' | ' + w.center(7) + ' | ' + 'SYMBOL'.center(7) + ' >')
                    else:
                        if w.isdigit():
                            print('< ' + str(inner_code).center(4) + ' | ' + w.center(7) + ' | ' + 'INT'.center(7) + ' >')
                        else:
                            if w.replace(".", "", 1).isdigit():
                                print('< ' + str(inner_code).center(4) + ' | ' + w.center(7) + ' | ' + 'FLOAT'.center(7) + ' >')
                            else:
                                if w.isidentifier():
                                    print('< ' + str(inner_code).center(4) + ' | ' + w.center(7) + ' | ' + 'ID'.center(7) + ' >')
        inner_code += 1
    print('----------<END>-------------')


if __name__ == "__main__":
    pyfile = input("Enter file name: ")
    with open(pyfile, 'r') as f:
        lines = f.read()
        words = re.findall(r"[a-zA-Z_]+|[(\d*\.)?\d]+|[0-9_]+|[\S]|[\n]", lines)
    slc_remover(words)
    mlc_remover(words)
    nl_remover(words)
    analyser(words)
