import os
from PIL import Image, ImageDraw, ImageFont

def generate_sample_jpeg():
    os.makedirs("images", exist_ok=True)
    image_path = os.path.join("images", "lista-material-escolar.jpeg")
    
    # Criar uma imagem branca
    width, height = 800, 1000
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    lines = [
        "Lista de Material Escolar",
        ".3 rolos de fita crepe",
        ".1 bloco de canson A4",
        ".1 fita adesiva",
        ".5 folhas de cartolina",
        ".3 placas de EVA",
        ".1 EVA com gliter",
        ".5 papel colorset",
        ".1 caneta permanente",
        ".1 pacote palito de sorvete",
        ".4 papel cartão",
        ".1 kit leoni n. 1",
        ".1 dicionário",
        ".1 pincel n.14"
    ]

    try:
        # Tenta carregar fonte padrão do sistema se disponível
        font = ImageFont.truetype("arial.ttf", 32)
        title_font = ImageFont.truetype("arialbd.ttf", 40)
    except IOError:
        font = ImageFont.load_default()
        title_font = font

    y = 60
    # Título
    draw.text((100, y), lines[0], fill=(0, 0, 0), font=title_font)
    draw.line([(100, y + 50), (600, y + 50)], fill=(200, 0, 0), width=3)
    y += 90

    # Itens
    for line in lines[1:]:
        draw.text((120, y), line, fill=(0, 0, 0), font=font)
        y += 55

    img.save(image_path, "JPEG")
    print(f"Imagem criada com sucesso em: {image_path}")

if __name__ == "__main__":
    generate_sample_jpeg()