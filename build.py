from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
(root / 'dist').mkdir(exist_ok=True)
(root / '.openai').mkdir(exist_ok=True)
css = (root / 'src/style.css').read_text()
script_paths = ['vendor/qrcode.js', 'vendor/jsQR.js', 'src/core.js', 'src/storage.js', 'src/labels.js', 'src/app.js']
scripts = []
for path in script_paths:
    text = (root / path).read_text()
    for tag in ['script', 'SCRIPT', 'body', 'BODY', 'head', 'HEAD']:
        text = text.replace('</' + tag, '<\\/' + tag)
    scripts.append('\n/* Bundled file: ' + path + ' */\n' + text)
shell = (root / 'src/shell.html').read_text()
page = shell.replace('<!-- STYLES -->', '<style>\n' + css + '\n</style>').replace('<!-- SCRIPTS -->', '<script>\n' + '\n;\n'.join(scripts) + '\n</script>')
(root / 'dist/index.html').write_text(page)
(root / 'index.html').write_text(page)
revision = hashlib.sha256(page.encode()).hexdigest()[:12]
worker = """/* Locust Ledger offline app shell. Records remain in IndexedDB. */
const PREFIX = 'locust-ledger:' + new URL(self.registration.scope).pathname + ':';
const CACHE = PREFIX + 'REVISION';
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(['./', './index.html'])).then(() => self.skipWaiting()));
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(key => key.startsWith(PREFIX) && key !== CACHE).map(key => caches.delete(key)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  if (event.request.method !== 'GET' || url.origin !== self.location.origin || event.request.mode !== 'navigate') return;
  event.respondWith(fetch(event.request).then(response => {
    if (response.ok) { const copy = response.clone(); event.waitUntil(caches.open(CACHE).then(cache => cache.put('./index.html', copy))); }
    return response;
  }).catch(() => caches.match('./index.html')));
});
""".replace('REVISION', revision)
(root / 'dist/sw.js').write_text(worker)
(root / 'sw.js').write_text(worker)
(root / '.openai/hosting.json').write_text(json.dumps({'static': {'directory': 'dist'}}))
print(f'Built index.html ({len(page.encode()):,} bytes) and sw.js; revision {revision}')
