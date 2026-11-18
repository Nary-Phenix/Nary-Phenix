#!/usr/bin/env python3
"""NARY OS — régénère TOUS les assets de image/ à partir des sources.

Usage :  cd image/src && python3 build.py            (tout)
         python3 build.py ic_about wallpaper boot     (seulement certains assets)

Prérequis : rsvg-convert (librsvg), ImageMagick (convert), Pillow.
Les fichiers .svg de ce dossier sont réécrits à chaque build : pour un changement de
style, modifier icons.py / phoenix.py / assets.py (ou éditer un .svg puis le rendre
à la main avec rsvg-convert).
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image

import assets
import icons
import phoenix

SRC = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.dirname(SRC)
os.chdir(SRC)

KB = 1024


def write(path, text):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def render(svg, png, w, h):
    subprocess.run(["rsvg-convert", "-w", str(w), "-h", str(h), svg, "-o", png], check=True)


def shrink(png, max_kb):
    """Recompresse sans perte (PNG truecolor). Pas de palette réduite : elle abîme les dégradés/glows."""
    im = Image.open(png).convert("RGBA")
    im.save(png, optimize=True)


# nom -> (générateur svg, largeur, hauteur, budget en Ko)
def registry():
    reg = {}
    reg["phoenix_logo"] = (phoenix.logo_svg, 1024, 1024, 700)
    reg["wallpaper"] = (phoenix.wallpaper_svg, 1920, 1080, 1500)
    reg["lockscreen"] = (lambda: assets.lock_svg(), 1920, 1080, 1500)
    for n in ("about", "devstudio", "projects", "terminal", "education", "contact", "settings"):
        reg[f"ic_{n}"] = ((lambda n=n: icons.icon_svg(n)), 512, 512, 160)
    for n in ("folder", "file", "github", "home"):
        reg[f"ic_{n}"] = ((lambda n=n: icons.icon_svg(n)), 256, 256, 60)
    for n in ("wifi", "bluetooth", "battery", "volume", "brightness"):
        reg[f"ic_{n}"] = ((lambda n=n: icons.icon_svg(n)), 128, 128, 20)
    for n, g in icons.DOCK.items():
        # le dock reprend les couleurs de l'application (ou de l'icône système) correspondante
        key = n if n in icons.ICONS else g
        reg[f"dock/dock_{n}"] = ((lambda key=key, g=g: icons.icon_svg(key, g)), 256, 256, 60)
    banners = {
        "about": ("About Me", "~/nary-os/apps/about", "#19E6FF", "#2D8CFF"),
        "projects": ("Projects", "~/nary-os/apps/projects", "#FF2BD6", "#FF7AE8"),
        "devstudio": ("Dev Studio", "~/nary-os/apps/dev-studio", "#2D5BFF", "#6F8CFF"),
    }
    for n, (t, p, c1, c2) in banners.items():
        reg[f"banners/banner_{n}"] = ((lambda t=t, p=p, c1=c1, c2=c2: assets.banner_svg(t, p, c1, c2)), 1600, 400, 400)
    return reg


def build_boot():
    frames = []  # (params, délai en centièmes de seconde)
    n = int(assets.DURATION * assets.FPS)
    for i in range(n + 1):
        p = assets.boot_params(i)
        if frames and frames[-1][0] == p:
            frames[-1][1] += 100 // assets.FPS
        else:
            frames.append([p, 100 // assets.FPS])
    frames[-1][1] += 400  # image finale (lockscreen) maintenue 4 s
    tmp = tempfile.mkdtemp(prefix="nary_boot_")
    cmd = ["convert", "-loop", "1"]
    for k, (p, delay) in enumerate(frames):
        svg = os.path.join(tmp, f"f{k:03d}.svg")
        png = os.path.join(tmp, f"f{k:03d}.png")
        write(svg, assets.lock_svg(960, 540, **p))
        render(svg, png, 960, 540)
        cmd += ["-delay", str(delay), png]
    out = os.path.join(IMG, "boot.gif")
    cmd += ["-layers", "OptimizeFrame", "-colors", "128", out]
    subprocess.run(cmd, check=True)
    # source de l'image finale du boot (= lockscreen)
    return out


def main(argv):
    reg = registry()
    wanted = argv or list(reg) + ["boot"]
    for name in wanted:
        if name == "boot":
            out = build_boot()
            print(f"{os.path.relpath(out, IMG):34s} {os.path.getsize(out)/KB:8.0f} Ko")
            continue
        gen, w, h, budget = reg[name]
        base = os.path.basename(name)
        svg = os.path.join(SRC, base + ".svg")
        png = os.path.join(IMG, name + ".png")
        os.makedirs(os.path.dirname(png), exist_ok=True)
        write(svg, gen())
        render(svg, png, w, h)
        shrink(png, budget)
        size = os.path.getsize(png) / KB
        flag = "" if size <= budget else f"  (> budget {budget} Ko)"
        print(f"{name + '.png':34s} {size:8.0f} Ko{flag}")


if __name__ == "__main__":
    main(sys.argv[1:])
