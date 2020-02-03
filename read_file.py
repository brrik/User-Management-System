def read_file(file_name):
    import os

    if not os.path.isfile(file_name):
        print("File is not found. Try again.")
    
    elif os.path.isfile(file_name):
        with open(file_name, mode = "r") as f:
            read_file = f.read()
            print("File found.\n" +
                  "~~~~~    File START    ~~~~~\n"+
                  read_file + "\n" +
                  "~~~~~     File END     ~~~~~\n"
                 )