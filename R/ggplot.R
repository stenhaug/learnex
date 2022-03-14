# links
## https://ggplot2.tidyverse.org/
## https://themockup.blog/static/slides/intro-plot.html#6
## https://r4ds.had.co.nz/data-visualisation.html
## https://ggplot2-book.org/
## https://www.r-graph-gallery.com/

library(tidyverse)

cars = read_csv("https://bit.ly/simple-data-cars")

cars %>%
    ggplot(aes(x = wt, y = mpg, color = as.factor(cyl))) +
    geom_point() +
    geom_smooth(se = FALSE, method = "lm", size = 0.2) +
    xlim(0, NA) +
    ylim(0, NA) +
    labs(
        x = "Weight of the Car",
        y = "MPG",
        title = "Heavier cars have worse fuel efficiency"
    )

cars %>%
    mutate(car_ordered = fct_reorder(car, mpg)) %>%
    ggplot(aes(y = car_ordered, x = mpg, fill = as.factor(cyl))) +
    geom_col() +
    theme_bw(base_size = 10) +
    labs(
        x = "Miles per Gallon (MPG)",
        y = NULL,
        fill = "Cylinders",
        title = "Cars by fuel efficiency",
        subtitle = "4 cylinder cars have best mpg",
        caption = "•Data from mpg in R.\n•Showing power of ggplot"
    )
