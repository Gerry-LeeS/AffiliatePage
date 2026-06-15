import re, sys
sys.stdout.reconfigure(encoding='utf-8')

updates = {
    'reviews/lunacasino.html':
        'Read our Luna Casino review before you claim. 100% up to £50 + 50 Free Spins (code LUNA) — we check the wagering terms, payout speed and whether the bonus is worth it.',
    'reviews/playojo.html':
        'Read our PlayOJO review before you claim. 80 wager-free spins — 0x wagering, every win paid as real cash. We verify the promise and test payouts. UKGC licensed.',
    'reviews/boylecasino.html':
        'Read our Boyle Casino review before you claim. 100 Free Spins or £50 Casino Bonus — we test both offers, payout speed and live casino quality. 40 years of trust.',
    'reviews/swiftcasino.html':
        'Read our Swift Casino review before you claim. Exclusive 100% up to £75 + 50 Free Spins, no code needed — we verify withdrawals, game selection and support.',
    'reviews/netbet.html':
        'Read our NetBet review before you claim. 100 Free Spins on Big Bass Splash — we break down the wager trigger, real value and whether NetBet’s payouts actually deliver.',
    'reviews/bestodds.html':
        'Read our BestOdds review before you claim. 250 Free Spins (code bop5x50fs, wager £20) — we calculate the real value and test payouts. Honest UKGC-verified verdict.',
    'reviews/kwiff.html':
        'Read our Kwiff review before you claim. 200 Free Spins on Book of Dead (wager £20) — sports-first, no PayPal. Our honest 3/5 rating explains who Kwiff is really for.',
    'reviews/bettom.html':
        'Read our BetTOM review before you claim. £50 bonus + 10 Free Spins on Big Bass Splash — same-day withdrawals tested. Is BetTOM worth it? Our honest 4.5/5 verdict.',
    'reviews/bresbet.html':
        'Read our BresBet review before you claim. 100 Free Spins (code CasinoWelcome26) + £20 Free Bet — we verify the trigger terms, wagering conditions and payout speed.',
    'reviews/livescorebet.html':
        'Read our LiveScore Bet review before you claim. Bet £10 Get £30 in Free Bets — sportsbook, casino and payouts all tested. Honest 4.5/5 verdict. UKGC licensed.',
}

for filepath, new_desc in updates.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_desc = re.search(r'(<meta name="description" content=")([^"]+)(")', content)
    if old_desc:
        content = content.replace(
            old_desc.group(0),
            old_desc.group(1) + new_desc + old_desc.group(3)
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(str(len(new_desc)) + ' chars — ' + filepath)
    else:
        print('NOT FOUND: ' + filepath)

print('Done')
