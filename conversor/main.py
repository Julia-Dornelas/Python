def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Escolha a conversão desejada:")
    print("1: Celsius para Fahrenheit")
    print("2: Fahrenheit para Celsius")
    
    escolha = input("Digite o número da opção escolhida (1 ou 2): ")
    
    if escolha == '1':
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit.")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit é igual a {celsius} graus Celsius.")
    else:
        print("Opção inválida! Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()