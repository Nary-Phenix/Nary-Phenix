"""NARY OS — icon generator (SVG). Used by build.py.

Pour changer une icône : modifier sa couleur dans ICONS ou son dessin dans glyph(),
puis lancer `python3 build.py` depuis ce dossier.
"""
import math


def darken(hexc, k):
    h = hexc.lstrip('#')
    r, g, b = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    return '#%02X%02X%02X' % (int(r * k), int(g * k), int(b * k))


def _gear():
    pts = []
    for i in range(8):
        a = i * 45
        for rr, da in [(112, -17), (142, -9), (142, 9), (112, 17)]:
            ang = math.radians(a + da)
            pts.append((256 + rr * math.cos(ang), 256 + rr * math.sin(ang)))
    poly = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z"
    hole = "M204 256 a52 52 0 1 0 104 0 a52 52 0 1 0 -104 0Z"
    return poly + " " + hole


GEAR = _gear()


def _sun_rays():
    out = []
    for i in range(8):
        a = math.radians(i * 45)
        x1, y1 = 256 + 112 * math.cos(a), 256 + 112 * math.sin(a)
        x2, y2 = 256 + 160 * math.cos(a), 256 + 160 * math.sin(a)
        out.append(f"M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}")
    return " ".join(out)


SUN_RAYS = _sun_rays()


def _wifi():
    arcs = []
    for r in (80, 150, 220):
        k = 0.7071 * r
        arcs.append(f"M{256 - k:.1f} {370 - k:.1f} A{r} {r} 0 0 1 {256 + k:.1f} {370 - k:.1f}")
    return " ".join(arcs)


WIFI = _wifi()

# nom -> (couleur de glow, couleur de reflet, échelle du pictogramme)
ICONS = {
    # applications (512x512)
    'about':      ('#19E6FF', '#2D8CFF', 1.0),
    'devstudio':  ('#2D5BFF', '#6F8CFF', 1.0),
    'projects':   ('#FF2BD6', '#FF7AE8', 1.0),
    'terminal':   ('#2BFFA0', '#19E6FF', 1.0),
    'education':  ('#8B2BE2', '#B87CFF', 1.0),
    'contact':    ('#FF5FB8', '#9B4DFF', 1.0),
    'settings':   ('#C7CCE0', '#5B7CFF', 1.0),
    # système
    'folder':     ('#E0147F', '#FF5FB8', 1.15),
    'file':       ('#5B7CFF', '#8FB4FF', 1.15),
    'github':     ('#B87CFF', '#19E6FF', 1.15),
    'home':       ('#19E6FF', '#8B2BE2', 1.15),
    # barre système (affichées à ~20 px : pictogramme agrandi)
    'wifi':       ('#19E6FF', '#2D8CFF', 1.12),
    'bluetooth':  ('#2D5BFF', '#6F8CFF', 1.12),
    'battery':    ('#2BFFA0', '#19E6FF', 1.12),
    'volume':     ('#B87CFF', '#FF7AE8', 1.12),
    'brightness': ('#FF5FB8', '#FFB3E6', 1.12),
}

# Pictogramme utilisé par chaque icône du dock (nom -> glyphe)
DOCK = {'home': 'home', 'projects': 'projects', 'terminal': 'terminal', 'contact': 'contact'}


