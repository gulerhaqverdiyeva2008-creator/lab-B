# CSPC Project

## PW1 --- Lab B
* **Verilənlər:** `decay_observed.csv` faylı zaman və radioaktiv parçalanma sayını (time, count) əks etdirən real müşahidə məlumatlarını göstərir.
* **Analitik Qanuna Uyğunluq:** Qrafikdən görünür ki, müşahidə olunan nöqtələr analitik parçalanma qanunu ($N_0 e^{-\lambda t}$) əyrisi ilə çox yaxşı uyğunluq təşkil edir.
* **Snakemake Boru Kəməri:** Snakemake boru kəməri daxil olan verilənlərdən `plot.py` skripti vasitəsilə `figure.png` qrafikinin avtomatik və ardıcıl şəkildə generasiya olunmasını təmin edir[cite: 1].