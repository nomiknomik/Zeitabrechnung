const CACHE = 'za-v9';
const SHELL = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => Promise.all(SHELL.map(u => c.add(u).catch(() => null)))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if(e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if(url.hostname === 'api.github.com') return;            // Sync nie aus dem Cache
  const seite = e.request.mode === 'navigate' || url.pathname.endsWith('/index.html') || url.pathname.endsWith('/app/');
  if(seite){                                               // network-first: Updates kommen sofort an
    e.respondWith(fetch(e.request).then(res => { const k = res.clone(); caches.open(CACHE).then(c => c.put(e.request, k)).catch(() => {}); return res; })
      .catch(() => caches.match(e.request).then(r => r || caches.match('./index.html'))));
    return;
  }
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(res => {
    const k = res.clone(); caches.open(CACHE).then(c => c.put(e.request, k)).catch(() => {}); return res; })));
});
