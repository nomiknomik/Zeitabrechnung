"""App-Icon: Uhr mit Muenze auf Terrakotta-Verlauf (Pillow). Erzeugt app/icon-192.png und app/icon-512.png."""
from PIL import Image, ImageDraw
S = 1024
def icon():
    img = Image.new('RGB', (S, S))
    top, bot = (214, 128, 86), (158, 71, 38)
    for y in range(S):
        t = y / S
        ImageDraw.Draw(img).line([(0, y), (S, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    d = ImageDraw.Draw(img)
    cream, w = (251, 245, 236), 46
    cx, cy, r = 450, 470, 270                      # Uhr
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=cream, width=w)
    d.line([(cx, cy), (cx, cy - 165)], fill=cream, width=w)
    d.line([(cx, cy), (cx + 120, cy + 70)], fill=cream, width=w)
    for p in [(cx, cy - 165), (cx + 120, cy + 70), (cx, cy)]:
        d.ellipse([p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2], fill=cream)
    mx, my, mr = 700, 710, 170                     # Muenze
    d.ellipse([mx - mr - 26, my - mr - 26, mx + mr + 26, my + mr + 26], fill=(176, 84, 48))
    d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=(226, 178, 92))
    d.ellipse([mx - mr + 30, my - mr + 30, mx + mr - 30, my + mr - 30], outline=(250, 226, 170), width=14)
    br = (158, 104, 40)                            # Euro-Zeichen
    d.arc([mx - 75, my - 85, mx + 95, my + 85], 45, 315, fill=br, width=24)
    d.line([(mx - 105, my - 22), (mx + 30, my - 22)], fill=br, width=20)
    d.line([(mx - 105, my + 22), (mx + 30, my + 22)], fill=br, width=20)
    return img
im = icon()
for n in (512, 192):
    im.resize((n, n), Image.LANCZOS).save(f'app/icon-{n}.png', optimize=True)
