import pickle

crypto = [
    ("bitcoin", "spot", 35000),
    ("ethereum", "spot", 2500),
    ("near", "spot", 9)
]

test1 = [('Natasha', 24)]
test2 = [('Andrey', 21)]
test3 = [('Oliviya', 2)]

try:
    # "a+"
    file = open("out.bin", "rb")

    try:
        # pickle.dump(crypto, file)
        # obj = pickle.load(file)
        # print(obj)

        # pickle.dump(test1, file)
        # pickle.dump(test2, file)
        # pickle.dump(test3, file)

        obj1 = pickle.load(file)
        obj2 = pickle.load(file)
        obj3 = pickle.load(file)

        print(obj1, obj2, obj3, sep="\n")

    finally:
        file.close()

except FileNotFoundError:
    print("No such file or directory")
