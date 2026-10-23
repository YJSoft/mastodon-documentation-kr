#!/usr/bin/env python3
"""Check local links, anchors, and media in built Korean documentation."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
import argparse
import re
import sys

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.redirect = set(), [], None
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('id', 'name' if tag == 'a' else 'id'):
            if attrs.get(key):
                self.ids.add(attrs[key])
        key = 'href' if tag in ('a', 'link') else 'src'
        if attrs.get(key):
            self.links.append(attrs[key])
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            match = re.search(r'url=(.+)', attrs.get('content', ''), re.I)
            if match:
                self.redirect = match[1].strip('"\' ')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('public', type=Path)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--content', type=Path, default=Path(__file__).resolve().parents[1] / 'content/ko')
    args = parser.parse_args()
    base = urlparse(args.base_url.rstrip('/') + '/')
    cache, errors, checked = {}, set(), 0
    def local_file(url):
        path = unquote(urlparse(url).path)
        if not path.startswith(base.path):
            return None
        file = args.public / path[len(base.path):]
        if file.is_dir():
            file /= 'index.html'
        return file
    def document(file):
        if file not in cache:
            cache[file] = Document(file.read_text())
        return cache[file]
    for source in sorted(args.content.rglob('*.md')):
        relative = source.relative_to(args.content)
        route = relative.parent if relative.stem == '_index' else relative.with_suffix('')
        suffix = '' if route == Path('.') else route.as_posix() + '/'
        url = urljoin(args.base_url.rstrip('/') + '/', suffix)
        file = local_file(url)
        if not file or not file.exists():
            errors.add(f'{relative}: missing output {url}'); continue
        for link in document(file).links:
            target = urljoin(url, link)
            parsed = urlparse(target)
            if parsed.scheme not in ('http', 'https') or parsed.netloc != base.netloc:
                continue
            checked += 1
            dest = local_file(target)
            if not dest:
                errors.add(f'{relative}: outside base path: {link}'); continue
            if not dest.is_file():
                errors.add(f'{relative}: missing target: {link}'); continue
            if dest.suffix != '.html':
                continue
            fragment = unquote(parsed.fragment)
            for _ in range(8):
                doc = document(dest)
                if not doc.redirect:
                    break
                target = urljoin(target, doc.redirect)
                redirected = local_file(target)
                if not redirected or not redirected.is_file():
                    break
                dest = redirected
            if fragment and fragment not in document(dest).ids:
                errors.add(f'{relative}: missing anchor: {link}')
    print(f'Checked {checked} local links and resources across {len(list(args.content.rglob("*.md")))} source pages')
    for error in sorted(errors):
        print('ERROR:', error)
    print(f'Site link errors: {len(errors)}')
    return bool(errors)

if __name__ == '__main__':
    sys.exit(main())
