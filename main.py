from modules.gerar_proposta import gerar_pdf

def main():
    proposta = {
        "cliente": "Maria Oliveira",
        "servico": "Consultoria de Marketing",
        "valor": "R$ 2.500,00",
        "prazo": "7 dias úteis",
        "desconto": "10%"
    }
    gerar_pdf(proposta, output_dir="output/propostas")

if __name__ == "__main__":
    main()
