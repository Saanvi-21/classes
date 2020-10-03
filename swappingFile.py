file_1 = input("Enter the first file name: ")
file_2 = input("Enter the second file name: ")

def swapData(file_1, file_2):
    try:
        with open(file_1, 'r') as f:
            data_1 = f.read()

        with open(file_2, 'r') as f:
            data_2 = f.read()


        with open(file_1, 'w') as f:
            f.write(data_2)
            f.close()

        with open(file_2, 'w') as f:
            f.write(data_1)
            f.close()

    except FileNotFoundError:
        print("[-] No such file(s) found!")

swapData(file_1, file_2)

    