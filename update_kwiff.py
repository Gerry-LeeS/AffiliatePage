with open('reviews/kwiff.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# 1) Update Schema ratingValue from 4.5 to 3
if '"ratingValue": "4.5"' in content:
    content = content.replace('"ratingValue": "4.5"', '"ratingValue": "3"')
    changes += 1
    print('1. Schema rating updated')

# 2) Update page title and description
old_title = '<title>Kwiff Casino Review 2026 — 200 Free Spins on Book of Dead, Tested &amp; Rated</title>'
new_title = '<title>Kwiff Casino Review 2026 — Honest Rating 3/5 | Supercharged Bets, No PayPal | Casino Site Reviews</title>'
if old_title in content:
    content = content.replace(old_title, new_title)
    changes += 1
    print('2. Title updated')

old_desc = 'content="Kwiff Casino review: we tested the 200 Free Spins offer, payout speed and game selection. Is Kwiff legit? UKGC licensed. Find out if it\'s worth your £20 wager."'
new_desc = 'content="Kwiff Casino honest review 2026. Strong Supercharged bets sportsbook, decent game library, but sparse casino promotions and no PayPal. UKGC licensed. Rated 3/5."'
if old_desc in content:
    content = content.replace(old_desc, new_desc)
    changes += 1
    print('3. Meta description updated')

# 3) Replace OG title
content = content.replace(
    'content="Kwiff Casino Review 2026 — 200 Free Spins on Book of Dead, Tested &amp; Rated"',
    'content="Kwiff Casino Review 2026 — Honest Rating 3/5 | Supercharged Bets Tested"'
)

# 4) Replace the 4.5 star display (4 full + 1 half) with 3 full + 2 empty
star_path = 'M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z'
if 'half-clip' in content:
    import re
    # Replace the entire stars div
    old_stars_pat = r'<div class="stars">.*?</div>\s*(?=</div>\s*</div>)'
    # Just do a direct string search for the block
    old_block = '''<div class="stars">
									<svg viewBox="0 0 24 24" class="star filled">
										<path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/>
									</svg>
									<svg viewBox="0 0 24 24" class="star filled">
										<path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/>
									</svg>
									<svg viewBox="0 0 24 24" class="star filled">
										<path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/>
									</svg>
									<svg viewBox="0 0 24 24" class="star filled">
										<path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/>
									</svg>
									<!-- Half star -->
									<svg viewBox="0 0 24 24" class="star" style="width:28px;height:28px;">
										<defs>
											<clipPath id="half-clip">
												<rect x="0" y="0" width="12" height="24" />
											</clipPath>
										</defs>
										<path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z" fill="rgba(212, 175, 55, 0.3)"/>
										<path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z" clip-path="url(#half-clip)" fill="var(--gold)"/>
									</svg>
								</div>'''
    new_block = '''<div class="stars" aria-label="3 out of 5 stars">
									<svg viewBox="0 0 24 24" class="star filled"><path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/></svg>
									<svg viewBox="0 0 24 24" class="star filled"><path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/></svg>
									<svg viewBox="0 0 24 24" class="star filled"><path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/></svg>
									<svg viewBox="0 0 24 24" class="star" style="opacity:0.2;"><path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/></svg>
									<svg viewBox="0 0 24 24" class="star" style="opacity:0.2;"><path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/></svg>
								</div>'''
    if old_block in content:
        content = content.replace(old_block, new_block)
        changes += 1
        print('4. Stars display updated to 3/5')
    else:
        print('4. WARNING: stars block not found exactly, trying search...')
        idx = content.find('half-clip')
        print(repr(content[idx-300:idx+100]))

# 5) Update Overview section
old_overview = '''<section class="review-section">
					<div class="section-icon">\U0001f3b0</div>
					<h2>Overview</h2>
					<p>
						Kwiff launched in 2015 and has built its identity around a genuinely unique product feature: Supercharged bets. When you place any sports bet on Kwiff, there is a random chance that your odds will be automatically boosted before your bet is confirmed — you accept the enhanced odds or decline and proceed at the original price. This is not a promotional overlay or a selected-market feature; it applies randomly across all sports bets, every time. For regular sports bettors, this adds ongoing value that compounds meaningfully over time.
					</p>
					<p>
						Kwiff has been UKGC licensed since 2015 and has a track record that most newer operators cannot match. The casino offering is substantial — exclusive game titles not available elsewhere, a strong slots library and a well-curated live casino section. Revolut is accepted as a payment method (rare among UK licensed casinos), making Kwiff a strong choice for players who bank digitally.
					</p>
				</section>'''
new_overview = '''<section class="review-section">
					<div class="section-icon">\U0001f3b0</div>
					<h2>Overview</h2>
					<p>
						Kwiff is primarily a sports betting platform with a casino section attached. Its standout feature — Supercharged bets — is genuinely unique: any sports bet you place has a random chance of having its odds automatically boosted before confirmation. This applies to all sports, all bet types, permanently. For regular sports bettors, this is a real differentiator with ongoing value. For players whose primary interest is casino gaming, it is irrelevant.
					</p>
					<p>
						Rated 3/5. Kwiff earns its score through UKGC credentials, a solid game library and a decade of operational track record. It loses ground on sparse casino promotions, a welcome offer requiring spend rather than simply depositing, no PayPal, and a platform clearly built around sports. Players prioritising casino bonuses, wager-free offers or PayPal will find better options among our top-rated picks.
					</p>
				</section>'''
if old_overview in content:
    content = content.replace(old_overview, new_overview)
    changes += 1
    print('5. Overview updated')
else:
    # Try to find it differently
    idx = content.find('Overview</h2>')
    if idx > 0:
        print('5. WARNING: overview found at', idx, 'but exact match failed')
        print(repr(content[idx:idx+200]))

# 6) Update pros/cons
old_pc = '''<ul>
								<li>Sleek website design with a dark theme.</li>
								<li>Very impressive casino selection.</li>
								<li>Supercharged bets opportunities.</li>
							</ul>
						</div>
						<div class="cons-box">
							<h3>✗ Cons</h3>
							<ul>
								<li>Not many casino promotions compared to sports.</li>
							</ul>'''
new_pc = '''<ul>
								<li>Unique Supercharged bets — random odds boosts on all sports bets, permanently.</li>
								<li>Strong game library with exclusive titles and Evolution Gaming live casino.</li>
								<li>Revolut accepted — rare in the UK market, useful for digital-bank users.</li>
								<li>Dedicated iOS and Android apps with genuine functionality.</li>
							</ul>
						</div>
						<div class="cons-box">
							<h3>✗ Cons</h3>
							<ul>
								<li>No PayPal — a significant gap vs Boyle Casino, NetBet and LiveScore Bet.</li>
								<li>Welcome offer requires wagering £20 (spending), not just depositing.</li>
								<li>Casino promotions are infrequent and low-value vs dedicated casino platforms.</li>
								<li>Platform DNA is sports-first; casino features and bonuses are clearly secondary.</li>
								<li>No Trustly or open banking despite the operator’s digital focus.</li>
							</ul>'''
if old_pc in content:
    content = content.replace(old_pc, new_pc)
    changes += 1
    print('6. Pros/Cons updated')
else:
    print('6. WARNING: pros/cons not found exactly')

# 7) Update verdict section
old_verdict = '''<section class="review-section" id="verdict">
					<div class="section-icon">⭐</div>
					<h2>Our Verdict</h2>
					<p>
						Kwiff earns its 4.5/5 rating through a genuinely distinctive product. The Supercharged bets mechanic is not a superficial marketing feature — it applies randomly to any bet, adds real odds value when triggered, and makes every sports wager slightly more exciting. The casino offering is also impressive, with exclusive titles and a well-curated slots library that goes beyond the standard catalogue available at most operators.
					</p>
					<p>
						The main limitation is that casino promotions are less frequent and less generous than at dedicated casino platforms like <a href="/reviews/playojo" style="color:var(--gold);">PlayOJO</a> or <a href="/reviews/lunacasino" style="color:var(--gold);">Luna Casino</a>. If casino bonuses are your priority, those alternatives offer more consistent rewards. For sports bettors who also enjoy casino play, Kwiff is a well-rounded and genuinely exciting operator.
					</p>
					<p style="font-size:0.85rem;color:var(--text-muted);margin-top:1rem;"><em>Reviewed by Jose Fontana, Casino Analyst. Last verified: May 2026.</em></p>
				</section>'''
new_verdict = '''<section class="review-section" id="verdict">
					<div class="section-icon">⭐</div>
					<h2>Our Verdict — 3/5</h2>
					<p>
						Kwiff is a legitimate UKGC-licensed operator with a decade of operational history, a strong game library and a genuinely unique sports betting feature in Supercharged bets. For sports bettors who also play casino games, it offers a coherent, well-built platform with something no competitor replicates on the sports side.
					</p>
					<p>
						The 3/5 rating reflects the casino-specific experience: sparse and infrequent promotions, a welcome bonus that requires active wagering to unlock rather than just depositing, and the absence of PayPal. Compared to <a href="/reviews/playojo" style="color:var(--gold);">PlayOJO</a> (0x wagering, wager-free free spins), <a href="/reviews/lunacasino" style="color:var(--gold);">Luna Casino</a> (strong deposit match) or <a href="/reviews/boylecasino" style="color:var(--gold);">Boyle Casino</a> (PayPal, generous welcome offer), Kwiff’s casino proposition is noticeably weaker.
					</p>
					<p>
						<strong>Best for:</strong> Sports bettors who want a side casino. The Supercharged mechanic alone is worth experiencing if you bet on sports regularly.<br>
						<strong>Not recommended for:</strong> Players whose primary interest is casino bonuses, wagering-free offers, or PayPal payments.
					</p>
					<p style="font-size:0.85rem;color:var(--text-muted);margin-top:1rem;"><em>Reviewed by Jose Fontana, Casino Analyst. Last verified: May 2026.</em></p>
				</section>'''
if old_verdict in content:
    content = content.replace(old_verdict, new_verdict)
    changes += 1
    print('7. Verdict updated')
else:
    print('7. WARNING: verdict not found')
    idx = content.find('id="verdict"')
    if idx > 0:
        print(repr(content[idx:idx+400]))

# 8) Update casino promotions paragraph
old_promo = 'Casino promotions at Kwiff are less frequent than at dedicated casino platforms like PlayOJO or Luna Casino — the platform\'s promotional energy is directed primarily at sports. For pure casino bonus volume, Kwiff is not the strongest option. For sports bettors who also enjoy casino play, the Supercharged mechanic provides a level of ongoing value that no other UK operator replicates.'
new_promo = 'Casino promotions at Kwiff are materially less frequent and less generous than at dedicated casino platforms like <a href="/reviews/playojo" style="color:var(--gold);">PlayOJO</a> or <a href="/reviews/lunacasino" style="color:var(--gold);">Luna Casino</a>. If regular casino bonus volume is important to your playing habits, this is a significant limitation. Kwiff’s promotional budget is directed at sports. The casino section is well-stocked and technically solid, but receives comparatively little promotional investment. Players should set expectations accordingly.'
if old_promo in content:
    content = content.replace(old_promo, new_promo)
    changes += 1
    print('8. Promotions paragraph updated')
else:
    print('8. WARNING: promotions paragraph not found')

with open('reviews/kwiff.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nTotal changes: {changes}')
