# Pune open-data collection

Running, source-cited dataset for the Aamchi Pune Live dashboard. Each figure notes its source and
date. Gathered slowly (paced) to respect rate limits. "verify" = needs deeper confirmation.

## Already on the dashboard (v1)
| Indicator | Value | As of | Source |
|---|---|---|---|
| PMC annual budget | ₹12,618 Cr (₹7,093 revenue / ₹5,524 capital); no tax hike | 2025-26 | PMC budget (Free Press Journal) |
| PCMC annual budget | ₹9,675.27 Cr | 2025-26 | PCMC budget (First India) |
| Trees | 4.09 million, 427 species (80% from 30 species); geo-located | 2019 | PMC GIS Tree Census / OpenCity |
| Water supplied | 866 MLD/day (post-leakage) | 2024 | PMC Water Supply / CSE |
| Solid waste | ~2,258 TPD; 95% source segregation | 2024 | PMC Solid Waste Mgmt |
| Smart City | 55 projects, ₹3,333.07 Cr, 100% complete (mission ended Mar 2025) | 2025 | PSCDCL / Smart Cities Mission |
| Ward divisions | 15 administrative divisions; 11 merged villages (+81 km²) | — | PMC |
| Air quality | SAFAR/CPCB stations: Shivajinagar, Pashan, Karve Rd, Katraj, Lohegaon, Hadapsar | live | SAFAR (IITM/IMD), CPCB |

## Collecting next (priority = useful + citable)
- [x] Budget multi-year trend (2016-17 → 2025-26)
- [x] AQI annual trend / yearly averages
- [x] Tree census: top species, ward-wise counts
- [ ] PMC facilities: hospitals, dispensaries, schools, gardens, public toilets
- [ ] Water/sewage: STP capacity, sewage generated vs treated, rivers
- [ ] Transport: PMPML fleet/ridership, Pune Metro lines/stations/length
- [ ] Population, area, density, slums, literacy
- [ ] Property tax: number of properties, collection
- [ ] PMC CARE grievances (aggregate)

## New findings
(appended below as gathered)

### Budget — multi-year trend (PMC)
| FY | Budget (₹ Cr) | YoY |
|---|---|---|
| 2021-22 | 7,650 | — |
| 2022-23 | 8,592 | +942 |
| 2023-24 | 9,515 | +923 |
| 2024-25 | 11,601 | +2,086 (crossed ₹10k Cr) |
| 2025-26 | 12,618 | +1,017 |
Source: news (Free Press Journal, Policenama) + machine-readable **OpenCity PMC Budgets dataset** (data.opencity.in/dataset/pmc-budgets — also has a 2026-27 doc). Note: one source labelled ₹11,601 Cr as 2025-26; majority attribute ₹11,601 to 2024-25 and ₹12,618 to 2025-26. verify 2026-27 figure (current FY as of Jun 2026).

### Tree census 2019 — detail
- Total **40,09,623 trees**, **427 species**; 80% from just 30 species.
- **Top 3 species = 47%** of all trees: Giripushpa (Gliricidia sepium), Subabul (Leucaena leucocephala), African Blackwood (Dalbergia melanoxylon) — all non-native.
- Of the top 10 species, only **4 are native**: Mango, Babul, Neem, False Ashoka (Polyalthia longifolia).
- **Ward-wise** (census used 14 admin wards): Ward 53 most at **7,71,000** (incl. Taljai forest), Ward 20 = **2,24,000** (incl. ARAI); **median ward ≈ 23,000** trees.
- Per-tree fields: species, girth, height, canopy diameter, health, ownership, economic benefit, flowering season — every tree geo-located.
- Machine-readable: **OpenCity "Pune Tree Census 2019"** (data.opencity.in/dataset/pune-tree-census-2019). Caveat: "ward 53/20" are old electoral/prabhag ward numbers, not the 15 regional offices.

### Air quality — annual AQI trend
| Year | Avg AQI | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| Pune | — | 63 | 91 | 110 | 114 | 104 | 118 | 135 |
Recent PM2.5 ~29 ug/m3. WARNING source: aqi.in (third-party aggregator), NOT official — illustrative only; replace with official CPCB/SAFAR annual averages before publishing. Trend: worsening 2020->23, dip 2024, rising 2025-26.

### Civic facilities (PMC)
- **28 dispensaries** (PMC Health Dept).
- **168 developed gardens**.
- Hospitals / PMC schools / public toilets / fire stations: counts not surfaced in search — available via **PMC Open Data Store** (opendata.punecorporation.org) and **OpenCity "Pune Healthcare — Hospitals & Clinics"** dataset. verify exact counts.

### Water & sewage
- Water supplied: **866 MLD/day**; sewage treatment capacity: **576 MLD** (current).
- Expanding toward ~**895 MLD** (one source says doubling to **1,125 MLD**) — figures inconsistent across reports; verify.
- **PARMM** (Pollution Abatement of River Mula-Mutha) under National River Conservation Programme, funded by **JICA** + PMC: **11 new STPs** + missing sewer links.
- Plants near completion: Mundhwa 20 MLD, Warje 28 MLD, Wadgaon 26 MLD; plus Hadapsar 7 MLD, Kharadi 30 MLD.
- **Story:** 866 MLD water in vs 576 MLD treated → untreated sewage gap into the Mula-Mutha (good transparency narrative).

### Public transport
- **Pune Metro:** 2 operational lines, **32.97 km, 28 stations** (Purple: PCMC Bhawan–Swargate 14.66 km/14 stations; Aqua: Vanaz–Ramwadi ~14 km/16 stations; 3rd line + 44 stations under construction). Daily ridership ~**2.21 lakh** (Oct 2025); FY2025-26 total **7.08 crore** riders, ₹110 Cr revenue.
- **PMPML buses:** fleet **1,584 buses**, daily ridership **~12–13.5 lakh**; +2,500 new buses by Apr–May 2026, target ~18–20 lakh/day.

