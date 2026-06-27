from csvreader import CsvReader
'''
if __name__ == "__main__":
    with CsvReader('good.csv', ',', True, 0, 0) as file:
        data = file.getdata()
        print(len(data))
        header = file.getheader()
        print(header)
'''


if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")
