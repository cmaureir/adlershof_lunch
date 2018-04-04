from datetime import datetime

from lib.albert import get_albert
from lib.lapetite import get_lapetite
from lib.esswirtschaft import get_esswirtschaft

week_days = {0: "Montag", 1: "Dienstag", 2: "Mittwoch", 3: "Donnerstag",
    4: "Freitag"}

if __name__ == "__main__":
    today = datetime.today().weekday()
    day_name = week_days[today]
    print(day_name)
    get_albert("http://www.albert-speisemanufaktur.de/speiseplan", day_name)
    print("-"*80)
    get_esswirtschaft("http://www.esswirtschaft.de/wochenkarte/wochenkarte.html",
        day_name)
    print("-"*80)
    #get_lapetite()
