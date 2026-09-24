# Circuito Activo website

This is a static bilingual site. Spanish pages live at the repository root and matching English pages live in `en/`. No build step is required to serve or deploy the generated HTML.

## Preview

```sh
python3 -m http.server 8766 --bind 127.0.0.1
```

Open `http://127.0.0.1:8766/` for Spanish or `http://127.0.0.1:8766/en/` for English.

## Editing content

Edit the paired Spanish and English copy in `tools/generate_site.py`, then run:

```sh
python3 tools/generate_site.py
```

Commit the generated HTML alongside the source script. `styles.css` and `script.js` are shared by both languages.

## Deployment

Keep GitHub Pages configured to publish `main` from the repository root. The `CNAME` file maps the custom domain. The generated site does not need a custom Actions workflow. Review the local preview before committing to `main`.

The contact page prepares an email draft in the visitor's browser. It does not send or store form data. Visitors can also copy the displayed email address or draft message. A hosted form endpoint or other backend is needed if submissions should arrive without a local email app.

GSAP 3.15.0 is self-hosted in `vendor/gsap.min.js` under its [standard license](https://gsap.com/standard-license/). Animations are disabled for visitors who prefer reduced motion.
