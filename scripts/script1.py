import pandas
visitors = [1234,789,4567,9506,4356]
errors = [34,90,75,52,60]
df = pandas.DataFrame( {"visitors": visitors, "errors": errors},index = ["mon","tue","wed","thur","fri"])

print(df)