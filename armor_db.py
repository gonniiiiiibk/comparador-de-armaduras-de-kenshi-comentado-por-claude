# =============================================================================
# BASE DE DATOS DE ARMADURAS DE KENSHI  (armor_db.py)
# -----------------------------------------------------------------------------
# Contiene los datos que consume main.py:
#   - ARMADURAS_DB       → diccionario con todas las armaduras (grado Masterwork)
#   - PARTES_CUERPO      → partes del cuerpo que se pueden cubrir
#   - ETIQUETAS          → nombre legible de cada parte del cuerpo
#   - STATS_PENALIZABLES → stats que una armadura puede reducir
#   - STATS_BONIFICABLES → stats que una armadura puede mejorar
#
# Estructura de cada entrada de ARMADURAS_DB:
#   "Nombre": {
#       "slot":           ranura donde se equipa (Cabeza, Cuerpo, Camisa,
#                         Piernas, Pies)
#       "clase":          peso de la armadura (Pesada, Media, Ligera)
#       "cut_res":        resistencia a cortes
#       "blunt_res":      resistencia a golpes contundentes
#       "harpoon_res":    resistencia a arpones
#       "cobertura":      {parte_del_cuerpo: fracción cubierta (0-1)}
#       "penalizaciones": {stat: multiplicador}  (menor a 1 = reduce el stat)
#       "bonificaciones": {stat: valor}  (>1 multiplicador; <=1 bonus plano,
#                         pueden ser enteros como 4, 8 o negativos como -4)
#       "nota":           descripción en texto libre
#   }
# =============================================================================

