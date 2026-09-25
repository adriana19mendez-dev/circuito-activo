(() => {
  const root = document.documentElement;
  const lang = root.lang === 'es' ? 'es' : 'en';
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const themeButton = document.querySelector('.theme-toggle');
  const setTheme = (theme) => {
    root.dataset.theme = theme;
    themeButton?.setAttribute('aria-pressed', String(theme === 'dark'));
    themeButton?.setAttribute('data-theme-state', theme);
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'dark' ? '#111a1a' : '#f4f0e8');
  };
  setTheme(root.dataset.theme === 'dark' ? 'dark' : 'light');
  themeButton?.addEventListener('click', () => {
    const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(theme);
    try { localStorage.setItem('ca-theme', theme); } catch (_) { /* private browsing */ }
  });

  const menuButton = document.querySelector('.menu-toggle');
  const menu = document.querySelector('#mobileMenu');
  const closeMenu = () => {
    if (!menu || !menuButton) return;
    menu.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
  };
  menuButton?.addEventListener('click', () => {
    menu.hidden = !menu.hidden;
    menuButton.setAttribute('aria-expanded', String(!menu.hidden));
  });
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape') closeMenu(); });
  document.addEventListener('click', (event) => {
    if (menu && !menu.hidden && !event.target.closest('.site-header')) closeMenu();
  });
  menu?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.querySelector('#year').textContent = String(new Date().getFullYear());

  const intro = document.querySelector('.intro');
  if (intro) {
    let seen = false;
    try {
      seen = sessionStorage.getItem('ca-intro-seen') === '1';
      sessionStorage.setItem('ca-intro-seen', '1');
    } catch (_) { /* private browsing */ }
    if (seen || reduceMotion.matches) intro.remove();
    else intro.addEventListener('animationend', (event) => {
      if (event.animationName === 'intro-exit') intro.remove();
    });
  }

  const gsap = window.gsap;
  if (gsap && !reduceMotion.matches) {
    const reveals = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);
        gsap.fromTo(entry.target, {autoAlpha: 0, y: 28}, {autoAlpha: 1, y: 0, duration: .85, ease: 'power3.out', clearProps: 'all'});
      });
    }, {rootMargin: '0px 0px -60px 0px', threshold: .06});
    reveals.forEach(node => observer.observe(node));
  }

  // Move by exactly one complete group; every group begins with the same word.
  // Add clones until the viewport is always covered, including wide desktop displays.
  const ticker = document.querySelector('.ticker');
  let tickerTween;
  const setupTicker = () => {
    if (!ticker || !gsap) return;
    tickerTween?.kill();
    const track = ticker.querySelector('.ticker-track');
    const first = track.querySelector('.ticker-group');
    if (!first) return;
    gsap.set(track, {x: 0});
    const width = first.getBoundingClientRect().width;
    if (!width) return;
    while (track.scrollWidth < ticker.clientWidth + width * 2) track.appendChild(first.cloneNode(true));
    if (!reduceMotion.matches) tickerTween = gsap.to(track, {x: -width, duration: Math.max(20, width / 48), repeat: -1, ease: 'none'});
  };
  document.fonts?.ready.then(setupTicker).catch(setupTicker);
  if (!document.fonts) setupTicker();
  let resizeTimer;
  window.addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(setupTicker, 180); });
  reduceMotion.addEventListener?.('change', () => { setupTicker(); });

  const copyButton = document.querySelector('#copyEmail');
  copyButton?.addEventListener('click', async () => {
    const status = document.querySelector('#copyStatus');
    try {
      await navigator.clipboard.writeText('amendez@circuitoactivo.com');
      status.textContent = lang === 'es' ? 'Dirección copiada.' : 'Address copied.';
    } catch (_) {
      status.textContent = lang === 'es' ? 'Selecciona la dirección de arriba para copiarla.' : 'Select the address above to copy it.';
    }
  });

  document.querySelector('#partnerForm')?.addEventListener('submit', event => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const subject = (lang === 'es' ? 'Consulta de aliado' : 'Partner enquiry') + ' — ' + data.get('business');
    const fields = lang === 'es'
      ? [['Negocio','business'],['Contacto','person'],['Correo','email'],['Ciudad o zona','city'],['Tipo de espacio','type'],['Mensaje','message']]
      : [['Business','business'],['Contact','person'],['Email','email'],['City or area','city'],['Venue type','type'],['Message','message']];
    const body = fields.map(([label,key]) => `${label}: ${data.get(key) || '—'}`).join('\n');
    const draft = document.querySelector('#emailDraft');
    draft.hidden = false;
    document.querySelector('#draftSubject').value = subject;
    document.querySelector('#draftBody').value = body;
    document.querySelector('#openDraft').href = `mailto:amendez@circuitoactivo.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    document.querySelector('#draftTitle').focus();
  });

  document.querySelector('#copyDraft')?.addEventListener('click', async () => {
    const subject = document.querySelector('#draftSubject').value;
    const body = document.querySelector('#draftBody').value;
    const status = document.querySelector('#draftStatus');
    try {
      await navigator.clipboard.writeText(`${subject}\n\n${body}`);
      status.textContent = lang === 'es' ? 'Mensaje copiado.' : 'Message copied.';
    } catch (_) {
      status.textContent = lang === 'es' ? 'Selecciona el texto de arriba para copiarlo.' : 'Select the text above to copy it.';
    }
  });
})();
