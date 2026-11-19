"""NARY OS — scène de bureau unique, découpée en tranches cliquables.

Principe : GitHub interdit tout positionnement CSS. On dessine donc UN bureau complet
(barre de menu, Phoenix, titre, icônes, dock) dans une image 1600x1000, puis on la découpe en
tranches rectangulaires collées les unes aux autres (images en ligne, sans espace, largeurs
en %). Les tranches qui portent une icône sont liées à leur application.

Pour changer la disposition : modifier APPS_LEFT / APPS_RIGHT / DOCK ou les constantes
ci-dessous, puis `python3 build.py desktop`.
"""
import base64
import os

import assets
import phoenix as ph

W, H = 1600, 1000
BAR_H = 48
ROW_H = 205
COL_L = 280            # largeur de la colonne d'icônes gauche
COL_R = 280            # largeur de la colonne d'icônes droite
ICON = 150             # taille des icônes de bureau
DOCK_Y = BAR_H + 4 * ROW_H        # 868
DOCK_TILE = 160
DOCK_X0 = 480

# (clé de l'icône, libellé, lien relatif depuis README.md)
APPS_LEFT = [
    ("about", "About Me", "apps/about.md"),
    ("devstudio", "Dev Studio", "apps/dev-studio.md"),
    ("projects", "Projects", "apps/projects.md"),
    ("terminal", "Terminal", "apps/terminal.md"),
]
APPS_RIGHT = [
    ("education", "Education", "apps/education.md"),
    ("contact", "Contact", "apps/contact.md"),
    ("settings", "Settings", "apps/settings.md"),
]
DOCK = [
    ("home", "Home", "desktop.md"),
    ("projects", "Projects", "apps/projects.md"),
    ("terminal", "Terminal", "apps/terminal.md"),
    ("contact", "Contact", "apps/contact.md"),
]


_CACHE = {}


def _data_uri(rel):
    """Intègre le PNG dans le SVG (librsvg refuse les chemins parents)."""
    if rel not in _CACHE:
        with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), rel), "rb") as fh:
            _CACHE[rel] = "data:image/png;base64," + base64.b64encode(fh.read()).decode()
    return _CACHE[rel]


def _icon(key, x, y, size, folder=""):
    return f'<image xlink:href="{_data_uri(folder + "ic_" + key + ".png")}" x="{x}" y="{y}" width="{size}" height="{size}"/>'


def _desktop_icon(key, label, cx, rowtop):
    x, y = cx - ICON // 2, rowtop + 12
    return (
        f'<ellipse cx="{cx}" cy="{y + ICON + 2}" rx="{ICON * 0.38:.0f}" ry="12" fill="#000" opacity="0.55" filter="url(#sh)"/>'
        f'{_icon(key, x, y, ICON)}'
        f'<text x="{cx}" y="{rowtop + 196}" text-anchor="middle" font-family="Inter" font-weight="600" font-size="30" '
        f'fill="#000" opacity="0.75" filter="url(#sh2)">{label}</text>'
        f'<text x="{cx}" y="{rowtop + 196}" text-anchor="middle" font-family="Inter" font-weight="600" font-size="30" fill="#F4F0FF">{label}</text>'
    )


