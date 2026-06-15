import os, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

all_pages = [
    'live-casino.html', 'slots-sites.html', 'trustly-casinos.html',
    'apple-pay-casinos.html', 'five-pound-deposit-casinos.html',
    'no-deposit-bonus.html', 'blackjack-casinos.html', 'live-roulette-casinos.html',
    'reviews/lunacasino-sister-sites.html', 'reviews/playojo-sister-sites.html',
    'reviews/boylecasino-sister-sites.html', 'reviews/swiftcasino-sister-sites.html',
    'reviews/netbet-sister-sites.html', 'reviews/bestodds-sister-sites.html',
    'reviews/kwiff-sister-sites.html', 'reviews/bettom-sister-sites.html',
    'reviews/bresbet-sister-sites.html', 'reviews/livescorebet-sister-sites.html',
]

# Known valid internal pages
valid_internal = {
    '/', '/exclusive', '/search', '/calculator', '/about', '/faq',
    '/responsible-gambling', '/affiliate-disclosure', '/privacy', '/terms',
    '/jose-fontana', '/paypal-casinos', '/no-wagering-casinos',
    '/fastest-withdrawal-casinos', '/new-casinos', '/best-casino-bonuses',
    '/live-casino', '/slots-sites', '/trustly-casinos', '/apple-pay-casinos',
    '/five-pound-deposit-casinos', '/no-deposit-bonus', '/blackjack-casinos',
    '/live-roulette-casinos', '/no-wagering-casinos',
    '/reviews/lunacasino', '/reviews/playojo', '/reviews/boylecasino',
    '/reviews/swiftcasino', '/reviews/netbet', '/reviews/bestbet',
    '/reviews/bestodds', '/reviews/kwiff', '/reviews/bettom',
    '/reviews/bresbet', '/reviews/livescorebet',
    '/reviews/lunacasino-sister-sites', '/reviews/playojo-sister-sites',
    '/reviews/boylecasino-sister-sites', '/reviews/swiftcasino-sister-sites',
    '/reviews/netbet-sister-sites', '/reviews/bestodds-sister-sites',
    '/reviews/kwiff-sister-sites', '/reviews/bettom-sister-sites',
    '/reviews/bresbet-sister-sites', '/reviews/livescorebet-sister-sites',
}

issues_found = 0

for filepath in all_pages:
    page_issues = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Validate all ld+json blocks are valid JSON
    schema_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    for i, block in enumerate(schema_blocks):
        try:
            json.loads(block.strip())
        except json.JSONDecodeError as e:
            page_issues.append('INVALID JSON in schema block ' + str(i+1) + ': ' + str(e))

    # 2. Check internal href links exist
    internal_links = re.findall(r'href="(/[^"#?]*)"', content)
    for link in internal_links:
        # Strip trailing slash for comparison
        link_clean = link.rstrip('/')
        if link_clean == '':
            link_clean = '/'
        if link_clean not in valid_internal and not link_clean.startswith('/images/') and not link_clean.startswith('/reviews/'):
            page_issues.append('UNKNOWN internal link: ' + link)

    # 3. Affiliate links present (at least 1 external claim link)
    aff_links = re.findall(r'href="(https?://(?:ads\.|promo\.|promos\.|site\.|netbet\.live|livepartners\.|gotoplay)[^"]+)"', content)
    if not aff_links:
        # Also check for other known affiliate domains
        aff_links2 = re.findall(r'rel="[^"]*sponsored[^"]*"', content)
        if not aff_links2:
            page_issues.append('NO affiliate/claim links found (rel=sponsored)')

    # 4. Check for placeholder/TODO text
    placeholders = re.findall(r'(?:TODO|PLACEHOLDER|FIXME|lorem ipsum|INSERT)', content, re.IGNORECASE)
    if placeholders:
        page_issues.append('PLACEHOLDER text found: ' + str(placeholders))

    # 5. Check canonical URL matches expected slug
    canonical_match = re.search(r'rel="canonical" href="([^"]+)"', content)
    if canonical_match:
        canon = canonical_match.group(1)
        if not canon.startswith('https://casinositereviews.co.uk/'):
            page_issues.append('CANONICAL wrong domain: ' + canon)
        # Check no trailing slash (except root)
        if canon.endswith('/') and canon != 'https://casinositereviews.co.uk/':
            page_issues.append('CANONICAL has trailing slash: ' + canon)

    # 6. Duplicate H1s
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if len(h1s) != 1:
        page_issues.append('H1 count: ' + str(len(h1s)) + ' (should be exactly 1)')

    # 7. Meta description length
    desc_match = re.search(r'name="description" content="([^"]+)"', content)
    if desc_match:
        dlen = len(desc_match.group(1))
        if dlen > 165:
            page_issues.append('Meta description too long: ' + str(dlen) + ' chars')
        elif dlen < 50:
            page_issues.append('Meta description too short: ' + str(dlen) + ' chars')

    # 8. Title length
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        tlen = len(title_match.group(1))
        if tlen > 70:
            page_issues.append('Title too long: ' + str(tlen) + ' chars — "' + title_match.group(1)[:60] + '..."')

    # 9. Images without alt text
    imgs_no_alt = re.findall(r'<img(?![^>]*alt=)[^>]*>', content)
    if imgs_no_alt:
        page_issues.append('IMG missing alt: ' + str(len(imgs_no_alt)) + ' found')

    # 10. Console-error risk: undefined JS references
    if 'onclick="toggleFaq(this)"' in content and 'function toggleFaq' not in content:
        page_issues.append('JS: toggleFaq called but not defined on page')

    if page_issues:
        print('\n[' + filepath + ']')
        for issue in page_issues:
            print('  ! ' + issue)
        issues_found += len(page_issues)
    else:
        print('[OK] ' + filepath)

print('\nTotal issues: ' + str(issues_found))
