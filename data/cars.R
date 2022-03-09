library(tidyverse)
library(googlesheets4)

cars <-
    mtcars %>%
    rownames_to_column() %>%
    select(
        car = rowname,
        mpg,
        wt,
        cyl
    )

cars %>%
    write_sheet(
        "https://docs.google.com/spreadsheets/d/1rirbFEhKckQ_e-D7YUQyGuAaxGxolQphNC9mqztK5IM/edit#gid=0",
        "cars"
    )

cars %>% write_csv("data/cars.csv")
