from autofilter import autofilter_main
import time

start_time = time.time()
filter_obj=autofilter_main(True)
df,raw_detected_column_datatype=filter_obj.extract_file_data('data/haleys-ac-2019.csv','haleys-ac-2019.csv')
result_column_name,result_column_datatype=filter_obj.extract_major_datatype(df)
print(result_column_name,result_column_datatype)

print("--- %s seconds ---" % (time.time() - start_time))




