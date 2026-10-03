import pandas as pd

# print(pd.__version__)

#series= pandas 1D labeled array  that can hold any type of data 

# data=[100,102,104,123,321,431]
# series=pd.Series(data,index=["a","b","c","e","r","t"])
# series.loc["a"]=1000
# print(series)
# print(series.loc["a"])     # return value at this label
# print(series[series>=110]) 




# calories={
#     "day1":1750,
#     "day02":2100,
#     "day03":1700
# }


# series=pd.Series(calories) # dont user index as keys act as index label
# print(series)




#dataframes are the tabular structure have rows and columns

# data={
#     "name":["spongebob","patric","squidward"],
#     "age":[30,20,40]
# }

# df=pd.DataFrame(data)

# #add new column
# df["job"]=["cooks","n/a","cashier"]
# #add new row 
# new_rows=pd.DataFrame(
#     [{"name":"sandy",
#     "age":28,"job":"engineer"},
#     {"name":"deny",
#     "age":58,"job":"ceo"},
#     {"name":"sam",
#     "age":39,"job":"driver"}]
# )
# df=pd.concat([df,new_rows])
# print(df)



#CSV and jason import in panda

df=pd.read_csv("data.csv")
# print(df)
#use to_string() for all data form that file 

dr=pd.read_json("data.json")
# print(dr)

#selection techniques

#by col

# print(df["rating"])

#by rows

# print(df.loc[1])

#searching 

order_no=input("enter order_id to get details: ")

try:
    order_no = int(order_no)
    order = df[df["order_id"] == order_no]

    if order.empty:
        print("order id not found!!")
    else:
        print(order)
except ValueError:
    print(" order id not found!!")



































































































































































