(() => {
  const TEST = new Date(2026, 10, 10); // Tue Nov 10, 2026
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const DAY = 864e5;

  // Countdown sticker
  const count = document.getElementById('count');
  if (count) {
    const left = Math.round((TEST - today) / DAY);
    const text = document.getElementById('countText');
    if (left > 1) { count.innerHTML = left + '<small>days</small>'; }
    else if (left === 1) { count.innerHTML = '1<small>day</small>'; text.textContent = 'until the Unit 4 test. Tomorrow!'; }
    else if (left === 0) { count.innerHTML = 'Today'; text.textContent = 'is the Unit 4 test. Good luck.'; }
    else { count.innerHTML = 'Done'; text.textContent = 'The Unit 4 test was Tuesday Nov 10. These notes stay up for the final.'; }
  }

  // Flag today's or the next class day in the agenda
  const days = [...document.querySelectorAll('.day[data-date]')];
  const parse = s => { const [y, m, d] = s.split('-').map(Number); return new Date(y, m - 1, d); };
  const next = days.find(el => parse(el.dataset.date) >= today);
  const nextEl = document.getElementById('next');
  if (next) {
    const isToday = +parse(next.dataset.date) === +today;
    next.classList.add('is-next');
    const f = document.createElement('span');
    f.className = 'flag'; f.textContent = isToday ? 'Today' : 'Next up';
    next.prepend(f);
    if (nextEl) {
      const d = next.querySelector('.date span').textContent.replace(' · ', ' ');
      nextEl.innerHTML = (isToday ? 'Today' : 'Next class') + ': ' + d + ' ' + next.querySelector('.date b').textContent +
        ', <a href="#agenda">' + next.querySelector('h4').textContent + '</a>.';
    }
    const study = document.getElementById('studyNext');
    const notesLink = next.querySelector('a[href^="notes.html#"]');
    if (study && notesLink) {
      study.href = notesLink.getAttribute('href');
      study.firstChild.textContent = 'Study next: ' + next.querySelector('h4').textContent.split(':')[0] + ' notes ';
    } else if (study) {
      study.href = 'notes.html#review';
      study.firstChild.textContent = 'Review for the test ';
    }
  } else if (nextEl) { nextEl.hidden = true; }

  // Homework checkboxes, remembered on this device only
  const KEY = 'u4-hw';
  let saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) {}
  const boxes = [...document.querySelectorAll('input[data-hw]')];
  const meter = document.getElementById('meter');
  const done = document.getElementById('done');
  const tally = () => {
    const n = boxes.filter(b => b.checked).length;
    if (meter) meter.style.width = (boxes.length ? n / boxes.length * 100 : 0) + '%';
    if (done && n) done.textContent = n + ' of ' + boxes.length + ' assignments checked off.';
  };
  boxes.forEach(b => {
    b.checked = !!saved[b.dataset.hw];
    b.addEventListener('change', () => {
      saved[b.dataset.hw] = b.checked;
      try { localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) {}
      tally();
    });
  });
  tally();

  // Reveal on scroll (content is visible without JS or with reduced motion)
  const rv = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(en => {
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    }), { rootMargin: '0px 0px -8% 0px' });
    rv.forEach((el, i) => { if (!el.style.getPropertyValue('--d') && el.classList.contains('day')) el.style.setProperty('--d', (i % 4) * 70 + 'ms'); io.observe(el); });
  } else rv.forEach(el => el.classList.add('in'));

  // Notes page: highlight the lesson you are reading in the contents
  const toc = document.querySelectorAll('.toc a');
  if (toc.length && 'IntersectionObserver' in window) {
    const map = new Map([...toc].map(a => [a.getAttribute('href').slice(1), a]));
    const io2 = new IntersectionObserver(es => es.forEach(en => {
      if (en.isIntersecting) { toc.forEach(a => { a.classList.remove('on'); a.removeAttribute('aria-current'); }); const a = map.get(en.target.id); if (a) { a.classList.add('on'); a.setAttribute('aria-current', 'location'); } }
    }), { rootMargin: '-30% 0px -60% 0px' });
    document.querySelectorAll('.lesson[id]').forEach(s => io2.observe(s));
  }
})();
