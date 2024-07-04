# ssb_data
python and api script to collect data from ssb

## Note for data source ##
1. overall econ:
2. GDP Growth : https://www.ssb.no/en/nasjonalregnskap-og-konjunkturer/nasjonalregnskap/statistikk/nasjonalregnskap/artikler
	https://www.ssb.no/en/nasjonalregnskap-og-konjunkturer/konjunkturer/statistikk/konjunkturtendensene/articles
3. Index of household consumption of goods: https://www.ssb.no/en/varehandel-og-tjenesteyting/varehandel/statistikk/varekonsumindeksen
4. Investment: https://www.ssb.no/en/statbank/table/12880/tableViewLayout1/
5. Import and export: external trade in goods https://www.ssb.no/en/utenriksokonomi/utenrikshandel/statistikk/utenrikshandel-med-varer
	-ref: Table 1 Imports of goods, main groups by SITC https://www.ssb.no/en/statbank/table/08792/tableViewLayout1/ 
	-ref: Table 2 Exports of goods, main groups by SITC
	-OR use import_export.exe (ref: table no. 08792 from ssb.no)
6. travel and tourism: 
	-guest nights: https://www.ssb.no/en/transport-og-reiseliv/reiseliv/statistikk/overnattingar
		-OR use guest_night.exe (ref: table no. 14162 from ssb.no)
	-number of tourists both international and norwegian tourists : https://www.ssb.no/en/statbank/table/14165/
		-OR use tourist_numbers.exe (ref: table no. 14165 from ssb.no)
7. unemployment:
	-employment and unemployment: Labour force survey https://www.ssb.no/en/arbeid-og-lonn/sysselsetting/statistikk/arbeidskraftundersokelsen
		-OR use unemployment_get_input.exe (ref: table no. 13760 from ssb.no)
8. report from IFP (OECD Economic Surveys: Norway 2024)
 https://www.oecd.org/en/publications/oecd-economic-surveys-norway-2024_cb13475f-en.html
