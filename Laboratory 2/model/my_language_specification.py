separators = ['[', ']', '{', '}', '(', ')', ';',' ', ':']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '&&', '||', '!', '!=', '&', '~',
             '|', '^', '++', '--', ',']
reservedWords = ['char' ,'nmbr', 'strng', 'array', 'rd', 'wrt', 'chck','is', 'true', 'false', 'let', 'until', 'and', 'else', 'for']

everything = separators + operators + reservedWords
codification = dict([(everything[i], i + 2) for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1