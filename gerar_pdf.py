from fpdf import FPDF

# Dados da proposta
dados_proposta = {
    "cliente": "Empresa Alpha",
    "email": "contato@alpha.com",
    "telefone": "(11) 99999-1111",
    "servico": "Criação de Identidade Visual",
    "preco_base": "R$ 3.753,00",
    "desconto": "5%",
    "imposto": "15%",
    "prazo_execucao": "45 dias",
    "preco_final": "R$ 4.100,15",
    "validade_proposta": "45 dias"
}

# Criando o PDF
class PropostaPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, "Proposta Comercial", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(50, 50, 100)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def chapter_body(self, text):
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, text)
        self.ln()

    def add_section(self, title, content):
        self.chapter_title(title)
        self.chapter_body(content)


pdf = PropostaPDF()
pdf.add_page()

# Capa e apresentação
pdf.add_section("1. Apresentação", 
    "Prezados,\n\nÉ com satisfação que apresentamos nossa proposta para atender à sua demanda por Criação de Identidade Visual. "
    "Nosso compromisso é oferecer um serviço de alta qualidade, com foco em criatividade, agilidade e resultados tangíveis para sua marca.\n"
    "Contamos com uma equipe especializada e dedicada a entregar soluções alinhadas aos objetivos da sua empresa.\n")

# Detalhamento do serviço
pdf.add_section("2. Detalhamento do Serviço", 
    f"Serviço proposto: {dados_proposta['servico']}\n"
    f"Prazo de execução: {dados_proposta['prazo_execucao']}\n")

# Condições comerciais
pdf.add_section("3. Condições Comerciais", 
    f"Preço base: {dados_proposta['preco_base']}\n"
    f"Desconto: {dados_proposta['desconto']}\n"
    f"Imposto: {dados_proposta['imposto']}\n"
    f"Preço final com impostos: {dados_proposta['preco_final']}\n"
    f"Validade da proposta: {dados_proposta['validade_proposta']}\n")

# Contato e encerramento
pdf.add_section("4. Informações de Contato", 
    f"Cliente: {dados_proposta['cliente']}\n"
    f"E-mail: {dados_proposta['email']}\n"
    f"Telefone: {dados_proposta['telefone']}\n")

pdf.add_section("5. Agradecimento", 
    "Agradecemos pela oportunidade de apresentar esta proposta.\n"
    "Ficamos à disposição para quaisquer esclarecimentos e esperamos poder iniciar esta parceria em breve.\n\n"
    "Atenciosamente,\nEquipe Comercial\nEmpresa Exemplo Ltda.")

# Salvar o PDF
caminho_arquivo = "Proposta_Comercial_Exemplo.pdf"
pdf.output(caminho_arquivo)
caminho_arquivo
