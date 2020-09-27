from autofilter import autofilter_main
import time

start_time = time.time()
filter_obj=autofilter_main(True)
df,raw_detected_column_datatype=filter_obj.extract_file_data('data/accounts_receivable.csv','accounts_receivable.csv')

result_column_name,result_column_datatype=filter_obj.extract_major_datatype(df)


# result=filter_obj.describe_data(df)

filter_obj.check_relationship(df)


# print(result_column_name,result_column_datatype)

print("--- %s seconds ---" % (time.time() - start_time))




