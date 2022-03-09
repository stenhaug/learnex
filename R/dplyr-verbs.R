library(tidyverse)

shots <-
    tribble(
        ~name, ~baskets,
        "Jen",   7,
        "Jen",   9,
        "Sara",  4,
        "Sara",  6,
        "Ben",   5,
        "Ben",   3,
        "Ben",   2,
    )

shots %>% select(baskets)

shots %>% filter(name == "Ben")

read_table("https://raw.githubusercontent.com/tbertinmahieux/MSongsDB/master/Tasks_Demos/CoverSongs/shs_dataset_train.txt")







