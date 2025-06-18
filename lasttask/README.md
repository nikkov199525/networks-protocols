# dnsmon система мониторинга использования DNS-резолверов

## Требования

- Docker
- docker-compose
- домен (для Let's Encrypt) или оставить `localhost.local`

## Запуск
в этой папке, тоесть lasttask:
```bash
bash certbot.sh
docker-compose up --build
заходить на адрес http://localhost:8000/
** Wildcard‑сертификат и SSL не включены в сборку

