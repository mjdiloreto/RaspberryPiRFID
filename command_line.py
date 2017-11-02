import cmd
from save_funcs import *

class RFID_Cmd(cmd.Cmd):

    def do_hello(self, line):
        """This command says hello."""
        print("hello " + line)

    def do_addMember(self, line):
        """This command allows new members to add their card ID and name to the NU Wireless database."""
        print("Tap the NU ID card:" + line)
        # nuID = getUID()
        nuID = 0
        firstName = input('Enter first name:')
        lastName = input('Enter last name:')
        ex = input('Enter directory to csv file:')
        # ex = "example.csv"
        save_funcs.save(ex,lastName,firstName,nuID)

if __name__ == '__main__':
    c = RFID_Cmd()

    c.cmdloop()