# =============================================================================
# ANALIZADOR DE ARMADURAS DE KENSHI v4  (archivo principal)
# -----------------------------------------------------------------------------
# Propósito:
#   Herramienta de consola para evaluar y comparar armaduras del juego Kenshi.
#   A cada armadura le calcula tres índices numéricos:
#       - Índice de Armadura (armor_index): qué tan bien protege.
#       - Índice de Debuff   (debuff_index): cuánto penaliza sus stats.
#       - Índice de Bonus    (bonus_index): cuánto mejora sus stats.
#
# Funcionalidades:
#   1. Compara TODAS las armaduras de la base de datos integrada (armor_db.py)
#      y muestra rankings (mejor equilibrio, top 3 armadura, top 3 bonus).
#   2. Permite ingresar armaduras manualmente, validando cada dato, y
#      compararlas entre sí.
#
# Estructura del archivo:
#   - Importación de datos           → ARMADURAS_DB, constantes de cuerpo y stats
#   - Funciones de entrada validada  → pedir_float, pedir_texto, pedir_si_no
#   - Lógica de cálculo              → evaluar_armadura
#   - Comparativa de la base de datos→ comparar_todas_las_armaduras
#   - Ingreso y visualización manual → ingresar_armadura, mostrar_resultado,
#                                      comparar_manuales
#   - Punto de entrada               → main()
# =============================================================================

# Se importan desde armor_db.py: la base de datos de armaduras, la lista de
# partes del cuerpo, sus etiquetas legibles y las listas de stats que una
# armadura puede penalizar o bonificar.
from armor_db import (
    ARMADURAS_DB, PARTES_CUERPO, ETIQUETAS,
    STATS_PENALIZABLES, STATS_BONIFICABLES,
)


# =============================================================================
# FUNCIONES DE ENTRADA VALIDADA
# Pequeñas utilidades que repiten la pregunta hasta recibir un dato válido.
# =============================================================================

def pedir_float(mensaje, minimo=0.0, maximo=1.0, permitir_vacio=False):
    """
    Pide un número decimal por consola y lo valida.

    Args:
        mensaje: texto que se muestra al usuario.
        minimo / maximo: rango permitido (inclusive).
        permitir_vacio: si es True, una entrada vacía devuelve None.

    Returns:
        float dentro del rango, o None si se dejó vacío y está permitido.
    """
    # Bucle hasta obtener un valor válido
    while True:
        # Se limpian espacios y se acepta la coma como separador decimal
        valor = input(mensaje).strip().replace(",", ".")
        # Entrada vacía permitida → se interpreta como "sin dato"
        if valor == "" and permitir_vacio:
            return None
        # Intento de conversión a número
        try:
            num = float(valor)
        except ValueError:
            print("  ⚠  Ingresa un número válido (ej: 0.75).")
            continue
        # Validación del rango
        if num < minimo or num > maximo:
            print(f"  ⚠  El valor debe estar entre {minimo} y {maximo}.")
            continue
        return num


def pedir_texto(mensaje):
    """Pide un texto no vacío; repite la pregunta si el usuario no escribe nada."""
    while True:
        txt = input(mensaje).strip()
        if txt:
            return txt
        print("  ⚠  Este campo no puede estar vacío.")


def pedir_si_no(mensaje):
    """
    Pregunta de sí/no. Devuelve True para s/si/sí/y/yes y False para n/no.
    Cualquier otra respuesta vuelve a preguntar.
    """
    while True:
        r = input(mensaje).strip().lower()
        if r in ("s", "si", "sí", "y", "yes"):
            return True
        if r in ("n", "no"):
            return False
        print("  ⚠  Responde 's' o 'n'.")


# =============================================================================
# LÓGICA DE CÁLCULO
# =============================================================================

