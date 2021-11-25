FROM mongo

COPY mongo-seed/CASHBACK.json /mongo-seed/CASHBACK.json


ADD /mongo-seed/import.sh /mongo-seed/import.sh
RUN chmod +x /mongo-seed/import.sh

CMD ["/mongo-seed/import.sh"]