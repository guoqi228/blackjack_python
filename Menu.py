class Menu():

    def __init__(self, name = 'Default Menu', menu = ['Option 0', 'Option 1', 'Option 2']):
        self.menu = menu
        self.name = name

    def show_menu(self):
        print('==========================================')
        print(self.name)
        print('==========================================')
        for i, item in enumerate(self.menu):
            print('{} -----> {}'.format(i, item))
        print('==========================================')

    def menu_length(self):
        return len(self.menu)
