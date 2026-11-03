"""Ejecuta los ejemplos cuantitativos de S3, S4 y S10 sin dependencias externas.

Uso, desde esta carpeta:
    python ejecutar_ejemplos.py

Genera archivos reproducibles dentro de las carpetas S3, S4 y S10.
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def linear_forecast(values: list[int], period: int) -> float:
    x_values = list(range(1, len(values) + 1))
    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(values) / len(values)
    slope = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, values))
    slope /= sum((x - x_mean) ** 2 for x in x_values)
    return y_mean + slope * (period - x_mean)


def run_s3() -> None:
    rows = read_csv(ROOT / "S3" / "ventas_retail_central.csv")
    totals: defaultdict[str, int] = defaultdict(int)
    for row in rows:
        totals[row["Region"]] += int(row["Ventas_Q"])

    summary = [
        {
            "Region": region,
            "Ventas_semestre_Q": totals[region],
            "Participacion_pct": round(totals[region] / sum(totals.values()) * 100, 2),
        }
        for region in sorted(totals, key=totals.get, reverse=True)
    ]
    write_csv(
        ROOT / "S3" / "resumen_ejecutable.csv",
        ["Region", "Ventas_semestre_Q", "Participacion_pct"],
        summary,
    )

    west = [row for row in rows if row["Region"] == "Occidente"]
    april = next(int(row["Ventas_Q"]) for row in west if row["Mes"] == "Abr")
    june = next(int(row["Ventas_Q"]) for row in west if row["Mes"] == "Jun")
    inventory_april = next(int(row["Inventario_final"]) for row in west if row["Mes"] == "Abr")
    inventory_june = next(int(row["Inventario_final"]) for row in west if row["Mes"] == "Jun")
    diagnosis = {
        "occidente_caida_Q": april - june,
        "occidente_caida_pct": round((april - june) / april * 100, 2),
        "inventario_reduccion_unidades": inventory_april - inventory_june,
        "diagnostico": "quiebre de inventario",
    }
    (ROOT / "S3" / "diagnostico.json").write_text(
        json.dumps(diagnosis, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def run_s4() -> None:
    rows = read_csv(ROOT / "S4" / "demanda_historica.csv")
    values = [int(row["Unidades_vendidas"]) for row in rows]
    moving_average = sum(values[-3:]) / 3
    linear = linear_forecast(values, 25)
    annual_growth = sum(values[12:]) / sum(values[:12])
    seasonal = values[12] * annual_growth
    forecasts = [
        {"Metodo": "Media movil 3 meses", "Pronostico_unidades": round(moving_average)},
        {"Metodo": "Tendencia lineal", "Pronostico_unidades": round(linear)},
        {"Metodo": "Estimacion estacional", "Pronostico_unidades": round(seasonal)},
    ]
    write_csv(ROOT / "S4" / "pronosticos_ejecutable.csv", ["Metodo", "Pronostico_unidades"], forecasts)
    (ROOT / "S4" / "justificacion.json").write_text(
        json.dumps(
            {
                "crecimiento_anual_pct": round((annual_growth - 1) * 100, 2),
                "metodo_recomendado": "Estimacion estacional",
                "pronostico_recomendado": round(seasonal),
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def run_s10() -> None:
    rows = read_csv(ROOT / "S10" / "clientes_crm.csv")
    by_segment: defaultdict[str, dict[str, int]] = defaultdict(
        lambda: {"Clientes": 0, "Ventas_Q": 0}
    )
    features = []
    for row in rows:
        segment = row["Segmento"]
        by_segment[segment]["Clientes"] += 1
        by_segment[segment]["Ventas_Q"] += int(row["Ventas_ultimo_trimestre_Q"])
        features.append(
            {
                "type": "Feature",
                "properties": {
                    "id": row["ID_Cliente"],
                    "nombre": row["Nombre"],
                    "segmento": segment,
                    "zona": row["Zona"],
                    "ventas_trimestre_Q": int(row["Ventas_ultimo_trimestre_Q"]),
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(row["Longitud"]), float(row["Latitud"])],
                },
            }
        )
    write_csv(
        ROOT / "S10" / "segmentos_ejecutable.csv",
        ["Segmento", "Clientes", "Ventas_trimestre_Q"],
        [
            {
                "Segmento": key,
                "Clientes": values["Clientes"],
                "Ventas_trimestre_Q": values["Ventas_Q"],
            }
            for key, values in sorted(by_segment.items())
        ],
    )
    (ROOT / "S10" / "clientes.geojson").write_text(
        json.dumps({"type": "FeatureCollection", "features": features}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    run_s3()
    run_s4()
    run_s10()
    print("Resultados generados en S3, S4 y S10")


if __name__ == "__main__":
    main()
