import cmd


class RFID_Cmd(cmd.Cmd):

    def do_hello(self, line):
        """This command says hello."""
        print("hello " + line)


if __name__ == '__main__':
    c = RFID_Cmd()

    c.cmdloop()