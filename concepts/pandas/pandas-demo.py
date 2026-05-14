import pandas as pd 


df = pd.read_csv("sample.csv")
print(df)
print(df.head()) # load first five data


# sorting 
print("\n")
print("--------------Ascending order(sort)------------")
sorted_df=df.sort_values(by="Age")  # ascending 
print(sorted_df)

print("\n")
print("-----------Descending order (sort)------------")
sorted_df=df.sort_values(by="Age", ascending=False)
print(sorted_df)

print("\n")
print("----------Age is greater than 20(filtered)--------------")
filtered=df[df['Age']>20]
print(filtered)

# convert filtered data in csv 
print("\n")
filtered.to_csv('under_twenty.csv',index=False)
print("--------------Average----------------")
print("Average Age: ",df['Age'].mean)
# print("Average Age: ",df['rating'].mean())




