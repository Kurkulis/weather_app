def readfile(file):
    lines = []
    city = file.rsplit(".", 1)[0].capitalize()
    with open(file, "r") as f:
        data = f.readlines()
        for line in data:
            lines += line.strip().split(" ")
    print("Loaded weather data from", city, end="")
    readfile.weatherData = lines


def getDate(date):
    day = date[3:5]+"-"+date[0:2]
    data = [s for s in readfile.weatherData if day in s]
    data = str(data).strip("[]").split(";")
    print("The weather on", date, "was on average", data[2], "centigrade")
    print("The lowest temperature was",
          data[3], "and the highest temperature was", data[4])
    print("There was", data[1], "mm rain", end="")


while True:
    print("ACME WEATHER DATA APP")
    print("1) Choose weather data file")
    print("2) See data for selected day")
    print("3) Calculate average statistics for the data")
    print("4) Print a scatterplot of the average temperatures")
    print("0) Quit program")
    choice = input("Choose what to do: ")

    if choice == "0":
        break

    elif choice == "1":
        file = input("Give name of the file: ")
        readfile(file)

    elif choice == "2":
        date = input("Give a date (dd.mm): ")
        getDate(date)

    print("\n")
