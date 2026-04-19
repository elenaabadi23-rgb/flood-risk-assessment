# 🌍 Automated Flood Risk Assessment Workflow

## 📌 Overview

This project presents an automated geospatial workflow that integrates raster-based flood hazard data with vector infrastructure layers to assess flood risk and generate a Flood Risk Index.

The objective is to transform spatial data into actionable insights for climate resilience and risk-aware urban planning.

---

## 🎯 Objective

* Quantify flood exposure at infrastructure level
* Identify high-risk zones
* Support data-driven decision-making in urban planning and investment

---

## ⚙️ Workflow

1. Load vector infrastructure data
2. Load flood risk raster data
3. Align CRS *(automated projection check and alignment)*
4. Compute zonal statistics *(mean flood intensity per feature)*
5. Generate Flood Risk Index *(handling missing values and data gaps)*
6. Export results as GeoJSON

---

## 🧠 Key Insight

By quantifying flood exposure at the infrastructure level, this workflow enables:

* Risk-based prioritization of assets
* Identification of vulnerable urban areas
* Data-driven climate resilience planning

---

## 📊 Output

* Flood Risk Index per infrastructure unit
* GeoJSON file for mapping and decision support

---

## 🛠️ Technologies

* Python
* GeoPandas
* Rasterio
* Rasterstats

---

## 🚀 Future Work

* Machine learning-based flood prediction
* Real-time climate data integration
* Multi-hazard risk analysis *(heat, drought, etc.)*
* ESG Integration: Linking flood risk data to corporate ESG reporting frameworks

---

## 🤝 Let’s Connect

Open to learning and exploring opportunities in geospatial analytics and climate risk.
