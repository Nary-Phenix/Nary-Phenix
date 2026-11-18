"""NARY OS — Phoenix generator (SVG). Used by build.py."""
import math, random

def pt(r, deg, L):
    a = math.radians(deg)
    return (r[0] + L*math.cos(a), r[1] + L*math.sin(a))

def feather(r, t, wfrac=0.12, bend=0.10, sign=1):
    dx, dy = t[0]-r[0], t[1]-r[1]
    L = math.hypot(dx, dy)
    ux, uy = dx/L, dy/L
    nx, ny = -uy*sign, ux*sign
    mx, my = r[0]+dx*0.5 + nx*bend*L, r[1]+dy*0.5 + ny*bend*L
    w = wfrac*L*2
    c1 = (mx + nx*w, my + ny*w)
    c2 = (mx - nx*w, my - ny*w)
    tip = (t[0] + nx*bend*L*0.6, t[1] + ny*bend*L*0.6)
    d = f"M{r[0]:.1f} {r[1]:.1f} Q{c1[0]:.1f} {c1[1]:.1f} {tip[0]:.1f} {tip[1]:.1f} Q{c2[0]:.1f} {c2[1]:.1f} {r[0]:.1f} {r[1]:.1f}Z"
    rib = f"M{r[0]:.1f} {r[1]:.1f} Q{mx:.1f} {my:.1f} {tip[0]:.1f} {tip[1]:.1f}"
    return d, rib, tip

_gid = [0]
def grad(r, t, stops):
    _gid[0] += 1
    gid = f"fg{_gid[0]}"
    s = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o,c,op in stops)
    return gid, f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{r[0]:.1f}" y1="{r[1]:.1f}" x2="{t[0]:.1f}" y2="{t[1]:.1f}">{s}</linearGradient>'

def particles(n, w, h, seed, cx=None, spread=None):
    random.seed(seed)
    out = []
    cols = ["#19E6FF", "#FF2BD6", "#8B2BE2", "#7FF3FF", "#FFFFFF"]
    for _ in range(n):
        x, y = random.uniform(0, w), random.uniform(0, h)
        r = random.choice([1.2, 1.6, 2.2, 3.0, 4.0])
        c = random.choice(cols)
        op = random.uniform(0.25, 0.9)
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{c}" opacity="{op:.2f}"/>')
    return "".join(out)

def logo_svg():
    d, b = phoenix_defs_and_body()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>{d}</defs>
<g transform="translate(512 512) scale(0.9) translate(-512 -512)">{b}
<g>{particles(40,1024,1024,7)}</g></g>
</svg>"""

def wallpaper_svg():
    d, b = phoenix_defs_and_body()
    W, H = 1920, 1080
    hz = 760
    grid = []
    for i in range(-24, 25):
        x2 = 960 + i*210
        grid.append(f'<line x1="{960 + i*34}" y1="{hz}" x2="{x2}" y2="{H}"/>')
    yy = hz
    step = 6
    while yy < H:
        grid.append(f'<line x1="0" y1="{yy:.0f}" x2="{W}" y2="{yy:.0f}"/>')
        step *= 1.32
        yy += step
    city = []
    random.seed(3)
    x = 0
    while x < W:
        bw = random.randint(40, 110); bh = random.randint(30, 150)
        city.append(f'<rect x="{x}" y="{hz-bh}" width="{bw}" height="{bh}"/>')
        x += bw + random.randint(0, 12)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05030A"/><stop offset="0.65" stop-color="#150A28"/><stop offset="1" stop-color="#2A0F45"/></linearGradient>
<radialGradient id="bigglow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#8B2BE2" stop-opacity="0.5"/><stop offset="0.45" stop-color="#2D5BFF" stop-opacity="0.18"/><stop offset="1" stop-color="#05030A" stop-opacity="0"/></radialGradient>
<linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF2BD6" stop-opacity="0.9"/><stop offset="1" stop-color="#8B2BE2" stop-opacity="0.15"/></linearGradient>
<linearGradient id="horizon" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF2BD6" stop-opacity="0"/><stop offset="0.5" stop-color="#FF2BD6" stop-opacity="1"/><stop offset="1" stop-color="#FF2BD6" stop-opacity="0"/></linearGradient>
<filter id="blur30"><feGaussianBlur stdDeviation="30"/></filter>
{d}
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<ellipse cx="960" cy="470" rx="900" ry="520" fill="url(#bigglow)"/>
<g>{particles(160,W,hz,11)}</g>
<g fill="#0A0514" opacity="0.95">{"".join(city)}</g>
<rect x="0" y="{hz}" width="{W}" height="{H-hz}" fill="#0A0514"/>
<g stroke="url(#floor)" stroke-width="1.6" opacity="0.55">{"".join(grid)}</g>
<rect x="260" y="{hz-3}" width="1400" height="6" fill="url(#horizon)" filter="url(#blur30)" opacity="0.9"/>
<rect x="260" y="{hz-1}" width="1400" height="2" fill="url(#horizon)"/>
<g transform="translate(448 20) scale(1.0)">{b}</g>
<g>{particles(70,W,H,21)}</g>
</svg>"""

