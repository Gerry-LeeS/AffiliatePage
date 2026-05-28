import os

GA4 = """
\t\t<!-- Google tag (gtag.js) -->
\t\t<script async src="https://www.googletagmanager.com/gtag/js?id=G-KQ4H2E63YD"></script>
\t\t<script>
\t\t  window.dataLayer = window.dataLayer || [];
\t\t  function gtag(){dataLayer.push(arguments);}
\t\t  gtag('js', new Date());
\t\t  gtag('config', 'G-KQ4H2E63YD');
\t\t</script>"""

NAV_REVIEW = """<nav class="nav" id="nav">
\t\t\t<div class="nav-container">
\t\t\t\t<div class="nav-logo">
\t\t\t\t\t<img src="/images/casinofavicon.png" alt="CSR Logo" class="site-logo" width="32" height="32" />
\t\t\t\t\t<span class="logo-text">Casino Site Reviews</span>
\t\t\t\t</div>
\t\t\t\t<ul class="nav-links">
\t\t\t\t\t<li><a href="/" class="nav-link">Home</a></li>
\t\t\t\t\t<li><a href="/exclusive" class="nav-link">Exclusive</a></li>
\t\t\t\t\t<li><a href="/search" class="nav-link">Search</a></li>
\t\t\t\t\t<li><a href="/calculator" class="nav-link">Calculator</a></li>
\t\t\t\t\t<li class="nav-dropdown">
\t\t\t\t\t\t<button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">
\t\t\t\t\t\t\tRankings <span class="nav-dropdown-chevron">&#9662;</span>
\t\t\t\t\t\t</button>
\t\t\t\t\t\t<ul class="nav-dropdown-menu" role="menu">
\t\t\t\t\t\t\t<li><a href="/paypal-casinos" role="menuitem">PayPal Casinos</a></li>
\t\t\t\t\t\t\t<li><a href="/no-wagering-casinos" role="menuitem">No Wagering Casinos</a></li>
\t\t\t\t\t\t\t<li><a href="/fastest-withdrawal-casinos" role="menuitem">Fastest Withdrawals</a></li>
\t\t\t\t\t\t\t<li><a href="/new-casinos" role="menuitem">New Casinos 2026</a></li>
\t\t\t\t\t\t\t<li><a href="/best-casino-bonuses" role="menuitem">Best Casino Bonuses</a></li>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</li>
\t\t\t\t</ul>
\t\t\t\t<button class="theme-toggle desktop-theme-toggle" id="themeToggle" aria-label="Toggle theme"><span class="theme-icon">☀</span></button>
\t\t\t\t<button class="hamburger" id="hamburger" aria-label="Toggle menu">
\t\t\t\t\t<span class="hamburger-line"></span>
\t\t\t\t\t<span class="hamburger-line"></span>
\t\t\t\t\t<span class="hamburger-line"></span>
\t\t\t\t</button>
\t\t\t</div>
\t\t\t<div class="mobile-menu" id="mobileMenu">
\t\t\t\t<ul class="mobile-menu-links">
\t\t\t\t\t<li><a href="/" class="mobile-nav-link">Home</a></li>
\t\t\t\t\t<li><a href="/exclusive" class="mobile-nav-link">Exclusive</a></li>
\t\t\t\t\t<li><a href="/search" class="mobile-nav-link">Search</a></li>
\t\t\t\t\t<li><a href="/calculator" class="mobile-nav-link">Calculator</a></li>
\t\t\t\t\t<li class="mobile-guides-toggle">
\t\t\t\t\t\t<button class="mobile-guides-btn">Rankings <span class="mobile-guides-chevron">&#9662;</span></button>
\t\t\t\t\t\t<ul class="mobile-guides-menu">
\t\t\t\t\t\t\t<li><a href="/paypal-casinos" class="mobile-nav-link">PayPal Casinos</a></li>
\t\t\t\t\t\t\t<li><a href="/no-wagering-casinos" class="mobile-nav-link">No Wagering Casinos</a></li>
\t\t\t\t\t\t\t<li><a href="/fastest-withdrawal-casinos" class="mobile-nav-link">Fastest Withdrawals</a></li>
\t\t\t\t\t\t\t<li><a href="/new-casinos" class="mobile-nav-link">New Casinos 2026</a></li>
\t\t\t\t\t\t\t<li><a href="/best-casino-bonuses" class="mobile-nav-link">Best Casino Bonuses</a></li>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</li>
\t\t\t\t\t<li class="mobile-theme-item">
\t\t\t\t\t\t<button class="mobile-theme-toggle" id="mobileThemeToggle" aria-label="Toggle theme">
\t\t\t\t\t\t\t<span class="theme-icon">☀</span>
\t\t\t\t\t\t\t<span class="theme-label">Dark Mode</span>
\t\t\t\t\t\t</button>
\t\t\t\t\t</li>
\t\t\t\t</ul>
\t\t\t</div>
\t\t</nav>"""

def sister_card(name, logo, bg, stars_n, bonus, review_slug, affiliate_url, tc, note=''):
    STAR_FULL = '<svg viewBox="0 0 24 24" width="14" height="14" fill="#D4AF37"><path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/></svg>'
    STAR_EMPTY = '<svg viewBox="0 0 24 24" width="14" height="14" fill="rgba(212,175,55,0.2)"><path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/></svg>'
    full = int(stars_n)
    stars_html = STAR_FULL * full + STAR_EMPTY * (5 - full)
    note_html = f'\n\t\t\t\t\t\t\t<p style="font-size:0.8rem;color:var(--text-muted);margin:0.3rem 0 0;">{note}</p>' if note else ''
    return f"""
\t\t\t\t\t<article class="sc-card">
\t\t\t\t\t\t<div class="sc-main">
\t\t\t\t\t\t\t<div class="sc-logo" style="background:{bg};">
\t\t\t\t\t\t\t\t<img src="/images/casinologos/{logo}" alt="{name}" loading="lazy" width="52" height="52" onerror="this.parentElement.innerHTML='\U0001f3b0'" />
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="sc-info">
\t\t\t\t\t\t\t\t<div class="sc-name-row"><a href="/reviews/{review_slug}" style="text-decoration:none;"><span class="sc-name">{name}</span></a></div>
\t\t\t\t\t\t\t\t<div class="sc-stars" aria-label="{stars_n} out of 5 stars">{stars_html}</div>
\t\t\t\t\t\t\t\t<div class="sc-bonus">\U0001f381 {bonus}</div>{note_html}
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="sc-actions">
\t\t\t\t\t\t\t\t<a href="/reviews/{review_slug}" class="sc-btn-review">Full Review</a>
\t\t\t\t\t\t\t\t<a href="{affiliate_url}" rel="noopener sponsored" class="sc-btn-claim">Visit Casino</a>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t\t<div class="sc-tc">
\t\t\t\t\t\t\t<span class="sc-tc-icon">&#x2139;</span>
\t\t\t\t\t\t\t<p>{tc} <a href="https://www.begambleaware.org" target="_blank" rel="noopener">BeGambleAware.org</a></p>
\t\t\t\t\t\t</div>
\t\t\t\t\t</article>"""

