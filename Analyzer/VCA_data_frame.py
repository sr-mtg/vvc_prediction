import pandas as pd
df_EH = pd.read_csv('../result_aau/EH.csv')
df_siti = pd.read_csv('../result_aau/siti.csv')
df_siti_msiti = pd.read_csv('../DataExtract/max_min_SITI.csv')
df_siti_meh = pd.read_csv('../DataExtract/max_min_Eh.csv')
#print(df_siti.head())
X = df_siti.drop('Name', axis=1)
X['E'] = df_EH['E']
X['h'] = df_EH['h']
#eh
X['max_E'] = df_siti_meh['max_E']
X['min_E'] = df_siti_meh['min_E']
X['max_h'] = df_siti_meh['max_h']
X['min_h'] = df_siti_meh['min_h']
#siti 'max_SI', 'min_SI', 'max_TI', 'min_TI'
X['max_SI'] = df_siti_msiti['max_SI']
X['min_SI'] = df_siti_msiti['min_SI']
X['max_TI'] = df_siti_msiti['max_TI']
X['min_TI'] = df_siti_msiti['min_TI']
#print(X.head())
df_size = pd.read_csv('../Crawl_result/size_of_video.txt')
X['Size'] = df_size['Size']

df_responsTime = pd.read_csv('../result_aau/x265_time_medium_c5_2xlarge.csv')
#print(df_responsTime.head())
Y = df_responsTime['time_QP27']