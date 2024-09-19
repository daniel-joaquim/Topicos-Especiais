self.addEventListener('install', (event) => {
    event.waitUntil(
      caches.open('cronometro-cache-v1').then((cache) => {
        return cache.addAll([
          '/',
          '/static/style.css',
          '/static/script.js',
          '/static/img/cronometro.png',
        ]);
      })
    );
  });

self.addEventListener("fetch", event => {
    console.log('teste')
})