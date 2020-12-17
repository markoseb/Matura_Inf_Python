


from zad4_1_2020 import  read_file, pandas_read_file ,write_line



def get_max_letter(word =""):
    max_lenght = 0
    max_letter = ""
    cur_lenght = 1
    letter_numb = 1
    word_lenght = len(word)
    for letter in word:
        if letter_numb < word_lenght:
            if letter == word[letter_numb ]:
                cur_lenght += 1
            else:
                if max_lenght < cur_lenght:
                    max_lenght = cur_lenght
                    max_letter = letter
                cur_lenght = 1
            letter_numb += 1
    write_line(text=f"{max_letter * max_lenght} {max_lenght}\n", file_path="wyniki4.txt")

def zad4_2_v2():
    inputData = pandas_read_file()

    write_line(text = "\nzad4_2_v2\n", file_path="wyniki4.txt")

    for l in inputData.values:
        get_max_letter(word=l[1])


def zad4_2():
    inputData = read_file("pary.txt")
    write_line(text = "\nzad4_2\n", file_path="wyniki4.txt")
    # for [i,_] in inputData:


    for [i, word] in inputData:
        get_max_letter(word=word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zad4_2()
