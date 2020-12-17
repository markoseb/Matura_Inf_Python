


from zad4_1_2020 import  read_file, pandas_read_file ,write_line





def zad4_3():
    inputData = pandas_read_file(file_name = "pary.txt")

    write_line(text = "zad4_3\n", file_path="wyniki4.txt")
    last_numb = [0,"null",0]
    for l in inputData.values:
        if len(l[1]) == l[0]:
            # write_line(text=f"{l}", file_path="wyniki4_3.txt")
            if l[0]<last_numb[0] or last_numb[0]==0:
                set_new_value(l,last_numb)
            elif last_numb[0]==l[0] :
                for i in range(len(l[1])-1):
                    if last_numb[1][i] > l[1][i]:
                        set_new_value(l, last_numb)



    write_line(text=f"{last_numb[0]} {last_numb[1]}", file_path="wyniki4.txt")


def set_new_value(input=[], output=[]):
    output[0] = input[0]
    output[1] = input[1]
    output[2] = len(input[1])
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zad4_3()