ARMADURAS_DB = {

    # -------------------------------------------------------------------------
    # SLOT: CABEZA  (cascos y máscaras)
    # -------------------------------------------------------------------------

    # --- Cascos pesados ---
    "Samurai Helmet": {
        "slot": "Cabeza", "clase": "Pesada",
        "cut_res": 0.90, "blunt_res": 0.63, "harpoon_res": 0.945,
        "cobertura": {"cabeza": 1.0},
        "penalizaciones": {"Precision Shooting": 0.60, "Ataque Cuerpo a Cuerpo": 0.96},
        "bonificaciones": {},
        "nota": "El casco con mayor resistencia a cortes (90%). Penaliza precisión de ballesta y ataque cuerpo a cuerpo."
    },
    "Tin Can": {
        "slot": "Cabeza", "clase": "Pesada",
        # Nota: harpoon_res supera 1.0 (valor en puntos, no un porcentaje máximo)
        "cut_res": 0.90, "blunt_res": 0.60, "harpoon_res": 1.80,
        "cobertura": {"cabeza": 1.0},
        "penalizaciones": {"Esquiva": 0.70, "Ataque Cuerpo a Cuerpo": 0.95},
        "bonificaciones": {},
        "nota": "La mayor resistencia a arpones del juego (180 pts). Penaliza esquiva y ataque."
    },
    "Crab Helmet": {
        "slot": "Cabeza", "clase": "Pesada",
        "cut_res": 0.85, "blunt_res": 0.70, "harpoon_res": 0.90,
        "cobertura": {"cabeza": 1.0},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Excelente equilibrio entre corte (85%) y contundente (70%)."
    },
    "Ancient Samurai Helmet": {
        "slot": "Cabeza", "clase": "Pesada",
        "cut_res": 0.73, "blunt_res": 0.51, "harpoon_res": 0.765,
        "cobertura": {"cabeza": 0.95},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Versión antigua, ligeramente inferior al Samurai Helmet moderno."
    },
    "Paladin's Heavy Hachigane": {
        "slot": "Cabeza", "clase": "Pesada",
        "cut_res": 0.81, "blunt_res": 0.60, "harpoon_res": 0.855,
        "cobertura": {"cabeza": 0.90},
        "penalizaciones": {"Ataque Cuerpo a Cuerpo": 0.98},
        "bonificaciones": {},
        "nota": "Protección casi total de la cabeza para builds de combate cuerpo a cuerpo."
    },

    # --- Cascos medios ---
    "Armoured Hood": {
        "slot": "Cabeza", "clase": "Media",
        "cut_res": 0.35, "blunt_res": 0.21, "harpoon_res": 0.35,
        "cobertura": {"cabeza": 0.90},
        "penalizaciones": {"Ballestas": 0.90, "Precision Shooting": 0.90, "Ataque Cuerpo a Cuerpo": 0.98, "Defensa Cuerpo a Cuerpo": 0.98},
        "bonificaciones": {},
        "nota": "Capucha reforzada. Buen equilibrio para exploradores."
    },
    "Armoured Face Plates": {
        "slot": "Cabeza", "clase": "Media",
        "cut_res": 0.25, "blunt_res": 0.21, "harpoon_res": 0.35,
        "cobertura": {"cabeza": 0.75},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Protección facial sin penalizaciones severas."
    },
    "Masked Helmet": {
        "slot": "Cabeza", "clase": "Media",
        "cut_res": 0.35, "blunt_res": 0.21, "harpoon_res": 0.35,
        "cobertura": {"cabeza": 1.0},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Cobertura total de la cabeza con protección media."
    },

    # --- Cascos y máscaras ligeras ---
    "Hachigane": {
        "slot": "Cabeza", "clase": "Ligera",
        "cut_res": 0.65, "blunt_res": 0.39, "harpoon_res": 0.855,
        "cobertura": {"cabeza": 0.45},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Protección ligera para la frente. Alta resistencia a arpones."
    },
    "Rattan Hat": {
        "slot": "Cabeza", "clase": "Ligera",
        "cut_res": 0.17, "blunt_res": 0.11, "harpoon_res": 0.13,
        "cobertura": {"cabeza": 0.70},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Sombrero de ratán, protección mínima."
    },
    "Ninja Mask": {
        "slot": "Cabeza", "clase": "Ligera",
        "cut_res": 0.03, "blunt_res": 0.14, "harpoon_res": 0.0,
        "cobertura": {"cabeza": 0.90},
        "penalizaciones": {},
        "bonificaciones": {"Sigilo": 1.10},   # multiplicador: +10% sigilo
        "nota": "Máscara ninja. Bonus de sigilo."
    },
    "Swamp Ninja Mask": {
        "slot": "Cabeza", "clase": "Ligera",
        "cut_res": 0.17, "blunt_res": 0.11, "harpoon_res": 0.13,
        "cobertura": {"cabeza": 0.70},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Máscara de los ninjas del pantano."
    },
    "Fog Mask": {
        "slot": "Cabeza", "clase": "Ligera",
        "cut_res": 0.32, "blunt_res": 0.16, "harpoon_res": 0.71,
        "cobertura": {"cabeza": 0.70},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Protección contra gas y arpones."
    },
    "Skeleton Mask": {
        "slot": "Cabeza", "clase": "Ligera",
        "cut_res": 0.32, "blunt_res": 0.16, "harpoon_res": 0.25,
        "cobertura": {"cabeza": 0.70},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Máscara para esqueletos."
    },

    # -------------------------------------------------------------------------
    # SLOT: CUERPO  (armaduras de torso, abrigos y similares)
    # -------------------------------------------------------------------------

    # --- Armaduras de cuerpo pesadas ---
    "Crab Armour": {
        "slot": "Cuerpo", "clase": "Pesada",
        "cut_res": 0.90, "blunt_res": 0.665, "harpoon_res": 1.026,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 0.90, "brazo_derecho": 0.90},
        # Sigilo en 0.00 → penalización máxima (anula el stat)
        "penalizaciones": {"Sigilo": 0.00, "Ballestas": 0.30, "Esquiva": 0.25, "Velocidad de Combate": 0.90, "Destreza": 0.85},
        "bonificaciones": {},
        "nota": "La armadura de cuerpo con mayor resistencia a cortes (90%). Penalizaciones muy severas a sigilo y esquiva."
    },
    "Samurai Armour": {
        "slot": "Cuerpo", "clase": "Pesada",
        "cut_res": 0.81, "blunt_res": 0.6175, "harpoon_res": 0.855,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 1.0, "brazo_derecho": 1.0, "pierna_izquierda": 1.0, "pierna_derecha": 1.0},
        "penalizaciones": {"Velocidad de Combate": 0.94, "Destreza": 0.88, "Esquiva": 0.88, "Sigilo": 0.50, "Asesinato": 0.50},
        "bonificaciones": {"Ataque Cuerpo a Cuerpo": 4, "Defensa Cuerpo a Cuerpo": 4},   # bonus planos (+4)
        "nota": "Protección completa del torso y extremidades. Bonus a ataque y defensa."
    },
    "Holy Chest Plate": {
        "slot": "Cuerpo", "clase": "Pesada",
        "cut_res": 0.81, "blunt_res": 0.53, "harpoon_res": 0.855,
        "cobertura": {"pecho": 1.0, "estomago": 1.0},
        "penalizaciones": {"Velocidad de Combate": 0.90, "Destreza": 0.85},
        "bonificaciones": {},
        "nota": "Placa pectoral sagrada. Muy buena protección de torso."
    },
    "Unholy Chest Plate": {
        "slot": "Cuerpo", "clase": "Pesada",
        "cut_res": 0.81, "blunt_res": 0.53, "harpoon_res": 0.855,
        "cobertura": {"pecho": 1.0, "estomago": 1.0},
        "penalizaciones": {"Velocidad de Combate": 0.90, "Destreza": 0.85},
        "bonificaciones": {},
        "nota": "Versión corrupta de la placa sagrada. Mismas estadísticas."
    },

    # --- Armaduras de cuerpo medias ---
    "Black Plate Jacket": {
        "slot": "Cuerpo", "clase": "Media",
        "cut_res": 0.58, "blunt_res": 0.34, "harpoon_res": 0.33,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 1.0, "brazo_derecho": 1.0},
        "penalizaciones": {"Destreza": 0.95},
        "bonificaciones": {},
        "nota": "Chaqueta de placas negra. Buena protección media."
    },
    "Mercenary Leather Armour": {
        "slot": "Cuerpo", "clase": "Media",
        "cut_res": 0.58, "blunt_res": 0.37, "harpoon_res": 0.33,
        "cobertura": {"pecho": 1.0, "estomago": 0.70, "brazo_izquierdo": 0.80, "brazo_derecho": 0.80},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Armadura de cuero mercenaria. Sin penalizaciones."
    },
    "Conscript Leather Armour": {
        "slot": "Cuerpo", "clase": "Media",
        "cut_res": 0.53, "blunt_res": 0.41, "harpoon_res": 0.33,
        "cobertura": {"pecho": 1.0, "estomago": 0.70, "brazo_izquierdo": 0.80, "brazo_derecho": 0.80},
        "penalizaciones": {"Ballestas": 0.90, "Precision Shooting": 0.90, "Artes Marciales": 0.96},
        "bonificaciones": {},
        "nota": "Armadura de cuero de conscripto. Ligera penalización a artes marciales."
    },

    # --- Armaduras de cuerpo ligeras ---
    "Drifters Leather Jacket": {
        "slot": "Cuerpo", "clase": "Ligera",
        "cut_res": 0.44, "blunt_res": 0.33, "harpoon_res": 0.33,
        "cobertura": {"pecho": 1.0, "estomago": 0.80, "brazo_izquierdo": 0.60, "brazo_derecho": 0.60},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Chaqueta de cuero de vagabundo. Protección ligera."
    },
    "Dustcoat": {
        "slot": "Cuerpo", "clase": "Ligera",
        "cut_res": 0.44, "blunt_res": 0.28, "harpoon_res": 0.35,
        "cobertura": {"cabeza": 0.25, "pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 1.0, "brazo_derecho": 1.0, "pierna_izquierda": 0.60, "pierna_derecha": 0.60},
        "penalizaciones": {},
        "bonificaciones": {"Sigilo": 1.10},
        "nota": "Abrigo de polvo. Excelente cobertura ligera y bonus de sigilo."
    },
    "Longcoat": {
        "slot": "Cuerpo", "clase": "Ligera",
        "cut_res": 0.41, "blunt_res": 0.26, "harpoon_res": 0.33,
        "cobertura": {"cabeza": 0.25, "pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 1.0, "brazo_derecho": 1.0, "pierna_izquierda": 0.60, "pierna_derecha": 0.60},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Abrigo largo. Similar al Dustcoat pero sin bonus de sigilo."
    },
    "Assassin's Rags": {
        "slot": "Cuerpo", "clase": "Ligera",
        "cut_res": 0.41, "blunt_res": 0.26, "harpoon_res": 0.41,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 0.95, "brazo_derecho": 0.95},
        "penalizaciones": {},
        # Mezcla de multiplicadores (1.10, 1.20, 1.30) y bonus planos (8, -4, 6).
        # Defensa Cuerpo a Cuerpo es negativo: resta al índice de bonus.
        "bonificaciones": {
            "Sigilo": 1.10, "Ballestas": 1.10, "Esquiva": 1.20,
            "Velocidad de Combate": 1.10, "Destreza": 1.20, "Asesinato": 1.30,
            "Ataque Cuerpo a Cuerpo": 8, "Defensa Cuerpo a Cuerpo": -4, "Artes Marciales": 6
        },
        "nota": "La armadura de sigilo por excelencia. Bonus masivos a infiltración y asesinato."
    },
    "Holy Servant Rags": {
        "slot": "Cuerpo", "clase": "Ligera",
        "cut_res": 0.03, "blunt_res": 0.02, "harpoon_res": 0.0,
        "cobertura": {"pecho": 1.0, "estomago": 0.70, "brazo_izquierdo": 0.50, "brazo_derecho": 0.50},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Harapos de sirviente sagrado. Prácticamente sin protección."
    },

    # -------------------------------------------------------------------------
    # SLOT: CAMISA  (cotas de malla y camisas, se usan bajo la armadura)
    # -------------------------------------------------------------------------

    # --- Camisas medias (cotas de malla) ---
    "Blackened Chainmail": {
        "slot": "Camisa", "clase": "Media",
        "cut_res": 0.4896, "blunt_res": 0.2268, "harpoon_res": 0.315,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 1.0, "brazo_derecho": 1.0},
        "penalizaciones": {"Sigilo": 0.78, "Ballestas": 0.70, "Esquiva": 0.90, "Velocidad de Combate": 0.97, "Destreza": 0.85},
        "bonificaciones": {},
        "nota": "La mejor camisa de malla en resistencias. Penalizaciones notables a sigilo y ballestas."
    },
    "Chainmail": {
        "slot": "Camisa", "clase": "Media",
        "cut_res": 0.4464, "blunt_res": 0.2052, "harpoon_res": 0.285,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 1.0, "brazo_derecho": 1.0},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Opción sólida de camisa para la mayoría de builds. Menos resistente que la Blackened."
    },
    "Rusty Chainmail": {
        "slot": "Camisa", "clase": "Media",
        "cut_res": 0.40, "blunt_res": 0.18, "harpoon_res": 0.20,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 1.0, "brazo_derecho": 1.0},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Cota de malla oxidada. Protección inferior."
    },
    "Hive Chainmail": {
        "slot": "Camisa", "clase": "Media",
        "cut_res": 0.4464, "blunt_res": 0.2052, "harpoon_res": 0.285,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 1.0, "brazo_derecho": 1.0},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Cota de malla para colmena. Mismas estadísticas que la Chainmail estándar."
    },

    # --- Camisas ligeras ---
    "Dark Leather Shirt": {
        "slot": "Camisa", "clase": "Ligera",
        "cut_res": 0.359, "blunt_res": 0.2285, "harpoon_res": 0.1785,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 0.30, "brazo_derecho": 0.30},
        "penalizaciones": {},
        "bonificaciones": {"Sigilo": 1.10},
        "nota": "Camisa de cuero oscuro. Bonus de sigilo."
    },
    "Leather Turtleneck": {
        "slot": "Camisa", "clase": "Ligera",
        "cut_res": 0.33, "blunt_res": 0.21, "harpoon_res": 0.16,
        "cobertura": {"pecho": 1.0, "estomago": 1.0, "brazo_izquierdo": 0.30, "brazo_derecho": 0.30},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Cuello alto de cuero. Protección ligera."
    },
    "Rag Shirt": {
        "slot": "Camisa", "clase": "Ligera",
        "cut_res": 0.10, "blunt_res": 0.05, "harpoon_res": 0.0,
        "cobertura": {"pecho": 1.0, "estomago": 1.0},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Camisa de harapos. Protección mínima."
    },

    # -------------------------------------------------------------------------
    # SLOT: PIERNAS  (grebas, pantalones y faldas)
    # -------------------------------------------------------------------------

    # --- Piernas pesadas ---
    "Samurai Legplates": {
        "slot": "Piernas", "clase": "Pesada",
        "cut_res": 0.8125, "blunt_res": 0.6175, "harpoon_res": 0.855,
        "cobertura": {"estomago": 0.50, "pierna_izquierda": 1.0, "pierna_derecha": 1.0},
        "penalizaciones": {"Velocidad de Combate": 0.90, "Destreza": 0.90, "Atletismo": 0.85},
        "bonificaciones": {},
        "nota": "La protección de piernas más alta del juego."
    },
    "Ancient Samurai Legplates": {
        "slot": "Piernas", "clase": "Pesada",
        "cut_res": 0.73, "blunt_res": 0.51, "harpoon_res": 0.765,
        "cobertura": {"estomago": 0.50, "pierna_izquierda": 1.0, "pierna_derecha": 1.0},
        "penalizaciones": {"Velocidad de Combate": 0.90, "Destreza": 0.90, "Atletismo": 0.85},
        "bonificaciones": {},
        "nota": "Versión antigua de las legplates. Ligeramente inferior."
    },

    # --- Piernas ligeras ---
    "Samurai Clothpants": {
        "slot": "Piernas", "clase": "Ligera",
        "cut_res": 0.418, "blunt_res": 0.266, "harpoon_res": 0.3325,
        "cobertura": {"estomago": 0.50, "pierna_izquierda": 1.0, "pierna_derecha": 1.0},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Pantalones de tela samurái. Protección ligera."
    },
    "Armoured Rag Skirt": {
        "slot": "Piernas", "clase": "Ligera",
        "cut_res": 0.41, "blunt_res": 0.45, "harpoon_res": 0.3325,
        "cobertura": {"pierna_izquierda": 1.0, "pierna_derecha": 1.0},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Falda de harapos blindada. Curiosamente, más resistencia contundente que a cortes."
    },
    "Black Leather Skirt": {
        "slot": "Piernas", "clase": "Ligera",
        "cut_res": 0.41, "blunt_res": 0.45, "harpoon_res": 0.33,
        "cobertura": {"pierna_izquierda": 1.0, "pierna_derecha": 1.0},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Falda de cuero negro. Similar a la Armoured Rag Skirt."
    },
    "Gi Pants": {
        "slot": "Piernas", "clase": "Ligera",
        "cut_res": 0.03, "blunt_res": 0.16, "harpoon_res": 0.0,
        "cobertura": {"pierna_izquierda": 1.0, "pierna_derecha": 1.0},
        "penalizaciones": {},
        "bonificaciones": {"Artes Marciales": 2},   # bonus plano (+2)
        "nota": "Pantalones de gi. Bonus de +2 a artes marciales."
    },
    "Ninja Pants": {
        "slot": "Piernas", "clase": "Ligera",
        "cut_res": 0.23, "blunt_res": 0.08, "harpoon_res": 0.23,
        "cobertura": {"pierna_izquierda": 1.0, "pierna_derecha": 1.0},
        "penalizaciones": {},
        "bonificaciones": {"Sigilo": 1.10},
        "nota": "Pantalones ninja. Bonus de sigilo."
    },

    # -------------------------------------------------------------------------
    # SLOT: PIES  (botas y calzado; cubren solo el 40% de cada pierna)
    # -------------------------------------------------------------------------

    # --- Calzado pesado ---
    "Samurai Boots": {
        "slot": "Pies", "clase": "Pesada",
        "cut_res": 0.8125, "blunt_res": 0.6175, "harpoon_res": 0.855,
        "cobertura": {"pierna_izquierda": 0.40, "pierna_derecha": 0.40},
        "penalizaciones": {"Atletismo": 0.85},
        "bonificaciones": {},
        "nota": "Las botas más resistentes, a costa de atletismo."
    },

    # --- Calzado medio ---
    "Plated Longboots": {
        "slot": "Pies", "clase": "Media",
        "cut_res": 0.66, "blunt_res": 0.45, "harpoon_res": 0.76,
        "cobertura": {"pierna_izquierda": 0.40, "pierna_derecha": 0.40},
        "penalizaciones": {"Sigilo": 0.69, "Atletismo": 0.98},
        "bonificaciones": {},
        "nota": "Buen equilibrio protección/movilidad. Penalización leve a sigilo y atletismo."
    },

    # --- Calzado ligero ---
    "Drifter's Boots": {
        "slot": "Pies", "clase": "Ligera",
        "cut_res": 0.41, "blunt_res": 0.26, "harpoon_res": 0.33,
        "cobertura": {"pierna_izquierda": 0.40, "pierna_derecha": 0.40},
        "penalizaciones": {"Sigilo": 0.90},
        "bonificaciones": {},
        "nota": "Botas de vagabundo. Protección decente con penalización menor."
    },
    "Wooden Sandals": {
        "slot": "Pies", "clase": "Ligera",
        "cut_res": 0.0, "blunt_res": 0.0, "harpoon_res": 0.0,
        "cobertura": {"pierna_izquierda": 0.40, "pierna_derecha": 0.40},
        "penalizaciones": {},
        "bonificaciones": {"Atletismo": 1.10, "Velocidad de Combate": 1.05},
        "nota": "Sandalias de madera. Sin protección, pero bonus de atletismo y velocidad de combate."
    },

    # --- Otras botas pesadas ---
    "Crab Shoes": {
        "slot": "Pies", "clase": "Pesada",
        "cut_res": 0.73, "blunt_res": 0.51, "harpoon_res": 0.755,
        "cobertura": {"pierna_izquierda": 0.40, "pierna_derecha": 0.40},
        "penalizaciones": {},
        "bonificaciones": {},
        "nota": "Zapatos de cangrejo. Alta protección, ligeramente inferior a las Samurai Boots."
    },
    "Ancient Samurai Boots": {
        "slot": "Pies", "clase": "Pesada",
        "cut_res": 0.73, "blunt_res": 0.51, "harpoon_res": 0.755,
        "cobertura": {"pierna_izquierda": 0.40, "pierna_derecha": 0.40},
        "penalizaciones": {"Atletismo": 0.85},
        "bonificaciones": {},
        "nota": "Versión antigua de las botas samurái."
    },
}


