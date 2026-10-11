# 📄 Transcrevendo Imagens em Texto com AWS Textract

Este projeto é uma aplicação em Python desenhada para extrair textos de imagens (OCR - Optical Character Recognition) utilizando o serviço **Amazon Textract** da AWS. 

O projeto foi estruturado seguindo boas práticas de desenvolvimento de software, incluindo modularização, tratamento de exceções, CLI (Interface de Linha de Comando) flexível e gestão de ambientes virtuais.

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.10+
- **AWS SDK:** `boto3`
- **Geração de Imagens (para testes):** `Pillow`
- **Serviço Cloud:** Amazon Textract (`detect_document_text`)

---

## 🏗️ Estrutura do Repositório

```text
aws-textract-image-ocr/
│
├── images/
│   └── lista-material-escolar.jpeg  # Imagem de teste gerada/utilizada
├── src/
│   ├── __init__.py
│   ├── extractor.py                 # Módulo de integração com AWS Textract
│   └── gerador_de_imagem_de_teste.py # Gera uma imagem de teste
├── .gitignore                       # Ficheiros ignorados pelo Git
├── LICENSE                          # Licença MIT do projeto
├── main.py                          # Ponto de entrada CLI da aplicação
└── requirements.txt                 # Dependências do projeto
```

---

## 🚀 Guia Passo a Passo: Configuração e Execução

Siga as instruções abaixo para clonar, configurar e executar o projeto no seu ambiente local.

### 1. Pré-requisitos Gerais

- **Python 3.10 ou superior** instalado na sua máquina.
- **Git** instalado.
- Uma conta ativa na **AWS** com permissões de utilização do Amazon Textract.
- **AWS CLI** instalado e configurado com as suas credenciais (`AWS Access Key ID` e `AWS Secret Access Key`).

Para configurar a AWS CLI na sua máquina, execute:
```bash
aws configure
```
*(Será solicitado que insira a sua Key, Secret, Região padrão [ex: `us-east-1`] e formato de saída [ex: `json`]).*

---

### 2. Clonar o Repositório

Abra o seu terminal/prompt de comando e clone este repositório:

```bash
git clone https://github.com/SEU-USUARIO/aws-textract-image-ocr.git
cd aws-textract-image-ocr
```

---

### 3. Criar e Ativar o Ambiente Virtual (`venv`)

É recomendável utilizar um ambiente virtual para isolar as dependências do projeto.

#### No Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### No Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### No Windows (Prompt de Comando - CMD):
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

*(Quando o ambiente estiver ativo, verá `(venv)` no início da linha do seu terminal).*

---

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias listadas no `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 5. Gerar a Imagem de Teste (`.jpeg`)

Se não tiver a imagem `lista-material-escolar.jpeg` na pasta `images/`, pode gerar uma imagem de exemplo com:

```bash
python -m src.gerador_de_imagem_de_teste
```
Este comando cria o ficheiro `images/lista-material-escolar.jpeg` contendo a lista visualizada na demonstração.

---

### 6. Executar o Sistema de OCR

Para processar a imagem e extrair o texto via AWS Textract, execute o ficheiro `main.py`:

```bash
python main.py
```

#### Opções de Linha de Comando (CLI):
Pode especificar uma imagem ou região AWS diferente através de argumentos:

```bash
python main.py --image images/lista-material-escolar.jpeg --region us-east-1
```

---

## 📊 Exemplo de Saída Esperada

Ao executar a aplicação, o resultado impresso no terminal será semelhante ao seguinte:

```text
Processando imagem: images/lista-material-escolar.jpeg...

==================== TEXTO EXTRAÍDO ====================
. Lista de Material Escolar
. 3 rolos de fita crepe
. 1 bloco de canson A4
. 1 fita adesiva
. 5 folhas de cartolina
. 3 placas de EVA
. 1 EVA com gliter
. 5 papel colorset
. 1 caneta permanente
. 1 pacote palito de sorvete
. 4 papel cartão
. 1 kit leoni n. 1
. 1 dicionário
. 1 pincel n.14
========================================================
```

---

## 💡 Insights & Aprendizados

- O **Amazon Textract** identifica autonomamente blocos de texto divididos por `LINE` (linha) e `WORD` (palavra).
- O endpoint `detect_document_text` é a escolha ideal e de menor latência para imagens simples, listas e documentos impressos sem tabelas complexas.
- O isolamento do código em módulos (`src/extractor.py`) permite reaproveitar a classe em APIs (FastAPI, Flask) ou funções Serverless (AWS Lambda).

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o ficheiro [LICENSE](LICENSE) para mais detalhes.