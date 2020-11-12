import pandas as pd
from os import listdir



mon_11 = 1360587600
mon_18 = 1361192400
file_path = '../processed_material/'
win10 = '../windowsize10/'
win227 = '../windowsize227/'
win300 = '../windowsize300/'

def create_window_size(win_size):
    windows = int(32400 / win_size)
    list_window = []
    #list_week = []
    #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",windows)
    for i in range(5):
        print(win_size)
        start = mon_11 + i * 86400
        for j in range(windows):
            x = start + j * win_size
            list_window.append(x)   #this list will consist of epoch time of time frame for given time(10secs, 221 secs or 5 mins)



    for i in range(5):
        print(win_size)
        start = mon_18 + i * 86400
        for j in range(windows):
            x = start + j * win_size
            list_window.append(x)

    read_files(list_window, win_size)





def read_files(list_window, windowsize):

    for file in [f for f in listdir(file_path) if not f.startswith('.') or f.startswith('~')]:  # to ignore hidden files
        curr_path = file_path + file
        df = pd.read_csv(curr_path)
        new_path1 = win10 + file
        new_path2 = win227 + file
        new_path3 = win300 + file
        #print("$$$$$$$$$", file)
        processed_list = df['Real First Packet'].tolist()    #consists of Real First Packets from .csv files
        processed_list.sort()
        templist_docperdur = df['doctets/duration'].tolist()  #consists of doctets/duration form .csv files

        doc_per_dur = check_window(processed_list, templist_docperdur, list_window, windowsize)

        ndf = pd.DataFrame()
        ndf['windows'] = list_window
        ndf['doctets/duration'] = doc_per_dur
        #print(processed_list)

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$", windowsize)
        #to simplify the whole process I have converted the dataframe to lists.

        #to create a dataframe for the preprocessed .csv files
        if windowsize == 10:
            ndf.to_csv(new_path1)

        elif windowsize == 227:
            ndf.to_csv(new_path2)

        else:
            ndf.to_csv(new_path3)




def check_window(processedlist, temp_list_docperdur,list_window, windowsize):
    winlist_length = len(list_window)
    max_row= len(processedlist)
    doc_per_dur = []
    #print('$$$$$$$$',max_row)
    row = 0
    for i in range(winlist_length):
        while row < max_row:
            if processedlist[row] < list_window[i]:
                row += 1
            else:
                break
        sum = 0
        k = 0
        while(row < len(temp_list_docperdur)):
            if list_window[i] <= processedlist[row] < (list_window[i] + windowsize):
                #print(row)
                sum += temp_list_docperdur[row]
                k += 1
                row += 1
            else:
                #print("Breaking at ", row, " and window" , list_window[i])
                break
        if k > 0:
            average = sum / k
            #print('********')
        else:
            average = 0.001

        doc_per_dur.append(average)
    return doc_per_dur


create_window_size(10)
#read_files(10)

create_window_size(227)
#read_files(227)

create_window_size(300)
#read_files(300)



