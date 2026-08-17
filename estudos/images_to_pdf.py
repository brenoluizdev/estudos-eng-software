"""
Junta uma sequencia de imagens (prints de tela) em um unico PDF, uma imagem
por pagina, em tamanho maximizado (pagina do PDF = tamanho da imagem).

Uso: python images_to_pdf.py saida.pdf img1.jpg img2.jpg img3.jpg ...
"""
import sys
from pathlib import Path

from PIL import Image


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    out_path = Path(sys.argv[1]).resolve()
    img_paths = [Path(p) for p in sys.argv[2:]]

    images = []
    for p in img_paths:
        if not p.exists():
            print(f"Aviso: imagem nao encontrada, pulando: {p}")
            continue
        img = Image.open(p).convert("RGB")
        images.append(img)

    if not images:
        print("Nenhuma imagem valida encontrada.")
        sys.exit(1)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    images[0].save(out_path, save_all=True, append_images=images[1:])
    print(f"OK: {out_path} ({len(images)} paginas)")


if __name__ == "__main__":
    main()