def wing_left():
    S = (480, 508)
    defs, body = [], []
    # flame tongues (behind)
    for a, L in zip(range(196, 262, 11), [520, 530, 520, 500, 470, 430]):
        t = pt(S, a, L)
        d, rib, tip = feather(S, t, 0.055, 0.20, -1)
        gid, gd = grad(S, tip, [(0,"#8B2BE2",0.0),(0.5,"#2D5BFF",0.55),(1,"#19E6FF",0.9)])
        defs.append(gd)
        body.append(f'<path d="{d}" fill="url(#{gid})"/>')
    layers = [
        (list(range(190, 270, 8)), [480,492,488,470,446,414,376,332,284,236], 0.085,
         [(0,"#8B2BE2",1),(0.5,"#2D5BFF",1),(1,"#19E6FF",0.95)], 0.35),
        (list(range(194, 268, 8)), [410,420,416,400,376,346,312,274,232], 0.08,
         [(0,"#FF2BD6",1),(0.35,"#8B2BE2",1),(1,"#19E6FF",1)], 0.55),
        (list(range(200, 262, 10)), [262,268,262,248,228,204,176], 0.07,
         [(0,"#FF2BD6",1),(0.6,"#B04BFF",1),(1,"#7FF3FF",1)], 0.6),
    ]
    for angs, lens, wf, stops, rop in layers:
        for a, L in zip(angs, lens):
            t = pt(S, a, L)
            bend = 0.07 + 0.11*max(0, (272-a))/80
            d, rib, tip = feather(S, t, wf, bend, 1)
            gid, gd = grad(S, tip, stops)
            defs.append(gd)
            body.append(f'<path d="{d}" fill="url(#{gid})" stroke="#CFF8FF" stroke-opacity="0.35" stroke-width="1.4"/>')
            body.append(f'<path d="{rib}" fill="none" stroke="#EFFFFF" stroke-opacity="{rop}" stroke-width="2" stroke-linecap="round"/>')
    return "".join(defs), "".join(body)

def tail():
    R = (512, 650)
    defs, body = [], []
    tips = [(512, 1000, 0.0), (452, 975, 0.1), (572, 975, -0.1), (394, 925, 0.2), (630, 925, -0.2), (338, 850, 0.3), (686, 850, -0.3)]
    for tx, ty, bend in tips[::-1]:
        sign = 1 if tx < 512 else -1
        d, rib, tip = feather(R, (tx, ty), 0.06, 0.04+abs(bend)*0.9, -sign)
        gid, gd = grad(R, tip, [(0,"#2D5BFF",1),(0.5,"#8B2BE2",1),(1,"#FF2BD6",0.95)])
        defs.append(gd)
        body.append(f'<path d="{d}" fill="url(#{gid})" stroke="#FFD6F7" stroke-opacity="0.3" stroke-width="1.4"/>')
        body.append(f'<path d="{rib}" fill="none" stroke="#FFFFFF" stroke-opacity="0.45" stroke-width="2" stroke-linecap="round"/>')
    return "".join(defs), "".join(body)

