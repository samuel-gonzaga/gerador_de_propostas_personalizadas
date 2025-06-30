import pandas as pd
import random

# Função fornecida para calcular a proposta
def calcular_proposta(dados_cliente):
    preco_base = dados_cliente.get('PrecoBase', 0)
    desconto = dados_cliente.get('Desconto', 0)
    imposto = dados_cliente.get('Imposto', 0)

    preco_descontado = preco_base * (1 - desconto / 100)
    preco_final = preco_descontado * (1 + imposto / 100)

    proposta = dados_cliente.copy()
    proposta['PrecoFinal'] = round(preco_final, 2)

    prazo_base = dados_cliente.get('PrazoDias', 0)
    proposta['PrazoFinal'] = prazo_base  # aqui pode aplicar regra futura

    return proposta

# Dados simulados
clientes = [
    {"Nome": "Empresa Alpha", "Email": "contato@alpha.com", "Telefone": "(11) 99999-1111"},
    {"Nome": "Beta Corp", "Email": "vendas@betacorp.com", "Telefone": "(21) 98888-2222"},
    {"Nome": "Gamma Ltda", "Email": "gamma@gammaltda.com", "Telefone": "(31) 97777-3333"},
    {"Nome": "Delta Serviços", "Email": "delta@servicos.com", "Telefone": "(41) 96666-4444"},
    {"Nome": "Epsilon Solutions", "Email": "contact@epsilon.com", "Telefone": "(51) 95555-5555"},
]

servicos = [
    "Consultoria de Marketing",
    "Desenvolvimento Web",
    "Gestão de Redes Sociais",
    "Criação de Identidade Visual",
    "Automação de Processos",
    "Treinamento Corporativo",
]

propostas = []

# Gerar dados e calcular proposta
for cliente in clientes:
    for _ in range(random.randint(1, 3)):
        servico = random.choice(servicos)
        preco_base = random.randint(2000, 8000)
        desconto = random.choice([0, 5, 10, 15])
        imposto = 15  # Fixo
        prazo_dias = random.choice([15, 30, 45])

        dados = {
            "Cliente": cliente["Nome"],
            "Email": cliente["Email"],
            "Telefone": cliente["Telefone"],
            "Servico": servico,
            "PrecoBase": preco_base,
            "Desconto": desconto,
            "Imposto": imposto,
            "PrazoDias": prazo_dias
        }

        proposta = calcular_proposta(dados)
        propostas.append(proposta)

# Criar DataFrame e salvar em Excel
df = pd.DataFrame(propostas)
file_path = "propostas_calculadas.xlsx"
df.to_excel(file_path, index=False)
