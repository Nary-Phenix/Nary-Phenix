<!-- NARY OS · HEADER -->
<table width="100%">
  <tr>
    <td align="left"><a href="../apps/projects.md">← Back</a> &nbsp;·&nbsp; <a href="../README.md"><img src="../image/ic_home.png" width="18" alt="Home"> Home</a></td>
    <td align="right"><sub>NARY OS v1.0</sub></td>
  </tr>
</table>

# Nary-Translator

`~/nary-os/projects/nary-translator`

| | |
|---|---|
| **Statut** | En développement |
| **Technologies** | Python, Termux, Tesseract |


## Présentation

Pipeline pensé pour **Android / Termux** qui transforme un chapitre de manhwa en texte structuré : téléchargement des pages, assemblage en archive CBZ, extraction du texte par OCR, nettoyage et rapport qualité. Le texte produit suit les codes de script des agences de traduction (dialogues, pensées, bruitages, etc.).

## Étapes

1. **Téléchargement** des images d'un chapitre depuis une URL.
2. **Archive CBZ** vérifiée.
3. **OCR** : découpage adaptatif des pages hautes avec recouvrement, stratégies par page, prétraitement léger.
4. **Texte structuré** page par page, avec les codes de la fiche de script.
5. **Rapport qualité** : pages vides ou douteuses signalées, sans métriques inventées.

## Principes

- Fonctionne avec des ressources limitées (Termux).
- Outils locaux et gratuits par défaut ; un module d'IA optionnel reste isolé et configurable.
- Les images originales ne sont jamais modifiées ; le texte brut est conservé.
- Pas de traduction automatique à ce stade.

## Avancement

Le projet est en cours de refonte vers une chaîne unique (`main.py`) avec une extraction locale plus fiable.


## Repository

<table>
  <tr>
    <td><a href="https://github.com/Nary-Phenix?tab=repositories"><img src="../image/ic_github.png" width="40" alt="GitHub"></a></td>
    <td><a href="https://github.com/Nary-Phenix?tab=repositories"><b>Voir sur GitHub</b></a><br><sub>Lien vers la liste de mes dépôts. *(à compléter)*</sub></td>
  </tr>
</table>

---

<!-- NARY OS · FOOTER -->
<p align="center">
  <sub><i>Samy nosorandreniny Token ka aza mifampidera produit</i></sub><br>
  <sub>NARY OS v1.0 — Your workspace. Your identity. Your system.</sub>
</p>
