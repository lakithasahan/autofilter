from autofilter import autofilter_main
import time
import enum
import os
start_time = time.time()
filter_obj=autofilter_main('data/accounts_receivable.csv','accounts_receivable.csv')
print("--- %s seconds ---" % (time.time() - start_time))
print(os.path.getsize('data/accounts_receivable.csv'))



# Enum for size units
class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4
def convert_unit(size_in_bytes, unit):
   """ Convert the size from bytes to other units like KB, MB or GB"""
   if unit == SIZE_UNIT.KB:
       return size_in_bytes/1024
   elif unit == SIZE_UNIT.MB:
       return size_in_bytes/(1024*1024)
   elif unit == SIZE_UNIT.GB:
       return size_in_bytes/(1024*1024*1024)
   else:
       return size_in_bytes


def get_file_size(file_name, size_type = SIZE_UNIT.BYTES ):
   """ Get file in size in given unit like KB, MB or GB"""
   size = os.path.getsize(file_name)
   return convert_unit(size, size_type)


size = get_file_size('data/accounts_receivable.csv', SIZE_UNIT.MB)
print('Size of file is : ', size ,  'MB')
