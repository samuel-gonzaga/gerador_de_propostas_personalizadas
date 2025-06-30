from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

def gerar_pdf(dados, template_dir='templates', output_dir='output/propostas'):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("proposta_template.html")
    
    html_content = template.render(**dados)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"Proposta_{dados['cliente'].replace(' ', '_')}.pdf"
    path = os.path.join(output_dir, filename)

    HTML(string=html_content).write_pdf(path)
    print(f"Proposta gerada: {path}")
