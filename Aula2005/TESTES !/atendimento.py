
def atendimento():
    print('\nATENDIMENTO:')
    print('-' * 12)
    print('1. SALDO')
    print('2. EXTRATO')
    print('3. PIX')
    print('4. VOLTAR')
    print('-' * 12)

    opcao = input('ESCOLHA: ')

    match opcao:
        case "1":
            print('SEU SALDO É: R$ 999.999.999')
            #saldo()

        case "2":
            print('EXTRATO: ')
            #extrato()
        case "3":
            print('ÁREA PIX:')
            #pix()
        case "4":
            print('...VOLTANDO AO MENU PRINCIPAL...')
            #bank.sistema()

        case "_":
            print('OPÇÃO INVÁLIDA!')
        

atendimento()
