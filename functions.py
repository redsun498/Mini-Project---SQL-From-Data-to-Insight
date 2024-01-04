import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

def change_year(df, column_name, update_dict):
    '''
    This function takes a dataframe, column and dictionary as its parameters and fills out the missing values of that specific column .It uses the loc method to fix on the index (the key in the dictionary) and the column you selected. It then stores the value of the key as the new value in that specific index in the column.
    '''
    for index,year in update_dict.items():
        df.loc[index, column_name] = year
    return df

def create_year_column(df,column_name,new_column):
    '''
    This function first changes a columns data type into datetime and then creates a new column with only the years from that newly converted columns data.
    '''
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    df[new_column] = df[column_name].dt.year
    
    return df 

def genre_sales_df(df,genre_column, release_date_column,sales_column,new_df,new_df_column,label):
    '''
    This function creates a new dataframe by utilizing an existing dataframe and the following columns: Genre, Release Date and Total Sales. It adds up the values of the sales and resets the index. Then it creates a 'Genre Category' column for this new dataframe where the value will be either the genre that you choose as the label or 'other' if is not that one.
    '''
    new_df = df.groupby([genre_column, release_date_column])[sales_column].sum().reset_index()
    new_df[new_df_column] = new_df[genre_column].apply(lambda x: label if x == label else 'Other')
    
    return new_df


def selected_genre_sales_df(df,column,label):
    '''
    This function takes a sales dataframe, a genre column and a label as a parameter. It will parse through the dataframe and identify if the label appears in the column. If so, it will add this information to a new dataframe. 
    '''
    selected_genre_sales_df = df[df[column] == label]
    return selected_genre_sales_df

def total_sales_graph(x,y,df,label):
    '''
    This function plots the total sales of the video game genre you input. The parameters are the following: x is the column Release Year, y is the column Total Sales, df is the dataframe that provides the data for the graph and label is the video game genre you are working with. 
    '''
    plt.figure(figsize=(12, 8))
    sns.lineplot(x=x, y= y, data=df, label= label, marker='o')
    plt.title(f'Total Sales over time for {label} Genre')
    plt.xlabel(x)
    plt.ylabel(f'{y} (in millions)')
    plt.legend()
    plt.show()

def all_genres_vs_one_genre_graph(df,x,y,hue, label):
    '''
    This function takes in a dataframe,x, y, hue and label as its parameters. The x will be the column release year, the y will be the column total sales, the hue will be the column genre category and the data will be come from the dataframe. It will show the difference between the highlighted video game genre vs all the other ones. 
    '''
    plt.figure(figsize=(12, 8))
    sns.lineplot(x= x, y=y, hue=hue, data=df, marker='o')
    plt.title(f'Total Sales over time for {label} vs. Other Genres')
    plt.xlabel(x)
    plt.ylabel(f'{y} (in millions)')
    plt.legend(title='Genre Category')
    plt.show()

def t_stastistic_p_value(df,genre_column,sales_column,label):
    '''
    This function will show the T-statistic and P-value of a piece of data. The parameters are a dataframe, a genre column, a sales column and a label which stands for the video game genre.
    '''
    
    # Separate data for Adventure genre and other genres
    adventure_data = df[df[genre_column] == label][sales_column].dropna()
    other_genres_data = df[df[genre_column] != label][sales_column].dropna()

    # two-sample t-test
    t_stat, p_value = ttest_ind(adventure_data, other_genres_data, equal_var=False)

    # Display the results
    print(f'T-statistic: {t_stat}')
    print(f'P-value: {p_value}')
    
    




