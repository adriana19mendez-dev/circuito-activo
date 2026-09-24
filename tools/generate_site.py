from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
EMAIL = "amendez@circuitoactivo.com"

COPY = {
    "es": {
        "nav": ["Inicio", "Para aliados", "Por qué nosotros", "Preguntas", "Contacto"],
        "theme": "Cambiar tema", "menu": "Menú", "skip": "Ir al contenido", "language": "English",
        "footer": "Una red local para moverte a tu manera.",
        "pages": {
            "index": ("Una red. Más formas de moverte.", "Circuito Activo reúne gimnasios, estudios y espacios de movimiento. Invitamos a los primeros aliados a definir con nosotros cómo funcionará el acceso."),
            "partners": ("Abre espacio a nuevos visitantes.", "Comparte la disponibilidad que funcione para tu negocio y presenta tu espacio a personas que buscan nuevas formas de moverse."),
            "why-us": ("Más opciones para las personas. Más formas de darse a conocer para los espacios.", "Nuestra red busca facilitar la exploración de opciones locales y acercar nuevos visitantes a los espacios participantes."),
            "faq": ("Respuestas claras, incluso sobre lo que aún estamos definiendo.", "Circuito Activo es una red que prepara su primera oferta pública junto con sus primeros aliados."),
            "contact": ("Hablemos de tu espacio.", "Cuéntanos sobre tu espacio y conversemos sobre si la alianza encaja."),
        },
    },
    "en": {
        "nav": ["Home", "For partners", "Why us", "FAQ", "Contact"],
        "theme": "Switch theme", "menu": "Menu", "skip": "Skip to content", "language": "Español",
        "footer": "A local network for movement on your terms.",
        "pages": {
            "index": ("One network. More ways to move.", "Circuito Activo brings gyms, studios and movement spaces together. We are inviting our first partners to shape how access will work."),
            "partners": ("Make room for new visitors.", "Share the availability that works for your business and introduce your space to people looking for ways to move."),
            "why-us": ("More choice for people. More ways to be discovered for venues.", "Our network is designed to help people explore local movement options and help participating venues meet new visitors."),
            "faq": ("Clear answers, even while details are being agreed.", "Circuito Activo is a network preparing its first public offering with early partners."),
            "contact": ("Let's talk about your space.", "Tell us about your venue and we'll discuss whether the partnership is a fit."),
        },
    },
}

PAGES = ["index", "partners", "why-us", "faq", "contact"]

def tag(text, cls=""):
    return f'<span class="{cls}">{escape(text)}</span>'

def link(lang, page):
    return f'{page}.html'

def block(lang, eyebrow, title, body="", extra=""):
    return f'''<section class="section"><div class="wrap">{tag(eyebrow, 'eyebrow reveal')}<div class="section-head reveal"><h2>{escape(title)}</h2>{f'<p>{escape(body)}</p>' if body else ''}</div>{extra}</div></section>'''

def card(number, title, body):
    return f'<article class="feature-card reveal"><span class="feature-number">{escape(str(number))}</span><h3>{escape(title)}</h3><p>{escape(body)}</p></article>'

def cardgrid(items):
    return '<div class="feature-grid">' + ''.join(card(*i) for i in items) + '</div>'

def button(lang, page, label, secondary=False):
    cls = "button button-outline" if secondary else "button button-primary"
    return f'<a class="{cls}" href="{link(lang,page)}">{escape(label)}<span aria-hidden="true">↗</span></a>'

def cta(lang, eyebrow, title, body, label):
    return f'''<section class="section cta-section"><div class="wrap"><div class="cta-panel reveal"><div><span class="eyebrow">{escape(eyebrow)}</span><h2>{escape(title)}</h2><p>{escape(body)}</p></div>{button(lang,'contact',label)}</div></div></section>'''