def evaluar_armadura(cut_res, blunt_res, harpoon_res, body_coverage,
                     penalizaciones, bonificaciones):
    """
    Calcula los índices de una armadura.

    Args:
        cut_res, blunt_res, harpoon_res: resistencias a cortes, golpes
            contundentes y arpones.
        body_coverage: dict {parte_del_cuerpo: cobertura (0-1)}.
        penalizaciones: dict {stat: multiplicador}; un valor < 1 reduce el stat.
        bonificaciones: dict {stat: valor}; >1 se toma como multiplicador,
            <=1 como bonus plano.

    Returns:
        dict con armor_index, debuff_index, bonus_index, cobertura_promedio
        y promedio_resistencias (todos redondeados a 4 decimales).
    """

    # --- Cobertura promedio ---
    # Promedio de la cobertura de las partes registradas en la armadura.
    # Si no hay ninguna parte, la cobertura es 0 (evita dividir por cero).
    if body_coverage:
        cobertura_promedio = sum(body_coverage.values()) / len(body_coverage)
    else:
        cobertura_promedio = 0.0

    # --- Índice de armadura ---
    # Promedio simple de las tres resistencias, ponderado por la cobertura.
    promedio_resistencias = (cut_res + blunt_res + harpoon_res) / 3

    armor_index = promedio_resistencias * cobertura_promedio

    # --- Índice de debuff ---
    # Cada penalización aporta (1 - multiplicador): cuanto más bajo el
    # multiplicador, mayor la penalización. Nunca baja de 0.
    debuff_index = sum(1.0 - mult for mult in penalizaciones.values())
    debuff_index = max(0.0, debuff_index)

    # --- Índice de bonus ---
    # Dos casos según el valor de cada bonificación:
    bonus_total = 0.0
    for val in bonificaciones.values():
        if val > 1.0:
            # Multiplicador (ej: 1.10 = +10%): se suma solo el excedente sobre 1
            bonus_total += (val - 1.0)
        else:
            # Bonus plano (ej: +4 de ataque): se escala dividiendo por 10
            # (los valores negativos terminan restando)
            bonus_total += val / 10.0

    # Se devuelven todos los resultados redondeados a 4 decimales
    return {
        "armor_index":          round(armor_index, 4),
        "debuff_index":         round(debuff_index, 4),
        "bonus_index":          round(bonus_total, 4),
        "cobertura_promedio":   round(cobertura_promedio, 4),
        "promedio_resistencias": round(promedio_resistencias, 4),
    }


# =============================================================================
# COMPARATIVA DE LA BASE DE DATOS INTEGRADA
# =============================================================================

def comparar_todas_las_armaduras():
    """
    Evalúa todas las armaduras de ARMADURAS_DB, imprime una tabla ordenada por
    índice de armadura y muestra tres rankings:
      - Mejor equilibrio (Armor - Debuff + Bonus)
      - Top 3 por índice de armadura
      - Top 3 por índice de bonus
    """
    # Encabezado de la sección
    print("\n" + "=" * 100)
    print("  COMPARATIVA TOTAL DE ARMADURAS (Base de Datos - Grado Masterwork)")
    print("=" * 100)

    # Se calcula el índice de cada armadura de la base de datos
    resultados = []
    for nombre, datos in ARMADURAS_DB.items():
        # Se reutiliza la misma función de evaluación que en el ingreso manual
        res = evaluar_armadura(
            cut_res=datos["cut_res"],
            blunt_res=datos["blunt_res"],
            harpoon_res=datos["harpoon_res"],
            body_coverage=datos["cobertura"],
            penalizaciones=datos["penalizaciones"],
            bonificaciones=datos["bonificaciones"],
        )
        # Se agregan al resultado los datos descriptivos para mostrarlos luego
        res["nombre"] = nombre
        res["slot"] = datos["slot"]
        res["clase"] = datos["clase"]
        resultados.append(res)

    # Orden descendente por índice de armadura (la mejor protección primero)
    resultados.sort(key=lambda x: x["armor_index"], reverse=True)

    # Encabezado de columnas de la tabla
    print(f"\n  {'Armadura':<24} {'Slot':<9} {'Clase':<8} "
          f"{'ArmorIdx':>10} {'DebuffIdx':>11} {'BonusIdx':>10}")
    print("  " + "-" * 96)

    # Una fila por armadura
    for r in resultados:
        print(f"  {r['nombre']:<24} {r['slot']:<9} {r['clase']:<8} "
              f"{r['armor_index']:>10.4f} {r['debuff_index']:>11.4f} "
              f"{r['bonus_index']:>10.4f}")
    print("=" * 100)

    # --- Ranking 1: mejor equilibrio ---
    # Puntaje combinado: protección + bonus - penalizaciones
    mejor = max(resultados,
                key=lambda x: x["armor_index"] - x["debuff_index"] + x["bonus_index"])
    print(f"\n  🏆 Mejor equilibrio (Armor - Debuff + Bonus): {mejor['nombre']}")
    print(f"     ArmorIdx={mejor['armor_index']:.4f} | "
          f"DebuffIdx={mejor['debuff_index']:.4f} | "
          f"BonusIdx={mejor['bonus_index']:.4f}")

    # --- Ranking 2: top 3 por armadura pura ---
    # La lista ya está ordenada, alcanza con tomar los primeros 3
    print("\n  🛡️  Top 3 por Índice de Armadura puro:")
    for i, r in enumerate(resultados[:3], 1):
        print(f"     {i}. {r['nombre']} ({r['slot']}) → {r['armor_index']:.4f}")

    # --- Ranking 3: top 3 por bonus ---
    # Se reordena por bonus_index y se toman los 3 mayores
    top_bonus = sorted(resultados, key=lambda x: x["bonus_index"], reverse=True)[:3]
    print("\n  ✨ Top 3 por Índice de Bonus:")
    for i, r in enumerate(top_bonus, 1):
        print(f"     {i}. {r['nombre']} ({r['slot']}) → {r['bonus_index']:.4f}")


