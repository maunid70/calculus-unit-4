"""Builds index.html from the Unit 4 schedule below. Run: python3 build.py
Edit DAYS when the teacher posts new slides or solutions, then rebuild."""
import html

CANVAS = "https://knoxschools.instructure.com/courses/1480483/files/{}?wrap=1"
SLIDES = "https://docs.google.com/presentation/d/{}/edit?usp=sharing"

I_SLIDES = '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="1.5" y="2.5" width="13" height="9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 11.5v3M5 14.5h6" stroke="currentColor" stroke-width="1.6"/></svg>'
I_NOTES = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 1.5h7l3 3v10H3z" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M5.5 7h5M5.5 10h5" stroke="currentColor" stroke-width="1.6"/></svg>'
I_LAB = '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M6.5 5v6l5-3z" fill="currentColor"/></svg>'
I_ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'

# t = topic tab: context, rates, motion, approx, test
DAYS = [
  ("Week of Oct 26", [
    dict(date="2026-10-28", wd="Wed", n="28", mo="Oct", t="context",
         titles=["Day 1: Interpreting Derivatives in Context", "Day 3: Rates of Change in Other Contexts"],
         topic="Units, the sentence template, rate in vs. rate out",
         slides="1g9NOh6Jriw_cf0Ld57_pX-kdgXamCdJXoLYCeWOZOrc", notes=["day1", "day3"], lab=("sheet7", "Water in, water out lab"),
         hw=[("d1", "Day 1 HW", 58322485, 58894026), ("d3", "Day 3 HW", 58322493, 58894031)]),
    dict(date="2026-10-29", wd="Thu", n="29", mo="Oct", t="rates",
         titles=["Day 4: Intro to Related Rates"], topic="The five steps; constants go in before you differentiate",
         slides="1tcMjKQSHax-dS-yUm7H7L6j7RPq1dc1sZL8yBNyeo1Y", notes=["day4"], lab=("sheet4", "Draining tank lab"),
         hw=[("d4", "Day 4 HW", 58894072, 58896941)]),
    dict(date="2026-10-30", wd="Fri", n="30", mo="Oct", t="rates",
         titles=["Day 5: More Advanced Related Rates"], topic="Cones and similar triangles. Quiz over Days 1 and 3",
         slides="1nG9-Aefs06rYTW5-BJoYTr1UZqpcMHemzW-Tz_BIzqg", notes=["day5"], lab=("", "Cylinder, cars and bubble labs"),
         hw=[("d5", "Day 5 HW", 58894073, 58909238), ("rrp", "Related Rates Practice", 58909230, 58918664)]),
  ]),
  ("Week of Nov 2", [
    dict(date="2026-11-02", wd="Mon", n="2", mo="Nov", t="motion",
         titles=["Day 2: Connecting Position, Velocity, and Acceleration"], topic="Signs of v and a, at rest, speeding up",
         slides="1qNGkA2BO0pcnLeIAGS8iSoAlbhqnRyVx1R2_WWc9YDg", notes=["day2"], lab=("sheet5", "Velocity Raptor lab"),
         extra=[("Motion Overview", 58926234)],
         hw=[("d2", "Day 2 HW", 58894074, 58926242), ("ctc", "Crack the Code", 58926240, 58926241)]),
    dict(date="2026-11-04", wd="Wed", n="4", mo="Nov", t="approx",
         titles=["Day 6: Approximating Values with Tangent Lines"], topic="Linearization; over or under from concavity. AP Exam sign-up closes today (AB-only students)",
         notes=["day6"], hw=[("d6", "Day 6 HW", 58894075, None)]),
    dict(date="2026-11-05", wd="Thu", n="5", mo="Nov", t="approx",
         titles=["Day 7: l'Hôpital's Rule"], topic="Limits that come out 0/0 or ∞/∞",
         notes=["day7"], hw=[("d7", "Day 7 HW", 58894076, None)]),
    dict(date="2026-11-06", wd="Fri", n="6", mo="Nov", t="test",
         titles=["Review"], topic="Personal Progress Checks",
         notes=["review"], hw=[("mcq", "PPC MCQ (on AP Classroom)", None, None),
                               ("ppca", "PPC FRQ Part A", 56036032, None), ("ppcb", "PPC FRQ Part B", 56036246, None)]),
  ]),
  ("Week of Nov 9", [
    dict(date="2026-11-09", wd="Mon", n="9", mo="Nov", t="approx",
         titles=["Bonus: Newton's Method"], topic="How some calculators find zeros from a graph", notes=["newton"], hw=[]),
    dict(date="2026-11-10", wd="Tue", n="10", mo="Nov", t="test", test=True,
         titles=["Unit 4 Test"], topic="Everything on this page. Bring your calculator.", hw=[]),
  ]),
]

def e(s): return html.escape(s, quote=True)

def day_html(d):
    cls = "day rv" + (" is-test" if d.get("test") else "")
    out = [f'<article class="{cls}" data-t="{d["t"]}" data-date="{d["date"]}">',
           f'<div class="date"><b>{d["n"]}</b><span>{d["wd"]} · {d["mo"]}</span></div>']
    for t in d["titles"]:
        out.append(f'<h4>{e(t)}</h4>')
    out.append(f'<p class="topic">{e(d["topic"])}</p>')
    links = []
    if d.get("slides"):
        links.append(f'<a class="chip" href="{SLIDES.format(d["slides"])}" target="_blank" rel="noopener">{I_SLIDES}Slides</a>')
    elif not d.get("test"):
        links.append('<span class="chip muted">Slides not posted yet</span>')
    for n in d.get("notes", []):
        label = "Notes" if len(d.get("notes", [])) == 1 else "Notes " + n.replace("day", "Day ")
        links.append(f'<a class="chip" href="notes.html#{n}">{I_NOTES}{label}</a>')
    if d.get("lab"):
        anchor, label = d["lab"]
        href = "labs/index.html" + (f"#{anchor}" if anchor else "")
        links.append(f'<a class="chip" href="{href}">{I_LAB}{label}</a>')
    for label, fid in d.get("extra", []):
        links.append(f'<a class="chip" href="{CANVAS.format(fid)}" target="_blank" rel="noopener">{I_NOTES}{e(label)}</a>')
    if links:
        out.append('<div class="links">' + "".join(links) + '</div>')
    if d["hw"]:
        out.append("<ul>")
        for key, label, fid, sol in d["hw"]:
            name = f'<a href="{CANVAS.format(fid)}" target="_blank" rel="noopener">{e(label)}</a>' if fid else f'<span>{e(label)}</span>'
            if sol:
                s = f'<a class="sol" href="{CANVAS.format(sol)}" target="_blank" rel="noopener">solutions</a>'
            elif fid:
                s = '<span class="sol">solutions not posted</span>'
            else:
                s = ""
            out.append(f'<li><label class="hw"><input type="checkbox" data-hw="{key}" aria-label="Done: {e(label)}">{name}</label>{s}</li>')
        out.append("</ul>")
    out.append("</article>")
    return "\n".join(out)

agenda = []
for wk, days in DAYS:
    agenda.append(f'<div class="week"><h3>{wk}</h3><div class="days">')
    agenda.extend(day_html(d) for d in days)
    agenda.append("</div></div>")

page = open("index.template.html").read().replace("<!--AGENDA-->", "\n".join(agenda)).replace("<!--ARROW-->", I_ARROW)
open("index.html", "w").write(page)
print("index.html written")
