with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add showCalcRecommendations call at end of calculateSpins
old_spins_end = "animateResults('spinsResults');\n}\n\nfunction calculateMatch()"
new_spins_end = "animateResults('spinsResults');\n\tshowCalcRecommendations('spins', wagering, totalValue);\n}\n\nfunction calculateMatch()"

if old_spins_end in content:
    content = content.replace(old_spins_end, new_spins_end)
    print('1. Added recommendation call to calculateSpins')
else:
    print('1. WARNING: calculateSpins end not found')

# 2. Add showCalcRecommendations call at end of calculateMatch
old_match_end = "animateResults('matchResults');\n}\n\nfunction animateResults("
new_match_end = "animateResults('matchResults');\n\tshowCalcRecommendations('match', wagering, amountToWager);\n}\n\nfunction animateResults("

if old_match_end in content:
    content = content.replace(old_match_end, new_match_end)
    print('2. Added recommendation call to calculateMatch')
else:
    print('2. WARNING: calculateMatch end not found')

# 3. Add the showCalcRecommendations function before animateResults
rec_function = '''
function showCalcRecommendations(type, wagering, totalWagerNeeded) {
\tconst panel = document.getElementById('calc-recommendations');
\tconst summary = document.getElementById('rec-summary');
\tconst cards = document.getElementById('rec-cards');
\tconst headline = document.getElementById('rec-headline');
\tif (!panel || !summary || !cards) return;

\tconst CASINOS = {
\t\tplayojo: {
\t\t\tname: 'PlayOJO',
\t\t\tbonus: '50 Free Spins — 0x Wagering (keep what you win)',
\t\t\tbadge: '0x WAGERING',
\t\t\tbadgeColor: '#10b981',
\t\t\tlogo: 'images/casinologos/playojo.png',
\t\t\tbg: '#17003a',
\t\t\treview: '/reviews/playojo',
\t\t\tclaim: 'https://site.gotoplayojo.com/redirect.aspx?pid=23&bid=2399',
\t\t\ttc: '18+. New customers. T&Cs apply.',
\t\t},
\t\tboyle: {
\t\t\tname: 'Boyle Casino',
\t\t\tbonus: '100 Free Spins — 0x Wagering',
\t\t\tbadge: '0x WAGERING',
\t\t\tbadgeColor: '#10b981',
\t\t\tlogo: 'images/casinologos/boyle_square.png',
\t\t\tbg: '#ffffff',
\t\t\treview: '/reviews/boylecasino',
\t\t\tclaim: 'https://promo.boylesports.com/gaming/promo/game8?btag=54248|0f036f7746684ebb9a8e6752ee0e068a',
\t\t\ttc: '18+. New customers. T&Cs apply.',
\t\t},
\t\tluna: {
\t\t\tname: 'Luna Casino',
\t\t\tbonus: '100% up to \\u00a350 + 50 Free Spins (Code: LUNA)',
\t\t\tbadge: '5/5',
\t\t\tbadgeColor: '#d4af37',
\t\t\tlogo: 'images/casinologos/luna.png',
\t\t\tbg: '#000000',
\t\t\treview: '/reviews/lunacasino',
\t\t\tclaim: 'https://ads.galaxyaffiliates.com/redirect.aspx?mid=5366&sid=15149&cid=&pid=&affid=8275',
\t\t\ttc: '18+. New customers. T&Cs apply.',
\t\t},
\t\tnetbet: {
\t\t\tname: 'NetBet',
\t\t\tbonus: '100 Free Spins on \\u00a320 Wager',
\t\t\tbadge: 'LOW WAGERING',
\t\t\tbadgeColor: '#6366f1',
\t\t\tlogo: 'images/casinologos/netbet.png',
\t\t\tbg: '#101010',
\t\t\treview: '/reviews/netbet',
\t\t\tclaim: 'https://netbet.livepartners.com/click.php?z=186827',
\t\t\ttc: '18+. New customers. T&Cs apply.',
\t\t},
\t};

\tfunction makeCard(casino) {
\t\treturn `<div style="display:flex;align-items:center;gap:0.85rem;padding:0.85rem 1rem;background:var(--bg-card,var(--bg-primary));border:1px solid var(--border);border-radius:12px;">
\t\t\t<div style="width:44px;height:44px;min-width:44px;border-radius:8px;background:${casino.bg};display:flex;align-items:center;justify-content:center;overflow:hidden;border:1px solid var(--border);">
\t\t\t\t<img src="${casino.logo}" alt="${casino.name}" width="44" height="44" style="object-fit:contain;padding:4px;" onerror="this.parentElement.innerHTML=\'\\uD83C\\uDFB0\'" loading="lazy">
\t\t\t</div>
\t\t\t<div style="flex:1;min-width:0;">
\t\t\t\t<div style="display:flex;align-items:center;gap:6px;margin-bottom:3px;">
\t\t\t\t\t<span style="font-weight:700;font-size:0.9rem;color:var(--text-primary);">${casino.name}</span>
\t\t\t\t\t<span style="background:${casino.badgeColor}20;color:${casino.badgeColor};border:1px solid ${casino.badgeColor}40;border-radius:999px;padding:1px 8px;font-size:9px;font-weight:700;letter-spacing:0.4px;">${casino.badge}</span>
\t\t\t\t</div>
\t\t\t\t<div style="font-size:0.8rem;color:var(--text-secondary);">\\uD83C\\uDF81 ${casino.bonus}</div>
\t\t\t\t<div style="font-size:0.72rem;color:var(--text-muted);margin-top:2px;">${casino.tc}</div>
\t\t\t</div>
\t\t\t<div style="display:flex;flex-direction:column;gap:5px;flex-shrink:0;">
\t\t\t\t<a href="${casino.review}" style="font-size:11px;padding:0.35rem 0.75rem;border:1px solid var(--border);border-radius:7px;color:var(--text-secondary);text-decoration:none;text-align:center;">Review</a>
\t\t\t\t<a href="${casino.claim}" rel="noopener sponsored" style="font-size:11px;padding:0.35rem 0.75rem;background:var(--gold);border-radius:7px;color:#000;font-weight:700;text-decoration:none;text-align:center;">Claim</a>
\t\t\t</div>
\t\t</div>`;
\t}

\tlet rec = [];
\tlet headlineText = 'Casinos that match your bonus profile:';
\tlet summaryText = '';

\tif (wagering === 0) {
\t\theadlineText = 'Perfect — you\'re looking at wager-free bonuses:';
\t\tsummaryText = 'These casinos offer 0x wagering free spins — winnings are paid as real cash immediately.';
\t\trec = ['playojo', 'boyle'];
\t} else if (wagering <= 20) {
\t\theadlineText = 'Good value — these casinos offer competitive low-wagering bonuses:';
\t\tsummaryText = `With ${wagering}x wagering you need to bet \\u00a3${totalWagerNeeded.toFixed(0)} before withdrawing. These casinos offer the best value for your profile.`;
\t\trec = ['playojo', 'boyle', 'luna'];
\t} else if (wagering <= 35) {
\t\theadlineText = 'Standard wagering — consider these well-rated alternatives:';
\t\tsummaryText = `${wagering}x wagering is average for the market. You\'d need to wager \\u00a3${totalWagerNeeded.toFixed(0)}. Consider a 0x wagering alternative instead.`;
\t\trec = ['playojo', 'boyle', 'luna', 'netbet'];
\t} else {
\t\theadlineText = '\\u26a0\\ufe0f High wagering — here are better alternatives:';
\t\tsummaryText = `${wagering}x wagering is high — you\'d need to bet \\u00a3${totalWagerNeeded.toFixed(0)} to withdraw. We recommend these lower-wagering options instead.`;
\t\trec = ['playojo', 'boyle'];
\t}

\tif (headline) headline.textContent = headlineText;
\tif (summary) summary.textContent = summaryText;
\tcards.innerHTML = rec.map(k => makeCard(CASINOS[k])).join('');
\tpanel.style.display = 'block';
\tpanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

'''

old_animate = '\nfunction animateResults('
new_animate = rec_function + '\nfunction animateResults('

if old_animate in content:
    content = content.replace(old_animate, new_animate, 1)
    print('3. showCalcRecommendations function added')
else:
    print('3. WARNING: animateResults function not found')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
