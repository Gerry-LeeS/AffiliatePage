import re
import os

sister_files = [
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

OLD_TOGGLE = '''function toggleFaq(btn) {
				const answer = btn.nextElementSibling;
				const isOpen = !answer.hidden;
				answer.hidden = isOpen;
				btn.setAttribute('aria-expanded', !isOpen);
				btn.querySelector('.faq-icon').textContent = isOpen ? '+' : '\\u2212';
			}'''

NEW_TOGGLE = '''function toggleFaq(btn) {
				const item = btn.closest('.faq-item');
				const isOpen = item.classList.contains('open');
				item.classList.toggle('open');
				btn.setAttribute('aria-expanded', String(!isOpen));
			}'''

for filepath in sister_files:
    if not os.path.exists(filepath):
        print(filepath + ': FILE NOT FOUND')
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Fix toggleFaq function
    if OLD_TOGGLE in content:
        content = content.replace(OLD_TOGGLE, NEW_TOGGLE)
        print(filepath + ': toggleFaq fixed')
    else:
        print(filepath + ': toggleFaq not matched — trying regex fallback')
        # Regex fallback for any variation
        content = re.sub(
            r'function toggleFaq\(btn\)\s*\{[^}]+\}',
            '''function toggleFaq(btn) {
				const item = btn.closest('.faq-item');
				const isOpen = item.classList.contains('open');
				item.classList.toggle('open');
				btn.setAttribute('aria-expanded', String(!isOpen));
			}''',
            content
        )

    # 2. Remove 'hidden' attribute from faq-answer divs
    content = content.replace('<div class="faq-answer" hidden>', '<div class="faq-answer">')

    # 3. Wrap bare question text in faq-question-text span
    # Pattern: button text between aria-expanded="false"> and \n...<span class="faq-icon">
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
        print(filepath + ': saved')
    else:
        print(filepath + ': no changes made')

print('Done')
