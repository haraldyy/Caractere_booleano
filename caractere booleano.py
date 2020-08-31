def caractere():
    c = int(input('Digite um caractere:'))
    if c <= 9:
        print(False)
    else:
        print(True)
def main():
    caractere()
if __name__=='__main__':
    main()
