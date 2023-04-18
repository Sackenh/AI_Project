from csv import reader, DictWriter
from json import dump
import xlsxwriter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#data points inside files are: age, sex, cp?, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, num

def create_correlation_matrix(): 
    data_list = []
    data_file = "processed.cleveland.data"

    with open(data_file, mode = "rt", newline="") as data:
        data_reader = reader(data)
        
        for row in data_reader: 
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, num = row

            if age == '?': 
                age = 0 
            else: 
                age = float(age)

            if sex == '?':
                sex = 0
            else: 
                sex = float(sex)

            if exang == '?':
                exang = 0
            else: 
                exang = float(exang)

            if oldpeak == '?':
                oldpeak = 0 
            else: 
                oldpeak = float(oldpeak)
            
            if ca == '?':
                ca = 0
            else: 
                ca = float(ca)

            if thal == '?':
                thal = 0
            else: 
                thal = float(thal)
            
            if num == '?':
                num = 0
            else: 
                num = float(num)
            
            interior_list = [age, sex, exang, oldpeak, ca, thal, num]
            data_list.append(interior_list)
        
    dataframe = pd.DataFrame(data_list, columns=['age', 'sex', 'exang', 'oldpeak', 'ca', 'thal', 'num'])
    print(dataframe)
    

    matrix = dataframe.corr()
    print(f"---------------------------------------------------------------------- Correlation Matrix ----------------------------------------------------------------------\n{matrix}")
    plt.figure(figsize = (10, 6))
    sns.heatmap(matrix, annot = True)
    plt.show()

    return dataframe
    

def view_filtered_data(filtered_data):
    num = 0
    for row in filtered_data:
        num+=1

        display_data = f"""
            Age: {row['age']}
            Sex: {row['sex']}
            Chest Pain: {row['chest pain']}
            Resting Electrocardiographic Results: {row['resting electrocardiographic results']}
            Number of Major Vessels Shown on Flourosopy: {row['num major vessels']}
            Angiographic Disease Status(0 - <50% diameter Narrowing, 1 - >50% diameter Narrowing): {row['num']}
        """
        print(f"-------------------Patient {num}----------------------")
        print(display_data)
        print("-------------------------------------------------------")
        


def load_unfiltered_data(): 
    data_list1 = []
    data_list2 = [] 
    data_list3 = []
    data_list4 = [] 
    data_file1 = "processed.cleveland.data" 
    data_file2 = "processed.hungarian.data"
    data_file3 = "processed.switzerland.data"
    data_file4 = "processed.va.data"     # <---------- change data file when needed

    with open(data_file1, mode = "rt", newline="") as data:
        data_reader = reader(data)
        
        for row in data_reader: 
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, num = row

            data_dictionary = {
                "age": age, #age in years
                "sex": sex, #(1 = male, 0 = female)
                "chest pain": cp, #Value 1 - Typical Angina, Value 2 - Atypical Angina, Value 3 - non-anginal pain, Value 4 - asymptomatic
                "resting electrocardiographic results": restecg, #Value 0 - Normal, Value 1 - having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
                "num major vessels": ca, #number of major vessels (0-3) colored by flourosopy
                "num": num #diagnosis of heart disease(angiographic disease status), Value 0 - <50% diameter narrowing, Value 1 - > 50% diameter narrowing
            }
            data_list1.append(data_dictionary)

    with open(data_file2, mode = "rt", newline="") as data:
        data_reader = reader(data)
        
        for row in data_reader: 
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, num = row

            data_dictionary = {
                "age": age, #age in years
                "sex": sex, #(1 = male, 0 = female)
                "chest pain": cp, #Value 1 - Typical Angina, Value 2 - Atypical Angina, Value 3 - non-anginal pain, Value 4 - asymptomatic
                "resting electrocardiographic results": restecg, #Value 0 - Normal, Value 1 - having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
                "num major vessels": ca, #number of major vessels (0-3) colored by flourosopy
                "num": num #diagnosis of heart disease(angiographic disease status), Value 0 - <50% diameter narrowing, Value 1 - > 50% diameter narrowing
            }
            data_list2.append(data_dictionary)

    with open(data_file3, mode = "rt", newline="") as data:
        data_reader = reader(data)
        
        for row in data_reader: 
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, num = row

            data_dictionary = {
                "age": age, #age in years
                "sex": sex, #(1 = male, 0 = female)
                "chest pain": cp, #Value 1 - Typical Angina, Value 2 - Atypical Angina, Value 3 - non-anginal pain, Value 4 - asymptomatic
                "resting electrocardiographic results": restecg, #Value 0 - Normal, Value 1 - having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
                "num major vessels": ca, #number of major vessels (0-3) colored by flourosopy
                "num": num #diagnosis of heart disease(angiographic disease status), Value 0 - <50% diameter narrowing, Value 1 - > 50% diameter narrowing
            }
            data_list3.append(data_dictionary)

    with open(data_file4, mode = "rt", newline="") as data:
        data_reader = reader(data)
        
        for row in data_reader: 
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, num = row

            data_dictionary = {
                "age": age, #age in years
                "sex": sex, #(1 = male, 0 = female)
                "chest pain": cp, #Value 1 - Typical Angina, Value 2 - Atypical Angina, Value 3 - non-anginal pain, Value 4 - asymptomatic
                "resting electrocardiographic results": restecg, #Value 0 - Normal, Value 1 - having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
                "num major vessels": ca, #number of major vessels (0-3) colored by flourosopy
                "num": num #diagnosis of heart disease(angiographic disease status), Value 0 - <50% diameter narrowing, Value 1 - > 50% diameter narrowing
            }
            data_list4.append(data_dictionary)
    
    return data_list1, data_list2, data_list3, data_list4

def save_filtered_data_textfile(filtered_data):
    save_file = "filtered-cleveland-data.txt"   #<--- change the value to change the save file destination
    with open(save_file, mode="at", newline="") as data_file:
        dump(filtered_data, data_file)
    print("Successfully Saved Data on Filesystem")


def save_filtered_data_spreadsheet(filtered_data1, filtered_data2, filtered_data3, filtered_data4):
    df1 = pd.DataFrame(filtered_data1)
    df2 = pd.DataFrame(filtered_data2)
    df3 = pd.DataFrame(filtered_data3)
    df4 = pd.DataFrame(filtered_data4)

    writer = pd.ExcelWriter("dataset.xlsx", engine = "xlsxwriter")

    df1.to_excel(writer, sheet_name="Sheet1")
    df2.to_excel(writer, sheet_name = "Sheet2")
    df3.to_excel(writer, sheet_name = "Sheet3")
    df4.to_excel(writer, sheet_name = "Sheet4")

    writer.close()
    


filtered_data1, filtered_data2, filtered_data3, filtered_data4 = load_unfiltered_data()
print(filtered_data1) #<--- uncomment this if you want to see awfully unformatted data
#save_filtered_data(filtered_data) <---- this will save all the data to a file(specified by you)
view_filtered_data(filtered_data1)       #<---- displays the data in an easy to read format
#save_filtered_data_spreadsheet(filtered_data1, filtered_data2, filtered_data3, filtered_data4)
dataframe = create_correlation_matrix()



#the predicted output of the patient is the num value ---- ask teacher if that value should be included within the correlation matrix or if that would skew the data

#https://github.com/adityabaranwal2021/HeartDisasePredictionNeuralNetwork/blob/main/heartdiseaseprediction.ipynb <---- could be useful reference

# for presentation --> 
# Start by saying what your problem is 
# steps taken to solve it 
# actual implementation 
# results 

