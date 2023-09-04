from config import loging_camp, sawmill, production_ratio
from lumber_camp import LumberCampConfig
from lumbermill import LumberMillConfig


def main():
    loging_camp = LumberCampConfig()
    lumbermill = LumberMillConfig()
    print(loging_camp)

    loging_camp.load_car(8, "Logs")
    loging_camp.load_car(8, "Cordwood")
    loging_camp.show_stock()
    loging_camp.reset_stock(sec=1.0)
    loging_camp.show_stock()
    while True:
        lumbermill.produce_output(ratio=lumbermill.ratio)
        print('producing')







if __name__ == '__main__':
    main()