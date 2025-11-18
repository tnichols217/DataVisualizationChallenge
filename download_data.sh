#/usr/bin/env bash

curl -L https://www.numbeo.com/quality-of-life/rankings.jsp -o rankings.jsp
curl -L https://assets.ctfassets.net/jeox55pd4d8n/7jLDkOc80R392YvAPqDxQ/90d7821e7337a593df39067e618aca76/Apartment_List_Rent_Estimates_2025_10.csv -o data/apmt.csv
