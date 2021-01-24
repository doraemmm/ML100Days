import pandas as pd
pcsv=pd.read_csv(r'D:\Downloads\test\boston.csv',header=0,usecols=['CHAS','PTRATIO','B','LSTAT'])
pcsv.to_excel(r'D:\Downloads\test\boston.xlsx')