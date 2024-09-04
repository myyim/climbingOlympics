import pandas as pd
import csv
from collections import defaultdict

url = 'https://olympics.com/OG2024/pdf/OG2024/CLB/OG2024_CLB_C74BL_CLBWBLCOMB------------SFNL--------.pdf' 
df = pd.read_html(url, converters=defaultdict(lambda: str))[0]
df.to_csv('women_semi.csv')
#df.to_csv('../data/currencycode.psv',index=False,sep='|',quoting=csv.QUOTE_NONE)

