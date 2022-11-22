# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from model.FiniteAutomata import FiniteAutomata
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    finiteAutomata = FiniteAutomata.readFile('fa.txt')
    arg=0
    print('1.Set of states \n2.Transitions\n3.Initial state\n4.Final state\n5.The alphabet')
    while arg!=-1 :
        arg=int(input('Your choice: '))
        if arg==1:
            print(finiteAutomata.printQ())
        elif arg==2:
            print(finiteAutomata.printS())
        elif arg == 3:
            print(finiteAutomata.printq0())
        elif arg == 4:
            print(finiteAutomata.printF())
        elif arg==5:
            print(finiteAutomata.printE())
        else:
            print('Wrong choice')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
