import csv,glob
import os.path
import pandas as pd
from csv import writer

class FileTool:
    
    def __init__(self, path, fields = [], *args):
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
        isFile = self.isFileExist()
        if isFile == True:
            print("No need to create new file! File is exist.")
        elif isFile == False:
            with open(path, 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(self.fields)

    def toJson(self):
        '''
        - Converts csv file to json format.
        '''
        with open(self.path, 'r') as file_csv:
            reader = csv.DictReader(file_csv)
        with open('{}'.format(path.split('.')[0]+'.json'), 'w') as file_json:
            for row in reader:
                json.dump(row, file_json)

    def searchData(self): 
        '''
        - Prints the data containing the searched word.
        '''
        search_ = input("Search a dataframe value: ")
        with open(self.path, 'r') as f:
            for line in f.readlines():
                if search_ in line:
                    print(line)
                    
    def appendData(self):
        '''
        - Adds new data to the data in a new row.
        '''
        appended_ = [item for item in input("Enter the data with spaces: ").split()]
        with open(self.path, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow2(appended_)  
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

    def updateData(self):
        '''
        - Updates the desired data.
        '''
        old_data = input("Enter old data: ")
        new_data = input("Enter new data: ")
        f_obj1 = open(self.path,'r')
        f_obj1 = ''.join([i for i in f_obj1]).replace(old_data, new_data)
        f_obj2 = open(self.path,'w')
        f_obj2.writelines(f_obj1)
        f_obj2.close()
        
    def mergeFiles(self): # TODO some bugs will be fixed. tekrar duzenlenmeli
        '''
        - Merges JSON or CSV all files in path.
        '''
        if self.path.endswith(".csv"): 
            dfs = glob.glob('path/*.csv')
            result = pd.concat([pd.read_csv(df) for df in dfs], ignore_index=True)
            result.to_csv('path/merged.csv', ignore_index=True)
        elif self.path.endswith(".json"): 
            read_files = glob.glob("*.json")
            with open("merged_file.json", "wb") as outfile:
                outfile.write('[{}]'.format(
                    ','.join([open(f, "rb").read() for f in read_files])))
        else:
            print('The file format is not suitable.')
    
    def Menu(self):
        '''
        Press [1] to search data,
        Press [2] to append data,
        Press [3] to delete data,
        Press [4] to update data,
        Press [5] to create new file,
        Press [6] to convert csv2json format,
        Press [7] to merge files,
        Press [8] to quit the program,
        '''
        while True:
            select_ = input("Press [1] to search data,\nPress [2] to append data,\nPress [3] to delete data,\nPress [4] to update data,\nPress [5] to create new file,\nPress [6] to convert csv2json format,\nPress [7] to merge files,\nPress [8] to quit the program,\nSelect the action you want to do: ")
            if select_ == '1':
                self.searchData()
            elif select_ == '2':
                self.appendData()
            elif select_ == '3':
                self.deleteData()
            elif select_ == '4':
                self.updateData()
            elif select_ == '5':
                self.createNewFile()
            elif select_ == '6':
                self.toJson()
            elif select_ == '7':
                break

path = 'innovators.csv'
ft = FileTool(path, fields=['Name','Contribution'])
ft.Menu()