# =============================================================================
# INGRESO MANUAL DE ARMADURAS
# =============================================================================

def ingresar_armadura():
    """
    Guía al usuario para ingresar los datos de una armadura manualmente.

    Returns:
        dict: Datos de la armadura (resistencias, cobertura, penalizaciones,
              bonificaciones) junto con los tres índices calculados.

    El flujo es:
        1. Pedir nombre.
        2. Pedir las tres resistencias.
        3. Pedir la cobertura de cada parte del cuerpo.
        4. Pedir penalizaciones (solo se guardan las que tengan mult < 1).
        5. Pedir bonificaciones (solo se guardan las que sean ≠ 0).
        6. Llamar a evaluar_armadura() y devolver todo junto.
    """
    print("\n" + "=" * 55)
    print("  INGRESO MANUAL DE ARMADURA")
    print("=" * 55)

    # 1. Nombre (obligatorio)
    nombre = pedir_texto("Nombre: ")

    # 2. Resistencias: valores obligatorios entre 0.0 y 1.0
    print("\n-- Resistencias (0.0 a 1.0) --")
    cut_res = pedir_float("  Resistencia a CORTES:       ")
    blunt_res = pedir_float("  Resistencia a CONTUNDENTE: ")
    harpoon_res = pedir_float("  Resistencia a ARPONES:     ")

    # 3. Cobertura por parte del cuerpo: opcional, vacío se guarda como 0.0
    print("\n-- Cobertura por parte (0.0 a 1.0, vacío = 0) --")
    cobertura = {}
    for parte in PARTES_CUERPO:
        val = pedir_float(f"  {ETIQUETAS[parte]:<18}: ", permitir_vacio=True)
        cobertura[parte] = val if val is not None else 0.0

    # 4. Penalizaciones: solo se guardan los multiplicadores menores a 1.0
    print("\n-- PENALIZACIONES (multiplicador 0-1, vacío = sin penalización) --")
    penalizaciones = {}
    for stat in STATS_PENALIZABLES:
        val = pedir_float(f"  {stat:<22}: ", permitir_vacio=True)
        if val is not None and val < 1.0:
            penalizaciones[stat] = val

    # 5. Bonificaciones: rango ampliado (0 a 100); solo se guardan valores ≠ 0
    print("\n-- BONIFICACIONES (mult >1 o suma plana, vacío = sin bonus) --")
    bonificaciones = {}
    for stat in STATS_BONIFICABLES:
        val = pedir_float(f"  {stat:<22}: ", minimo=0.0, maximo=100.0,
                          permitir_vacio=True)
        if val is not None and val != 0:
            bonificaciones[stat] = val

    # 6. Cálculo de los índices con los datos ingresados
    resultado = evaluar_armadura(cut_res, blunt_res, harpoon_res,
                                 cobertura, penalizaciones, bonificaciones)

    # Se devuelve un único dict: datos ingresados + índices calculados
    return {
        "nombre": nombre,
        "cut_res": cut_res, "blunt_res": blunt_res, "harpoon_res": harpoon_res,
        "cobertura": cobertura,
        "penalizaciones": penalizaciones,
        "bonificaciones": bonificaciones,
        **resultado,
    }


