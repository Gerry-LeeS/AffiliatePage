import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

all_pages = [
    'live-casino.html',
    'slots-sites.html',
    'trustly-casinos.html',
    'apple-pay-casinos.html',
    'five-pound-deposit-casinos.html',
    'no-deposit-bonus.html',
    'blackjack-casinos.html',
    'live-roulette-casinos.html',
    'reviews/lunacasino-sister-sites.html',
    'reviews/playojo-sister-sites.html',
    'reviews/boylecasino-sister-sites.html',
    'reviews/swiftcasino-sister-sites.html',
    'reviews/netbet-sister-sites.html',
    'reviews/bestodds-sister-sites.html',
    'reviews/kwiff-sister-sites.html',
    'reviews/bettom-sister-sites.html',
    'reviews/bresbet-sister-sites.html',
    'reviews/livescorebet-sister-sites.html',
]

def check(filepath):
    issues = []
    is_review = filepath.startswith('reviews/')
    css_path = '../style.css' if is_review else 'style.css'
    js_path = '../script.js' if is_review else 'script.js'

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. GA4
    if 'G-KQ4H2E63YD' not in content:
        issues.append('MISSING GA4 tag')

    # 2. CSS path
    if css_path not in content:
        issues.append('WRONG/MISSING style.css path (expected: ' + css_path + ')')

    # 3. script.js path
    if js_path not in content:
        issues.append('WRONG/MISSING script.js path (expected: ' + js_path + ')')

    # 4. script.js has defer
    if js_path in content and 'defer' not in content[content.find(js_path)-50:content.find(js_path)+100]:
        issues.append('script.js missing defer attribute')

    # 5. calculator.css on category pages (not sister sites)
    if not is_review and 'calculator.css' not in content:
        issues.append('MISSING calculator.css (needed for hero section)')

    # 6. canonical tag
    if 'rel="canonical"' not in content:
        issues.append('MISSING canonical tag')

    # 7. lang attribute
    if '<html lang="en">' not in content:
        issues.append('MISSING lang="en" on html tag')

    # 8. title tag
    title_match = re.search(r'<title>(.*?)</title>', content)
    if not title_match:
        issues.append('MISSING title tag')
    elif len(title_match.group(1)) > 70:
        pass  # just note, not critical

    # 9. meta description
    if 'name="description"' not in content:
        issues.append('MISSING meta description')

    # 10. FAQ: toggleFaq defined
    if 'toggleFaq' in content:
        if 'faq-item' not in content:
            issues.append('toggleFaq defined but no .faq-item elements found')
        # Old broken implementation
        if 'answer.hidden' in content:
            issues.append('FAQ: old toggleFaq still uses answer.hidden (broken)')
        # faq-answer hidden attribute
        if '<div class="faq-answer" hidden>' in content:
            issues.append('FAQ: .faq-answer still has hidden attribute')
        # faq-question-text span missing
        if 'faq-question' in content and 'faq-question-text' not in content:
            issues.append('FAQ: missing faq-question-text span wrapper')

    # 11. Nav: new 3 links in desktop dropdown
    if 'Best Live Casino' not in content:
        issues.append('NAV: missing "Best Live Casino" link')
    if 'Best Slots Sites' not in content:
        issues.append('NAV: missing "Best Slots Sites" link')
    if 'No Deposit Bonuses' not in content:
        issues.append('NAV: missing "No Deposit Bonuses" link')

    # 12. Mobile nav present
    if 'mobile-menu' not in content:
        issues.append('MISSING mobile nav')

    # 13. Theme toggle script (inline before nav)
    if "localStorage.getItem('theme')" not in content:
        issues.append('MISSING theme-restore inline script')

    # 14. Skip link
    if 'skip-link' not in content:
        issues.append('MISSING skip-link (accessibility)')

    # 15. Schema: at least one ld+json block
    if 'application/ld+json' not in content:
        issues.append('MISSING schema (ld+json)')

    # 16. BreadcrumbList schema
    if 'BreadcrumbList' not in content:
        issues.append('MISSING BreadcrumbList schema')

    # 17. Footer present
    if '<footer' not in content:
        issues.append('MISSING footer')

    # 18. BeGambleAware in footer
    if 'begambleaware' not in content.lower():
        issues.append('MISSING BeGambleAware link')

    # 19. Responsible gambling / 18+ disclaimer
    if '18+' not in content:
        issues.append('MISSING 18+ disclaimer')

    # 20. Broken internal image refs (images/ path check for category pages)
    img_srcs = re.findall(r'src="([^"]+)"', content)
    for src in img_srcs:
        if src.startswith('images/') or src.startswith('/images/'):
            clean = src.lstrip('/')
            if not os.path.exists(clean):
                issues.append('BROKEN image ref: ' + src)

    # 21. Category pages: hero section
    if not is_review:
        if 'calculator-hero' not in content:
            issues.append('MISSING calculator-hero hero section')

    # 22. Sister sites: review-hero section
    if is_review:
        if 'review-hero' not in content:
            issues.append('MISSING review-hero section')

    # 23. Affiliate links: rel="noopener sponsored"
    aff_links = re.findall(r'<a[^>]+href="https?://(?:ads\.|promo\.|promos\.|site\.|netbet\.|livepartners\.|gotoplay)[^"]*"[^>]*>', content)
    for link in aff_links:
        if 'sponsored' not in link:
            issues.append('AFFILIATE LINK missing rel="sponsored": ' + link[:80])

    # 24. No hardcoded #000 or #fff colors in style attributes (should use CSS vars)
    hardcoded = re.findall(r'style="[^"]*(?:color|background):\s*#(?:000000|ffffff|fff|000)\b[^"]*"', content, re.IGNORECASE)
    # Only flag if not inside a logo container (logo bg is expected)
    # This is noisy so just count
    if len(hardcoded) > 5:
        issues.append('STYLE: ' + str(len(hardcoded)) + ' hardcoded #000/#fff color values (minor)')

    # 25. Open Graph tags
    if 'og:title' not in content:
        issues.append('MISSING og:title')
    if 'og:description' not in content:
        issues.append('MISSING og:description')

    return issues

print('=' * 60)
print('AUDIT: All 18 new pages')
print('=' * 60)

total_issues = 0
for page in all_pages:
    if not os.path.exists(page):
        print('\n[MISSING FILE] ' + page)
        continue
    issues = check(page)
    if issues:
        print('\n[' + page + ']')
        for issue in issues:
            print('  ! ' + issue)
        total_issues += len(issues)
    else:
        print('[OK] ' + page)

print('\n' + '=' * 60)
print('Total issues found: ' + str(total_issues))
