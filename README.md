# Autofilter
![filter_data_python](https://user-images.githubusercontent.com/24733068/94353989-0bfd5180-00ba-11eb-937c-6f233010a696.png)


Autofilter is a Python library for dealing with data cleansing.



## Usage

```python
from autofilter import autofilter_main
import time

start_time = time.time()
filter_obj=autofilter_main(True)
df,raw_detected_column_datatype=filter_obj.extract_file_data('data/accounts_receivable.csv','accounts_receivable.csv')

result_column_name,result_column_datatype=filter_obj.extract_major_datatype(df)
result=filter_obj.describe_data(df)
filter_obj.check_relationship(df)


# print(result_column_name,result_column_datatype)

print("--- %s seconds ---" % (time.time() - start_time))
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
