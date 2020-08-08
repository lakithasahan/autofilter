import sklearn
import vaex
import pandas as pd
# import ppscore as pps
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from autofilter_library_building.autofilterv1.file_specs_detect import get_file_size, SIZE_UNIT


class autofilter_main():

    def __init__(self,text):
        if text==True:
            print('Autofiter initialising')
            print('Design By:Lakitha Sahan ')
            print('Copyright 2020 ')



        else:
            pass





    ###########################Main functions starting point #############################
    ######################################################################################
    ######################################################################################
    def extract_file_data(self, file_path, file_name):
        print('extract_file_data')
        size = round(get_file_size(file_path, SIZE_UNIT.MB), 2)
        print('Size of file is : ', size, 'MB')
        file_type_list = str(file_name).split('.')
        file_type = file_type_list[len(file_type_list) - 1]

        if file_type == 'csv':
            df = vaex.from_csv(file_path, copy_index=False)


        elif file_type == 'hdf5':
            df = vaex.open(file_path)

        elif file_type == 'parquet':
            df = vaex.open(file_path)

        self.column_datatype_list = []
        column_data_types_raw = list(df.dtypes)
        for x in range(len(column_data_types_raw)):
            self.column_datatype_list.append(str(column_data_types_raw[x]))
        raw_detected_column_datatype=self.column_datatype_list
        return df,raw_detected_column_datatype

    def extract_major_datatype(self,df):

        df = df.to_pandas_df()
        numpy_array = df.values
        datatype_list=[]

        column_name_list=df.columns
        column_datatype_list=self.column_datatype_list
        column_wise_data_type=[]

        result_column_name=[]
        result_column_datatype=[]
        for x in range(len(column_name_list)):

            for y in range(len(numpy_array)):

                if column_datatype_list[x]=="<class 'str'>":
                    result=self.type_checker(numpy_array[y][x])
                    column_wise_data_type.append(result)

                else:
                    column_wise_data_type.append(str(column_datatype_list[x]))
            major_datatype,column_name=self.column_wise_datatype_(column_wise_data_type,column_name_list[x])
            result_column_name.append(column_name)
            result_column_datatype.append(major_datatype)
            column_wise_data_type=[]
        return result_column_name,result_column_datatype












    ##########################Main Function End############################################



    ###########################Control Functions###########################################




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

        series_data=pd.Series(data)

        detected_data_types=series_data.value_counts(normalize=True)
        for x in  range(len(list(detected_data_types))):
            data_percentage_list=list(detected_data_types)
            data_percentage=data_percentage_list[x]
            if data_percentage>=0.55:
                data_type_name_list=list(detected_data_types.index)
                major_datatype=data_type_name_list[x]


        return major_datatype,column_name


