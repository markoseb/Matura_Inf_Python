# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/


A = [1,2,3,2,2,7,6,5]
B = [2,7,6,5,1,2,3,2]
def cz_k_podobne(n,A,B,k):

    if A!=B:

        for i in range(k):
            if A[i] != B[n-k+i]:
                return False
        for i in range(n - k):
            if B[k+i] != A[i]:
                return False

    return True

def cz_podobne(n1=8,A1=A,B1=B):
    for i in range (n1):
        if cz_k_podobne(n=n1, A=A1,B=B1,k=i):
            print ("True")
    return False




def mod_fun(n=1234):
    w=0

    while n!=0:
        w=w + n%10


        print(w)
        n=n//10





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cz_podobne()
    mod_fun(n=1234)