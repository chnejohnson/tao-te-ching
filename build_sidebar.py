import re
import json

with open('Ursula K Le Guin.md', 'r') as f:
    tao_te_ching_md_raw = f.read()

chapter_pattern = re.compile(
    r'# (?P<chapter>[\d]{1,2})[ ]*\n##[ ]*(?P<chapter_name>(?:[ ]*\w+)*)[ ]*\n(?P<text>[^#]*)')
chapter_matches = re.findall(chapter_pattern, tao_te_ching_md_raw)


def sidebar_text(num, name): return '{0} - {1}'.format(num, name)


def sidebar_link(num, name): return '/tao_te_ching/{0}_{1}'.format(
    num, name.lower().replace(' ', '_'))


items = []
# Modify src/sidebar.json
for num, name, text in chapter_matches:
    item = {"text": sidebar_text(num, name), "link": sidebar_link(num, name)}
    items.append(item)

print(items)


def read_json(file_name):
    with open(file_name, 'r') as input_file:
        return json.load(input_file)


def write_json(file_name, content):
    with open(file_name, 'w') as output_file:
        json.dump(content, output_file, indent=4)


data = read_json('src/.vitepress/sidebar.json')

data[0]['items'] = items

write_json('src/.vitepress/sidebar.json', data)