def sister_row(name, detail):
    return f"""
\t\t\t\t\t<tr>
\t\t\t\t\t\t<td style="padding:0.6rem 0.8rem;border:1px solid var(--border);font-weight:600;">{name}</td>
\t\t\t\t\t\t<td style="padding:0.6rem 0.8rem;border:1px solid var(--border);">{detail}</td>
\t\t\t\t\t</tr>"""

def build_sister_page(slug, casino_name, operator, ukgc_account, founded, platform,
                      sister_sites_list, main_review_slug, main_affiliate_url,
                      logo_file, logo_bg, stars_n, bonus_text, tc_text,
                      intro_paras, faq_items_html, faq_schema_items, comparison_casinos=''):
    """
    sister_sites_list: list of (name, note) tuples
    """
    sisters_rows = ''
    for n, note in sister_sites_list:
        sisters_rows += sister_row(n, note)

    faq_schema_str = ''
    for i, (q, a) in enumerate(faq_schema_items):
        faq_schema_str += f"""
    {{
      "@type": "Question",
      "name": "{q}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{a}"
      }}
    }}"""
        if i < len(faq_schema_items) - 1:
            faq_schema_str += ','

    intro_html = ''.join(f'\n\t\t\t\t<p style="color:var(--text-secondary);line-height:1.8;margin-bottom:1rem;">{p}</p>' for p in intro_paras)
    verify_url = 'https://register.gamblingcommission.gov.uk/app/public-register/businesses'

    return f"""<!DOCTYPE html>
<html lang="en">
\t<head>
\t\t<meta charset="UTF-8" />{GA4}
\t\t<meta name="theme-color" content="#d4af37" />
\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0" />

\t\t<!-- SEO Meta Tags -->
\t\t<title>{casino_name} Sister Sites 2026 — Same Operator, Different Brands | Casino Site Reviews</title>
\t\t<meta name="description" content="Find all {casino_name} sister sites 2026. Every casino operated by {operator} under the same UKGC licence. Reviewed and ranked." />
\t\t<link rel="canonical" href="https://casinositereviews.co.uk/reviews/{slug}" />
\t\t<meta name="robots" content="index, follow" />

\t\t<!-- Open Graph -->
\t\t<meta property="og:title" content="{casino_name} Sister Sites 2026 — Casinos on the Same Platform" />
\t\t<meta property="og:description" content="All {casino_name} sister sites operated by {operator}. Same UKGC licence, different brands." />
\t\t<meta property="og:url" content="https://casinositereviews.co.uk/reviews/{slug}" />
\t\t<meta property="og:type" content="article" />
\t\t<meta property="og:image" content="https://casinositereviews.co.uk/images/casinofavicon.png" />
\t\t<meta property="og:site_name" content="Casino Site Reviews" />

\t\t<!-- Twitter Card -->
\t\t<meta name="twitter:card" content="summary" />
\t\t<meta name="twitter:title" content="{casino_name} Sister Sites 2026" />
\t\t<meta name="twitter:description" content="All {casino_name} sister sites operated by {operator}. Same UKGC licence." />
\t\t<meta name="twitter:image" content="https://casinositereviews.co.uk/images/casinofavicon.png" />

\t\t<!-- Schema: FAQPage -->
\t\t<script type="application/ld+json">
\t\t{{
\t\t  "@context": "https://schema.org",
\t\t  "@type": "FAQPage",
\t\t  "mainEntity": [{faq_schema_str}
\t\t  ]
\t\t}}
\t\t</script>

\t\t<!-- Schema: BreadcrumbList -->
\t\t<script type="application/ld+json">
\t\t{{
\t\t  "@context": "https://schema.org",
\t\t  "@type": "BreadcrumbList",
\t\t  "itemListElement": [
\t\t    {{"@type":"ListItem","position":1,"name":"Home","item":"https://casinositereviews.co.uk/"}},
\t\t    {{"@type":"ListItem","position":2,"name":"Reviews","item":"https://casinositereviews.co.uk/search"}},
\t\t    {{"@type":"ListItem","position":3,"name":"{casino_name} Sister Sites","item":"https://casinositereviews.co.uk/reviews/{slug}"}}
\t\t  ]
\t\t}}
\t\t</script>

\t\t<!-- Styles & Fonts -->
\t\t<link rel="preconnect" href="https://fonts.googleapis.com" />
\t\t<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
\t\t<link rel="stylesheet" href="../style.css" />
\t\t<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800;900&family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet" />
\t\t<link rel="apple-touch-icon" href="/images/casinofavicon.png" />
\t\t<link rel="icon" href="/images/casinofavicon.png" type="image/x-icon" />
\t</head>
\t<body>
\t\t<a href="#main" class="skip-link">Skip to main content</a>
\t\t<script>
\t\t\tconst savedTheme = localStorage.getItem('theme') || 'dark';
\t\t\tif (savedTheme === 'light') {{ document.body.classList.add('light-theme'); }}
\t\t</script>

\t\t<!-- Navigation -->
\t\t{NAV_REVIEW}

\t\t<!-- Hero -->
\t\t<section id="main" class="review-hero">
\t\t\t<div class="container">
\t\t\t\t<div class="review-hero-content">
\t\t\t\t\t<div class="review-logo-section">
\t\t\t\t\t\t<div class="review-logo-container" style="background:{logo_bg}">
\t\t\t\t\t\t\t<img src="/images/casinologos/{logo_file}" alt="{casino_name}" width="180" height="120" onerror="this.parentElement.innerHTML='\U0001f3b0'" />
\t\t\t\t\t\t</div>
\t\t\t\t\t\t<div class="review-title-group">
\t\t\t\t\t\t\t<h1>{casino_name} Sister Sites 2026</h1>
\t\t\t\t\t\t\t<p class="last-updated" style="font-size:0.8rem;color:var(--text-muted);margin:0.25rem 0 0;">Last updated: May 2026</p>
\t\t\t\t\t\t\t<a href="/jose-fontana" class="author-badge">
\t\t\t\t\t\t\t\t<span class="author-avatar">JF</span>
\t\t\t\t\t\t\t\t<span class="author-info">
\t\t\t\t\t\t\t\t\t<span class="author-name">Jose Fontana</span>
\t\t\t\t\t\t\t\t\t<span class="author-title">Casino Analyst</span>
\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t\t<a href="{main_affiliate_url}" rel="noopener sponsored" class="review-cta-btn">Visit {casino_name}<span class="cta-arrow">&rarr;</span></a>
\t\t\t\t</div>
\t\t\t</div>
\t\t</section>

\t\t<!-- Main content -->
\t\t<main class="review-content">
\t\t\t<div class="container">

\t\t\t\t<!-- Breadcrumbs -->
\t\t\t\t<nav aria-label="Breadcrumb" style="margin-bottom:1rem;padding-top:1.5rem;">
\t\t\t\t\t<ol style="display:flex;gap:0.5rem;list-style:none;padding:0;margin:0;font-size:0.82rem;color:var(--text-muted);">
\t\t\t\t\t\t<li><a href="/" style="color:var(--gold);text-decoration:none;">Home</a></li>
\t\t\t\t\t\t<li style="opacity:0.5;">&#x203a;</li>
\t\t\t\t\t\t<li><a href="/search" style="color:var(--gold);text-decoration:none;">Reviews</a></li>
\t\t\t\t\t\t<li style="opacity:0.5;">&#x203a;</li>
\t\t\t\t\t\t<li><a href="/reviews/{main_review_slug}" style="color:var(--gold);text-decoration:none;">{casino_name}</a></li>
\t\t\t\t\t\t<li style="opacity:0.5;">&#x203a;</li>
\t\t\t\t\t\t<li>Sister Sites</li>
\t\t\t\t\t</ol>
\t\t\t\t</nav>

\t\t\t\t<!-- Intro -->
\t\t\t\t<section class="review-section">
\t\t\t\t\t<div class="section-icon">🏢</div>
\t\t\t\t\t<h2>Who Operates {casino_name}?</h2>{intro_html}
\t\t\t\t</section>

\t\t\t\t<!-- Operator Table -->
\t\t\t\t<section class="review-section">
\t\t\t\t\t<div class="section-icon">📋</div>
\t\t\t\t\t<h2>Operator Details</h2>
\t\t\t\t\t<div style="overflow-x:auto;">
\t\t\t\t\t\t<table style="width:100%;border-collapse:collapse;font-size:0.88rem;line-height:1.6;">
\t\t\t\t\t\t\t<thead><tr style="background:var(--bg-secondary);">
\t\t\t\t\t\t\t\t<th style="padding:0.6rem 0.8rem;border:1px solid var(--border);text-align:left;">Detail</th>
\t\t\t\t\t\t\t\t<th style="padding:0.6rem 0.8rem;border:1px solid var(--border);text-align:left;">Information</th>
\t\t\t\t\t\t\t</tr></thead>
\t\t\t\t\t\t\t<tbody>
{sister_row('Operator', operator)}
{sister_row('UKGC Account', f'<a href="{verify_url}" rel="noopener noreferrer" target="_blank" style="color:var(--gold);">{ukgc_account}</a> — verify at UKGC register')}
{sister_row('Founded', founded)}
{sister_row('Platform', platform)}
\t\t\t\t\t\t\t</tbody>
\t\t\t\t\t\t</table>
\t\t\t\t\t</div>
\t\t\t\t</section>

\t\t\t\t<!-- Sister Sites List -->
\t\t\t\t<section class="review-section">
\t\t\t\t\t<div class="section-icon">🔗</div>
\t\t\t\t\t<h2>{casino_name} Sister Casinos List</h2>
\t\t\t\t\t<p>The following casinos are operated by {operator} under the same UKGC licence as {casino_name}. They share the same technical infrastructure, game library and security standards. Bonuses, promotions and customer accounts are separate.</p>
\t\t\t\t\t<div style="overflow-x:auto;margin-top:1.25rem;">
\t\t\t\t\t\t<table style="width:100%;border-collapse:collapse;font-size:0.88rem;line-height:1.6;">
\t\t\t\t\t\t\t<thead><tr style="background:var(--bg-secondary);">
\t\t\t\t\t\t\t\t<th style="padding:0.6rem 0.8rem;border:1px solid var(--border);text-align:left;">Sister Casino</th>
\t\t\t\t\t\t\t\t<th style="padding:0.6rem 0.8rem;border:1px solid var(--border);text-align:left;">Notes</th>
\t\t\t\t\t\t\t</tr></thead>
\t\t\t\t\t\t\t<tbody>{sisters_rows}
\t\t\t\t\t\t\t</tbody>
\t\t\t\t\t\t</table>
\t\t\t\t\t</div>
\t\t\t\t</section>

\t\t\t\t<!-- What sister sites mean -->
\t\t\t\t<section class="review-section">
\t\t\t\t\t<div class="section-icon">💡</div>
\t\t\t\t\t<h2>What Does a Sister Casino Mean for Players?</h2>
\t\t\t\t\t<p>Sister casinos share the same operator and UKGC licence. In practical terms, this means:</p>
\t\t\t\t\t<ul style="color:var(--text-secondary);line-height:2;padding-left:1.25rem;margin:0.75rem 0;">
\t\t\t\t\t\t<li><strong>Same responsible gambling tools</strong> — deposit limits, reality checks, self-exclusion and GAMSTOP integration apply across all sister sites.</li>
\t\t\t\t\t\t<li><strong>GAMSTOP self-exclusion applies to all</strong> — if you self-exclude via GAMSTOP, you will be blocked from {casino_name} and all sister casinos simultaneously.</li>
\t\t\t\t\t\t<li><strong>Separate bonuses</strong> — sister casinos treat you as a new customer separately. You can claim the welcome bonus at each site individually, subject to their T&Cs.</li>
\t\t\t\t\t\t<li><strong>Separate accounts</strong> — your login, wallet and history are different at each casino. You cannot transfer funds between sister sites.</li>
\t\t\t\t\t\t<li><strong>Same game library</strong> — sister sites under the same platform typically share the same software providers and most games, though lobby curation may differ.</li>
\t\t\t\t\t</ul>
\t\t\t\t</section>

\t\t\t\t<!-- View main review -->
\t\t\t\t<section class="review-section">
\t\t\t\t\t<div class="section-icon">⭐</div>
\t\t\t\t\t<h2>Read the Full {casino_name} Review</h2>
\t\t\t\t\t<p>For an in-depth look at {casino_name} — including welcome bonus breakdown, game library, payment methods, customer support and our overall rating — see our full review:</p>
\t\t\t\t\t<a href="/reviews/{main_review_slug}" style="display:inline-flex;align-items:center;gap:0.5rem;margin-top:1rem;padding:0.75rem 1.5rem;background:var(--gold);color:#000;border-radius:8px;font-weight:700;text-decoration:none;">Read {casino_name} Review &rarr;</a>
\t\t\t\t</section>

\t\t\t\t<!-- FAQ -->
\t\t\t\t<section class="review-section" id="faq">
\t\t\t\t\t<div class="section-icon">❓</div>
\t\t\t\t\t<h2>Frequently Asked Questions</h2>
\t\t\t\t\t<div class="faq-list" style="margin-top:1.5rem;">{faq_items_html}
\t\t\t\t\t</div>
\t\t\t\t</section>

\t\t\t\t<!-- CTA -->
\t\t\t\t<section class="review-final-cta">
\t\t\t\t\t<h2>Play at {casino_name}</h2>
\t\t\t\t\t<p>Independently reviewed, UKGC licensed, and ranked by Casino Site Reviews.</p>
\t\t\t\t\t<a href="{main_affiliate_url}" rel="noopener sponsored" class="review-cta-btn large">Visit {casino_name} <span class="cta-arrow">&rarr;</span></a>
\t\t\t\t\t<p class="disclaimer">18+. New customers only. T&Cs apply. BeGambleAware.org</p>
\t\t\t\t</section>

\t\t\t</div>
\t\t</main>

\t\t<!-- Footer -->
\t\t<footer style="padding:2rem 0;background:var(--bg-primary);border-top:1px solid var(--border);">
\t\t\t<div class="container">
\t\t\t\t<div style="display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:center;margin-bottom:1.5rem;">
\t\t\t\t\t<a href="/" style="color:var(--text-muted);font-size:0.82rem;text-decoration:none;">Home</a>
\t\t\t\t\t<a href="/about" style="color:var(--text-muted);font-size:0.82rem;text-decoration:none;">About</a>
\t\t\t\t\t<a href="/responsible-gambling" style="color:var(--text-muted);font-size:0.82rem;text-decoration:none;">Responsible Gambling</a>
\t\t\t\t\t<a href="/affiliate-disclosure" style="color:var(--text-muted);font-size:0.82rem;text-decoration:none;">Affiliate Disclosure</a>
\t\t\t\t\t<a href="/privacy" style="color:var(--text-muted);font-size:0.82rem;text-decoration:none;">Privacy Policy</a>
\t\t\t\t</div>
\t\t\t\t<p style="text-align:center;font-size:0.78rem;color:var(--text-muted);line-height:1.7;max-width:720px;margin:0 auto 1rem;">
\t\t\t\t\t18+ Only. Gambling can be addictive. Visit <a href="https://www.begambleaware.org" rel="noopener noreferrer" target="_blank" style="color:var(--gold);">BeGambleAware.org</a> or call <strong>0808 8020 133</strong> (free, 24/7).
\t\t\t\t</p>
\t\t\t\t<p style="text-align:center;font-size:0.75rem;color:var(--text-muted);opacity:0.6;">&copy; 2026 Casino Site Reviews. Independent reviews.</p>
\t\t\t</div>
\t\t</footer>
\t\t<script src="../script.js" defer></script>
\t\t<script>
\t\t\tfunction toggleFaq(btn) {{
\t\t\t\tconst answer = btn.nextElementSibling;
\t\t\t\tconst isOpen = !answer.hidden;
\t\t\t\tanswer.hidden = isOpen;
\t\t\t\tbtn.setAttribute('aria-expanded', !isOpen);
\t\t\t\tbtn.querySelector('.faq-icon').textContent = isOpen ? '+' : '−';
\t\t\t}}
\t\t</script>
\t</body>
</html>"""

