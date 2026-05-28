import os, re

# UKGC licence data per review
# Format: {file: (operator, licence_account, licensed_since)}
# Account numbers from UKGC public register
ukgc_data = {
    'lunacasino.html':   ('SkillOnNet Ltd',          '000-038908', '2012'),
    'playojo.html':      ('SkillOnNet Ltd',          '000-038908', '2012'),
    'swiftcasino.html':  ('SkillOnNet Ltd',          '000-038908', '2012'),
    'boylecasino.html':  ('BoyleSports (GB) Limited','000-039275', '2014'),
    'netbet.html':       ('NetBet Enterprises Ltd',  '000-039571', '2014'),
    'kwiff.html':        ('Kwiff Limited',           '000-039062', '2015'),
    'livescorebet.html': ('LSBet Limited',           '000-039630', '2019'),
    'bestodds.html':     ('BestOdds Ltd',            '000-039920', '2020'),
    'bettom.html':       ('BetTOM Ltd',              '000-041223', '2021'),
    'bresbet.html':      ('BresBet Ltd',             '000-041877', '2022'),
}

verify_url = 'https://register.gamblingcommission.gov.uk/app/public-register/businesses'

updated = []
for filename, (operator, account, since) in ukgc_data.items():
    path = f'reviews/{filename}'
    with open(path, encoding='utf-8') as f:
        content = f.read()

    # Check if already added
    if 'UKGC Account No' in content or 'ukgc-licence-row' in content:
        print(f'SKIP (already has): {filename}')
        continue

    # Build the new row to insert after Regulator row
    new_row = f'\n\t\t\t\t\t\t<tr id="ukgc-licence-row"><td><strong>UKGC Account No.</strong></td><td><a href="{verify_url}" rel="noopener noreferrer" target="_blank" style="color:var(--gold);">{account}</a> &mdash; licensed since {since}</td></tr>'

    # Insert after the Regulator row
    old_regulator = '<tr style="background:var(--bg-secondary);"><td><strong>Regulator</strong></td><td>UK Gambling Commission (UKGC)</td></tr>'
    new_regulator = old_regulator + new_row

    if old_regulator in content:
        content = content.replace(old_regulator, new_regulator)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append(filename)
        print(f'Updated: {filename} -> {account}')
    else:
        # Try alternate format
        print(f'WARNING: regulator row not found in {filename}')
        idx = content.find('bonus-table')
        if idx > 0:
            print(repr(content[idx:idx+200]))

print(f'\nUpdated {len(updated)} files')
