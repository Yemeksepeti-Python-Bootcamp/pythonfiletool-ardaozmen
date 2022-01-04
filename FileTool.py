import csv
import os.path
from csv import writer

class FileTool:
    def __init__(self, path, fields = [], *args, **kwargs):
        self.path = path
        self.fields = fields

    def isFileExist(self):
        '''
        - checks the file path. 
        - returns a boolean value.
        '''
        return os.path.exists(self.path)
    
    def createNewFile(self):
        '''
        - If there is no file matching the format in the path, 
        - it creates a new file.
        '''
        isFile = isFileExist(self.path)
        if isFile == True:
            print("No need to create new file! File is exist.")
        elif isFile == False:
            with open(path, 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                fields = [item for item in input("Enter the list of fields: ").split()]
                writer.writerow(fields)

    def toJson(self):
        '''
        - Converts csv file to json format.
        '''
        with open(self.path, 'r') as file_csv:
            reader = csv.DictReader(file_csv)
        with open('myfile.json', 'w') as file_json: 
            for row in reader:
                json.dump(row, file_json)

    def searchData(self): 
        '''
        - Prints the data containing the searched word.
        '''
        search_ = input("Search a keyword: ")
        reader = csv.reader(open(filename, 'r'))
        for row in reader:
            if row[0] == search_ or row[1] == search_:
                return row[:]
        return None # return None if no match

    def appendData(self):
        '''
        - Adds new data to the data in a new row.
        '''
        appended_ = [item for item in input("Enter the data with spaces: ").split()]
        with open(self.path, 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            writer_object.writerow(appended_)  
            f_object.close()

    def deleteData(self):
        '''
        - Deletes the desired data.
        '''
        deleted_ = input("Enter a deleted what you want: ")
        with open(self.path, 'r+') as f_object:
            lines = f_object.readlines()
            for line in lines:
                if line.strip("\n") != deleted_:
                    f_object.write(line)