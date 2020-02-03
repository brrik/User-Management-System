def yn_check(hoge):
    if hoge == "y" or hoge == "Y":
        result = "yes"
        return result
    elif hoge == "n" or hoge == "N":
        result = "no"
        return result
    else:
        print("ERROR")
        result = "ERROR"
        return result