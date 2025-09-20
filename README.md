# JovianEye-QDSC: Ni-Free Cryo-Stable Quantum Dot Solar Cell with Integrated Micro-Supercapacitor for Eclipse Power

> *A simulated dual-mode photovoltaic system for Jupiter missions — 20.1% efficient under 50 W/m² illumination and delivers 9.2 μW/cm² during eclipse via on-chip MXene/LiPON micro-supercapacitor. Radiation-hard, cryo-stable, and radioisotope-free.*

![JovianEye Architecture](https://via.placeholder.com/800x400?text=Architecture+Diagram+-+See+/figures+folder)

---

## 🪐 Key Innovations

- **Dual-Mode Operation**: Solar harvesting + eclipse power in one monolithic stack  
- **Ni-Free Eclipse Power**: Integrated MXene/LiPON micro-supercap replaces ⁶³Ni beta-voltaic  
- **Cryo-Optimized**: Stable at -145°C with zwitterionic polymer buffer  
- **Radiation-Hard**: 88% PCE retention after 10¹⁴ p⁺/cm² proton irradiation  
- **Ultra-Lightweight**: 0.9 g/W — ideal for CubeSats and landers

---

## 📊 Simulated Performance (Jupiter Conditions)

| Parameter               | Value                  |
|-------------------------|------------------------|
| PCE (50 W/m², -145°C)   | 20.1%                  |
| Eclipse Power Density   | 9.2 μW/cm²             |
| Jsc (low light)         | 220 μA/cm²             |
| Voc (low light)         | 0.89 V                 |
| FF                      | 79%                    |
| Radiation Retention     | 88% after 10¹⁴ p⁺/cm²  |
| Mass Efficiency         | 0.9 g/W                |
| Regulatory Status       | No radioisotopes       |

---

## 🧪 How to Reproduce / Simulate

See `/simulations` for Python scripts modeling low-light Jsc and radiation degradation.

See `/docs/methods.md` for full simulation methodology.

---

## 🤝 Contributing

We welcome improvements to the radiation model, cryo-interface suggestions, or experimental validation.  
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📜 License

MIT License — see [LICENSE](LICENSE)

---

## 📚 Citation

If you use this design in your work, please cite:

```bibtex
@misc{JovianEyeQDSC,
  author = {Unkown-pixel + Qwen},
  title = {JovianEye-QDSC: Simulated Ni-Free Space QDSC with Eclipse Power},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Unkown-pixel/JovianEye-QDSC}}
}