def home(lang):
    es = lang == "es"
    title, desc = COPY[lang]["pages"]["index"]
    lead = "El movimiento no tiene una sola forma." if es else "Movement has more than one shape."
    meta = "Una red local de movimiento" if es else "A local movement network"
    hero = f'''<section class="home-hero"><div class="wrap hero-layout"><div class="hero-copy"><span class="eyebrow hero-eyebrow">{meta}</span><h1>{escape(title.split('. ')[0])}.<br><em>{escape(title.split('. ')[1])}</em></h1><p class="hero-lead">{escape(desc)}</p><div class="hero-actions">{button(lang,'partners','Quiero ser aliado' if es else 'Become a partner')}{button(lang,'why-us','Conoce la red' if es else 'Explore the network',True)}</div><p class="hero-footnote">{escape('Los planes y el acceso para usuarios se anunciarán antes del lanzamiento público.' if es else 'Plans and member access will be announced before the public launch.')}</p></div><div class="hero-art" aria-label="Circuito Activo" role="img"><span class="art-label art-label-top">{escape('MÁS OPCIONES' if es else 'MORE CHOICE')}</span><img src="{'' if lang=='es' else '../'}circuito-activo-logo.png" alt="" width="480" height="480"><span class="art-label art-label-bottom">{escape('UN SOLO CIRCUITO' if es else 'ONE NETWORK')}</span></div></div><div class="hero-index wrap"><span>01 / 05</span><span>{escape(lead)}</span><span aria-hidden="true">↓</span></div></section>'''
    words = ["PILATES", "YOGA", "FUERZA", "BOXEO", "CICLISMO", "DANZA", "MOVILIDAD"] if es else ["PILATES", "YOGA", "STRENGTH", "BOXING", "CYCLING", "DANCE", "MOBILITY"]
    # Three copies keep the line filled even on wide screens; JS measures one group for a seamless loop.
    group = '<div class="ticker-group">' + ''.join(f'<span>{w}<i aria-hidden="true">✳</i></span>' for w in words) + '</div>'
    ticker = f'<div class="ticker" aria-label="{escape(", ".join(words))}"><div class="ticker-track" aria-hidden="true">{group*3}</div></div>'
    cards = [
        ("01", "Muévete con variedad" if es else "Move with variety", "Explora distintas disciplinas y espacios locales en una sola red." if es else "Explore different disciplines and local spaces in one network."),
        ("02", "Descubre espacios reales" if es else "Discover real places", "Conoce los gimnasios, estudios y personas que hacen especial cada experiencia." if es else "Meet the gyms, studios and people behind each experience."),
        ("03", "Crece junto a la red" if es else "Grow with the network", "Cada aliado acuerda la disponibilidad que encaja con su actividad." if es else "Each partner agrees on availability that fits their business."),
    ]
    section1 = block(lang,"LA IDEA" if es else "THE IDEA","Un lugar para muchas formas de moverte." if es else "One place for many ways to move.","Circuito Activo conecta a personas con espacios de movimiento locales. Estamos incorporando a los primeros aliados antes de abrir el acceso al público." if es else "Circuito Activo connects people with local movement spaces. We are welcoming our first partners before opening access to the public.",cardgrid(cards))
    dark = f'''<section class="section"><div class="wrap"><div class="dark-feature reveal"><div class="dark-feature-top"><span class="eyebrow">{escape('PARA LOS ESPACIOS' if es else 'FOR VENUES')}</span><span class="round-mark">↗</span></div><h2>{escape('Tu espacio tiene algo único. Hagamos que más personas lo conozcan.' if es else 'Your space has something unique. Let more people discover it.')}</h2><p>{escape('La red ofrece una nueva forma de presentar tu espacio a personas interesadas en moverse. La disponibilidad y las condiciones se acuerdan contigo antes de participar.' if es else 'The network offers a new way to introduce your venue to people interested in movement. Availability and terms are agreed with you before you join.')}</p>{button(lang,'partners','Para gimnasios y estudios' if es else 'For gyms and studios',True)}</div></div></section>'''
    return hero + ticker + section1 + dark + cta(lang,"HABLEMOS" if es else "LET'S TALK","El siguiente movimiento empieza aquí." if es else "Your next move starts here.","Conversemos sobre cómo puede encajar tu espacio en Circuito Activo." if es else "Let's discuss how your venue could fit into Circuito Activo.","Escríbenos" if es else "Get in touch")

def standard_hero(lang, page, eyebrow):
    title, desc = COPY[lang]["pages"][page]
    return f'''<section class="page-hero"><div class="wrap"><span class="eyebrow reveal">{escape(eyebrow)}</span><h1 class="reveal">{escape(title)}</h1><p class="hero-lead reveal">{escape(desc)}</p><span class="page-hero-decoration" aria-hidden="true">◌</span></div></section>'''

