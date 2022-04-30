library(tidyverse)

stars = c(4, 3, 2)

stars + 11

class(stars)

names = c("ben", "daniel", "ariel")
class(names)

movie_ratings = tibble(
    who = names,
    rating = stars
)

movie_ratings$rating




