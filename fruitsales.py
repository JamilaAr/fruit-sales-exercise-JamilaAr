import pandas as pd

#create DataFrame with fruits sales information

data ={'Apples' : [35, 41],
       'Bananas' : [21, 34]
}

#Define the index of DataFrame

index = ['2017 Sales', '2018 Sales']

#create the DataFrame
df = pd.DataFrame(data, index)

#print the DataFrame
print(df)

#write the data to a CSV file
 
df.to_csv('fruit.csv')


print("the data has been printed to 'fruit.csv' file")