def partners(lang):
    es = lang == 'es'
    hero = standard_hero(lang,'partners','PARA GIMNASIOS Y ESTUDIOS' if es else 'FOR GYMS & STUDIOS')
    items = [
        ('01','Comparte lo que funciona' if es else 'Share what works','Define qué clases, horarios o plazas encajan con tu negocio.' if es else 'Choose which classes, times or places fit your business.'),
        ('02','Da a conocer tu espacio' if es else 'Showcase your space','Presenta tu ambiente, tus entrenadores y tu oferta a nuevas personas.' if es else 'Introduce your atmosphere, instructors and offer to new people.'),
        ('03','Mantén tu identidad' if es else 'Keep your identity','Tu marca y tu relación con tus clientes siguen siendo tuyas.' if es else 'Your brand and your customer relationships remain yours.'),
    ]
    sec = block(lang,'LA OPORTUNIDAD' if es else 'THE OPPORTUNITY','Más visibilidad, a tu manera.' if es else 'More discovery, on your terms.','Cada espacio es diferente. Por eso, la participación se define de forma individual, antes de empezar.' if es else 'Every venue works differently. That is why participation is agreed individually before it begins.',cardgrid(items))
    steps = [
        ('01','Conversemos' if es else 'Start a conversation','Cuéntanos cómo funciona tu espacio y qué quieres ofrecer.' if es else 'Tell us how your venue works and what you want to offer.'),
        ('02','Definamos la alianza' if es else 'Define the partnership','Acordamos disponibilidad, condiciones y próximos pasos.' if es else 'We agree on availability, terms and next steps.'),
        ('03','Prepárate para participar' if es else 'Get ready to join','Te acompañamos en la preparación de la primera oferta pública.' if es else 'We prepare together for the first public offering.'),
    ]
    process = f'''<section class="section"><div class="wrap process"><div><span class="eyebrow">{escape('CÓMO EMPEZAR' if es else 'HOW TO BEGIN')}</span><h2>{escape('Una alianza que empieza con una conversación.' if es else 'A partnership that starts with a conversation.')}</h2></div><div class="process-list">{''.join(f'<div class="process-step reveal"><span>{n}</span><div><h3>{escape(t)}</h3><p>{escape(d)}</p></div></div>' for n,t,d in steps)}</div></div></section>'''
    return hero+sec+process+cta(lang,'PRIMEROS ALIADOS' if es else 'FOUNDING PARTNERS','Construyamos algo que funcione para tu espacio.' if es else 'Make this work for your venue.','Estamos incorporando a los primeros aliados. Las condiciones se conversan directamente con cada espacio.' if es else 'We are welcoming our first partners. Terms are discussed directly with each venue.','Hablemos' if es else 'Let’s talk')

def why_us(lang):
    es = lang == 'es'
    hero = standard_hero(lang,'why-us','LA RED' if es else 'THE NETWORK')
    items = [
        ('01','Variedad cercana' if es else 'Local variety','Una red que reúne distintas disciplinas y espacios en tu ciudad.' if es else 'A network bringing different disciplines and venues together in your city.'),
        ('02','Acceso sencillo' if es else 'Simple access','Estamos definiendo una experiencia clara, sin cálculos complicados.' if es else 'We are defining a clear experience without complicated calculations.'),
        ('03','Aliados con voz' if es else 'Partners have a say','Los primeros espacios ayudan a definir cómo funcionará la participación.' if es else 'Our first venues help shape how participation works.'),
    ]
    sec = block(lang,'NUESTRO ENFOQUE' if es else 'OUR APPROACH','Más movimiento. Más posibilidades.' if es else 'More movement. More possibility.','Queremos que explorar nuevas formas de moverse sea fácil para las personas y práctico para los espacios que las reciben.' if es else 'We want exploring new ways to move to feel easy for people and practical for the venues that welcome them.',cardgrid(items))
    feature = f'''<section class="section"><div class="wrap"><div class="quote-panel reveal"><span class="eyebrow">{escape('EL PROPÓSITO' if es else 'THE PURPOSE')}</span><blockquote>{escape('Moverte debería abrir posibilidades, no limitarte a un solo lugar.' if es else 'Movement should open possibilities, not tie you to one place.')}</blockquote><p>{escape('Circuito Activo une espacios locales con personas curiosas por descubrirlos. El acceso público y los planes se anunciarán cuando estén definidos.' if es else 'Circuito Activo connects local venues with people curious to discover them. Public access and plans will be announced when they are defined.')}</p></div></div></section>'''
    return hero+sec+feature+cta(lang,'SÚMATE' if es else 'JOIN THE CONVERSATION','¿Tienes un espacio de movimiento?' if es else 'Run a movement space?','Hablemos sobre lo que puede aportar tu espacio a la red.' if es else 'Let’s talk about what your venue could bring to the network.','Contactar' if es else 'Get in touch')

