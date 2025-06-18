#!/bin/bash
SSL_DIR="./ssl"
DOMAIN="localhost.local"  # замените на свой домен

if [[ $1 == "--issue" ]]; then
  ~/.acme.sh/acme.sh --issue -d "*.${DOMAIN}" --dns dns_cf     --key-file "${SSL_DIR}/privkey.pem"     --fullchain-file "${SSL_DIR}/fullchain.pem"
  exit 0
fi

if [[ $1 == "--renew" ]]; then
  ~/.acme.sh/acme.sh --renew -d "*.${DOMAIN}" --force     --key-file "${SSL_DIR}/privkey.pem"     --fullchain-file "${SSL_DIR}/fullchain.pem"
  exit 0
fi

cat >/etc/cron.d/renew <<EOF
0 3 * * * root /app/certbot.sh --renew >>/var/log/renew.log 2>&1
EOF
chmod 644 /etc/cron.d/renew