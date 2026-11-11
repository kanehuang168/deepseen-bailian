#!/usr/bin/env python3
"""Mechanical Skill checks; does not claim to evaluate semantic quality."""
import argparse, json, re
from pathlib import Path
from urllib.parse import unquote

def inspect(root, workbuddy=False):
    root = Path(root).resolve(); findings = []
    skill = root / 'SKILL.md'
    if not skill.is_file(): return ['missing SKILL.md']
    text = skill.read_text(encoding='utf-8-sig'); parts = text.split('---', 2)
    if len(parts) < 3 or parts[0].strip(): return ['invalid frontmatter']
    head = parts[1]
    keys = ['name', 'description'] + (['version', 'display_name', 'display_name_en', 'description_zh', 'description_en'] if workbuddy else [])
    for key in keys:
        if not re.search(r'(?m)^' + key + r':\s*\S', head): findings.append('missing ' + key)
    name = re.search(r'(?m)^name:\s*([^\s]+)', head)
    if name and not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name.group(1).strip('"\'')): findings.append('invalid name')
    for p in root.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8-sig')):
            if target.startswith(('https:', 'http:', '#', 'mailto:')): continue
            path = (p.parent / unquote(target.split('#')[0])).resolve()
            if not path.is_relative_to(root) or not path.is_file(): findings.append(str(p.relative_to(root)) + ': missing ' + target)
    return findings

def main():
    p = argparse.ArgumentParser(); p.add_argument('root'); p.add_argument('--workbuddy', action='store_true'); a = p.parse_args()
    result = inspect(a.root, a.workbuddy)
    print(json.dumps({'errors':result, 'scope':'mechanical checks only; examples and actual task behavior require review'}, ensure_ascii=False))
    return 1 if result else 0

if __name__ == '__main__': raise SystemExit(main())
