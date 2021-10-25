class Main:
    pass


class AMD:
    def __init__(self, connector, memory, year_creation):
        self.connector = connector
        self.year_creation = year_creation
        self.memory = memory

    def output(self):
        print(self.connector,self.memory,self.year_creation)


class  RX_5500(AMD):
    pass


class RX_6600(AMD):
    pass


class RX_6700(AMD):

    pass


if __name__ == '__main__':
    rx_5500 = RX_5500("HDMI", " 8 gb", "2016 y.")
    rx_6600 = RX_6600("VGA", "8gb", "2018 y.")
    rx_6700 = RX_6700("HDMI", "12gb", "2020 y")
    jobs = [rx_5500, rx_6600, rx_5500]
    for j in jobs:
        j.output()