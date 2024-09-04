import tabula
import pandas as pd
dfs = tabula.read_pdf('men_boulder.pdf',pages=1,stream=True)

specPages = {'dbtran25':'14-47','frd15':'314-326','pis12':'156-165'}
specfile = './FFM7.0DataSpec.Debit.pdf'
spec = 'dbtran25' # 'dbtran25', 'frd15', 'pis12'
pages = specPages[spec]	# specPages[spec], 'all'
outdir = '../data/'

dfs = tabula.read_pdf('men_boulder.pdf',pages=1,stream=True)

"""
for k,df in enumerate(dfs):
    # Correct column names
    for i,c in enumerate(df.columns):
        val = str(df.at[0,c])
        if 'nan' not in val.lower():
            df.rename(columns={c:c+' '+val},inplace=True)

    # Remove the 0th row and reset index
    df.drop([0],inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Concatenate dataframes
    if k == 0:
        outdf = df.copy()
    else:
        outdf = pd.concat([outdf,df],ignore_index=True)

# Group
col_ref = 'Field Order'  # a column without multi-line rows
col_merge = 'Field Format/Description'  # column with multi-line rows (modify for columns)
for i in outdf.index:  # Need to be string to use join
    outdf.at[i,col_merge] = str(outdf.at[i,col_merge])
fid = outdf[col_ref].notna().cumsum()
cols = dict.fromkeys(outdf.columns.difference([col_merge]), 'first')
cols[col_merge] = ' '.join
outdf = outdf.groupby(fid).agg(cols)
outdf.reset_index(drop=True,inplace=True)
outdf = outdf[['Field Name','Field Format/Description','Type','Position']]  # column order

outdf.set_index('Field Name',inplace=True)
print(outdf)
outdf.T.to_json(outdir+spec+'.json')
outdf.to_csv(outdir+spec+'.csv')
"""
