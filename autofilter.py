# import sklearn
# import scipy
# import vaex, pandas as pd
# # import ppscore as pps
# import numpy as np
# import cupy as cp

# import os
# # import modin.pandas as pd

import sklearn
import time

import vaex, pandas as pd
import warnings
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
import logging
# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.WARNING)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')

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
        """

        :param file_path: This is the data location,ex: csv file location
        :param file_name: This is the file name
        :return:
        """
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

        elif file_type =='s3':
            df = vaex.open(file_path)


        self.column_datatype_list = []
        column_data_types_raw = list(df.dtypes)
        for x in range(len(column_data_types_raw)):
            self.column_datatype_list.append(str(column_data_types_raw[x]))
        raw_detected_column_datatype=self.column_datatype_list
        return df,raw_detected_column_datatype

    def extract_major_datatype(self,df,majority_ratio=0.55):
        """

        :param majority_ratio:
        :param df: df object to extract major datatype
        :return:
        """
        df = df.to_pandas_df()
        numpy_array = df.to_numpy()
        print(df)


        datatype_list=[]

        column_name_list=df.columns
        column_datatype_list=self.column_datatype_list
        column_wise_data_type=[]

        result_column_name=[]
        result_column_datatype=[]
        for x in range(len(column_name_list)):

            for y in range(len(numpy_array)):

                if column_datatype_list[x]=="<class 'str'>":
                    result,remove_row_flag=self.type_checker(numpy_array[y][x])
                    column_wise_data_type.append(result)
                    if remove_row_flag==True:
                        logger.critical('Fatal error. Cannot continue at'+str(column_name_list[x])+str(y))

                else:
                    column_wise_data_type.append(str(column_datatype_list[x]))
            major_datatype,column_name=self.column_wise_datatype_(column_wise_data_type,column_name_list[x],majority_ratio)
            result_column_name.append(column_name)
            result_column_datatype.append(major_datatype)
            column_wise_data_type=[]
        return result_column_name,result_column_datatype


    def describe_data(self,df):
        """

        :param df:
        """
        print('Data stats')

        stats_df=df.describe()
        describe_data_list=[]
        column_names_list=list(stats_df.columns)
        for x in range(len(column_names_list)):
            result=stats_df[column_names_list[x]]
            json_data_format={'count':result['count'],'null_count':result['NA'],'mean':result['mean'],'std':result['std'],'min':result['min'],'max':result['max']}
            data={'column_name':column_names_list[x],'describe_data':json_data_format}
            describe_data_list.append(data)


        return describe_data_list




    def check_relationship(self,df):
        print('asdas')

        # df = pd.read_csv('data/accounts_receivable.csv')
        # pps.matrix(df)
        # print(pps.matrix(df))
        # plt.figure(1)
        # plt.figure(figsize=(16, 12))
        # sns.heatmap(pps.matrix(df), annot=True, fmt=".2f")
        # plt.show()



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
        remove_row_flag=False
        try:
            pd.to_datetime(data)
            detected_type='datetime'
        except:
            try:
                float(data)
                detected_type = 'float64'
            except:
                try:
                    int(data)
                    detected_type = 'int'
                except:
                    detected_type='null'
                    remove_row_flag=True

        return detected_type,remove_row_flag


    def column_wise_datatype_(self,data,column_name,majority_ratio):

        series_data=pd.Series(data)
        detected_data_types=series_data.value_counts(normalize=True)
        for x in  range(len(list(detected_data_types))):
            data_percentage_list=list(detected_data_types)
            data_percentage=data_percentage_list[x]
            if data_percentage>=majority_ratio:
                data_type_name_list=list(detected_data_types.index)
                major_datatype=data_type_name_list[x]


        return major_datatype,column_name


