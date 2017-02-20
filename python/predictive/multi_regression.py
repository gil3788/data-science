import pandas as pd
import statsmodels.api as sm

dataFrame = pd.read_excel('sample_data.xlsx')
dataFrame.head()
#sample_data.xlsx has the following structure: #
#OrderDate,Region(String),Rep(String),Item(String),Units,UnitCost,Total#


##Use pd.Categorical(dataFrame."Name of Column").codes to turn text data values to numerical codes##
##Stats models library cannot process "string" values##
dataFrame['Region_ord'] = pd.Categorical(dataFrame.Region).codes
dataFrame['Item_ord'] = pd.Categorical(dataFrame.Item).codes

#X-axis / multivaraite set to take into consideration#
X = dataFrame[['Units','Total']]
Y = dataFrame[['Item_ord']]

X1 = sm.add_constant(X)
est = sm.OLS(Y, X1).fit()

print est.summary()