def glyph(name, f, d):
    """f = couleur principale, d = couleur des détails."""
    sj = 'stroke-linejoin="round" stroke-linecap="round"'
    if name == 'about':
        return (f'<circle cx="256" cy="186" r="64" fill="{f}" stroke="{f}" stroke-width="10"/>'
                f'<path d="M122 398 C122 298 190 272 256 272 C322 272 390 298 390 398 Z" fill="{f}" stroke="{f}" stroke-width="12" {sj}/>')
    if name == 'devstudio':
        return (f'<g fill="none" stroke="{f}" stroke-width="36" {sj}>'
                '<path d="M186 168 L100 256 L186 344"/><path d="M326 168 L412 256 L326 344"/><path d="M286 146 L226 366"/></g>')
    if name in ('projects', 'folder'):
        return (f'<path d="M108 176 Q108 144 140 144 L210 144 Q224 144 234 156 L254 180 L372 180 Q404 180 404 212 L404 232 L108 232 Z" fill="{f}" opacity="0.65"/>'
                f'<path d="M108 216 Q108 194 132 194 L380 194 Q404 194 404 218 L404 356 Q404 390 370 390 L142 390 Q108 390 108 356 Z" fill="{f}"/>'
                f'<path d="M132 222 H380" stroke="{d}" stroke-width="7" stroke-linecap="round" opacity="0.55"/>')
    if name == 'terminal':
        return (f'<g fill="none" stroke="{f}" stroke-width="38" {sj}>'
                '<path d="M124 172 L252 256 L124 340"/><path d="M290 352 H404"/></g>')
    if name == 'education':
        return (f'<path d="M256 138 L428 214 L256 290 L84 214 Z" fill="{f}" stroke="{f}" stroke-width="12" {sj}/>'
                f'<path d="M150 266 L256 314 L362 266 V332 C362 362 312 386 256 386 C200 386 150 362 150 332 Z" fill="{f}" stroke="{f}" stroke-width="8" {sj}/>'
                f'<path d="M428 214 V322" stroke="{f}" stroke-width="12" {sj}/><circle cx="428" cy="336" r="14" fill="{f}"/>')
    if name == 'contact':
        return (f'<rect x="92" y="150" width="328" height="212" rx="36" fill="{f}"/>'
                f'<path d="M112 184 L256 282 L400 184" fill="none" stroke="{d}" stroke-width="22" {sj}/>')
    if name == 'settings':
        return f'<path d="{GEAR}" fill="{f}" fill-rule="evenodd" stroke="{f}" stroke-width="8" stroke-linejoin="round"/>'
    if name == 'home':
        return (f'<path d="M256 112 L426 262 H386 V390 H306 V292 H206 V390 H126 V262 H86 Z" fill="{f}" stroke="{f}" stroke-width="12" {sj}/>')
    if name == 'file':
        return (f'<path d="M152 104 H292 L372 184 V392 Q372 410 354 410 H152 Q134 410 134 392 V122 Q134 104 152 104 Z" fill="{f}" stroke="{f}" stroke-width="8" {sj}/>'
                f'<path d="M292 108 V166 Q292 184 310 184 H368" fill="none" stroke="{d}" stroke-width="12" {sj}/>'
                f'<path d="M180 262 H326 M180 318 H326 M180 362 H270" fill="none" stroke="{d}" stroke-width="18" {sj}/>')
    if name == 'github':
        return (f'<g fill="none" stroke="{f}" stroke-width="30" {sj}>'
                '<circle cx="180" cy="136" r="34"/><circle cx="180" cy="376" r="34"/><circle cx="340" cy="196" r="34"/>'
                '<path d="M180 170 V342"/><path d="M340 230 C340 300 180 270 180 342"/></g>')
    if name == 'wifi':
        return (f'<g fill="none" stroke="{f}" stroke-width="34" {sj}><path d="{WIFI}"/></g>'
                f'<circle cx="256" cy="374" r="28" fill="{f}"/>')
    if name == 'bluetooth':
        return (f'<path d="M172 178 L340 330 L256 410 L256 102 L340 182 L172 334" fill="none" stroke="{f}" stroke-width="32" {sj}/>')
    if name == 'battery':
        return (f'<rect x="84" y="168" width="296" height="176" rx="38" fill="none" stroke="{f}" stroke-width="28"/>'
                f'<rect x="394" y="222" width="30" height="68" rx="10" fill="{f}"/>'
                f'<rect x="124" y="208" width="190" height="96" rx="14" fill="{f}"/>')
    if name == 'volume':
        return (f'<path d="M104 208 H186 L286 128 V384 L186 304 H104 Z" fill="{f}" stroke="{f}" stroke-width="14" {sj}/>'
                f'<g fill="none" stroke="{f}" stroke-width="28" {sj}><path d="M330 204 Q366 256 330 308"/><path d="M372 160 Q440 256 372 352"/></g>')
    if name == 'brightness':
        return (f'<circle cx="256" cy="256" r="72" fill="{f}"/>'
                f'<path d="{SUN_RAYS}" fill="none" stroke="{f}" stroke-width="28" {sj}/>')
    raise KeyError(name)


def icon_svg(name, glyph_name=None, size=512):
    """Icône sur tuile sombre opaque. size = taille de rendu (le viewBox reste 512)."""
    c1, c2, sc = ICONS[name]
    gname = glyph_name or name
    detail_main = '#0B0618'
    t = f'translate(256 256) scale({sc}) translate(-256 -256)'
    ext = ""
    for off, k in [(14, 0.22), (10, 0.30), (6, 0.38), (3, 0.46)]:
        ext += f'<g transform="translate(0 {off * (1 if sc <= 1 else 0.8):.1f})">{glyph(gname, darken(c1, k), darken(c1, k))}</g>'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="{size}" height="{size}">
<defs>
<linearGradient id="tile" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#150A29"/><stop offset="1" stop-color="#06030D"/></linearGradient>
<radialGradient id="cy" cx="0" cy="0" r="0.75"><stop offset="0" stop-color="#19E6FF" stop-opacity="0.30"/><stop offset="1" stop-color="#19E6FF" stop-opacity="0"/></radialGradient>
<radialGradient id="mg" cx="1" cy="1" r="0.75"><stop offset="0" stop-color="#FF2BD6" stop-opacity="0.34"/><stop offset="1" stop-color="#FF2BD6" stop-opacity="0"/></radialGradient>
<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.10"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>
<linearGradient id="rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient>
<linearGradient id="gl" gradientUnits="userSpaceOnUse" x1="0" y1="130" x2="0" y2="400"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient>
<clipPath id="clip"><rect x="8" y="8" width="496" height="496" rx="116"/></clipPath>
<filter id="b18" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="16"/></filter>
<filter id="b8" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>
</defs>
<rect x="8" y="8" width="496" height="496" rx="116" fill="url(#tile)"/>
<g clip-path="url(#clip)">
  <rect width="512" height="512" fill="url(#cy)"/>
  <rect width="512" height="512" fill="url(#mg)"/>
  <rect x="8" y="8" width="496" height="230" fill="url(#gloss)"/>
  <rect x="14" y="14" width="484" height="484" rx="110" fill="none" stroke="{c1}" stroke-width="26" opacity="0.55" filter="url(#b8)"/>
  <ellipse cx="256" cy="470" rx="150" ry="22" fill="#000" opacity="0.55" filter="url(#b8)"/>
  <g transform="{t}">
    <g filter="url(#b18)" opacity="0.95">{glyph(gname, c1, c1)}</g>
    {ext}
    <g fill="url(#gl)" stroke="none">{glyph(gname, "url(#gl)", detail_main)}</g>
  </g>
</g>
<rect x="11" y="11" width="490" height="490" rx="113" fill="none" stroke="url(#rim)" stroke-width="5"/>
<rect x="17" y="17" width="478" height="478" rx="107" fill="none" stroke="#FFFFFF" stroke-opacity="0.10" stroke-width="2"/>
</svg>"""
