# this is a vector
c(4, 2, 3)

# vectors are the basic building block of R

# i can assign it to a variable
stars = c(4, 2, 3)

# which then shows up in my environment
# easily can access it
stars + 2

# there's this idea of datatypes
class(stars)

# maybe that was the number of stars
names = c("ben", "daniel", "ariel")

class(names)

tibble(
    who = names,
    rating = stars
)