### Demographics
- **Pune city population: ~4.57 million (2025 est.)** (Census 2011: ~3.12M); Pune Metropolitan Region ~7.4M.
- **Literacy ~86%** (among India's most educated cities).
- Slums: ~690,545 people / 22.1% (Census 2011); PMC estimated ~40% in slums (2011) — declared vs actual gap.
- PMC area after mergers: not cleanly confirmed (PMR ≈ 7,256 km² is the whole region, not PMC). verify PMC-proper area/density.

### Property tax (PMC's main own-revenue)
- FY2024-25 collection: **₹2,365.31 Cr** (target ₹2,847.23 Cr → ~83%; prev year ₹2,273 Cr).
- **~12.5 lakh properties** in the tax net.
- Portal: propertytax.punecorporation.org. **Story:** collection vs target gap = transparency tile.

### Grievances (PMC CARE)
- PMC CARE: **17M+ interactions** to date; chatbot helpline 8888251001 (16,465 sessions in 2024).
- PMC launched a **complaint follow-up / independent-verification system** after a surge in unresolved-complaint grievances (signals resolution-time pain).
- ⚠ **Received / resolved / avg-resolution-time / pending are NOT openly published** — only filing portal (complaint.pmc.gov.in). This is itself a transparency gap → strong "make this public" pitch for the dashboard.

### Education (PMC)
- Secondary: **~40 high schools** — 19 Marathi-medium (3 jr colleges), 4 Urdu-medium, 1 Marathi night school, 1 ITI, 1 technical school; + 15 English & 2 Marathi-medium run via NGOs.
- PMC also runs many primary schools (count/enrollment not surfaced).
- Machine-readable: **OpenCity "Pune Schools Data"** (data.opencity.in/dataset/pune-schools-data) — class-wise enrollment, school list.

### Machine-readable open-data inventory (download-ready)
**OpenCity — data.opencity.in?city=Pune** (CSV/KML/XLSX), incl.:
- PMC Budgets (2016-17 → 2026-27)
- Air quality: hourly 2017–2023, **10 SAFAR stations** (so ~10 stations, not 6)
- PMPML buses + performance · Pune Metro
- Ward-wise slums + population · census · public toilets · parks · property tax
- Tree census 2019 (4.09M, geo-located, ward, management) · Jal Dharohar water-bodies census · Pune Libraries
**Other portals:** opendata.pmc.gov.in / opendata.punecorporation.org (PMC Open Data Store), smartcities.data.gov.in/cities/Pune, DataMeet `Pune_wards` (GeoJSON boundaries), OpenStreetMap.

## Unique / high-value finds

### Dam water levels (Pune's water security) — LIVE-ready ⭐
- Pune drinking water comes from the **Khadakwasla cluster**: Khadakwasla + Panshet + Varasgaon + Temghar.
- Cluster live-storage capacity **29.15 TMC**; as of **June 2026 ~4.13 TMC ≈ 14.2%** (pre-monsoon low → water-management directives).
- Pune region total live storage ~77.02 TMC; demand ~4 TMC (Pune) + 1.5 TMC (PCMC).
- Updated daily by **WRD Maharashtra** (also mirrored at numerical.co.in). Excellent live gauge — especially Mar–Jun. verify exact daily figure at use-time.

### Flood-risk zones — high-impact map layer ⭐
- Recurring flood-prone localities: **Sinhagad Road (Ekta Nagar/Ekta Nagari, Vitthalwadi, Nimbaj Nagar), Bavdhan, Baner, Deccan Gymkhana** — low-lying, along the Mutha.
- Driven by **Khadakwasla dam water release + heavy rain**; 2024 inundated 150+ homes (Army/NDRF deployed; CM ordered flood-protection wall). 2019 Ambil Odha cloudburst killed 19+.
- **Blue flood line** = level expected over 25 years (re-survey planned); **red flood line** = higher return period. Good explainer + risk-map overlay.

### Water bodies (Jal Dharohar census)
- India's first Water Bodies Census (Ministry of Jal Shakti, 2018-19, released 2023). Machine-readable **OpenCity "Maharashtra Water Bodies Census"** (incl. Pune) — lakes/wells/tanks. Pune-specific counts: verify in dataset.
- ✅ **Official PMC dam-status page found:** pmc.gov.in/en/b/current-status-dams-pune-region-2025 — use this as the authoritative source for the dam tile (replaces third-party).

### Road safety
- 2023: **351** road-accident deaths. 2024: **1,404 accidents, 1,320 injuries, 320 fatalities**. 2025: fatal accidents dipped (Pune Police road-safety report); black spots + night traffic flagged.
- Traffic police maintain a **"black spots" list** (exact junctions in the police report — not openly mapped; co-improvement with PMC). Useful safety layer once locations obtained.

### Other unique angles worth a future pass
Heritage structures (PMC heritage list/grades), libraries count, EV-charging & streetlights (Smart City assets), parking, fire incidents, births/deaths (vital stats), PMPML GTFS / Metro real-time feeds, ready-reckoner land rates, open-space per capita.

## Status
Thorough paced pass complete across budget, air, trees, facilities, water/sewage, transport, demographics, property tax, grievances, education + dataset inventory. Many series are download-ready (CSV) for deeper charts. Remaining `verify` items flagged inline. Next: wire selected datasets into the dashboard (trend charts + ward choropleth).
