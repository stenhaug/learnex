library(tidyverse)
library(googlesheets4)

raw <-
    read_sheet(
        "https://docs.google.com/spreadsheets/d/1rirbFEhKckQ_e-D7YUQyGuAaxGxolQphNC9mqztK5IM/edit#gid=0",
        "raw"
    )

raw %>% write_csv("data/test.csv")

read_csv("https://raw.githubusercontent.com/stenhaug/learnex/master/data/test.csv")

read_csv("https://bit.ly/bentestcsvchange")