FAQ = {
    'es': [
        ('¿Circuito Activo ya existe?', 'Sí. Circuito Activo es una red local de movimiento. Estamos incorporando a los primeros espacios aliados y definiendo con ellos la primera oferta antes del lanzamiento público.'),
        ('¿Puedo usar la red como usuario ahora?', 'Todavía no. El acceso para usuarios y los planes se anunciarán antes del lanzamiento público.'),
        ('¿Cómo se acordarán las condiciones comerciales?', 'Las condiciones se conversan directamente con cada espacio antes de participar. Aún no hay una tarifa pública ni un modelo único para todos.'),
        ('¿Mi estudio tendrá que incluir todas las clases?', 'No. La disponibilidad se acuerda contigo y puede limitarse a determinadas clases, horarios o plazas.'),
        ('¿Sustituye Circuito Activo mis propias membresías?', 'No. La red está pensada como una forma adicional de dar a conocer tu espacio. Tus membresías y relaciones directas con clientes siguen siendo tuyas.'),
        ('¿La red es solo para gimnasios?', 'No. También invitamos a estudios de yoga y pilates, espacios de fuerza, danza, ciclismo, boxeo, movilidad y otras disciplinas de movimiento.'),
        ('¿Funcionará con créditos?', 'La experiencia de acceso aún se está definiendo. Queremos que sea clara y fácil de entender; comunicaremos los detalles antes de abrirla al público.'),
        ('¿Cómo puedo participar como aliado?', f'Escríbenos a {EMAIL} o utiliza la página de contacto. Conoceremos tu espacio y hablaremos de cómo podría encajar en la red.'),
    ],
    'en': [
        ('Does Circuito Activo already exist?', 'Yes. Circuito Activo is a local movement network. We are welcoming our first venue partners and defining the initial offering with them before the public launch.'),
        ('Can I use the network as a member now?', 'Not yet. Member access and plans will be announced before the public launch.'),
        ('How will commercial terms be agreed?', 'Terms are discussed with each venue before participation. There is no public price or single set of terms for every partner yet.'),
        ('Would my studio need to include every class?', 'No. Availability is agreed with you and can be limited to selected classes, times or places.'),
        ('Will Circuito Activo replace my own memberships?', 'No. The network is designed as an additional way for people to discover your venue. Your memberships and direct customer relationships remain yours.'),
        ('Is the network only for gyms?', 'No. We also welcome yoga and Pilates studios, strength spaces, dance, cycling, boxing, mobility and other movement disciplines.'),
        ('Will there be credits?', 'The access experience is still being defined. We want it to be clear and easy to understand; we will share the details before opening it to the public.'),
        ('How can I join as a partner?', f'Email {EMAIL} or use the contact page. We will learn about your venue and discuss how it could fit into the network.'),
    ],
}

def faq(lang):
    es = lang == 'es'
    hero = standard_hero(lang,'faq','PREGUNTAS FRECUENTES' if es else 'FREQUENTLY ASKED QUESTIONS')
    details = ''.join(f'<details class="faq-item reveal"><summary><span>{escape(q)}</span><span class="faq-plus" aria-hidden="true">+</span></summary><div class="faq-answer"><p>{escape(a)}</p></div></details>' for q,a in FAQ[lang])
    body = f'''<section class="section"><div class="wrap faq-layout"><div><span class="eyebrow">{escape('LO QUE SABEMOS' if es else 'WHAT WE KNOW')}</span><h2>{escape('Sin letra pequeña.' if es else 'The details, clearly.')}</h2><p>{escape('Si algo aún no está definido, te lo decimos con claridad.' if es else 'When something is still being decided, we say so plainly.')}</p></div><div class="faq-list">{details}</div></div></section>'''
    return hero+body+cta(lang,'¿ALGUNA OTRA DUDA?' if es else 'ANOTHER QUESTION?','Conversemos.' if es else 'Let’s talk.','Estamos disponibles para hablar sobre tu espacio y el futuro de la red.' if es else 'We are available to talk about your venue and the future of the network.','Contáctanos' if es else 'Contact us')

