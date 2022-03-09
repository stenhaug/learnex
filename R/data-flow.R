library(tidyverse)
library(googlesheets4)

raw <-
    read_sheet(
        "https://docs.google.com/spreadsheets/d/1rirbFEhKckQ_e-D7YUQyGuAaxGxolQphNC9mqztK5IM/edit#gid=0",
        "raw"
    )

raw %>% write_csv("data/test.csv")



