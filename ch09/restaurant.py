# 9-1 Restaurant class


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant.")
        print(str(self.number_served) + " people visited this restaurant before.")

    def open_restaurant(self):
        print("Welcome to " + self.restaurant_name)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        # Must pass parameters to super class, and put default valued param at the end
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def describe_ice_cream(self):
        print("Have following flavors:")
        for flavor in self.flavors:
            print(flavor)