# =============================================================================
# CONSTANTES AUXILIARES
# =============================================================================

# Partes del cuerpo que se pueden cubrir. main.py las recorre en este orden
# al pedir la cobertura en el ingreso manual.
PARTES_CUERPO = [
    "cabeza", "pecho", "estomago",
    "brazo_izquierdo", "brazo_derecho",
    "pierna_izquierda", "pierna_derecha",
]

# Nombre legible (para mostrar en pantalla) de cada parte del cuerpo
ETIQUETAS = {
    "cabeza":           "Cabeza",
    "pecho":            "Pecho",
    "estomago":         "Estómago",
    "brazo_izquierdo":  "Brazo Izq.",
    "brazo_derecho":    "Brazo Der.",
    "pierna_izquierda": "Pierna Izq.",
    "pierna_derecha":   "Pierna Der.",
}

# Stats que una armadura puede penalizar (se piden como multiplicador 0-1
# en el ingreso manual)
STATS_PENALIZABLES = [
    "Sigilo", "Ballestas", "Precision Shooting", "Esquiva",
    "Destreza", "Velocidad de Combate", "Atletismo", "Asesinato",
    "Daño de Ataque",
]

# Stats que una armadura puede bonificar (se piden como multiplicador o
# suma plana en el ingreso manual)
STATS_BONIFICABLES = [
    "Ataque Cuerpo a Cuerpo", "Defensa Cuerpo a Cuerpo",
    "Artes Marciales", "Protección de Puños",
    "Sigilo", "Ballestas", "Esquiva",
    "Destreza", "Velocidad de Combate", "Atletismo", "Asesinato",
]
