with open('calculator.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = 'wagering requirements for the best value!\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</section>'

new = '''wagering requirements for the best value!
\t\t\t\t\t</div>

\t\t\t\t\t<!-- Recommendations panel — shown after calculation -->
\t\t\t\t\t<div id="calc-recommendations" style="display:none;margin-top:1.5rem;border-top:1px solid var(--border);padding-top:1.5rem;">
\t\t\t\t\t\t<h3 style="font-family:var(--font-display);font-size:1.1rem;color:var(--text-primary);margin-bottom:0.5rem;" id="rec-headline">Based on your numbers:</h3>
\t\t\t\t\t\t<p style="font-size:0.88rem;color:var(--text-secondary);margin-bottom:1.2rem;" id="rec-summary"></p>
\t\t\t\t\t\t<div id="rec-cards" style="display:flex;flex-direction:column;gap:0.75rem;"></div>
\t\t\t\t\t\t<p style="margin-top:1rem;font-size:0.82rem;text-align:center;">
\t\t\t\t\t\t\t<a href="/no-wagering-casinos" style="color:var(--gold);">See all 0x wagering casinos &rarr;</a>
\t\t\t\t\t\t</p>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t</div>
\t\t</section>'''

if old in content:
    content = content.replace(old, new)
    with open('calculator.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Recommendations panel inserted')
else:
    print('NOT FOUND')
