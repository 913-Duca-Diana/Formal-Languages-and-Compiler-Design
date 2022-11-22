# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Model.my_language_specification import *
from Model.pif import ProgramInternalForm
from Model.scanner import isConstant, isIdentifier, tokenGenerator
from Model.st import SymbolTable

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fileName= input("Insert the name of the file you want to use: ")
    file=open(fileName, 'r')
    pif1 = open("pif.txt", "w+")
    st = open("st.txt", "w+")
    f = open("output.txt", "w+")

    for line in file:
        f.write(line)
        f.write('\n')

    with open(fileName, 'r') as file:
        for line in file:
            print([token for token in tokenGenerator(line, separators)])

    symbolTable=SymbolTable()
    pif= ProgramInternalForm()

    with open(fileName, 'r') as file:
        lineNo = 0
        for line in file:
            lineNo += 1
            for token in tokenGenerator(line[0:-1], separators):
                if token in separators + operators + reservedWords:
                    pif.add(codification[token], -1)
                elif (symbolTable.find(token)==-1 and (line.split()[0] not in reservedWords)):
                    #check if the token is not in the symbol table and the beggining of the line is not a reserved word(chck, let,wrt, rd
                    raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))
                elif isIdentifier(token) :
                    id = symbolTable.insert(token)
                    pif.add(codification['identifier'], id)

                elif isConstant(token):
                    id = symbolTable.insert(token)
                    pif.add(codification['constant'], id)


    pif1.write("Program Internal Form: \n %s\n\n" %pif.__str__())
    st.write("Symbol Table: \n %s\n\n" %symbolTable.__str__())

    st.write("Codification table: \n")
    for e in codification:
        st.write(" %s  ->  %s\n" %(e,codification[e].__str__()))

    print('Lexically correct!')
# !!!!!!!!!!!!!!!check for random tokens in the program for example a '#' after the first { !!!!!!!!!!!!!!!!!!!!!

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
