# 1. Použijeme stabilný a odľahčený Python
FROM python:3.11-slim
 
# 2. Nastavíme pracovný priečinok vo vnútri kontajnera
WORKDIR /app
 
# 3. Optimalizácia pre Python v Dockeri (okamžitý výpis logov do terminálu)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
 
# 4. Skopírujeme zoznam závislostí a nainštalujeme ich
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# 5. Skopírujeme celý kód aplikácie vrátane templates a weather.db
COPY . .
 
# 6. Otvoríme port (zmeňte na 5000 alebo iný, podľa toho, na akom porte vám počúva app.py)
EXPOSE 5000
 
# 7. Príkaz na spustenie aplikácie
CMD ["python", "app.py"]
