class UserInput():

    @classmethod
    def int_input(cls, int_min = -10000, int_max=10000):
        '''
        ask for user input for a integer in a certain range
        then return the integer
        '''
        int_num = None
        is_int = False
        while not is_int:
            try:
                int_num = int(input('Please enter a integer: '))
                if int_num in range(int_min, int_max + 1):
                    is_int = True
                else:
                    print('Invalid input, please enter a integer from {} to {}!'.format(int_min, int_max))
            except:
                print('Invalid input, please enter a integer from {} to {}!'.format(int_min, int_max))
        print('==========================================')
        return int_num

    @classmethod
    def yes_input(cls):
        is_yes = False
        while not is_yes:
            try:
                yes_or_no = str(input('Please enter Yes or No: '))
                if yes_or_no.lower() == 'yes' or  yes_or_no.lower() == 'y':
                    is_yes = True
                    return True
                elif yes_or_no.lower() == 'no' or  yes_or_no.lower() == 'n':
                    is_yes = True
                    return False
                else:
                    print('Invalid input, please enter Yes or No!')
            except:
                print('Invalid input, please enter Yes or No!')