def mostrar_resultado(d):
    """
    Imprime el detalle de una armadura ingresada manualmente: resistencias,
    cobertura, penalizaciones, bonificaciones y un cuadro final con los índices.

    Args:
        d: dict devuelto por ingresar_armadura().
    """
    print("\n" + "-" * 55)
    print(f"  RESULTADO: {d['nombre']}")
    print("-" * 55)

    # Resistencias expresadas en porcentaje
    print(f"\n  Resistencias: Corte {d['cut_res']*100:.1f}% | "
          f"Contundente {d['blunt_res']*100:.1f}% | "
          f"Arpones {d['harpoon_res']*100:.1f}%")

    # Cobertura: solo se listan las partes con cobertura mayor a 0
    print("\n  Cobertura:")
    for parte, val in d["cobertura"].items():
        if val > 0:
            print(f"    {ETIQUETAS[parte]:<18}: {val*100:5.1f}%")

    # Penalizaciones (si hay): se muestra el multiplicador y el % de reducción
    if d["penalizaciones"]:
        print("\n  Penalizaciones:")
        for stat, mult in d["penalizaciones"].items():
            print(f"    {stat:<22}: {mult:.2f}x ({(1-mult)*100:.1f}% menos)")

    # Bonificaciones (si hay): >1 se muestra como multiplicador, el resto como suma plana
    if d["bonificaciones"]:
        print("\n  Bonificaciones:")
        for stat, val in d["bonificaciones"].items():
            if val > 1.0:
                print(f"    {stat:<22}: {val:.2f}x (+{(val-1)*100:.1f}%)")
            else:
                print(f"    {stat:<22}: +{val:g}")

    # Cuadro resumen con los tres índices
    print("\n  ╔══════════════════════════════════════════╗")
    print(f"  ║  ÍNDICE DE ARMADURA: {d['armor_index']:.4f}  ({d['armor_index']*100:.1f}%)  ║")
    print(f"  ║  ÍNDICE DE DEBUFF:   {d['debuff_index']:.4f}  ({d['debuff_index']*100:.1f}%)  ║")
    print(f"  ║  ÍNDICE DE BONUS:    {d['bonus_index']:.4f}                  ║")
    print("  ╚══════════════════════════════════════════╝")


def comparar_manuales(armaduras):
    """
    Muestra una tabla comparativa de las armaduras ingresadas a mano,
    ordenadas de mayor a menor índice de armadura.

    Args:
        armaduras: lista de dicts devueltos por ingresar_armadura().
    """
    print("\n" + "=" * 85)
    print("  COMPARACIÓN DE ARMADURAS INGRESADAS MANUALMENTE")
    print("=" * 85)
    print(f"  {'Armadura':<24} {'ArmorIdx':>10} {'DebuffIdx':>12} {'BonusIdx':>10}")
    print("  " + "-" * 81)
    for d in sorted(armaduras, key=lambda x: x["armor_index"], reverse=True):
        print(f"  {d['nombre']:<24} {d['armor_index']:>10.4f} "
              f"{d['debuff_index']:>12.4f} {d['bonus_index']:>10.4f}")
    print("=" * 85)


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

def main():
    """
    Flujo principal del programa:
      1. Muestra el banner.
      2. Imprime la comparativa de la base de datos.
      3. Ofrece ingresar armaduras manualmente (repetible).
      4. Si se ingresó más de una, las compara entre sí.
    """
    # Banner de bienvenida
    print("╔═══════════════════════════════════════════════════╗")
    print("║   ANALIZADOR DE ARMADURAS DE KENSHI v4           ║")
    print("║   Base de datos integrada + comparativa total     ║")
    print("╚═══════════════════════════════════════════════════╝")

    # Comparativa automática de todas las armaduras de la base de datos
    comparar_todas_las_armaduras()

    # Modo manual opcional
    print("\n" + "-" * 100)
    if pedir_si_no("¿Querés ingresar armaduras manualmente para comparar? (s/n): "):
        armaduras = []
        # Se ingresan armaduras hasta que el usuario decida parar
        while True:
            armaduras.append(ingresar_armadura())
            mostrar_resultado(armaduras[-1])
            if not pedir_si_no("\n¿Ingresar otra armadura? (s/n): "):
                break

        # La comparación solo tiene sentido con 2 o más armaduras
        if len(armaduras) > 1:
            comparar_manuales(armaduras)

    print("\n¡Listo! Gracias por usar el analizador. 🛡️\n")


# Ejecuta main() solo si el archivo se corre directamente (no al importarlo)
if __name__ == "__main__":
    main()
