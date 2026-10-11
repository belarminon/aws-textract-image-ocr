import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError

class TextractExtractor:
    """Classe responsável pela integração com o serviço AWS Textract."""
    
    def __init__(self, region_name: str = "us-east-1"):
        try:
            self.client = boto3.client("textract", region_name=region_name)
        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(f"Erro ao inicializar o cliente AWS Textract: {str(e)}")

    def extract_text_from_image(self, image_path: str) -> list[str]:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"O ficheiro '{image_path}' não foi encontrado.")

        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        try:
            response = self.client.detect_document_text(
                Document={"Bytes": image_bytes}
            )
            
            extracted_lines = [
                block["Text"]
                for block in response.get("Blocks", [])
                if block["BlockType"] == "LINE"
            ]
            
            return extracted_lines

        except ClientError as e:
            raise RuntimeError(f"Erro na API do AWS Textract: {e.response['Error']['Message']}")
        except BotoCoreError as e:
            raise RuntimeError(f"Erro de comunicação com a AWS: {str(e)}")