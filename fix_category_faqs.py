import re
import os

category_files = [
    'live-casino.html',
    'slots-sites.html',
    'trustly-casinos.html',
    'apple-pay-casinos.html',
    'five-pound-deposit-casinos.html',
    'no-deposit-bonus.html',
    'blackjack-casinos.html',
    'live-roulette-casinos.html',
]

NEW_TOGGLE = '''function toggleFaq(btn) {
			const item = btn.closest('.faq-item');
			const isOpen = item.classList.contains('open');
			item.classList.toggle('open');
			btn.setAttribute('aria-expanded', String(!isOpen));
		}'''

for filepath in category_files:
    if not os.path.exists(filepath):
        print(filepath + ': FILE NOT FOUND')
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Fix toggleFaq — replace any variation
    content = re.sub(
        r'function toggleFaq\(btn\)\s*\{[^}]+\}',
        NEW_TOGGLE,
        content
    )

    # 2. Remove 'hidden' attribute from faq-answer divs
    content = content.replace('<div class="faq-answer" hidden>', '<div class="faq-answer">')

    # 3. Wrap bare question text in faq-question-text span
    def wrap_question_text(m):
        indent = m.group(1)
        text = m.group(2).strip()
        icon_line = m.group(3)
        return indent + '<span class="faq-question-text">' + text + '</span>\n' + icon_line

    content = re.sub(
        r'([ \t]+)([^\n<][^\n]+?)\n([ \t]+<span class="faq-icon">)',
        wrap_question_text,
        content
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(filepath + ': fixed and saved')
    else:
        print(filepath + ': no changes needed')

print('Done')
