def cout_words(filename):
    try:
        with open(filename) as f_obj:
            coutents=f_obj.read()
    except FileNotFoundError:
        msg="Sorry,the file"+filename+"is not exit"
        print(msg)
    else:
        words=coutents.split()
        num_words=len(words)
        print("The file"+filename+"has about "+str(num_words)+"words")

filename="pi_dilith1.txt"
cout_words(filename)
