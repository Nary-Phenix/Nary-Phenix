# NARY OS — Spécification technique

**Version du document :** 1.0 (Phase 1 — Foundation)
**Dernière mise à jour :** 2026-11-18

> *Samy nosorandreniny Token ka aza mifampidera produit*

> NARY OS — Your workspace. Your identity. Your system.

---

## 1. Identité du projet

| Champ | Valeur |
|---|---|
| Nom | NARY OS |
| Type | GitHub Profile README Operating System Simulation |
| Version initiale | 1.0 |
| Identité visuelle | Cyberpunk / Premium Dark |
| Navigation | Multipage Markdown |
| Environnement cible | GitHub Profile Overview (rendu du README) |

**Objectif :** transformer le README de profil GitHub en une simulation visuelle d'un système d'exploitation de bureau. Un visiteur doit découvrir directement un bureau : wallpaper, barre système, icônes d'applications, dock, interface futuriste.

**Hors périmètre :** un portfolio externe, un site web, tout ce qui nécessite un serveur.

---

## 2. Identité visuelle

- Dark premium : surfaces noires et violet profond.
- Fenêtres arrondies, icônes 3D avec glow néon, ombres douces.
- Accents : magenta, violet, bleu électrique, cyan.
- Dock inférieur avec icônes colorées.
- Inspiration : environnements macOS futuristes (références : capture « Files » à dossiers magenta, et dossier néon violet à intérieur noir).

### 2.1 Wallpaper — Phoenix

- Phoenix majestueux, ailes déployées.
- Flammes bleues, violettes et cyan ; particules lumineuses discrètes.
- Fond sombre, élégant, futuriste. Composition paysage 16:9.
- Un dégradé abstrait générique n'est **pas** un substitut acceptable.

Fichiers : `image/wallpaper.png` (bureau) et `image/lockscreen.png` (écran de verrouillage).

### 2.2 Icônes

- Aucun emoji comme icône d'application.
- Vraies icônes graphiques : relief 3D, glow néon, ombres douces, coins arrondis, cohérence totale (même éclairage, même perspective).
- Lisibles à petite taille.
- Une image par icône, stockée dans `image/`.

| Application | Couleur d'identité |
|---|---|
| About Me | Cyan / bleu |
| Dev Studio | Bleu électrique |
| Projects | Magenta |
| Terminal | Vert / cyan |
| Education | Violet |
| Contact | Rose / violet |
| Settings | Argent / bleu |

### 2.3 Slogan officiel

Texte **exact**, à ne jamais traduire, modifier ni corriger :

```
Samy nosorandreniny Token ka aza mifampidera produit
```

Emplacements obligatoires :

1. Boot screen (`boot.gif`).
2. Bureau principal (section identité).
3. Signature / footer système (chaque page).

Présentation : élégante, visible sans écraser l'interface.

---

## 3. Applications

| # | Application | Fichier | Contenu |
|---|---|---|---|
| 1 | About Me | `apps/about.md` | Présentation, parcours, profil |
| 2 | Dev Studio | `apps/dev-studio.md` | Compétences, langages, frameworks, technologies, outils |
| 3 | Projects | `apps/projects.md` | Explorateur de projets, liste des réalisations |
| 4 | Terminal | `apps/terminal.md` | Terminal simulé, commandes visuelles, liens navigables |
| 5 | Education | `apps/education.md` | Formations, certifications, parcours académique |
| 6 | Contact | `apps/contact.md` | GitHub, LinkedIn, réseaux, moyens de contact |
| 7 | Settings | `apps/settings.md` | Infos système, version, crédits |

Fiches projets (`projects/`) : `case-zero.md`, `nary-translator.md`, `wordprofessional.md`, `nary-os.md`. Chacune contient un lien vers le **vrai dépôt GitHub** du projet.

---

## 4. Navigation

- Principale : **Desktop → application** (clic sur une icône).
- Chaque application propose : bouton **Back**, bouton **Home**, header commun, titre, chemin virtuel, contenu spécifique, footer NARY OS.
- Définitions :
  - **Home** = toujours le bureau (`desktop.md`). Le `README.md` est l'écran de verrouillage ; un clic sur son GIF ouvre le bureau.
  - **Back** = niveau précédent (application → bureau `desktop.md` ; fiche projet → `apps/projects.md`).
- Tous les liens sont **relatifs** (voir `ARCHITECTURE.md`).

---

## 5. Boot screen

Séquence pré-rendue en GIF (`image/boot.gif`) :

1. Écran noir.
2. Apparition du logo Phoenix.
3. Apparition de « NARY OS ».
4. Révélation du slogan officiel.
5. Affichage de la version.
6. Transition vers le bureau.

---

## 6. Contraintes techniques

**Interdit :** JavaScript (custom ou inline), CSS externe ou `style`/`class`, dépendances serveur, interactions impossibles dans un README, zones cliquables superposées à une image de bureau.

**Autorisé :** Markdown, HTML accepté par GitHub (`table`, `img`, `a`, `picture`, `details`, `br`, `sub`, `kbd`…), PNG/WebP, GIF, liens relatifs.

**Principe de simulation :** une image de bureau composée (non cliquable) + des icônes individuelles cliquables placées dans une table compatible Markdown, + un dock sous forme de table d'images liées. On ne prétend pas simuler du positionnement CSS.

**Exigences :** compatibilité mobile, fiabilité de navigation, rendu GitHub correct avant tout effet décoratif.

---

## 7. Phases de développement

| Phase | Contenu |
|---|---|
| 1 — Foundation | Architecture, conventions, documentation, palette, dimensions des assets |
| 2 — Assets | Spécs wallpaper/lockscreen, icônes, logo Phoenix, boot.gif, autres ressources |
| 3 — Desktop | README principal, intégration des ressources, bureau, applications cliquables |
| 4 — Applications | Templates, sept applications, fiches projets |
| 5 — Tests | Liens, rendu GitHub, mobile, optimisation images/animations |

Détail dans `ROADMAP.md`. Validation des assets et du design du bureau **avant** les phases 4 et 5.
