from NumberServed import Restaurant


class IceCreamStand(Restaurant):
    """ An ice cream stand is a specific kind of restaurant """

    def __init__(self, flavors):
        super().__init__("IceCreamStand", "Ice cream stuff")
        self.flavors = flavors

    def displayFlavors(self):
        print("Flavors availible : ")
        for flavor in self.flavors:
            print(flavor)


myIceCreamRest = IceCreamStand(['Scimo', 'Panito', 'Mongo'])
myIceCreamRest.describe_restaurant()
myIceCreamRest.displayFlavors()
