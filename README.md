# 🅿️ ParkSathi — Make your parking easy

**ParkSathi** is a high-performance, Django-based geospatial web application designed to eliminate the stress of finding parking in Kathmandu. By merging real-time location tracking with interactive mapping and voice assistance, ParkSathi guides users directly to their destination with precision.

---

## 🚀 Key Features

* **Live GPS Navigation:** Real-time tracking of the user's position using the `watchPosition` API for a dynamic "following" camera experience.
* **Voice Turn-by-Turn Guidance:** Integrated **Speech Synthesis** engine that announces directions (left, right, straight) when within 30 meters of a junction.
* **Dynamic Route Calculation:** Powered by the **Leaflet Routing Machine** and OpenStreetMap (OSM) for accurate, live pathfinding.
* **Kathmandu GeoJSON Integration:** Custom-mapped parking zones across Kathmandu for highly localized accuracy.
* **Smart Proximity Alerts:** Automatic "Arrived" detection and notification once the user is within 15 meters of the target parking spot.
* **Immersive Dark UI:** A sleek, glassmorphic design built with Tailwind CSS, optimized for low-light navigation and clarity.

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **Backend** | [Django 5.2](https://www.djangoproject.com/) |
| **Frontend** | HTML5, Tailwind CSS, Lucide Icons |
| **Mapping** | [Leaflet.js](https://leafletjs.com/) |
| **Routing Engine** | Leaflet Routing Machine (OSM) |
| **Voice Engine** | Web Speech API (SpeechSynthesis) |
| **Database** | SQLite (Dev) / PostgreSQL (Prod) |
| **Deployment** | [Vercel](https://vercel.com/) |
| **Static Management** | WhiteNoise |

---

## 🆕 Latest Updates
* **Voice Integration:** Added a hands-free experience for drivers and riders to ensure safety while navigating.
* **UI Morphing Logo:** A modern, organic-shaped CSS animation providing a unique and professional brand identity.

---

## ⚠️ Note for Users

**This version is now fully functional for Desktop! and for mobile version the work is on progress** 📱🔊

To ensure the best experience:
1. **Location Access:** Grant the browser permission to access your GPS.
2. **Sound/Media:** Ensure your device volume is up and media permissions are enabled for the **Voice Navigation** to work correctly.

---

## 👨‍💻 Built By

**Kripesh Bhele**

* **LinkedIn:** [kripesh-bhele-74b4612bb](https://www.linkedin.com/in/kripesh-bhele-74b4612bb/)
* **GitHub:** [krio69](https://github.com/krio69)

---

> © 2026 All Rights Reserved
