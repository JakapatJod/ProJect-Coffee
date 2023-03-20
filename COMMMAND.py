import colorama
from colorama import Back , Fore , Style
colorama.init(autoreset=True)

def Run():
    
    print(Back.GREEN+'='*160)
    print('')
    print(Fore.MAGENTA+'\t\t\t\t\t\t\t\t\t    STOCK')
    print(Fore.RED+'\t\tCoffee\t\t\tPRICE\t\t\tTEA\t\t\tPRICE\t\t\tDESSERT\t\t\tPRICE')
    print(Fore.YELLOW+'\t\tEspresso\t\t\ts\t\tGreen Tea\t\t\ts\t\t\tCupcake\t\t\ts')
    print(Fore.YELLOW+'\t\tCappucino\t\t\ts\t\tBlack Tea\t\t\ts\t\t\tDonut\t\t\ts')
    print(Fore.YELLOW+'\t\tLatte\t\t\t\ts\t\tChocolate\t\t\ts\t\t\tCheesecake\t\ts')
    print(Fore.YELLOW+'\t\tMocha\t\t\t\ts\t\tWhite Chocolate\t\t\ts\t\t\tPudding\t\t\ts')
    print(Fore.YELLOW+'\t\tAmericano\t\t\ts\t\tMilk\t\t\t\ts\t\t\tWaffle\t\t\ts')
    print(Fore.YELLOW+'\t\tMacchiato\t\t\ts\t\tThai Tea\t\t\ts\t\t\tCake\t\t\ts')

    print('')
    print(Back.GREEN+'='*160)

        
Run()