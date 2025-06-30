from fpdf import FPDF
import os

def criar_pdf(proposta, output_dir='output/propostas'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(0, 10, f"Proposta Comercial para {proposta['Cliente']}", ln=True)
    pdf.cell(0, 10, f"Serviço: {proposta['Servico']}", ln=True)
    pdf.cell(0, 10, f"Preço Final: R$ {proposta['PrecoFinal']}", ln=True)
    pdf.cell(0, 10, f"Prazo: {proposta['PrazoFinal']} dias", ln=True)
    
    filename = f"{output_dir}/Proposta_{proposta['Cliente'].replace(' ', '_')}.pdf"
    pdf.output(filename)
