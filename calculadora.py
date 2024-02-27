print('#-' * 15), print('Bem vindo a calculadora 3000!'), print('#-' * 15)
print('\n Digite + para adição \n Digite - para subtração \n / Digite para divisão \n * Digite para multiplicação')    
prefixo = str(input('Digite o prefixo desejado: '))
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo núemro: '))

adc = n1 + n2 #Adição
sub = n1 - n2 #Subtração
div = n1 / n2 #Divisão
mult = n1 * n2 #Multiplicação

if prefixo == '+': 
    print('{} + {} = {}'.format(n1, n2, adc))
else:
    if prefixo == '-': 
        print('{} - {} = {}'.format(n1, n2, sub))
    else:
        if prefixo == '/': 
            print('{} / {} = {:.2f}'.format(n1, n2, div))
        else:
            if prefixo == '*': 
                print('{} * {} = {}'.format(n1, n2, mult))
