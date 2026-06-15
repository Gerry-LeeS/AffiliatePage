import re, sys, os
sys.stdout.reconfigure(encoding='utf-8')

# ---- Titles (all under 63 chars) ----
titles = {
    'about.html':
        'About Casino Site Reviews — Independent UK Casino Experts',
    'best-casino-bonuses.html':
        'Best Casino Bonuses UK 2026 — Ranked by Real Value | CSR',
    'calculator.html':
        'Wagering Calculator — Work Out Casino Bonus Value | CSR',
    'exclusive.html':
        'Exclusive UK Casino Bonuses 2026 — Deals Only Here | CSR',
    'faq.html':
        'Casino FAQs — UK Online Casino Questions Answered | CSR',
    'fastest-withdrawal-casinos.html':
        'Fastest Withdrawal Casinos UK 2026 — Same Day Payouts | CSR',
    'new-casinos.html':
        'New Casino Sites UK 2026 — Best Newly Launched Operators | CSR',
    'no-wagering-casinos.html':
        'No Wagering Casinos UK 2026 — Keep What You Win | CSR',
    'paypal-casinos.html':
        'Best PayPal Casinos UK 2026 — Instant Deposits | CSR',
    'search.html':
        'Search UK Casino Reviews — Find Your Casino | CSR',
    'reviews/bestodds.html':
        'BestOdds Casino Review 2026 — 250 Free Spins Tested | CSR',
    'reviews/bettom.html':
        'BetTOM Review 2026 — £50 Bonus + Free Spins | CSR',
    'reviews/boylecasino.html':
        'Boyle Casino Review 2026 — 100 Free Spins or £50 Bonus | CSR',
    'reviews/bresbet.html':
        'BresBet Review 2026 — 100 Free Spins + £20 Free Bet | CSR',
    'reviews/kwiff.html':
        'Kwiff Review 2026 — 200 Free Spins, Honest 3/5 Rating | CSR',
    'reviews/livescorebet.html':
        'LiveScore Bet Review 2026 — Bet £10 Get £30 | CSR',
    'reviews/lunacasino.html':
        'Luna Casino Review 2026 — £50 Bonus + 50 Free Spins | CSR',
    'reviews/netbet.html':
        'NetBet Review 2026 — 100 Free Spins on Big Bass Splash | CSR',
    'reviews/playojo.html':
        'PlayOJO Review 2026 — 80 Wager-Free Spins | CSR',
}

# ---- Meta descriptions (all under 158 chars) ----
metas = {
    'about.html':
        'Casino Site Reviews publishes independent editorial reviews of UKGC-licensed UK casinos. Every review is authored by Jose Fontana, Casino Analyst. No paid placements.',
    'best-casino-bonuses.html':
        'Best UK casino bonuses 2026 — ranked by real value after wagering. Free spins, match bonuses and no-wagering offers. Every casino UKGC licensed.',
    'calculator.html':
        'Free wagering calculator: enter your bonus amount and multiplier to see exactly how much you need to wager before withdrawing. Instant results.',
    'exclusive.html':
        'Exclusive UK casino bonus deals negotiated by Casino Site Reviews — higher free spins, reduced wagering and offers not available elsewhere. UKGC licensed only.',
    'jose-fontana.html':
        'Jose Fontana is a casino analyst at Casino Site Reviews, independently reviewing UKGC-licensed UK casinos across bonuses, payouts, games and support.',
}

updated = 0
for filepath, new_title in titles.items():
    if not os.path.exists(filepath):
        print('NOT FOUND: ' + filepath)
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    old_t = re.search(r'<title>(.*?)</title>', c)
    if old_t:
        c = c.replace('<title>' + old_t.group(1) + '</title>', '<title>' + new_title + '</title>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(str(len(new_title)) + ' — ' + filepath)
        updated += 1

for filepath, new_meta in metas.items():
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    old_m = re.search(r'(<meta name="description" content=")([^"]+)(")', c)
    if old_m:
        c = c.replace(old_m.group(0), old_m.group(1) + new_meta + old_m.group(3))
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        print('meta ' + str(len(new_meta)) + ' — ' + filepath)
        updated += 1

print('Done — ' + str(updated) + ' files updated')
