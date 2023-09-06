
from lumber_camp import LumberCampConfig
from lumbermill import LumberMillConfig
from flatcar import FlatcarConfig
from stake_flatcar import StakeFlatcarConfig


def main():
    loging_camp = LumberCampConfig()
    lumbermill = LumberMillConfig()
    print(loging_camp)
    print(lumbermill)
    loging_camp.load_car(8, "logs")
    loging_camp.load_car(8, "cordwood")
    loging_camp.show_stock()
    loging_camp.reset_stock(sec=1.0)
    loging_camp.show_stock()
    flatcar = FlatcarConfig()
    print(flatcar.product_1)
    print(flatcar.max_load_1)
    flatcar.railroad = "Canadian National"
    print(flatcar.railroad)
    flatcar.road_number_prefix = "CN"
    print(flatcar.road_number_prefix)
    flatcar.road_number = 123456
    print(flatcar.road_number)
    flatcar.load_1 = 8
    print(flatcar.show_load())
    print(flatcar.show_durability())
    flatcar.reduce_durability(1)
    print(flatcar.show_durability())
    stake_flatcar = StakeFlatcarConfig()
    print(stake_flatcar.product_1)








if __name__ == '__main__':
    main()