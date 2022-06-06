import os
import re

with open('Ursula K Le Guin.md', 'r') as f:
    tao_te_ching_md_raw = f.read()

chapter_pattern = re.compile(
    r'# (?P<chapter>[\d]{1,2})[ ]*\n##[ ]*(?P<chapter_name>(?:[ ]*\w+)*)[ ]*\n(?P<text>[^#]*)')
chapter_matches = re.findall(chapter_pattern, tao_te_ching_md_raw)


def foldername(num, name): return '{0}_{1}'.format(
    num, name.lower().replace(' ', '_'))


def linkname(num, name): return '{0} - {1}'.format(num, name)


def summary_line(num, name): return '* [{0}]({1}/README.md)'.format(
    linkname(num, name), foldername(num, name))


# Create the SUMMARY.md
with open('SUMMARY.md', 'w') as f:
    f.write('# SUMMARY\n')
    for match in chapter_matches:
        f.write(summary_line(match[0], match[1]) + '\n')

if not os.path.exists('src/tao_te_ching'):
    os.mkdir('src/tao_te_ching')

# Create 81 markdown file
for num, name, text in chapter_matches:
    file_name = foldername(num, name)
    with open('src/tao_te_ching/' + file_name + '.md', 'w') as f:
        f.write('# {0} - {1}\n\n'.format(num, name))
        f.write(text)
