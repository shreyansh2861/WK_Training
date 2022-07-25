def outerFunction():
    text = "Shreyansh"

    def innerFunction():
        #test+="Patil"
        print(text)

    return innerFunction()

ifn = outerFunction()
ifn()