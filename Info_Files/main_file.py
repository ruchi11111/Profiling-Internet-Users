from os import listdir
import pandas as pd

feb11_20138am = 1360587600
feb22_20135am = 1361570400
path = '../files_material/'
new_path = '../processed_material/'      #new path for the processed files


def function_file_list():               #gives a list of files in directory
    i=0
    for file in [f for f in listdir(path) if not f.startswith('.') or f.startswith('~')]:  #to ignore hidden files
        i += 1
        function_processed_data(file)
        print(i)


def function_processed_data(filename):               #intermediate data for all files eliminating useless columns and rows
    file_path = path + filename
    df = pd.read_excel(file_path)
    #print(df.info())
    del df['unix_secs']
    del df['sysuptime']
    del df['dpkts']
    del df['doctets/dpkts']
    del df['Real End Packet']
    del df['first']
    del df['last']
    print("******************")
    df['Real First Packet'] = df['Real First Packet']/1000
    #print(df.info())
    df = df[((df['Real First Packet'] > feb11_20138am) & (df['Real First Packet'] < feb22_20135am)) & (df['Duration'] != 0)]
    df['doctets/duration'] = (df['doctets']/df['Duration']) * 1000
    del df['doctets']
    del df['Duration']
    print(df.info())
    new_file_name = filename.strip('xlsx')
    new_file_name = new_file_name + 'csv'
    csv_path = new_path + new_file_name

    df.to_csv(csv_path, index=False)



function_file_list()