def desktop_svg():
    d, b = ph.phoenix_defs_and_body()
    s = 0.62
    tx, ty = 800 - 512 * s, 50
    hz = 868
    grid = []
    for i in range(-30, 31):
        grid.append(f'<line x1="{800 + i * 30}" y1="{hz}" x2="{800 + i * 190}" y2="{H}"/>')
    yy, step = hz, 5
    while yy < H:
        grid.append(f'<line x1="0" y1="{yy:.0f}" x2="{W}" y2="{yy:.0f}"/>')
        step *= 1.35
        yy += step
    import random
    random.seed(5)
    city, x = [], 0
    while x < W:
        bw, bh = random.randint(30, 90), random.randint(20, 100)
        city.append(f'<rect x="{x}" y="{hz - bh}" width="{bw}" height="{bh}"/>')
        x += bw + random.randint(0, 10)

    out = [f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05030A"/><stop offset="0.7" stop-color="#150A28"/><stop offset="1" stop-color="#2A0F45"/></linearGradient>
<radialGradient id="bigglow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#8B2BE2" stop-opacity="0.5"/><stop offset="0.45" stop-color="#2D5BFF" stop-opacity="0.18"/><stop offset="1" stop-color="#05030A" stop-opacity="0"/></radialGradient>
<linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF2BD6" stop-opacity="0.9"/><stop offset="1" stop-color="#8B2BE2" stop-opacity="0.15"/></linearGradient>
<linearGradient id="horizon" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF2BD6" stop-opacity="0"/><stop offset="0.5" stop-color="#FF2BD6" stop-opacity="1"/><stop offset="1" stop-color="#FF2BD6" stop-opacity="0"/></linearGradient>
<linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#120A1F" stop-opacity="0.96"/><stop offset="1" stop-color="#0A0514" stop-opacity="0.92"/></linearGradient>
<linearGradient id="dockg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A1B45" stop-opacity="0.78"/><stop offset="1" stop-color="#0E0719" stop-opacity="0.9"/></linearGradient>
<linearGradient id="dockrim" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#19E6FF"/><stop offset="0.5" stop-color="#8B2BE2"/><stop offset="1" stop-color="#FF2BD6"/></linearGradient>
<linearGradient id="lline" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#19E6FF" stop-opacity="0"/><stop offset="0.5" stop-color="#19E6FF" stop-opacity="0.9"/><stop offset="1" stop-color="#FF2BD6" stop-opacity="0"/></linearGradient>
<filter id="blur30"><feGaussianBlur stdDeviation="26"/></filter>
<filter id="sh" x="-30%" y="-100%" width="160%" height="300%"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="sh2" x="-10%" y="-30%" width="120%" height="160%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="tglow" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="12"/></filter>
<filter id="sglow" x="-10%" y="-100%" width="120%" height="300%"><feGaussianBlur stdDeviation="5"/></filter>
{d}
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<ellipse cx="800" cy="380" rx="780" ry="470" fill="url(#bigglow)"/>
<g>{ph.particles(120, W, hz, 41)}</g>
<g fill="#0A0514" opacity="0.95">{"".join(city)}</g>
<rect x="0" y="{hz}" width="{W}" height="{H - hz}" fill="#0A0514"/>
<g stroke="url(#floor)" stroke-width="1.5" opacity="0.5">{"".join(grid)}</g>
<rect x="200" y="{hz - 3}" width="1200" height="6" fill="url(#horizon)" filter="url(#blur30)"/>
<rect x="200" y="{hz - 1}" width="1200" height="2" fill="url(#horizon)"/>
<g transform="translate({tx:.1f} {ty}) scale({s})">{b}</g>
<g>{ph.particles(50, W, H, 51)}</g>
"""]
    # identité : titre + slogan (texte exact)
    out.append(f"""<text x="800" y="745" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="70" letter-spacing="20" fill="#FF2BD6" filter="url(#tglow)" opacity="0.8">NARY OS</text>
<text x="800" y="745" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="70" letter-spacing="20" fill="#EDEAF7">NARY OS</text>
<rect x="330" y="768" width="940" height="2" fill="url(#lline)"/>
<text x="800" y="814" text-anchor="middle" font-family="Inter" font-style="italic" font-weight="500" font-size="30" letter-spacing="1" fill="#19E6FF" filter="url(#sglow)" opacity="0.7">{assets.SLOGAN}</text>
<text x="800" y="814" text-anchor="middle" font-family="Inter" font-style="italic" font-weight="500" font-size="30" letter-spacing="1" fill="#E6FBFF">{assets.SLOGAN}</text>
""")
    # icônes de bureau
    for i, (k, lab, _) in enumerate(APPS_LEFT):
        out.append(_desktop_icon(k, lab, COL_L // 2, BAR_H + i * ROW_H))
    for i, (k, lab, _) in enumerate(APPS_RIGHT):
        out.append(_desktop_icon(k, lab, W - COL_R // 2, BAR_H + i * ROW_H))
    # dock
    px0, px1 = DOCK_X0 - 20, DOCK_X0 + DOCK_TILE * len(DOCK) + 20
    out.append(f'<rect x="{px0}" y="{DOCK_Y + 10}" width="{px1 - px0}" height="112" rx="44" fill="url(#dockg)"/>'
               f'<rect x="{px0 + 1}" y="{DOCK_Y + 11}" width="{px1 - px0 - 2}" height="110" rx="43" fill="none" stroke="url(#dockrim)" stroke-width="2.5" opacity="0.85"/>')
    for i, (k, lab, _) in enumerate(DOCK):
        cx = DOCK_X0 + DOCK_TILE * i + DOCK_TILE // 2
        out.append(f'<image xlink:href="{_data_uri("dock/dock_" + k + ".png")}" x="{cx - 48}" y="{DOCK_Y + 18}" width="96" height="96"/>')
    # barre de menu (par-dessus)
    out.append(f'<rect width="{W}" height="{BAR_H}" fill="url(#bar)"/>'
               f'<rect y="{BAR_H - 2}" width="{W}" height="2" fill="url(#dockrim)" opacity="0.6"/>'
               f'<text x="28" y="32" font-family="Montserrat" font-weight="800" font-size="22" letter-spacing="3" fill="#FF2BD6">NARY OS</text>')
    mx = 190
    for item in ("File", "Edit", "View", "Go", "Window", "Help"):
        out.append(f'<text x="{mx}" y="31" font-family="Inter" font-weight="500" font-size="21" fill="#C9C2DD">{item}</text>')
        mx += 24 + 13 * len(item)
    sx = W - 40
    out.append(f'<text x="{sx}" y="31" text-anchor="end" font-family="Inter" font-weight="600" font-size="20" letter-spacing="2" fill="#8A829F">v1.0</text>')
    ix = sx - 90
    for k in ("battery", "volume", "bluetooth", "wifi", "brightness"):
        out.append(_icon(k, ix - 32, 8, 32))
        ix -= 48
    out.append("</svg>")
    return "".join(out)


def slices():
    """Découpage : liste de lignes ; chaque ligne = liste de tranches (nom, x0, x1, y0, y1, lien, alt)."""
    rows = [[("desk_bar", 0, W, 0, BAR_H, None, "Barre de menu NARY OS")]]
    for i in range(4):
        y0, y1 = BAR_H + i * ROW_H, BAR_H + (i + 1) * ROW_H
        k, lab, link = APPS_LEFT[i]
        row = [(f"desk_{k}", 0, COL_L, y0, y1, link, lab)]
        if i < len(APPS_RIGHT):
            k2, lab2, link2 = APPS_RIGHT[i]
            row.append((f"desk_r{i + 1}_mid", COL_L, W - COL_R, y0, y1, None, ""))
            row.append((f"desk_{k2}", W - COL_R, W, y0, y1, link2, lab2))
        else:
            row.append((f"desk_r{i + 1}_mid", COL_L, W, y0, y1, None, ""))
        rows.append(row)
    dock = [("desk_dock_left", 0, DOCK_X0, DOCK_Y, H, None, "")]
    for i, (k, lab, link) in enumerate(DOCK):
        x0 = DOCK_X0 + i * DOCK_TILE
        dock.append((f"desk_dock_{k}", x0, x0 + DOCK_TILE, DOCK_Y, H, link, lab))
    dock.append(("desk_dock_right", DOCK_X0 + DOCK_TILE * len(DOCK), W, DOCK_Y, H, None, ""))
    rows.append(dock)
    return rows


def pct(v):
    return f"{v:g}"


def html_block(rows, folder="image/desktop/"):
    """Bloc HTML : chaque ligne = images collées (aucune espace entre les balises)."""
    lines = []
    for row in rows:
        parts, used = [], 0.0
        for n, (name, x0, x1, y0, y1, link, alt) in enumerate(row):
            w = round((x1 - x0) / W * 100, 4)
            if n == len(row) - 1:
                w = round(100 - used, 4)
            used += w
            img = f'<img src="{folder}{name}.png" width="{pct(w)}%" alt="{alt}">'
            parts.append(f'<a href="{link}">{img}</a>' if link else img)
        lines.append("".join(parts))
    return "<p align=\"center\">\n" + "<br>\n".join(lines) + "\n</p>"