def crest():
    R = (512, 222)
    defs, body = [], []
    for a, L, wf, b in [(-90,200,0.05,0.10),(-68,170,0.05,0.16),(-112,170,0.05,0.16),(-46,125,0.05,0.2),(-134,125,0.05,0.2)]:
        t = pt(R, a, L)
        sign = 1 if a > -90 else -1
        if a == -90: sign = 1
        d, rib, tip = feather(R, t, wf, b, sign)
        gid, gd = grad(R, tip, [(0,"#19E6FF",1),(0.55,"#8B2BE2",1),(1,"#FF2BD6",1)])
        defs.append(gd)
        body.append(f'<path d="{d}" fill="url(#{gid})" stroke="#FFFFFF" stroke-opacity="0.35" stroke-width="1.3"/>')
    return "".join(defs), "".join(body)

def phoenix_defs_and_body():
    wd, wb = wing_left()
    td, tb = tail()
    cd, cb = crest()
    BODY = "M512 300 C546 300 560 340 568 392 C582 456 582 540 558 606 C546 646 528 678 512 712 C496 678 478 646 466 606 C442 540 442 456 456 392 C464 340 478 300 512 300Z"
    HEAD = "M512 206 C546 206 562 236 560 266 C558 296 538 320 512 324 C486 320 466 296 464 266 C462 236 478 206 512 206Z"
    defs = f"""
<radialGradient id="halo" cx="0.5" cy="0.45" r="0.5">
  <stop offset="0" stop-color="#8B2BE2" stop-opacity="0.55"/>
  <stop offset="0.5" stop-color="#2D5BFF" stop-opacity="0.18"/>
  <stop offset="1" stop-color="#05030A" stop-opacity="0"/>
</radialGradient>
<linearGradient id="bodyg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#7FF3FF"/><stop offset="0.35" stop-color="#19E6FF"/>
  <stop offset="0.7" stop-color="#2D5BFF"/><stop offset="1" stop-color="#8B2BE2"/>
</linearGradient>
<radialGradient id="core" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.95"/><stop offset="1" stop-color="#7FF3FF" stop-opacity="0"/></radialGradient>
<linearGradient id="beakg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#FF7AE8"/>
</linearGradient>
<filter id="glow" x="-25%" y="-25%" width="150%" height="150%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="glowS" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
{wd}{td}{cd}
<g id="wingL">{wb}</g>
<g id="tailG">{tb}</g>
"""
    body = f"""
<g id="phoenix">
  <ellipse cx="512" cy="470" rx="470" ry="420" fill="url(#halo)"/>
  <g filter="url(#glow)" opacity="0.85"><use xlink:href="#wingL"/><use xlink:href="#wingL" transform="translate(1024 0) scale(-1 1)"/><use xlink:href="#tailG"/></g>
  <use xlink:href="#tailG"/>
  <use xlink:href="#wingL"/>
  <use xlink:href="#wingL" transform="translate(1024 0) scale(-1 1)"/>
  {cb}
  <g filter="url(#glowS)" opacity="0.8"><path d="{BODY}" fill="#19E6FF"/></g>
  <path d="{BODY}" fill="url(#bodyg)" stroke="#E6FDFF" stroke-opacity="0.5" stroke-width="2"/>
  <g fill="none" stroke="#EFFFFF" stroke-opacity="0.35" stroke-width="3" stroke-linecap="round">
    <path d="M470 440 Q512 478 554 440"/><path d="M462 490 Q512 534 562 490"/><path d="M468 540 Q512 580 556 540"/><path d="M480 590 Q512 618 544 590"/>
  </g>
  <ellipse cx="512" cy="430" rx="46" ry="60" fill="url(#core)"/>
  <path d="{HEAD}" fill="url(#bodyg)" stroke="#E6FDFF" stroke-opacity="0.6" stroke-width="2"/>
  <path d="M494 262 Q512 252 530 262 Q526 300 512 336 Q498 300 494 262Z" fill="url(#beakg)"/>
  <g filter="url(#glowS)"><path d="M470 242 L504 254 L496 270 Z" fill="#FF2BD6"/><path d="M554 242 L520 254 L528 270 Z" fill="#FF2BD6"/></g>
  <path d="M470 242 L504 254 L496 270 Z" fill="#FFFFFF"/><path d="M554 242 L520 254 L528 270 Z" fill="#FFFFFF"/>
</g>
"""
    return defs, body
