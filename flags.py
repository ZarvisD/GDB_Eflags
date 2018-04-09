import gdb

class SimpleCommand(gdb.Command):
    def __init__(self):
        # This registers our class as "simple_command"
        super(SimpleCommand, self).__init__("change_flags", gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        # When we call "simple_command" from gdb, this is the method
        # that will be called.
        # print("Hello from simple_command!")
        eflags=['CF','PF','AF','ZF','SF','TF','IF','DF','OF','IOPL','NT','RF','VM','AC','VIF','VIP','ID'] #List of all the flags to the best of my knowledge
        s_flag=['CF','PF','AF','ZF','SF','OF'] # List of all the status FLAGS
        status_flag={'CF':0x0001,
                    'PF':0x0004,
                    'AF':0x0010,
                    'ZF':0x0040,
                    'SF':0x0080,
                    'OF':0x0800}
        flags= gdb.execute("print $eflags",False,True)
        flags=flags[8:][:-2] # Trimming the output to make it usable
        s=flags.split() # spitting and storing it a List called 's'
        for item in s:
            if item in flags:
                print(item+" is set") # "This prints out all the FLAGS that are Set"
        gdb.write("Please enter the STATUS FLAG you would like to set/reset \n")
        gdb.write("Following are STATUS FLAGS 'CF','PF','AF','ZF','SF','OF' \n")
        choice=input()
        if choice in s_flag: #It checks if user_entered input is in the list of Status Flags
            if choice in s:  #It checks it user choice flag is set or not and then takes the corresponding action.
                # print (choice)
                gdb.execute("set $ps=$ps&~"+hex(status_flag[choice]),False,True)
                gdb.write(choice +" flag has been unset \n")
                gdb.execute("print $eflags")

            else:
                gdb.execute("set $ps=$ps|"+hex(status_flag[choice]),False,True)
                gdb.write(choice +" flag has been set \n")
                gdb.execute("print $eflags")     


SimpleCommand()
