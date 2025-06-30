# Usa imagem oficial do Python com Debian (já compatível com os pacotes necessários)
FROM python:3.11-slim

# Atualiza os pacotes e instala dependências do WeasyPrint (GTK, Pango, Cairo, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libxml2 \
    libxslt1.1 \
    libjpeg-dev \
    libpng-dev \
    curl \
    && apt-get clean

# Define diretório de trabalho no container
WORKDIR /app

# Copia todos os arquivos do seu projeto local para o container
COPY . .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão ao iniciar o container (ajuste se seu script principal for outro)
CMD ["python", "main.py"]
