# AP Calc AB · Unit 4 study planner

A static study site for Unit 4 (derivatives in context, related rates, motion, tangent line approximation, l'Hôpital's Rule).

- `index.html` — agenda by day with Canvas links, homework checkboxes (saved in each visitor's browser), test countdown, learning objectives, labs
- `notes.html` — study notes and a worked example for every day
- `labs/` — the seven interactive sheets (related rates, motion, rates in context)

## Publish on GitHub Pages

1. Make a new repository on GitHub and upload everything in this folder (or `git push` it).
2. In the repo: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, pick `main` and `/ (root)`, then **Save**.
3. After a minute the site is live at `https://<your-username>.github.io/<repo-name>/`.

## Updating the schedule

When the teacher posts new slides or solutions, edit the `DAYS` list in `build.py` (Canvas file IDs are the number in the file's URL), then run:

```
python3 build.py
```

That regenerates `index.html` from `index.template.html`. Edit `notes.html` directly for notes.

Homework and slide links point to Canvas and Google Slides, so classmates need to be signed in to open them.
