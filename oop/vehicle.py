class Vehicle:

# special method for constructs
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        # priavte with __
        self.__warnings = []


    # sepcial method to output an object of the class as i.e. print(car1)
    def __repr__(self):
        print('Printing...')
        return 'Top Speed {}, Warning: {}'.format(self.top_speed, len(self.__warnings))

    # since private, can only be accessed INSIDE the class
    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)


    def get_warnings(self):
        return self.__warnings


    def drive(self):        
        print('I am driving {}'.format(self.top_speed))
