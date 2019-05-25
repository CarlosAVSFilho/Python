def leiaDinheiro(text):
    n = input(text)

    if n.count(',') > 0:
        n = n.replace(',', '.')

    while is_float(n) is False:
        print(f'\033[91mERRO: "{n}" é um preço inválido!\033[m')
        n = input('Digite o preço: R$')
        if n.count(',') > 0:
            n = n.replace(',', '.')

    if is_float(n) is True:
        return float(n)


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


# def leiaDinheiro(text):
#     tpreco = ""
#     while True:
#         tpreco = input(text).replace(",", ".")
#
#         if not tpreco.replace(".", "").isnumeric():
#             print(f'\033[31m ERRO: "{tpreco}" não é um preço válido.')
#         else:
#             break
#     return float(tpreco)
