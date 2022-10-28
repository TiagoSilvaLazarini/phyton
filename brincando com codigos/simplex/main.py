from colorama import Fore
import max
import min

if __name__ == "__main__":

    _res = False

    while True:
        print(f"{Fore.BLUE}----------{Fore.MAGENTA}Resolutor de funções simplex{Fore.BLUE}----------")
        print(f"Digite {Fore.CYAN}(max){Fore.BLUE} para maximização, {Fore.CYAN}(min){Fore.BLUE} para minimização ou {Fore.CYAN}(s){Fore.BLUE} para sair")
        match_str = input(f"{Fore.MAGENTA}digite{Fore.RESET} ༼ つ ◕_◕ ༽つ: ")
        match match_str:
            case "min":
                print(f"{Fore.RED}Sempre coloque um espaço emtre as variaveis ou numeros diferentes ex:(2+3-6-8) -> (2 3 -6 -8){Fore.RESET}")
                simplex = min.Simplex()
                variaveis = input(f"{Fore.BLUE}entre o nome das variaveis ex:{Fore.CYAN}(x X y z ...){Fore.BLUE}:{Fore.RESET} ")
                while _res == False:
                    try:
                        folga = int(input(f"{Fore.BLUE}numero de variaveis de folga ex:{Fore.CYAN}(serão 3 funções então 3){Fore.BLUE}:{Fore.RESET} "))
                        _res = True
                    except:
                        print(f"{Fore.RED}Ooops! esta entrada so aceita numeros){Fore.RESET}")
                simplex.edit_ord_a(variaveis.split(),folga)
                _res = False
                while _res == False:
                    try:
                        lst = list(map(int, input(f"{Fore.BLUE}entre o max Z{Fore.CYAN}(sem o nome das variaveis){Fore.BLUE}:{Fore.RESET} ").strip().split()))
                        _res = simplex.set_max_Z(lst)
                    except:
                        print(f"{Fore.RED}Ooops! esta entrada so aceita numeros){Fore.RESET}")

                for _ in range(folga):
                    _res = False
                    while _res == False:
                        try:
                            lst = list(map(int, input(f"{Fore.BLUE}entre as restrições{Fore.CYAN}(sem o nome das variaveis){Fore.BLUE}:{Fore.RESET} ").strip().split()))
                            _res = simplex.set_restricoes(lst)
                        except:
                            print(f"{Fore.RED}Ooops! esta entrada so aceita numeros){Fore.RESET}")
                
                simplex.resolver()

            case "max":
                print(f"{Fore.RED}Sempre coloque um espaço emtre as variaveis ou numeros diferentes ex:(2+3-6-8) -> (2 3 -6 -8){Fore.RESET}")
                simplex = max.Simplex()
                variaveis = input(f"{Fore.BLUE}entre o nome das variaveis ex:{Fore.CYAN}(x X y z ...){Fore.BLUE}:{Fore.RESET} ")
                while _res == False:
                    try:
                        folga = int(input(f"{Fore.BLUE}numero de variaveis de folga ex:{Fore.CYAN}(serão 3 funções então 3){Fore.BLUE}:{Fore.RESET} "))
                        _res = True
                    except:
                        print(f"{Fore.RED}Ooops! esta entrada so aceita numeros){Fore.RESET}")
                simplex.edit_ord_a(variaveis.split(),folga)
                _res = False
                while _res == False:
                    try:
                        lst = list(map(int, input(f"{Fore.BLUE}entre o max Z{Fore.CYAN}(sem o nome das variaveis){Fore.BLUE}:{Fore.RESET} ").strip().split()))
                        _res = simplex.set_max_Z(lst)
                    except:
                        print(f"{Fore.RED}Ooops! esta entrada so aceita numeros){Fore.RESET}")

                for _ in range(folga):
                    _res = False
                    while _res == False:
                        try:
                            lst = list(map(int, input(f"{Fore.BLUE}entre as restrições{Fore.CYAN}(sem o nome das variaveis){Fore.BLUE}:{Fore.RESET} ").strip().split()))
                            _res = simplex.set_restricoes(lst)
                        except:
                            print(f"{Fore.RED}Ooops! esta entrada so aceita numeros){Fore.RESET}")
                
                simplex.resolver()

            case "s":
                print(f"{Fore.YELLOW}----------Estamos eperando sua volta----------{Fore.RESET}")
                break
            case _:
                ...