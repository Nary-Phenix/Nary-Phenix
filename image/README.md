# NARY OS — Index des assets (`image/`)

Toutes les ressources graphiques du projet sont dans ce dossier. Chaque image a une **source SVG** dans `src/` et peut être remplacée ou régénérée sans toucher aux pages Markdown.

## Changer un asset

**Option 1 — le remplacer par ton propre fichier** (le plus simple)
Remplace le fichier en gardant **exactement le même nom et les mêmes dimensions** (tableaux ci-dessous). Aucun lien du README ni des pages n'est à modifier.

**Option 2 — le régénérer depuis les sources**
```bash
cd image/src
python3 build.py                # tout régénérer
python3 build.py ic_about boot  # seulement certains assets
```
Prérequis : `rsvg-convert`, ImageMagick (`convert`), Python 3 + Pillow.
- Couleurs et pictogrammes des icônes : `src/icons.py`
- Phoenix et wallpaper : `src/phoenix.py`
- Lockscreen, bannières, boot et **slogan officiel** : `src/assets.py`

> Les textes des PNG (titres, slogan) utilisent les polices Montserrat, Inter et DejaVu Sans Mono au moment du rendu. Les PNG livrés sont la référence ; si ces polices manquent sur une autre machine, le rendu de texte peut différer.

Le slogan officiel n'est défini qu'à un seul endroit (`SLOGAN` dans `src/assets.py`) : **ne pas le modifier**.

---

## Identité

| Fichier | Dimensions | Rôle | Source |
|---|---|---|---|
| `wallpaper.png` | 1920×1080 | Fond du bureau (Phoenix, skyline, grille néon) | `src/wallpaper.svg` |
| `lockscreen.png` | 1920×1080 | Écran de verrouillage : aperçu dans Settings et dernière image du boot | `src/lockscreen.svg` |
| `phoenix_logo.png` | 1024×1024 (transparent) | Logo Phoenix, à utiliser sur fond sombre | `src/phoenix_logo.svg` |
| `boot.gif` | 960×540 | Séquence de démarrage (noir → Phoenix → NARY OS → slogan → version → lockscreen), lecture unique | généré par `build.py` |

## Applications (bureau)

| Fichier | Dimensions | Application | Source |
|---|---|---|---|
| `ic_about.png` | 512×512 | About Me | `src/ic_about.svg` |
| `ic_devstudio.png` | 512×512 | Dev Studio | `src/ic_devstudio.svg` |
| `ic_projects.png` | 512×512 | Projects | `src/ic_projects.svg` |
| `ic_terminal.png` | 512×512 | Terminal | `src/ic_terminal.svg` |
| `ic_education.png` | 512×512 | Education | `src/ic_education.svg` |
| `ic_contact.png` | 512×512 | Contact | `src/ic_contact.svg` |
| `ic_settings.png` | 512×512 | Settings | `src/ic_settings.svg` |

## Icônes système

| Fichier | Dimensions | Usage | Source |
|---|---|---|---|
| `ic_folder.png` | 256×256 | Dossiers (explorateur de projets) | `src/ic_folder.svg` |
| `ic_file.png` | 256×256 | Fichiers | `src/ic_file.svg` |
| `ic_github.png` | 256×256 | Liens vers les dépôts GitHub (pictogramme de branche, pas le logo Octocat) | `src/ic_github.svg` |
| `ic_home.png` | 256×256 | Bouton Home des pages | `src/ic_home.svg` |

## Barre système

| Fichier | Dimensions | Source |
|---|---|---|
| `ic_wifi.png` | 128×128 | `src/ic_wifi.svg` |
| `ic_bluetooth.png` | 128×128 | `src/ic_bluetooth.svg` |
| `ic_battery.png` | 128×128 | `src/ic_battery.svg` |
| `ic_volume.png` | 128×128 | `src/ic_volume.svg` |
| `ic_brightness.png` | 128×128 | `src/ic_brightness.svg` |

## Dock (`dock/`)

| Fichier | Dimensions | Lien prévu | Source |
|---|---|---|---|
| `dock/dock_home.png` | 256×256 | Bureau | `src/dock_home.svg` |
| `dock/dock_projects.png` | 256×256 | Projects | `src/dock_projects.svg` |
| `dock/dock_terminal.png` | 256×256 | Terminal | `src/dock_terminal.svg` |
| `dock/dock_contact.png` | 256×256 | Contact | `src/dock_contact.svg` |

## Bannières (`banners/`)

| Fichier | Dimensions | Page | Source |
|---|---|---|---|
| `banners/banner_about.png` | 1600×400 | About Me | `src/banner_about.svg` |
| `banners/banner_projects.png` | 1600×400 | Projects | `src/banner_projects.svg` |
| `banners/banner_devstudio.png` | 1600×400 | Dev Studio | `src/banner_devstudio.svg` |

---

## Règles à respecter pour tout remplacement

- Même nom de fichier, mêmes dimensions, minuscules, sans espaces (GitHub est sensible à la casse).
- Icônes : **tuile sombre opaque** aux coins arrondis (pas de glow sur fond transparent : illisible sur le thème clair de GitHub).
- Poids cibles : icônes 512 ≤ 160 Ko, icônes 256 et dock ≤ 60 Ko, barre système ≤ 20 Ko, bannières ≤ 400 Ko, wallpaper/lockscreen ≤ 1,5 Mo, boot.gif ≤ 4 Mo.
- Format PNG (ou WebP) ; GIF uniquement pour `boot.gif`.
