def make_coffee():
    customer = input('Welcome to Coffee Kiosk. Please enter your name: ')
    print('Hi {},We serve 3 different types of Coffee'.format(customer))
    print('Pick 1,2, or three according to your taste')
    print('1. White Coffee')
    print('2. Black Coffee')
    print('3. Tangawizi')
    print('------------------------------------\n')

    choice = int(input('Please enter your selection: \n'))

    def serve_coffee(customer, choice):
        if choice == 1:
            print('Grab a cup')
            print('Add some coffee')
            print('Add some sugar')
            print('Add milk')
            print('Stir your coffee\n')
            print('There you go {}, your white coffee is served...ENJOY'.format(customer))
        elif choice == 2:
            print('Grab a cup')
            print('Add some coffee')
            print('Add some sugar')
            print('Add hot water')
            print('Stir your coffee\n')
            print('There you go {}, your black coffee is served...ENJOY'.format(customer))
        elif choice == 3:
            print('Grab a cup')
            print('Add some coffee')
            print('Add some sugar')
            print('Add milk')
            print('Add hot water')
            print('Add tangawizi')
            print('Stir your coffee\n')
            print('There you go {}, your tangawizi coffee is served...ENJOY'.format(customer))
        else:
            # checks if the choices  are more than 3
            print('Sorry. We do not serve that type of coffee')

    serve_coffee(customer, choice)


make_coffee()
