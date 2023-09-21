
from rollingstock.rs_protocol import CarConfig
from location import Location

from config import flatcar


def main():
    fc = CarConfig(railroad="alaska rail", prefix='arr', number=1001,
                   location=Location('freight_depot','maps/freight_depot.pdf'), **flatcar)



if __name__ == '__main__':
    main()
