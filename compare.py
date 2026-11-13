import csv
from collections import Counter


def compare_csvs(file1, file2, col_index=1, has_header=True):
  """Compara los valores de una columna entre dos archivos CSV y muestra estadísticas."""
  with (
      open(file1, mode="r", encoding="utf-8") as f1,
      open(file2, mode="r", encoding="utf-8") as f2,
  ):
    rows1 = list(csv.reader(f1))
    rows2 = list(csv.reader(f2))

  if has_header:
    rows1 = rows1[1:]
    rows2 = rows2[1:]

  len1, len2 = len(rows1), len(rows2)
  min_len = min(len1, len2)

  if len1 != len2:
    print(
        f"\033[33m[WARNING]\033[0m Diferente número de filas: {file1} ({len1})"
        f" vs {file2} ({len2})"
    )

  matches = 0
  mismatches = []
  dist1 = Counter()
  dist2 = Counter()

  for i in range(min_len):
    val1 = rows1[i][col_index].strip()
    val2 = rows2[i][col_index].strip()

    dist1[val1] += 1
    dist2[val2] += 1

    if val1 == val2:
      matches += 1
    else:
      mismatches.append((i, val1, val2))

  accuracy = (matches / min_len) * 100 if min_len > 0 else 0.0

  # --- Imprimir Reporte Estadístico ---
  print("\n\033[1;36m╔══════════════════════════════════════════════════╗")
  print("║           COMPARACIÓN DE ARCHIVOS CSV            ║")
  print("╚══════════════════════════════════════════════════╝\033[0m")
  print(f"📄 Archivo 1 : {file1} ({len1} filas)")
  print(f"📄 Archivo 2 : {file2} ({len2} filas)")
  print(f"✅ Coincidencias : {matches} / {min_len} ({accuracy:.2f}%)")
  print(f"❌ Diferencias   : {len(mismatches)}")

  # Distribución por categoría / casa
  all_labels = sorted(set(dist1.keys()) | set(dist2.keys()))
  print("\n\033[1m📊 Distribución de valores:\033[0m")
  print(
      f"{'Categoría':<15} | {'Archivo 1':<12} | {'Archivo 2':<12} |"
      f" {'Diferencia':<10}"
  )
  print("-" * 58)
  for label in all_labels:
    c1 = dist1[label]
    c2 = dist2[label]
    diff = c1 - c2
    diff_str = f"+{diff}" if diff > 0 else str(diff)
    print(f"{label:<15} | {c1:<12} | {c2:<12} | {diff_str:<10}")

  # Mostrar primeras 5 discrepancias si existen
  if mismatches:
    print("\n\033[1;33m🔍 Primeras diferencias encontradas:\033[0m")
    for idx, v1, v2 in mismatches[:5]:
      print(f"   Fila {idx}: '{v1}' != '{v2}'")

  return accuracy, mismatches

if __name__ == "__main__":
  # Compara la columna 1 ("Hogwarts House") entre ambos archivos
  compare_csvs("house.csv", "dataset_truth.csv", col_index=1)