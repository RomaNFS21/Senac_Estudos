finalizar = ''

while finalizar.upper().lower() != "sim" :
    #################################### TIPO DE SERVIÇO ####################################
    tipoServico = str(input("\n Favor informe abaixo qual o tipo de serviço que sera realizado \n As opções são MANUTENÇÃO, REDES, SUPORTE, INSTALAÇÃO \n"))

    #################################### VALOR ####################################
    valorServico = float(input("\n Informe o valor total do serviço \n"))

    #################################### COMISSÃO ####################################
    porcentagemComissao = float(input("\n Qual sera a porcetagem de comissão nesse serviço ? \n "))
    #valorComissao = ((valorServico*porcentagemComissao) / 100)
 
    #################################### DATA ####################################
    diaHoje = str(input("\n Informe a data a seguir somente com números \n Qual o dia de hoje ? \n "))

    mesHoje = str(input("\n Qual o mês atual ? \n "))

    anoHoje = str(input("\n Qual o ano atual ? \n "))

    #################################### DESCRIÇÃO ####################################
    descricaoServico = str(input("\n Informe a descrição do serviço a ser realizado \n"))

    #################################### CONCLUIR OU CANCELAR ####################################
    print(f"\n \n O tipo de serviço a ser realizado é: {tipoServico} \n O valor do serviço ficou: R$ {valorServico} \n A comissão do serviço vai ser de: {porcentagemComissao}% \n O serviço vai ser registrado no dia: {diaHoje}/{mesHoje}/{anoHoje} \n A descrição do serviço é: {descricaoServico}")
    finalizar = str(input("\n Você confirma as informações acima ? \n Digite SIM para salvar, NÃO para preencher novamente e CANCELAR para descartar tudo \n"))