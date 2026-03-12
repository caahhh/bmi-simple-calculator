#var
def pedir_numero(mensagem):
    while True:
        try:
                return float(input(mensagem))#
        except ValueError:
            print("Valor inválido, digite novamente.")

altura = pedir_numero("Informe sua altura (0.00): ")
peso = pedir_numero('Informe seu peso (00.00): ')

imc = peso/(altura * altura)

if imc < 18.50:
    print(f'Seu imc é: {imc:.1f} e está abaixo do normal')
elif imc <= 24.90:
    print(f'Seu imc é: {imc:.1f} e está normal')
elif imc >= 25:
    print(f'Seu imc é: {imc:.1f} e está acima do normal')