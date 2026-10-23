#!/usr/bin/env python3
"""Check Korean coverage and invariants without third-party dependencies."""
from collections import Counter
from pathlib import Path
import argparse
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r'^\s*(`{3,}|~{3,})(.*)$')
SHORTCODE = re.compile(r'{{[<%]\s*(/)?([\w-]+)(.*?)\s*[>%]}}', re.S)
LINK = re.compile(r'\]\(([^\n]*?)\)')

def parts(text):
    """Exclude front matter and fenced examples when inspecting prose."""
    lines = text.splitlines(keepends=True)
    if lines and lines[0].strip() == '---':
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == '---')
        lines = lines[end + 1:]
    prose, blocks, block = [], [], []
    marker = None
    for line in lines:
        match = FENCE.match(line)
        if marker:
            block.append(line)
            if match and match[1][0] == marker[0] and len(match[1]) >= len(marker) and not match[2].strip():
                blocks.append(''.join(block)); block = []; marker = None
        elif match:
            marker = match[1]; block = [line]
        else:
            prose.append(line)
    if marker:
        raise ValueError('Unclosed code fence')
    return ''.join(prose), blocks

def shortcodes(text):
    found = []
    for close, name, args in SHORTCODE.findall(text):
        # Only presentation text can differ; paths and behavior must be stable.
        args = re.sub(r'\b(caption|title|alt|description|name)="(?:\\.|[^"\\])*"', r'\1="TRANSLATED"', args)
        found.append((close, name, ' '.join(args.split())))
    return found

def inline_code(text):
    return Counter(value for _, value in re.findall(r'(?<!`)(`+)(?!`)([^\n]+?)\1(?!`)', text))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report-english', action='store_true', help='Print long unchanged English prose for review')
    args = parser.parse_args()
    sources = sorted((ROOT / 'content/en').rglob('*.md'))
    corrections = json.loads((ROOT / 'scripts/link_corrections.json').read_text())
    errors, unchanged, covered = [], [], 0
    for source in sources:
        rel = source.relative_to(ROOT / 'content/en')
        target = ROOT / 'content/ko' / rel
        if not target.exists():
            errors.append(f'{rel}: missing Korean file'); continue
        covered += 1
        en_source = source.read_text()
        for before, after in corrections.get(rel.as_posix(), []):
            en_source = en_source.replace(before, after)
        en, en_code = parts(en_source)
        ko, ko_code = parts(target.read_text())
        if en_code != ko_code:
            errors.append(f'{rel}: fenced code differs')
        if inline_code(en) != inline_code(ko):
            errors.append(f'{rel}: inline code differs')
        for anchor in re.findall(r'\{#([^}]+)\}', en):
            if '{#' + anchor + '}' not in ko:
                errors.append(f'{rel}: missing anchor #{anchor}')
        if Counter(shortcodes(en)) != Counter(shortcodes(ko)):
            errors.append(f'{rel}: shortcode structure/arguments differ')
        if Counter(LINK.findall(en)) != Counter(LINK.findall(ko)):
            errors.append(f'{rel}: Markdown link destinations differ')
        if en.strip() and not re.search('[가-힣]', ko):
            errors.append(f'{rel}: no Korean body text')
        en_lines = set(en.splitlines())
        for line in ko.splitlines():
            if line not in en_lines or re.search('[가-힣]', line):
                continue
            plain = re.sub(r'`[^`]*`|{{.*?}}|<[^>]*>|https?://\S+', '', line)
            if len(re.findall(r'\b[A-Za-z]{2,}\b', plain)) >= 8:
                unchanged.append(f'{rel}: {line[:240]}')
    print(f'Korean coverage: {covered}/{len(sources)} Markdown files')
    for error in errors:
        print('ERROR:', error)
    print(f'Long unchanged English lines requiring review: {len(unchanged)}')
    if args.report_english:
        for line in unchanged:
            print('REVIEW:', line)
    print(f'Structural errors: {len(errors)}')
    return bool(errors)

if __name__ == '__main__':
    sys.exit(main())
