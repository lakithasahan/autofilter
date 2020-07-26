import sklearn
import vaex
import pandas as pd
import ppscore as pps
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class autofilter_main():

    def __init__(self,file_path,file_name):

        self.df=self.file_type_detection(file_path,file_name)

        self.df=self.df.head(100)

        self.column_datatype_list=[]
        column_data_types_raw = list(self.df.dtypes)
        for x in range(len(column_data_types_raw)):
            self.column_datatype_list.append(str(column_data_types_raw[x]))


        self.date_time_column_detection(self.df)




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


    def column_relationships(self,df):
        df = df.to_pandas_df()
        plt.figure(1)
        plt.figure(figsize=(16, 12))
        sns.heatmap(pps.matrix(df), annot=True, fmt=".2f")
        plt.show()

        plt.figure(2)
        plt.figure(figsize=(16, 12))

        sns.heatmap(pd.DataFrame(df.corr()), annot=True, fmt=".2f")
        plt.show()

    # def detect_column_datatypes(self,df):

    def date_time_column_detection(self,df):
        print(df)
        df = df.to_pandas_df()
        numpy_array = df.values
        datatype_list=[]

        print(numpy_array)



        print(self.column_datatype_list)
        column_name=df.columns
        column_datatype_list=self.column_datatype_list
        detected_data_type=[]
        for x in range(len(column_name)):

            for y in range(len(numpy_array)):

                if column_datatype_list[x]=="<class 'str'>":
                    print(numpy_array[y][x])
                    try:
                        print(pd.to_datetime(str(numpy_array[y][x])))
                        detected_data_type.append('Datetime')
                    except:
                        detected_data_type.append('str')

                else:
                    detected_data_type.append(str(column_datatype_list[x]))
        print(detected_data_type)
