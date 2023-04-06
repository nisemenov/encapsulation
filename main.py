class FullEncapsulation:
    def __init__(self, attr_1):
        self.__attr_1 = attr_1
        self.__attr_2 = 100

    def get_attr(self):
        for i in self.__dict__.items():
            print(i)
        print()

    def set_attr(self,  v):
        self.__attr_3 = v
        print(f'\nAttribute {self.__attr_3 = } was set.\n')

    def __setattr__(self, key, value):
        if (key == '_FullEncapsulation__attr_1'
                or key == '_FullEncapsulation__attr_2'
                or key == '_FullEncapsulation__attr_3'):
            self.__dict__[key] = value
        else:
            raise AttributeError
