import numpy as np
np.random.seed(1)

# let's say we want to simulate someone having a 30% of getting a question right
# we want to compare a random variable to 0.3. should that be normal or uniform?

# here is code that does it once
np.random.normal(0.5, 0.1) < 0.3
np.random.uniform(0, 1) < 0.3

# if we do this, 10,000 times we should get about 30% correct

# gets too low of a percent
normal_draws = np.random.normal(0.5, 0.1, 10000)
np.mean(normal_draws < 0.3)

# gets the right percent
uniform_draws = np.random.uniform(0, 1, 10000)
np.mean(uniform_draws < 0.3)

# conclusion: use uniform
# for example, the following code simulates someone responding
# to a question they have a 30% chance of answering correct

if np.random.uniform(0, 1) < 0.3:
    "correct"
else:
    "incorrect"

