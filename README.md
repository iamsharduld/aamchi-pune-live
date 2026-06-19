# आमची पुणे · Aamchi Pune Live

A **public-data civic dashboard prototype for Pune** — budget, green cover, water, waste, air
quality and Smart City delivery, in one clear, citizen-friendly, bilingual (English / मराठी) view.

🔗 **Live demo:** https://iamsharduld.github.io/aamchi-pune-live/

> ⚠️ **Prototype — not an official Pune Municipal Corporation product.** An independent,
> public-interest demonstration of what an open, real-time city dashboard could look like.
> Figures are compiled from openly published sources (see the in-page table) and may be outdated;
> AQI values are illustrative samples until a live feed is connected. Verify on official sources
> before relying on any number.

## What it shows
- **KPIs:** annual budget, tree count, water supplied/day, waste handled/day, Smart City projects, ward divisions
- **Pune map** (Leaflet + OpenStreetMap/CARTO) with real SAFAR/CPCB air-quality monitoring localities
- **Charts:** budget revenue/capital split, waste-segregation rate, Smart City completion, green cover
- **Data sources & freshness** table, with each figure tagged *open data* or *live-feed-ready*

## Data sources
- PMC Budget 2025-26 (reported) · PMC GIS Tree Census 2019 (opendata.pmc.gov.in)
- PMC Water Supply / CSE · PMC Solid Waste Management
- PSCDCL / Smart Cities Mission · SAFAR (IITM/IMD) & CPCB air quality
- Map: OpenStreetMap; DataMeet `Pune_wards` (for a future ward choropleth)

## Run locally
It's a single static file. Open `index.html` in a browser (needs internet for the map tiles,
Leaflet, and the Marathi web font).

## The idea
Build on Pune's **own open data** today; wire live ICCC / SAFAR / PMC-CARE feeds via a data-sharing
arrangement to make it real-time. A transparency-and-access layer that complements official portals.

## Licence
Code: MIT. Underlying figures are public government data; attribute the original official sources.
