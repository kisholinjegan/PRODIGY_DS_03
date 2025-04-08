import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv("bank.csv",delimiter=',')
print(df.head(5))
print(df.columns)
df_obj=df.select_dtypes(include='object').columns

df_num=df.select_dtypes(exclude='object').columns
for feature in df_num:
    sns.histplot(x=feature,data=df,bins=25,kde=True,color='#5f366e')
    plt.show()             