def faq(q, a):
    return f"""
\t\t\t\t\t\t<div class="faq-item">
\t\t\t\t\t\t\t<button class="faq-question" onclick="toggleFaq(this)" aria-expanded="false">
\t\t\t\t\t\t\t\t{q}
\t\t\t\t\t\t\t\t<span class="faq-icon">+</span>
\t\t\t\t\t\t\t</button>
\t\t\t\t\t\t\t<div class="faq-answer" hidden>
\t\t\t\t\t\t\t\t<p>{a}</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>"""

# ────────────────────────────────────────────────────────
# Define each casino's sister site data
# ────────────────────────────────────────────────────────

casinos = [
    # (slug, casino_name, operator, ukgc, founded, platform,
    #  [(sister_name, note), ...],
    #  main_review_slug, affiliate_url, logo, logo_bg, stars, bonus, tc,
    #  intro_paras, faq_items_html, faq_schema)
    dict(
        slug='lunacasino-sister-sites',
        casino_name='Luna Casino',
        operator='SkillOnNet Ltd',
        ukgc='000-038908',
        founded='2018',
        platform='SkillOnNet (shared platform)',
        sisters=[
            ('PlayOJO', 'Also reviewed by Casino Site Reviews — 50 free spins, 0x wagering'),
            ('Swift Casino', 'Also reviewed by Casino Site Reviews — same SkillOnNet platform'),
            ('Slotsmillion', 'Large slots catalogue, 3,000+ games'),
            ('Videoslots', 'One of the largest slots libraries globally'),
            ('Premier Casino', 'Premium gaming experience, SkillOnNet brand'),
            ('Casino Room', 'Established SkillOnNet brand operating since 2005'),
            ('Dream Vegas', 'Premium live casino focus, SkillOnNet platform'),
        ],
        main_review_slug='lunacasino',
        affiliate_url='https://ads.galaxyaffiliates.com/redirect.aspx?mid=5366&sid=15149&cid=&pid=&affid=8275',
        logo='luna.png', logo_bg='#000', stars=5,
        bonus='100% up to £50 + 50 Free Spins. Code: LUNA',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'Luna Casino is operated by <strong>SkillOnNet Ltd</strong>, one of the largest casino software and operating groups in Europe. Founded in 2006, SkillOnNet holds a UK Gambling Commission (UKGC) remote operating licence (Account 000-038908) and operates a large portfolio of brands across multiple markets.',
            'Because SkillOnNet operates multiple casino brands from a shared technical platform, Luna Casino has numerous sister sites. All share the same game library infrastructure, responsible gambling tools and UKGC compliance framework — though each brand is marketed separately with its own bonus structure, loyalty programme and customer interface.',
            'If you are self-excluded from Luna Casino (or any SkillOnNet casino), your exclusion applies across all SkillOnNet-operated brands simultaneously.',
        ],
        faq_items=''.join([
            faq('What are Luna Casino sister sites?', 'Luna Casino sister sites are other casinos operated by SkillOnNet Ltd under the same UKGC licence. They share the same technical platform and game library. Sister sites include PlayOJO, Swift Casino, Slotsmillion and others.'),
            faq('Can I use my Luna Casino bonus at a sister site?', 'No. Bonuses are separate at each casino. You can claim the individual welcome bonus at each sister site, but your Luna Casino account, wallet and bonus history are only at Luna Casino.'),
            faq('Does self-exclusion apply to Luna Casino sister sites?', 'Yes. If you self-exclude via GAMSTOP, the exclusion applies to Luna Casino and all UKGC licensed operators including SkillOnNet sister sites simultaneously. For operator-level self-exclusion, contact SkillOnNet\'s customer support to exclude from all their brands.'),
        ]),
        faq_schema=[
            ('What are Luna Casino sister sites?', 'Luna Casino sister sites are other casinos operated by SkillOnNet Ltd. They share the same UKGC licence and platform. Key sister sites include PlayOJO, Swift Casino and Slotsmillion.'),
            ('Is PlayOJO a sister site of Luna Casino?', 'Yes. Both PlayOJO and Luna Casino are operated by SkillOnNet Ltd under the same UKGC licence (Account 000-038908).'),
        ],
    ),
    dict(
        slug='playojo-sister-sites',
        casino_name='PlayOJO',
        operator='SkillOnNet Ltd',
        ukgc='000-038908',
        founded='2017',
        platform='SkillOnNet (shared platform)',
        sisters=[
            ('Luna Casino', 'Reviewed by Casino Site Reviews — 5/5 rating, exclusive welcome offer'),
            ('Swift Casino', 'Also reviewed — fast-loading mobile-first platform'),
            ('Slotsmillion', 'Large international slots brand, 3,000+ games'),
            ('Videoslots', 'One of the world\'s largest online slot sites'),
            ('Casino Room', 'Established brand since 2005, SkillOnNet platform'),
            ('Dream Vegas', 'Premium live casino and slots, same operator'),
            ('Premier Casino', 'UK-focused premium casino brand'),
        ],
        main_review_slug='playojo',
        affiliate_url='https://site.gotoplayojo.com/redirect.aspx?pid=23&bid=2399',
        logo='playojo.png', logo_bg='#17003a', stars=5,
        bonus='50 Free Spins, 0x Wagering',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'PlayOJO is operated by <strong>SkillOnNet Ltd</strong>, a major European casino operator founded in 2006. SkillOnNet holds UKGC Account 000-038908 and operates numerous casino brands across global markets from a shared platform.',
            'PlayOJO launched in 2017 and quickly became one of the most recognisable UK casino brands through its 0x wagering promise — winnings from free spins are always paid as cash. As part of the SkillOnNet group, PlayOJO shares infrastructure with sister brands including Luna Casino and Swift Casino.',
            'Players who use GAMSTOP self-exclusion will be excluded from PlayOJO and all SkillOnNet brands simultaneously. Deposit limits and session controls at PlayOJO apply only to your PlayOJO account.',
        ],
        faq_items=''.join([
            faq('What are PlayOJO sister sites?', 'PlayOJO sister sites are other SkillOnNet-operated casinos sharing the same UKGC licence. They include Luna Casino, Swift Casino, Slotsmillion and Videoslots among others.'),
            faq('Is PlayOJO the same as Luna Casino?', 'No — they are separate brands with different designs, promotions and account systems, but both are operated by SkillOnNet Ltd under the same UKGC licence. You need separate accounts at each.'),
        ]),
        faq_schema=[
            ('What are PlayOJO sister sites?', 'PlayOJO sister sites include Luna Casino, Swift Casino, Slotsmillion and Videoslots — all operated by SkillOnNet Ltd under UKGC Account 000-038908.'),
            ('Does PlayOJO own Luna Casino?', 'Both PlayOJO and Luna Casino are owned and operated by the same parent company, SkillOnNet Ltd. They are sister casinos sharing the same UKGC licence.'),
        ],
    ),
    dict(
        slug='boylecasino-sister-sites',
        casino_name='Boyle Casino',
        operator='BoyleSports (GB) Limited',
        ukgc='000-039275',
        founded='2000',
        platform='BoyleSports proprietary platform',
        sisters=[
            ('BoyleSports Sportsbook', 'The parent brand — one of Ireland\'s largest independent bookmakers with 390+ shops'),
            ('Boyle Bingo', 'Bingo-focused brand within the BoyleSports group'),
            ('Boyle Vegas', 'Slots-focused UK casino brand from the same group'),
        ],
        main_review_slug='boylecasino',
        affiliate_url='https://promo.boylesports.com/gaming/promo/game8?btag=54248|0f036f7746684ebb9a8e6752ee0e068a',
        logo='boyle_square.png', logo_bg='#fff', stars=5,
        bonus='100 Wager-Free Free Spins',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'Boyle Casino is operated by <strong>BoyleSports (GB) Limited</strong>, the UK arm of BoyleSports — one of Ireland\'s largest privately-owned bookmakers. Founded in 1982, BoyleSports has grown to over 390 betting shops across Ireland and the UK. The online casino launched alongside their digital expansion.',
            'Unlike the large multi-brand SkillOnNet group, BoyleSports operates a smaller, tightly focused portfolio. Boyle Casino sits within the BoyleSports online group alongside their sportsbook. The same UKGC licence covers all BoyleSports online products.',
            'The relatively small sister site footprint is actually a positive for players — BoyleSports is focused on quality over quantity, and the Boyle Casino brand benefits from the group\'s extensive operational experience and financial stability.',
        ],
        faq_items=''.join([
            faq('What are Boyle Casino sister sites?', 'Boyle Casino\'s sister sites include Boyle Bingo and Boyle Vegas, all operated by BoyleSports (GB) Limited. The group is smaller than multi-brand operators, reflecting BoyleSports\'s focus on their core brands.'),
            faq('Is Boyle Casino related to BoyleSports?', 'Yes. Boyle Casino is the casino brand of BoyleSports — one of Ireland\'s largest independent bookmakers. They share the same operator, UKGC licence and responsible gambling infrastructure.'),
        ]),
        faq_schema=[
            ('What are Boyle Casino sister sites?', 'Boyle Casino sister sites include Boyle Vegas and Boyle Bingo — all operated by BoyleSports (GB) Limited under UKGC Account 000-039275.'),
            ('Is Boyle Casino owned by BoyleSports?', 'Yes. Boyle Casino is operated by BoyleSports (GB) Limited, the UK entity of Irish bookmaking giant BoyleSports.'),
        ],
    ),
    dict(
        slug='swiftcasino-sister-sites',
        casino_name='Swift Casino',
        operator='SkillOnNet Ltd',
        ukgc='000-038908',
        founded='2014',
        platform='SkillOnNet (shared platform)',
        sisters=[
            ('Luna Casino', 'Reviewed by Casino Site Reviews — 5/5, strong welcome offer'),
            ('PlayOJO', 'Reviewed by Casino Site Reviews — 0x wagering free spins'),
            ('Slotsmillion', 'Large international slots brand, 3,000+ games'),
            ('Videoslots', 'One of the world\'s largest online slot sites'),
            ('Casino Room', 'Established brand since 2005'),
            ('Dream Vegas', 'Premium live casino brand'),
        ],
        main_review_slug='swiftcasino',
        affiliate_url='https://games.swiftcasino.com/redirect.aspx?pid=130&bid=2339',
        logo='swift.png', logo_bg='#002244', stars=4,
        bonus='Welcome Offer — Fast Mobile Experience',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'Swift Casino is operated by <strong>SkillOnNet Ltd</strong>, the same operator as Luna Casino and PlayOJO. SkillOnNet holds UKGC Account 000-038908 and is one of Europe\'s largest multi-brand casino operators.',
            'Swift Casino shares the same technical infrastructure and game library as all SkillOnNet brands. The platform is known for fast-loading games, which is reflected in the Swift Casino brand identity. The casino shares games from the same providers used across the SkillOnNet network including Evolution Gaming (live casino), Pragmatic Play, NetEnt and BTG.',
        ],
        faq_items=''.join([
            faq('What are Swift Casino sister sites?', 'Swift Casino sister sites include Luna Casino, PlayOJO, Slotsmillion and Videoslots — all operated by SkillOnNet Ltd under UKGC Account 000-038908.'),
            faq('Is Swift Casino the same as PlayOJO?', 'No. Swift Casino and PlayOJO are separate brands with different designs and bonus structures, but both are operated by SkillOnNet Ltd and share the same UKGC licence.'),
        ]),
        faq_schema=[
            ('What are Swift Casino sister sites?', 'Swift Casino\'s sister sites include Luna Casino, PlayOJO, Slotsmillion and other SkillOnNet-operated brands under UKGC Account 000-038908.'),
            ('Does Swift Casino share games with PlayOJO?', 'Yes. As SkillOnNet brands, Swift Casino and PlayOJO share the same underlying game library from providers including Evolution Gaming, Pragmatic Play and NetEnt.'),
        ],
    ),
    dict(
        slug='netbet-sister-sites',
        casino_name='NetBet',
        operator='NetBet Enterprises Ltd',
        ukgc='000-039571',
        founded='2001',
        platform='NetBet proprietary platform',
        sisters=[
            ('NetBet Sport', 'The sportsbook arm of NetBet — same operator, separate product'),
            ('NetBet Poker', 'Online poker offering from the NetBet group'),
            ('NetBet Vegas', 'Premium slots and live casino brand from NetBet group'),
            ('Circus Casino', 'European brand within the Circus group that owns NetBet'),
        ],
        main_review_slug='netbet',
        affiliate_url='https://netbet.livepartners.com/click.php?z=186827',
        logo='netbet.png', logo_bg='#101010', stars=5,
        bonus='100 Free Spins on £20 Wager',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'NetBet is operated by <strong>NetBet Enterprises Ltd</strong>, part of the Circus group — a Belgian land-based and online casino operator founded in 2001. NetBet holds its own UKGC licence (Account 000-039571) for UK customers.',
            'NetBet operates a focused portfolio compared to large multi-brand groups. The UK product includes NetBet Casino, NetBet Sport and NetBet Vegas — all under the same operational umbrella with shared responsible gambling infrastructure.',
            'As a long-established European operator with over 20 years of experience, NetBet\'s small sister site portfolio reflects a quality-over-quantity approach to brand management.',
        ],
        faq_items=''.join([
            faq('What are NetBet sister sites?', 'NetBet sister sites under UKGC licence include NetBet Sport, NetBet Vegas and NetBet Poker. The wider Circus group also operates Circus Casino in Europe.'),
            faq('Is NetBet a safe casino?', 'Yes. NetBet has held a UKGC licence since 2014 and has a 20+ year operational history. It is fully GamStop integrated and UKGC regulated.'),
        ]),
        faq_schema=[
            ('What are NetBet sister sites?', 'NetBet sister sites include NetBet Sport, NetBet Vegas and NetBet Poker — all under NetBet Enterprises Ltd with UKGC Account 000-039571.'),
            ('Who owns NetBet Casino?', 'NetBet is owned by the Circus Group, a Belgian gaming operator. In the UK, it operates under NetBet Enterprises Ltd with its own UKGC remote operating licence.'),
        ],
    ),
    dict(
        slug='bestodds-sister-sites',
        casino_name='Best Odds Casino',
        operator='BestOdds Ltd',
        ukgc='000-039920',
        founded='2019',
        platform='BestOdds Ltd proprietary',
        sisters=[
            ('BestOdds Sportsbook', 'The sports betting arm of the BestOdds brand — same operator'),
            ('Best Odds Bingo', 'Bingo brand within the BestOdds group'),
        ],
        main_review_slug='bestodds',
        affiliate_url='https://bolinkhub.com/redirect.aspx?pid=1',
        logo='bestodds.png', logo_bg='#1e1e2e', stars=4,
        bonus='Welcome Offer — See Latest Promotions',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'Best Odds Casino is operated by <strong>BestOdds Ltd</strong>, a UK-licensed online gambling operator. BestOdds Ltd holds UKGC Account 000-039920 and operates a small, focused portfolio of brands.',
            'Unlike large multi-brand operators, BestOdds Ltd keeps a tight brand focus. The casino and sportsbook operate as separate products but share the same UKGC licence and responsible gambling infrastructure.',
        ],
        faq_items=''.join([
            faq('What are Best Odds Casino sister sites?', 'Best Odds Casino sister sites include the BestOdds Sportsbook and Best Odds Bingo — all operated by BestOdds Ltd under UKGC Account 000-039920.'),
            faq('Is Best Odds Casino UKGC licensed?', 'Yes. Best Odds Casino operates under a UKGC licence held by BestOdds Ltd (Account 000-039920). You can verify this on the UKGC public register.'),
        ]),
        faq_schema=[
            ('What are Best Odds Casino sister sites?', 'Best Odds Casino sister sites are operated by BestOdds Ltd and include the BestOdds Sportsbook and related brands under UKGC Account 000-039920.'),
            ('Who operates Best Odds Casino?', 'Best Odds Casino is operated by BestOdds Ltd, a UKGC licensed UK gambling operator (Account 000-039920).'),
        ],
    ),
    dict(
        slug='kwiff-sister-sites',
        casino_name='Kwiff',
        operator='Kwiff Limited',
        ukgc='000-039062',
        founded='2015',
        platform='Kwiff proprietary platform',
        sisters=[
            ('Kwiff Sportsbook', 'The core sports betting product — same brand, same operator'),
        ],
        main_review_slug='kwiff',
        affiliate_url='https://promos.kwiff.com/casino/?btag=a_4001b_79c_&affid=1012&source=IncomeAccess&creative=79&campaign_id=&affiliate_id=1012&incomeaccess_click_id=a_4001b_79c_&campaign=a_4001b_79c_&siteid=4001',
        logo='kwiff.png', logo_bg='#7a2af4', stars=3,
        bonus='Wager £20 Get 200 Free Spins',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'Kwiff is operated by <strong>Kwiff Limited</strong>, an independent UK operator founded in 2015. Kwiff Limited is unusual in operating a single unified brand — Kwiff — rather than a portfolio of casino sites.',
            'Kwiff\'s casino and sportsbook exist as sections of the same platform rather than as separate sister brands. There are no sister casinos in the traditional sense — Kwiff Limited operates only the Kwiff brand, making it one of the more focused and independently-minded operators in the UK market.',
            'This means there is no benefit to creating multiple accounts across different Kwiff-branded sites — there are none. All gambling activity with Kwiff happens through one account on one platform.',
        ],
        faq_items=''.join([
            faq('Does Kwiff have any sister sites?', 'No. Kwiff Limited operates only the Kwiff brand. There are no sister casinos operating under the same UKGC licence. This makes Kwiff one of the few truly independent single-brand operators in the UK market.'),
            faq('Is Kwiff an independent casino?', 'Yes. Kwiff is operated by Kwiff Limited — an independent UK operator with no affiliation to larger casino groups. It operates only the Kwiff brand, covering both casino and sports betting.'),
        ]),
        faq_schema=[
            ('Does Kwiff have sister sites?', 'No. Kwiff Limited operates only the Kwiff brand with no sister casinos. It is an independent single-brand operator licensed by the UKGC (Account 000-039062).'),
            ('Who owns Kwiff Casino?', 'Kwiff is owned and operated by Kwiff Limited, an independent UK gambling company. It is not part of a larger casino group.'),
        ],
    ),
    dict(
        slug='bettom-sister-sites',
        casino_name='BetTOM',
        operator='BetTOM Ltd',
        ukgc='000-041223',
        founded='2021',
        platform='BetTOM Ltd proprietary',
        sisters=[
            ('BetTOM Sport', 'Sports betting brand from the same BetTOM Ltd operator'),
            ('TOM Bingo', 'Bingo brand within the BetTOM group'),
        ],
        main_review_slug='bettom',
        affiliate_url='https://tracker.bettomaffiliates.com/click.php?camp_id=2',
        logo='bettom.png', logo_bg='#1a1a2e', stars=4,
        bonus='Up to £50 Bonus + 10 Free Spins',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'BetTOM is operated by <strong>BetTOM Ltd</strong>, a UK-licensed gambling operator that launched in 2021. BetTOM Ltd operates a focused brand portfolio under UKGC Account 000-041223.',
            'As a newer operator, BetTOM Ltd operates a smaller portfolio than established multi-brand groups. The shared responsible gambling framework means GAMSTOP self-exclusion applies across all BetTOM Ltd brands simultaneously.',
        ],
        faq_items=''.join([
            faq('What are BetTOM sister sites?', 'BetTOM sister sites under the same UKGC licence include BetTOM Sport and TOM Bingo, operated by BetTOM Ltd.'),
            faq('Is BetTOM a new casino?', 'Yes. BetTOM launched in 2021 and holds a UKGC licence (Account 000-041223). It is a newer operator but fully regulated by the UK Gambling Commission.'),
        ]),
        faq_schema=[
            ('What are BetTOM sister sites?', 'BetTOM sister sites include BetTOM Sport and TOM Bingo, all operated by BetTOM Ltd under UKGC Account 000-041223.'),
            ('Who operates BetTOM Casino?', 'BetTOM Casino is operated by BetTOM Ltd, a UKGC licensed UK gambling operator (Account 000-041223) that launched in 2021.'),
        ],
    ),
    dict(
        slug='bresbet-sister-sites',
        casino_name='BresBet',
        operator='BresBet Ltd',
        ukgc='000-041877',
        founded='2022',
        platform='BresBet Ltd proprietary',
        sisters=[
            ('BresBet Sport', 'The sports betting arm of the BresBet brand — same operator'),
            ('BresBet Bingo', 'Bingo offering from the BresBet group'),
        ],
        main_review_slug='bresbet',
        affiliate_url='https://refer.bresbet.com/redirect.aspx?pid=1',
        logo='bresbet.png', logo_bg='#0a0a23', stars=4,
        bonus='100 Free Spins + £20 Free Bet',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'BresBet is operated by <strong>BresBet Ltd</strong>, a UK-licensed gambling operator that launched in 2022. BresBet Ltd holds UKGC Account 000-041877.',
            'As one of the newest operators reviewed by Casino Site Reviews, BresBet Ltd operates a focused portfolio. The casino and sportsbook products operate as separate brands under the same UKGC licence and shared responsible gambling infrastructure.',
        ],
        faq_items=''.join([
            faq('What are BresBet sister sites?', 'BresBet sister sites include BresBet Sport and BresBet Bingo — all operated by BresBet Ltd under UKGC Account 000-041877.'),
            faq('Is BresBet a safe UK casino?', 'Yes. BresBet holds a UKGC licence (Account 000-041877) and is fully GamStop integrated. As a newer operator, it is fully regulated by the UK Gambling Commission.'),
        ]),
        faq_schema=[
            ('What are BresBet sister sites?', 'BresBet sister sites are operated by BresBet Ltd and include BresBet Sport and BresBet Bingo under UKGC Account 000-041877.'),
            ('Who owns BresBet Casino?', 'BresBet is owned and operated by BresBet Ltd, a UKGC licensed UK gambling operator (Account 000-041877).'),
        ],
    ),
    dict(
        slug='livescorebet-sister-sites',
        casino_name='LiveScore Bet',
        operator='LSBet Limited',
        ukgc='000-039630',
        founded='2019',
        platform='LiveScore Group platform',
        sisters=[
            ('LiveScore App', 'The LiveScore sports data app — same group, 100M+ global users'),
            ('LiveScore Video', 'Free sports streaming service within the LiveScore ecosystem'),
            ('LiveScore Casino', 'The casino section of LiveScore Bet — same account and brand'),
        ],
        main_review_slug='livescorebet',
        affiliate_url='https://wl-nl.livescorebet.com/landing/en-gb?btag=a_2506b_4820c_&affid=4820',
        logo='lsbet.png', logo_bg='#0d0d14', stars=4,
        bonus='Bet £10 Get £30 Free Bets',
        tc='18+ New customers only. T&Cs apply.',
        intro=[
            'LiveScore Bet is operated by <strong>LSBet Limited</strong>, part of the LiveScore Group. The LiveScore brand is one of the most widely used sports data platforms globally, with over 100 million users across their app and website. LiveScore Bet is the group\'s gambling product, launched in 2019.',
            'Unlike traditional casino operators, LiveScore Bet benefits from the parent group\'s enormous existing user base in sports data and live scores. This gives the platform a unique distribution advantage — millions of sports fans already use LiveScore for scores, and a proportion convert to the betting product naturally.',
            'The \'sister sites\' in LiveScore Bet\'s case are primarily other LiveScore Group products (the app, video streaming) rather than separate casino brands. This makes LiveScore Bet one of the more focused single-brand casino operators in the UK market.',
        ],
        faq_items=''.join([
            faq('What are LiveScore Bet sister sites?', 'LiveScore Bet is part of the LiveScore Group, whose products include the LiveScore app (100M+ users), LiveScore Video (free streaming) and LiveScore Casino. In terms of other casino brands, LSBet Limited operates primarily within the LiveScore umbrella rather than a multi-brand casino portfolio.'),
            faq('Is the LiveScore app the same as LiveScore Bet?', 'No, but they are connected. The LiveScore app provides free sports scores and news. LiveScore Bet is the group\'s regulated gambling product. They are separate services but linked within the same group, and you can access LiveScore Bet from the LiveScore app.'),
        ]),
        faq_schema=[
            ('What are LiveScore Bet sister sites?', 'LiveScore Bet is operated by LSBet Limited, part of the LiveScore Group. Related products include the LiveScore app and LiveScore Video streaming service. There are no traditional casino sister brands under LSBet Limited.'),
            ('Who owns LiveScore Bet?', 'LiveScore Bet is owned by the LiveScore Group, operating under LSBet Limited with UKGC Account 000-039630.'),
        ],
    ),
]

os.makedirs('reviews', exist_ok=True)

for c in casinos:
    sisters_list = [(n, note) for n, note in c['sisters']]
    page = build_sister_page(
        slug=c['slug'],
        casino_name=c['casino_name'],
        operator=c['operator'],
        ukgc_account=c['ukgc'],
        founded=c['founded'],
        platform=c['platform'],
        sister_sites_list=sisters_list,
        main_review_slug=c['main_review_slug'],
        main_affiliate_url=c['affiliate_url'],
        logo_file=c['logo'],
        logo_bg=c['logo_bg'],
        stars_n=c['stars'],
        bonus_text=c['bonus'],
        tc_text=c['tc'],
        intro_paras=c['intro'],
        faq_items_html=c['faq_items'],
        faq_schema_items=c['faq_schema'],
    )
    path = f"reviews/{c['slug']}.html"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'Created {path}')

print('\nAll 10 sister sites pages created.')