def contact(lang):
    es = lang == 'es'
    hero = standard_hero(lang,'contact','CONTACTO' if es else 'CONTACT')
    labels = {'business':'Nombre del negocio' if es else 'Business name','person':'Persona de contacto' if es else 'Contact person','email':'Tu correo' if es else 'Your email','city':'Ciudad o zona' if es else 'City or area','type':'Tipo de espacio' if es else 'Venue type','message':'Cuéntanos un poco más' if es else 'Tell us more'}
    field = lambda key, typ='text', extra='': f'<div class="field"><label for="{key}">{labels[key]} <span aria-hidden="true">*</span></label><input id="{key}" name="{key}" type="{typ}" autocomplete="{extra}" required></div>'
    page = hero + f'''<section class="section"><div class="wrap contact-layout"><div class="contact-info reveal"><span class="eyebrow">{escape('DIRECTO Y SENCILLO' if es else 'DIRECT AND SIMPLE')}</span><h2>{escape('Estamos a un correo de distancia.' if es else 'We are one email away.')}</h2><p>{escape('¿Prefieres escribir directamente? Aquí tienes nuestra dirección. Puedes copiarla o abrir tu aplicación de correo.' if es else 'Prefer to write directly? Here is our address. Copy it or open your email app.')}</p><a class="email-address" href="mailto:{EMAIL}">{EMAIL}</a><div class="contact-actions"><button class="button button-outline" id="copyEmail" type="button" data-copied="{escape('Copiado' if es else 'Copied')}">{escape('Copiar dirección' if es else 'Copy address')}</button><a class="text-link" href="mailto:{EMAIL}">{escape('Abrir correo' if es else 'Open email app')} ↗</a></div><p class="copy-status" id="copyStatus" role="status" aria-live="polite"></p></div><form id="partnerForm" class="form-panel reveal"><span class="eyebrow">{escape('PRESENTA TU ESPACIO' if es else 'INTRODUCE YOUR VENUE')}</span><h2>{escape('Prepara tu mensaje.' if es else 'Prepare your message.')}</h2><p>{escape('Completa los datos y prepararemos un correo en tu aplicación. Revísalo y envíalo desde allí; este sitio no recoge ni guarda el formulario.' if es else 'Fill in the details and we will prepare an email in your email app. Review and send it there; this site does not collect or store the form.')}</p><div class="form-grid">{field('business',extra='organization')}{field('person',extra='name')}{field('email','email','email')}{field('city',extra='address-level2')}<div class="field field-full"><label for="type">{labels['type']} <span aria-hidden="true">*</span></label><select id="type" name="type" required><option value="">{escape('Selecciona una opción' if es else 'Choose an option')}</option>{''.join(f'<option>{escape(x)}</option>' for x in (['Gimnasio','Yoga / Pilates','Fuerza / entrenamiento funcional','Ciclismo','Boxeo / artes marciales','Danza','Movilidad / bienestar','Otro'] if es else ['Gym','Yoga / Pilates','Strength / functional training','Cycling','Boxing / martial arts','Dance','Mobility / wellness','Other']))}</select></div><div class="field field-full"><label for="message">{labels['message']}</label><textarea id="message" name="message" rows="4"></textarea></div></div><button class="button button-primary" type="submit">{escape('Preparar correo' if es else 'Prepare email')} <span aria-hidden="true">↗</span></button><p class="form-note">{escape('Después de preparar el mensaje, podrás revisarlo, copiarlo o abrirlo en tu aplicación de correo.' if es else 'After preparing the message, you can review it, copy it or open it in your email app.')}</p></form></div></section>'''

    draft = f'''<div class="draft-panel" id="emailDraft" hidden><h3 tabindex="-1" id="draftTitle">{escape('Revisa tu correo' if es else 'Review your email')}</h3><p>{escape('El mensaje aún no se ha enviado.' if es else 'This message has not been sent yet.')}</p><p><strong>{escape('Para' if es else 'To')}:</strong> {EMAIL}</p><label for="draftSubject">{escape('Asunto' if es else 'Subject')}</label><input id="draftSubject" readonly><label for="draftBody">{escape('Mensaje' if es else 'Message')}</label><textarea id="draftBody" readonly rows="10"></textarea><div class="draft-actions"><a class="button button-primary" id="openDraft" href="mailto:{EMAIL}">{escape('Abrir aplicación de correo' if es else 'Open email app')} <span aria-hidden="true">↗</span></a><button class="button button-outline" id="copyDraft" type="button">{escape('Copiar mensaje' if es else 'Copy message')}</button></div><p id="draftStatus" role="status" aria-live="polite"></p></div>'''
    return page.replace('</form>', draft + '</form>')

