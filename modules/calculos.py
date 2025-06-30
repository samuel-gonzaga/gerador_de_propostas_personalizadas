def calcular_proposta(dados_cliente):
    preco_base = dados_cliente.get('PrecoBase', 0)
    desconto = dados_cliente.get('Desconto', 0)
    imposto = dados_cliente.get('Imposto', 0)
    
    preco_descontado = preco_base * (1 - desconto/100)
    preco_final = preco_descontado * (1 + imposto/100)
    
    proposta = dados_cliente.copy()
    proposta['PrecoFinal'] = round(preco_final, 2)
    # Calcular prazo ajustado, por exemplo
    prazo_base = dados_cliente.get('PrazoDias', 0)
    proposta['PrazoFinal'] = prazo_base  # Pode ajustar conforme regras
    
    return proposta
