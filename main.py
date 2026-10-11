import argparse
import sys
import os
from src.extractor import TextractExtractor

def main():
    parser = argparse.ArgumentParser(
        description="Transcreve o texto de uma imagem utilizando o AWS Textract."
    )
    parser.add_argument(
        "--image",
        type=str,
        default=os.path.join(os.path.dirname(__file__), "images", "lista-material-escolar.jpeg"),
        help="Caminho para o ficheiro de imagem"
    )
    parser.add_argument(
        "--region",
        type=str,
        default="us-east-1",
        help="Região da AWS (padrão: us-east-1)"
    )

    args = parser.parse_args()

    print(f"Processando imagem: {args.image}...\n")

    try:
        extractor = TextractExtractor(region_name=args.region)
        lines = extractor.extract_text_from_image(args.image)

        print("==================== TEXTO EXTRAÍDO ====================")
        for line in lines:
            print(f". {line}")
        print("========================================================")

    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()