BODY = {'index':home, 'partners':partners, 'why-us':why_us, 'faq':faq, 'contact':contact}

def render(lang, page):
    t = COPY[lang]
    depth = '' if lang == 'es' else '../'
    other = 'en' if lang == 'es' else 'es'
    other_href = f'en/{page}.html' if lang == 'es' else f'../{page}.html'
    canonical = f'https://circuitoactivo.com/{"en/" if lang=="en" else ""}{"" if page=="index" else page+".html"}'
    nav = ''.join(f'<a href="{link(lang,p)}" {"aria-current=\"page\"" if p==page else ""}>{escape(label)}</a>' for p,label in zip(PAGES,t['nav']))
    title, desc = t['pages'][page]
    intro = f'''<div class="intro" aria-hidden="true"><div class="intro-symbol"><img src="{depth}circuito-activo-logo.png" alt=""></div><span>CIRCUITO ACTIVO</span></div>''' if page=='index' else ''
    return f'''<!doctype html><html lang="{lang}" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#f4f0e8"><title>{escape(title)} | Circuito Activo</title><meta name="description" content="{escape(desc)}"><link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="es" href="https://circuitoactivo.com/{'' if page=='index' else page+'.html'}"><link rel="alternate" hreflang="en" href="https://circuitoactivo.com/en/{'' if page=='index' else page+'.html'}"><link rel="icon" href="{depth}favicon.ico" sizes="any"><link rel="icon" type="image/png" href="{depth}favicon.png"><link rel="apple-touch-icon" href="{depth}favicon.png"><link rel="stylesheet" href="{depth}styles.css"><script>try{{document.documentElement.dataset.theme=localStorage.getItem('ca-theme')||'light'}}catch(e){{}}</script><script defer src="{depth}vendor/gsap.min.js"></script><script defer src="{depth}script.js"></script></head><body data-page="{page}"><a class="skip-link" href="#main">{escape(t['skip'])}</a>{intro}<header class="site-header"><div class="wrap header-inner"><a class="brand" href="index.html" aria-label="Circuito Activo · {escape(t['nav'][0])}"><img src="{depth}circuito-activo-logo.png" alt="" width="40" height="40"><span>CIRCUITO<br>ACTIVO</span></a><nav class="desktop-nav" aria-label="{escape(t['menu'])}">{nav}</nav><div class="header-actions"><a class="language-switch" href="{other_href}" hreflang="{other}" lang="{other}">{escape(t['language'])}</a><button class="theme-toggle" type="button" aria-label="{escape(t['theme'])}" aria-pressed="false"><span class="theme-icon" aria-hidden="true">◐</span></button><button class="menu-toggle" type="button" aria-controls="mobileMenu" aria-expanded="false" aria-label="{escape(t['menu'])}"><span></span><span></span></button></div></div><nav class="mobile-menu" id="mobileMenu" aria-label="{escape(t['menu'])}" hidden>{nav}</nav></header><main id="main">{BODY[page](lang)}</main><footer class="site-footer"><div class="wrap footer-main"><div><a class="footer-brand" href="index.html">CIRCUITO ACTIVO <span>↗</span></a><p>{escape(t['footer'])}</p></div><nav aria-label="{escape(t['menu'])}">{nav}</nav></div><div class="wrap footer-bottom"><span>© <span id="year">2026</span> Circuito Activo</span><a href="mailto:{EMAIL}">{EMAIL}</a><span>{escape('Hecho para moverse.' if lang=='es' else 'Made to move.')}</span></div></footer></body></html>'''

for lang in COPY:
    dest = ROOT if lang == 'es' else ROOT/'en'
    dest.mkdir(parents=True,exist_ok=True)
    for page in PAGES:
        (dest/f'{page}.html').write_text(render(lang,page),encoding='utf-8')

print('Generated 10 static pages')
