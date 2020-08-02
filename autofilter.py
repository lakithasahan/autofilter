import sklearn
import vaex
import pandas as pd
# import ppscore as pps
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class autofilter_main():

    def __init__(self,file_path,file_name):

        self.df=self.file_type_detection(file_path,file_name)

        self.df=self.df.head(100)


        self.column_datatype_list=[]
        column_data_types_raw = list(self.df.dtypes)
        for x in range(len(column_data_types_raw)):
            self.column_datatype_list.append(str(column_data_types_raw[x]))


        self.column_type_detection_main(self.df)





    def file_type_detection(self,file_path,file_name):
        print('file type detection')
        file_type_list=str(file_name).split('.')
        file_type=file_type_list[len(file_type_list)-1]
        print(file_type)

        if file_type=='csv':
            df = vaex.from_csv(file_path, copy_index=False)


        elif file_type=='hdf5':
            df=vaex.open(file_path)

        elif file_type=='parquet':
            df = vaex.open(file_path)

        return df


    # def column_relationships(self,df):
    #     df = df.to_pandas_df()
    #     plt.figure(1)
    #     plt.figure(figsize=(16, 12))
    #     sns.heatmap(pps.matrix(df), annot=True, fmt=".2f")
    #     plt.show()
    #
    #     plt.figure(2)
    #     plt.figure(figsize=(16, 12))
    #
    #     sns.heatmap(pd.DataFrame(df.corr()), annot=True, fmt=".2f")
    #     plt.show()
    #
    # # def detect_column_datatypes(self,df):

    def column_type_detection_main(self,df):
        print(df)
        df = df.to_pandas_df()
        numpy_array = df.values
        datatype_list=[]

        print(numpy_array)

        print(self.column_datatype_list)
        column_name_list=df.columns
        column_datatype_list=self.column_datatype_list
        column_wise_data_type=[]
        for x in range(len(column_name_list)):

            for y in range(len(numpy_array)):

                if column_datatype_list[x]=="<class 'str'>":
                    result=self.type_checker(numpy_array[y][x])
                    column_wise_data_type.append(result)

                else:
                    column_wise_data_type.append(str(column_datatype_list[x]))
            self.column_wise_datatype_(column_wise_data_type,column_name_list[x])
            column_wise_data_type=[]


    def type_checker(self,data):
        try:
            pd.to_datetime(data)
            detected_type='datetime'
        except:
            try:
                float(data)
                detected_type = 'float64'
            except:
                try:
                    str(data)
                    detected_type = 'str'
                except:
                    detected_type='null'

        return detected_type


    def column_wise_datatype_(self,data,column_name):
        print('Column type detection '+str(column_name))
        series_data=pd.Series(data)

        detected_data_types=series_data.value_counts()
        print(list(detected_data_types.index))
        print(list(detected_data_types))


