import pandas as pd
xls = pd.ExcelFile('data/Sales_Pipeline_Forecast_Model_2023.xlsx')

sheets = xls.sheet_names
print(sheets)

sp_df = pd.read_excel(xls, 'SuperPixel')
print(sp_df.head())

wsc_df = pd.read_excel(xls, 'Wasted Spend Calculator')
print(wsc_df.head())

ab_df = pd.read_excel(xls, 'Audience Builder')
print(ab_df.head())

af_df = pd.read_excel(xls, 'Affiliate Program')
print(af_df.head())