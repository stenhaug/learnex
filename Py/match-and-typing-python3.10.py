# https://realpython.com/python310-new-features/#matching-literal-patterns
# https://towardsdatascience.com/switch-case-statements-are-coming-to-python-d0caf7b2bfd3

# basic with list
numbers = []

match numbers:
        case []:
            "SDKHLFSDI"

match numbers:
        case []:
            what = 0
        case [first, *rest]:
            1

# basic with dict
something = {
    "ben": "awesome",
    "emma": "great"
}

match something:
    case {"ben": y}:
        x = 10

y
x

# nested dict
user = {
    "name": {"first": "Pablo", "last": "Galindo Salgado"},
    "title": "Python 3.10 release manager",
}

match user:
    case {"name": {"first": first_name}}:
        pass

first_name

# function
def sum_list(numbers):
    match numbers:
        case []:
            return 0
        case [first, *rest]:
            return first + sum_list(rest)

sum_list([1, 2, 3])

# typing
def mean(numbers: list[float | int]) -> float:
    return sum(numbers) / len(numbers)

mean([0, 1, 100])

sum([10, 1])

# see for example here age must be an int
user = {"dob": {
        "date": "1957-05-20T08:36:09.083Z",
        "age": 64
    }}

match user:
        case {"dob": {"age": int(age)}}:
            age
        case {"dob": dob}:
            now = datetime.now()
            dob_date = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S")
            


