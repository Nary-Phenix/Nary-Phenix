"""NARY OS — lockscreen, banners et séquence de boot (SVG). Used by build.py.

Le slogan officiel est défini UNE seule fois ici (SLOGAN) et ne doit jamais être modifié.
"""
import phoenix as ph

SLOGAN = "Samy nosorandreniny Token ka aza mifampidera produit"
VERSION = "VERSION 1.0"
TITLE_FONT = "Montserrat"
BODY_FONT = "Inter"
MONO_FONT = "DejaVu Sans Mono"


def _bg_layers(op):
    """Fond du lockscreen (ciel, halo, étoiles, ligne d'horizon)."""
    return f"""<g opacity="{op:.3f}">
<rect width="1920" height="1080" fill="url(#lsky)"/>
<ellipse cx="960" cy="470" rx="900" ry="520" fill="url(#lglow)"/>
<g>{ph.particles(150, 1920, 1080, 31)}</g>
<rect x="260" y="1038" width="1400" height="4" fill="url(#lhz)" filter="url(#lb30)" opacity="0.9"/>
<rect x="260" y="1040" width="1400" height="2" fill="url(#lhz)"/>
</g>"""


def lock_svg(w=1920, h=1080, bg=1.0, phoenix=1.0, pscale=1.0, title=1.0, slogan=1.0, version=1.0):
    d, b = ph.phoenix_defs_and_body()
    s = 0.72 * pscale
    cx, cy = 960, 400
    tx, ty = cx - 512 * s, cy - 512 * s
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1920 1080" width="{w}" height="{h}">
<defs>
<linearGradient id="lsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05030A"/><stop offset="0.7" stop-color="#120824"/><stop offset="1" stop-color="#220C3A"/></linearGradient>
<radialGradient id="lglow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#8B2BE2" stop-opacity="0.45"/><stop offset="0.5" stop-color="#2D5BFF" stop-opacity="0.15"/><stop offset="1" stop-color="#05030A" stop-opacity="0"/></radialGradient>
<linearGradient id="lhz" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF2BD6" stop-opacity="0"/><stop offset="0.5" stop-color="#FF2BD6" stop-opacity="1"/><stop offset="1" stop-color="#FF2BD6" stop-opacity="0"/></linearGradient>
<linearGradient id="lline" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#19E6FF" stop-opacity="0"/><stop offset="0.5" stop-color="#19E6FF" stop-opacity="0.9"/><stop offset="1" stop-color="#FF2BD6" stop-opacity="0"/></linearGradient>
<filter id="lb30"><feGaussianBlur stdDeviation="30"/></filter>
<filter id="tglow" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="sglow" x="-10%" y="-100%" width="120%" height="300%"><feGaussianBlur stdDeviation="6"/></filter>
{d}
</defs>
<rect width="1920" height="1080" fill="#000000"/>
{_bg_layers(bg)}
<g opacity="{phoenix:.3f}"><g transform="translate({tx:.1f} {ty:.1f}) scale({s:.4f})">{b}</g></g>
<g opacity="{title:.3f}">
  <text x="960" y="870" text-anchor="middle" font-family="{TITLE_FONT}" font-weight="800" font-size="92" letter-spacing="26" fill="#FF2BD6" filter="url(#tglow)" opacity="0.8">NARY OS</text>
  <text x="960" y="870" text-anchor="middle" font-family="{TITLE_FONT}" font-weight="800" font-size="92" letter-spacing="26" fill="#EDEAF7">NARY OS</text>
</g>
<g opacity="{slogan:.3f}">
  <rect x="420" y="913" width="1080" height="2" fill="url(#lline)"/>
  <text x="960" y="962" text-anchor="middle" font-family="{BODY_FONT}" font-style="italic" font-weight="500" font-size="34" letter-spacing="1.5" fill="#19E6FF" filter="url(#sglow)" opacity="0.7">{SLOGAN}</text>
  <text x="960" y="962" text-anchor="middle" font-family="{BODY_FONT}" font-style="italic" font-weight="500" font-size="34" letter-spacing="1.5" fill="#E6FBFF">{SLOGAN}</text>
</g>
<g opacity="{version:.3f}">
  <text x="960" y="1020" text-anchor="middle" font-family="{BODY_FONT}" font-weight="600" font-size="22" letter-spacing="8" fill="#8A829F">{VERSION}</text>
</g>
</svg>"""


def banner_svg(title, path, c1, c2):
    d, b = ph.phoenix_defs_and_body()
    s = 0.46
    tx, ty = 1290 - 512 * s, 200 - 512 * s
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1600 400" width="1600" height="400">
<defs>
<linearGradient id="bbg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#07040F"/><stop offset="1" stop-color="#1A0B2E"/></linearGradient>
<radialGradient id="bglow" cx="0.8" cy="0.5" r="0.45"><stop offset="0" stop-color="{c1}" stop-opacity="0.38"/><stop offset="1" stop-color="{c1}" stop-opacity="0"/></radialGradient>
<linearGradient id="bbar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient>
<linearGradient id="brim" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="#FF2BD6"/></linearGradient>
<clipPath id="bclip"><rect x="4" y="4" width="1592" height="392" rx="36"/></clipPath>
<filter id="bb" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10"/></filter>
{d}
</defs>
<rect x="4" y="4" width="1592" height="392" rx="36" fill="url(#bbg)"/>
<g clip-path="url(#bclip)">
  <rect width="1600" height="400" fill="url(#bglow)"/>
  <g opacity="0.9"><g transform="translate({tx:.1f} {ty:.1f}) scale({s})">{b}</g></g>
  <rect x="90" y="108" width="10" height="184" rx="5" fill="{c1}" filter="url(#bb)"/>
  <rect x="90" y="108" width="10" height="184" rx="5" fill="url(#bbar)"/>
  <text x="136" y="218" font-family="{TITLE_FONT}" font-weight="800" font-size="92" fill="#EDEAF7">{title}</text>
  <text x="140" y="276" font-family="{MONO_FONT}" font-size="30" fill="{c2}">{path}</text>
</g>
<rect x="6" y="6" width="1588" height="388" rx="34" fill="none" stroke="url(#brim)" stroke-width="4" opacity="0.8"/>
</svg>"""


def _ease(t, a, b):
    if t <= a:
        return 0.0
    if t >= b:
        return 1.0
    x = (t - a) / (b - a)
    return x * x * (3 - 2 * x)


FPS = 10
DURATION = 7.0


def boot_params(i):
    """Paramètres de la frame i : black -> phoenix -> NARY OS -> slogan -> version -> lockscreen."""
    t = i / FPS
    p = _ease(t, 0.7, 2.0)
    return dict(
        bg=round(_ease(t, 5.0, 6.2), 3),
        phoenix=round(p, 3),
        pscale=round(0.9 + 0.1 * p, 3),
        title=round(_ease(t, 2.1, 2.9), 3),
        slogan=round(_ease(t, 3.1, 4.2), 3),
        version=round(_ease(t, 4.4, 5.0), 3),
    )
