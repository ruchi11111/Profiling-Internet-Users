import pandas as pd
from os import listdir
from scipy.stats import spearmanr

winsize10 = '../windowsize10/'
winsize227 = '../windowsize227/'
winsize300 = '../windowsize300/'
path_spear = '../spearman/'
list_path = ['../windowsize10', '../windowsize227', '../windowsize300']
list_files= ['../spearman/win10.csv','../spearman/win227.csv','../spearman/win300.csv']
mon_11 = 1360587600
mon_18 = 1361192400

def get_data(win_size):
    windows = int(32400 / win_size)
    list_week = []
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", windows)
    for i in range(5):
        print(win_size)
        start = mon_11 + i * 86400
        for j in range(windows):
            x = start + j * win_size
            list_week.append('week1') #just to mark an entry if it belongs to week1 or week2

    for i in range(5):
        print(win_size)
        start = mon_18 + i * 86400
        for j in range(windows):
            x = start + j * win_size
            list_week.append('week2')


    for path in list_path:
        df = pd.DataFrame()
        df['week'] = list_week
        file_list = listdir(path)
        for file in file_list:
            if win_size == 10:
                curr_path = winsize10 + file
            elif win_size == 227:
                curr_path = winsize227 + file
            else:
                curr_path = winsize300 + file
            temp_df = pd.read_csv(curr_path)
            temp_df.info()
            list_octetdur = []   #this list will include doctets/duration
            list_octetdur = temp_df['doctets/duration'].tolist()
            df[file] = list_octetdur
        if win_size == 10:
            name_path = path_spear + 'win10.csv'
            df.to_csv(name_path, index = False)
        elif win_size == 227:
            name_path = path_spear + 'win227.csv'
            df.to_csv(name_path, index = False)
        else:
            name_path = path_spear + 'win300.csv'
            df.to_csv(name_path, index=False)


def begin_cal():
    i=0
    windows = ['ten','twotwoseven','threehundred']
    for files in list_files:
        spearman_calculation(files, windows[i])
        i += 1


def spearman_calculation(files,windows):
    df = pd.read_csv(files)
    df_w1 = df[df.week == 'week1']
    df_w2 = df[df.week == 'week2']
    df_w1.drop(['week'], axis=1, inplace=True)
    df_w2.drop(['week'], axis=1, inplace=True)
    list_h = [i for i in range(54)]
    df = pd.DataFrame(columns=list_h)
    for i in range(df_w1.shape[1]):
        week1user = df_w1.iloc[:, i]
        list_random = []
        for j in range(df_w2.shape[1]):
            week2user = df_w2.iloc[:, j]
            rho, p = spearmanr(week1user, week2user)   #r1a2b
            list_random.append(rho)
        series_random = pd.Series(list_random, index=df.columns)
        df = df.append(series_random, ignore_index=True)
    df.fillna(0.001,inplace= True)
    finalpath = "../spearman_outputs/" + windows + ".csv"
    df.to_csv(finalpath)

get_data(10)
get_data(227)
get_data(300)
begin_cal()




