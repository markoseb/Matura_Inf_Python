import pandas as pd
import os



THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DATAFILE_PATH = os.path.join(BASE_DIR,"dataFile")



def pandas_read_file(file_name = "pary.txt"):
    return  pd.read_csv(f"{DATAFILE_PATH}/{file_name}", sep=" ", encoding='utf-8', header=None)

# def read_file(file_name = "przyklad.txt"):
#     pary_file= open (f"{DATAFILE_PATH}/{file_name}",'r')
#     pairs = []
#     for l in range (100): #100 lines
#         n, word = pary_file.readline().split()
#         pairs.append([int(n),word])
#     return pairs
#     pary_file.close()

def read_file(file_name = "przyklad.txt", sep = " "):
    with open (f"{DATAFILE_PATH}/{file_name}",'r') as pary_file:
        pairs = []
        for l in pary_file:
            pairs.append(l.split(sep=sep))
    pary_file.close()
    return pairs



def create_new_file(DataFrame=None,data_list=[] ,columns=["a","b","c"],fileName='wyniki4.txt'):
    mode = 'a'
    header = False
    filepath= f"{DATAFILE_PATH}/{fileName}"
    if not os.path.isfile(filepath):
        mode = 'w'
        header = True
    if len(data_list) >0:
        df = pd.DataFrame(data_list, columns=columns)
    else:
        df=DataFrame
    df.to_csv(path_or_buf=filepath, index=False, mode=mode, header=header, encoding='utf-8', sep=' ')




def write_line(text="",file_path="wyniki4.txt"):
    with open(f"{DATAFILE_PATH}/{file_path}",'a') as f:
        f.write(f"{text}\n")


def czy_pierwsza(liczba = 0):
    if liczba == 2 :
        return True
    if liczba <=1 or liczba % 2 ==0:
        return False
    pierw= int(liczba ** 0.5) +1
    if liczba >=3:
        for l in range (3,pierw,2):
            if liczba % l == 0 :
                return False

    return True


def zad4_1_pandas():
    inputData = pandas_read_file()
    dataFrame = []
    write_line(text = "zad4_1_pandas\n", file_path="wyniki4.txt")
    for i in inputData.values:
        if i[0]>4 and i[0] % 2 ==0:
            for  number in range(3,i[0],2):
                if czy_pierwsza(number) and czy_pierwsza(i[0]-number):
                    dictNumber ={"a" : i[0],"b":number, "c" :i[0]-number}
                    dataFrame.append(dictNumber)
                    break

    create_new_file( data_list=dataFrame, fileName='wyniki4.txt')
    write_line(text="\n", file_path="wyniki4.txt")


def zad4_1_standard():
    inputData = read_file(file_name="pary.txt")
    write_line(text = "zad4_1\n", file_path="wyniki4.txt")
    for [i,_] in inputData:
        i_converted = int(i)
        print (inputData)
        if i_converted>4 and i_converted % 2 ==0:
            for  number in range(3,i_converted,2):
                if czy_pierwsza(number) and czy_pierwsza(i_converted-number):
                    write_line(text=f"{i_converted} {number} {i_converted-number}",file_path="wyniki4.txt")
                    break
    # for [i, _] in inputData:
    write_line(text="\n", file_path="wyniki4.txt")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zad4_1_standard()
    # zad4_1_pandas()
