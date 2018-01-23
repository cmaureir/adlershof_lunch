from lib.albert import *

if __name__ == "__main__":
    today = datetime.datetime.today().weekday()
    day_name = week_days[today]
    get_albert("http://www.albert-speisemanufaktur.de/speiseplan", day_name)
