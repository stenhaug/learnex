import pandas as pd
import numpy as np

tmp = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003], 
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
} 
data = pd.DataFrame(tmp)

######################## essence ###############################

# filter and select
data[data.state == "Ohio"][["state", "year"]]
data.loc[data.state == "Ohio", ["state", "year"]]
data[data.state == "Nevada"].reset_index()

# arrange
data.sort_values(["state", "pop"])
data.sort_values(["state", "pop"], ascending = False)
data.sort_values(["state", "pop"], ascending = [True, False])

# mutate
data.assign(popyear = data.year + data.new2, new99 = 99)

# group by summarize
data.groupby("state", as_index = False).mean()

data.groupby("state", as_index = False).aggregate({"year": min})

data.groupby(
    "state", as_index = False
    ).aggregate(
        {
            "year": min,
            "pop": np.mean
        }
    )

data.groupby("state").aggregate(['min', max, np.median])

data.reindex()

######################## thinking ###############################

# get a series
data["year"]

# add a new column
data["new1"] = 1
data["new2"] = 2
data["new3"] = 3
data.new1
data

# remove that column 
del data["new1"]
data.drop(["new2", "new3"], axis = 1)

# select a couple of columns (still data because no type printed)
data[["state", "year"]]

# filter rows
data[0:2]
data[data.state == "Nevada"]

# https://towardsdatascience.com/8-ways-to-filter-pandas-dataframes-d34ba585c1b8
# iloc filters row and columns at the same time — i is for integer think of it as or index
data.iloc[0:2, 0:3]

# loc is the same but with label for like the word SURPRISE - label works with boolean
data.loc[data.state == "Nevada", ["state", "year"]]

# rank
data.sort_values("pop")
data.sort_values(["state", "pop"])

# the lesson here is passing a list refers to columns, a series refers to rows

# assign is mutate
data.assign(
    new4 = 4,
    new5 = data.new2 + data.year
)

# this is like select with a regex
# basically filter is a fancy way to look at the index labels
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html
# Subset the dataframe rows or columns according to the specified index labels. Note that this routine does not filter a dataframe on its contents. The filter is applied to the labels of the index.
data.filter(regex = "new")
data.filter(like = "new")

data[["pop", "new2", "new3"]].apply(lambda x: x + 1)

data.select_dtypes(include=np.number).apply(lambda x: x + 1000)

