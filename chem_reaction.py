chem_reactions = {
"CO2": { 
    1: {
        "equation": "C + O2 → CO2",
        "property": "燃燒反應",
        "conditions": "點燃，氧氣充足",
        "reversible": False
    },
    2: {
        "equation": "2CO + O2 → 2CO2",
        "property": "燃燒反應",
        "conditions": "點燃",
        "reversible": False
    },
    3: {
        "equation": "CaCO3 → CaO + CO2",
        "property": "熱分解反應",
        "conditions": "高溫（>800°C）",
        "reversible": False
    },
    4: {
        "equation": "2NaHCO3 → Na2CO3 + H2O + CO2",
        "property": "熱分解反應",
        "conditions": "加熱",
        "reversible": False
    },
    5: {
        "equation": "CaCO3 + 2HCl → CaCl2 + H2O + CO2",
        "property": "與酸反應",
        "conditions": "稀鹽酸",
        "reversible": False
    },
    6: {
        "equation": "Na2CO3 + 2HCl → 2NaCl + H2O + CO2",
        "property": "與酸反應",
        "conditions": "稀鹽酸",
        "reversible": False
    },
    7: {
        "equation": "Ca(HCO3)2 → CaCO3 + H2O + CO2",
        "property": "熱分解反應",
        "conditions": "加熱",
        "reversible": False
    },
    8: {
        "equation": "CH4 + 2O2 → CO2 + 2H2O",
        "property": "燃燒反應",
        "conditions": "點燃",
        "reversible": False
    },
    9: {
        "equation": "C2H5OH + 3O2 → 2CO2 + 3H2O",
        "property": "燃燒反應",
        "conditions": "點燃",
        "reversible": False
    },
    10: {
        "equation": "C6H12O6 + 6O2 → 6CO2 + 6H2O",
        "property": "燃燒反應",
        "conditions": "點燃",
        "reversible": False
    },
    11: {
        "equation": "2C2H6 + 7O2 → 4CO2 + 6H2O",
        "property": "燃燒反應",
        "conditions": "點燃",
        "reversible": False
    },
    12: {
        "equation": "CaO + CO2 → CaCO3",
        "property": "化合反應",
        "conditions": "高 CO2 分壓",
        "reversible": False
    },
    13: {
        "equation": "MgO + CO2 → MgCO3",
        "property": "化合反應",
        "conditions": "加熱",
        "reversible": False
    },
    14: {
        "equation": "CO2 + H2O ⇌ H2CO3",
        "property": "溶水反應",
        "conditions": "水溶液",
        "reversible": True
    },
    15: {
        "equation": "6CO2 + 6H2O → C6H12O6 + 6O2",
        "property": "固碳反應（光合作用）",
        "conditions": "光照，葉綠素催化",
        "reversible": False
    },
},
"H2O": {
    1: {
        "equation": "2H2 + O2 → 2H2O",
        "property": "燃燒反應",
        "conditions": "點燃",
        "reversible": False
    },
    2: {
        "equation": "2H2O → 2H2 + O2",
        "property": "電解反應",
        "conditions": "直流電，稀硫酸或氫氧化鈉",
        "reversible": False
    },
    3: {
        "equation": "Na2O + H2O → 2NaOH",
        "property": "化合反應",
        "conditions": "水溶液",
        "reversible": False
    },
    4: {
        "equation": "CaO + H2O → Ca(OH)2",
        "property": "化合反應",
        "conditions": "水，放熱反應",
        "reversible": False
    },
    5: {
        "equation": "SO3 + H2O → H2SO4",
        "property": "溶水反應",
        "conditions": "水溶液",
        "reversible": False
    },
    6: {
        "equation": "CO2 + H2O ⇌ H2CO3",
        "property": "溶水反應",
        "conditions": "水溶液",
        "reversible": True
    },
    7: {
        "equation": "NH3 + H2O ⇌ NH4+ + OH-",
        "property": "溶水反應（弱鹼）",
        "conditions": "水溶液",
        "reversible": True
    },
    8: {
        "equation": "HCl + H2O → H3O+ + Cl-",
        "property": "溶水反應（強酸）",
        "conditions": "水溶液",
        "reversible": False
    },
    9: {
        "equation": "H2SO4 + H2O → H3O+ + HSO4-",
        "property": "溶水反應（強酸）",
        "conditions": "水溶液",
        "reversible": False
    },
    10: {
        "equation": "C6H12O6 + 6O2 → 6CO2 + 6H2O",
        "property": "燃燒反應",
        "conditions": "點燃",
        "reversible": False
    },
    11: {
        "equation": "CH4 + 2O2 → CO2 + 2H2O",
        "property": "燃燒反應",
        "conditions": "點燃",
        "reversible": False
    },
    12: {
        "equation": "Ca(HCO3)2 → CaCO3 + CO2 + H2O",
        "property": "分解反應",
        "conditions": "加熱",
        "reversible": False
    },
    13: {
        "equation": "2NaHCO3 → Na2CO3 + H2O + CO2",
        "property": "分解反應",
        "conditions": "加熱",
        "reversible": False
    },
    14: {
        "equation": "2C2H5OH + O2 → 2CH3CHO + 2H2O",
        "property": "氧化還原反應",
        "conditions": "Cu 或 Ag 催化，加熱",
        "reversible": False
    },
    15: {
        "equation": "2H2 + Cl2 → 2HCl + H2O",
        "property": "化合反應",
        "conditions": "光照",
        "reversible": False
    }
},
"NH3": {
    1: {
        "equation": "N2 + 3H2 → 2NH3",
        "property": "哈柏法",
        "conditions": {
            "temperature": "400-500°C",
            "pressure": "150-300 atm",
            "catalyst": "Fe"
        },
        "reversible": True
    },
    2: {
        "equation": "NH3 + HCl → NH4Cl",
        "property": "酸鹼反應",
        "conditions": {
            "state": "氣體或水溶液"
        },
        "reversible": False
    },
    3: {
        "equation": "2NH3 + H2SO4 → (NH4)2SO4",
        "property": "酸鹼反應",
        "conditions": {
            "state": "氣體或水溶液"
        },
        "reversible": False
    },
    4: {
        "equation": "4NH3 + 3O2 → 2N2 + 6H2O",
        "property": "燃燒反應",
        "conditions": {
            "temperature": "高溫",
            "ignition": "點燃"
        },
        "reversible": False
    },
    5: {
        "equation": "NH3 + CuO → Cu + H2O + N2",
        "property": "還原反應",
        "conditions": {
            "temperature": "加熱"
        },
        "reversible": False
    },
    6: {
        "equation": "NH3 + HNO3 → NH4NO3",
        "property": "酸鹼反應",
        "conditions": {
            "state": "水溶液或氣體吸收"
        },
        "reversible": False
    },
    7: {
        "equation": "NH3 + CO2 → NH4HCO3",
        "property": "酸鹼反應",
        "conditions": {
            "state": "水溶液或低溫吸收"
        },
        "reversible": False
    },
    8: {
        "equation": "NH3 + Cl2 → N2 + HCl",
        "property": "氧化還原反應",
        "conditions": {
            "temperature": "光照或加熱"
        },
        "reversible": False
    },
    9: {
        "equation": "NH3 + O2 → NO + H2O",
        "property": "氧化反應",
        "conditions": {
            "temperature": "高溫 (>800°C)",
            "catalyst": "Pt/ Rh"
        },
        "reversible": False
    },
    10: {
        "equation": "NH3 + Br2 → N2 + HBr",
        "property": "氧化還原反應",
        "conditions": {
            "temperature": "光照"
        },
        "reversible": False
    },
    11: {
        "equation": "NH3 + I2 → NI3 + H2",
        "property": "氧化還原反應",
        "conditions": {
            "temperature": "低溫",
            "note": "危險反應，極易爆炸"
        },
        "reversible": False
    },
    12: {
        "equation": "NH3 + ZnCl2 → [Zn(NH3)4]Cl2",
        "property": "配位反應",
        "conditions": {
            "state": "水溶液"
        },
        "reversible": True
    },
    13: {
        "equation": "NH3 + CuSO4 → [Cu(NH3)4]SO4",
        "property": "配位反應",
        "conditions": {
            "state": "水溶液"
        },
        "reversible": True
    },
    14: {
        "equation": "NH3 + H2O ⇌ NH4OH",
        "property": "鹼性反應",
        "conditions": {
            "state": "水溶液"
        },
        "reversible": True
    },
    15: {
        "equation": "2NH3 → N2 + 3H2",
        "property": "分解反應",
        "conditions": {
            "temperature": "高溫"
        },
        "reversible": False
    }
    },
    "NaCl": {
    1: {
        "equation": "NaOH + HCl → NaCl + H2O",
        "property": "酸鹼中和反應",
        "conditions": "水溶液",
        "reversible": False
    },
    2: {
        "equation": "NaCl → Na+ + Cl-",
        "property": "電解質解離反應",
        "conditions": "水溶液",
        "reversible": True
    },
    3: {
        "equation": "2NaCl → 2Na + Cl2",
        "property": "氯化鈉熔融電解",
        "conditions": "熔融 NaCl，直流電",
        "reversible": False
    },
    4: {
        "equation": "AgNO3 + NaCl → AgCl + NaNO3",
        "property": "沉澱反應",
        "conditions": "水溶液",
        "reversible": False
    },
    5: {
        "equation": "NaCl + H2SO4 → NaHSO4 + HCl",
        "property": "酸鹼反應",
        "conditions": "濃硫酸，加熱",
        "reversible": False
    },
    6: {
        "equation": "NaCl + Ag → AgCl + Na",
        "property": "置換反應",
        "conditions": "一般條件下不自發",
        "reversible": False
    },
    7: {
        "equation": "NaCl + Pb(NO3)2 → PbCl2 + NaNO3",
        "property": "沉澱反應",
        "conditions": "水溶液",
        "reversible": False
    },
    8: {
        "equation": "NaCl + KNO3 → KCl + NaNO3",
        "property": "離子交換反應",
        "conditions": "水溶液中無明顯反應",
        "reversible": False
    },
    9: {
        "equation": "NaCl + NH4OH → NH4Cl + NaOH",
        "property": "酸鹼反應",
        "conditions": "水溶液中無明顯反應",
        "reversible": False
    },
    10: {
        "equation": "NaCl + Ba(NO3)2 → BaCl2 + NaNO3",
        "property": "沉澱反應",
        "conditions": "生成物皆可溶，實際不反應",
        "reversible": False
    },
    11: {
        "equation": "NaCl + HNO3 → NaNO3 + HCl",
        "property": "酸鹼反應",
        "conditions": "水溶液中無淨反應",
        "reversible": False
    },
    12: {
        "equation": "NaCl + Ca(OH)2 → CaCl2 + NaOH",
        "property": "酸鹼反應",
        "conditions": "水溶液中無淨反應",
        "reversible": False
    },
    13: {
        "equation": "NaCl + Fe(NO3)3 → FeCl3 + NaNO3",
        "property": "沉澱反應",
        "conditions": "生成物皆可溶，無沉澱",
        "reversible": False
    },
    14: {
        "equation": "NaCl + Zn → ZnCl2 + Na",
        "property": "置換反應",
        "conditions": "一般條件下不自發",
        "reversible": False
    },
    15: {
        "equation": "NaCl + CuSO4 → CuCl2 + Na2SO4",
        "property": "離子交換反應",
        "conditions": "水溶液中無淨反應",
        "reversible": False
    }
},
    "CH4": {
    1: {
        "equation": "CH4 + 2O2 → CO2 + 2H2O",
        "property": "燃燒反應",
        "conditions": "點燃",
        "reversible": False
    },
    2: {
        "equation": "CH4 + H2O → CO + 3H2",
        "property": "重整反應（蒸氣重整）",
        "conditions": "700-1100°C，催化劑：Ni",
        "reversible": True
    },
    3: {
        "equation": "CH4 + Cl2 → CH3Cl + HCl",
        "property": "取代反應",
        "conditions": "光照",
        "reversible": False
    },
    4: {
        "equation": "CH4 + 4S → CS2 + 2H2S",
        "property": "硫化反應",
        "conditions": "高溫",
        "reversible": False
    },
    5: {
        "equation": "CH4 + O2 → C + 2H2O",
        "property": "不完全燃燒",
        "conditions": "點燃，氧氣不足",
        "reversible": False
    },
    6: {
        "equation": "CH4 + 2O2 → CO + 2H2O",
        "property": "不完全燃燒",
        "conditions": "點燃，氧氣不足",
        "reversible": False
    },
    7: {
        "equation": "CH4 + 2Cl2 → CH2Cl2 + 2HCl",
        "property": "取代反應",
        "conditions": "光照",
        "reversible": False
    },
    8: {
        "equation": "CH4 + 3Cl2 → CHCl3 + 3HCl",
        "property": "取代反應",
        "conditions": "光照",
        "reversible": False
    },
    9: {
        "equation": "CH4 + 4Cl2 → CCl4 + 4HCl",
        "property": "取代反應",
        "conditions": "光照",
        "reversible": False
    },
    10: {
        "equation": "CH4 + HNO3 → CH3NO2 + H2O",
        "property": "硝化反應",
        "conditions": "低溫",
        "reversible": False
    },
    11: {
        "equation": "CH4 + O2 → CO + 2H2",
        "property": "部分氧化反應",
        "conditions": "高溫，催化劑：Pt/Pd",
        "reversible": False
    },
    12: {
        "equation": "CH4 + 2O2 → HCHO + H2O",
        "property": "部分氧化反應",
        "conditions": "高溫，催化劑：Ag",
        "reversible": False
    },
    13: {
        "equation": "CH4 + NH3 → HCN + 3H2",
        "property": "氨化反應",
        "conditions": "高溫，催化劑：Pt/Rh",
        "reversible": False
    },
    14: {
        "equation": "CH4 + H2O → CO2 + 4H2",
        "property": "重整反應（蒸氣重整）",
        "conditions": "高溫，催化劑：Ni",
        "reversible": True
    },
    15: {
        "equation": "CH4 → C + 2H2",
        "property": "分解反應",
        "conditions": "高溫",
        "reversible": False
    }
},
    "Fe": {
    1: {
        "equation": "2Fe + O2 → 2FeO",
        "property": "氧化還原反應",
        "conditions": "高溫",
        "reversible": False
    },
    2: {
        "equation": "4Fe + 3O2 → 2Fe2O3",
        "property": "氧化還原反應",
        "conditions": "室溫或高溫",
        "reversible": False
    },
    3: {
        "equation": "3Fe + 2O2 → Fe3O4",
        "property": "氧化還原反應",
        "conditions": "高溫",
        "reversible": False
    },
    4: {
        "equation": "Fe + 2HCl → FeCl2 + H2",
        "property": "酸金屬反應",
        "conditions": "水溶液，稀 HCl",
        "reversible": False
    },
    5: {
        "equation": "Fe + H2SO4 → FeSO4 + H2",
        "property": "酸金屬反應",
        "conditions": "水溶液，稀 H2SO4",
        "reversible": False
    },
    6: {
        "equation": "Fe + Cl2 → FeCl3",
        "property": "氧化還原反應",
        "conditions": "加熱或光照",
        "reversible": False
    },
    7: {
        "equation": "Fe + Br2 → FeBr3",
        "property": "氧化還原反應",
        "conditions": "加熱",
        "reversible": False
    },
    8: {
        "equation": "Fe + I2 → FeI2",
        "property": "氧化還原反應",
        "conditions": "加熱",
        "reversible": False
    },
    9: {
        "equation": "Fe + S → FeS",
        "property": "硫化反應",
        "conditions": "加熱",
        "reversible": False
    },
    10: {
        "equation": "Fe + 2H2O → FeO + H2",
        "property": "氧化還原反應",
        "conditions": "高溫",
        "reversible": False
    },
    11: {
        "equation": "Fe + CuSO4 → FeSO4 + Cu",
        "property": "置換反應",
        "conditions": "水溶液",
        "reversible": False
    },
    12: {
        "equation": "Fe + 2AgNO3 → Fe(NO3)2 + 2Ag",
        "property": "置換反應",
        "conditions": "水溶液",
        "reversible": False
    },
    13: {
        "equation": "Fe + 2NaOH → Na2FeO2 + H2",
        "property": "鹼金屬反應",
        "conditions": "加熱，熔融 NaOH",
        "reversible": False
    },
    14: {
        "equation": "Fe + 2KOH → K2FeO2 + H2",
        "property": "鹼金屬反應",
        "conditions": "加熱，熔融 KOH",
        "reversible": False
    },
    15: {
        "equation": "Fe + O2 + H2O → Fe(OH)3",
        "property": "腐蝕反應",
        "conditions": "潮濕空氣，室溫",
        "reversible": False
    }
},

"Cl2": {
    1: {
        "equation": "Cl2 + H2 → 2HCl",
        "property": "氯化反應",
        "conditions": "點燃，需火花或光照",
        "reversible": False
    },
    2: {
        "equation": "Cl2 + H2O → HCl + HClO",
        "property": "溶水反應",
        "conditions": "水溶液，室溫",
        "reversible": True
    },
    3: {
        "equation": "Cl2 + 2Na → 2NaCl",
        "property": "金屬與氯反應",
        "conditions": "加熱或熔融 Na",
        "reversible": False
    },
    4: {
        "equation": "Cl2 + Fe → FeCl3",
        "property": "金屬與氯反應",
        "conditions": "加熱",
        "reversible": False
    },
    5: {
        "equation": "Cl2 + Cu → CuCl2",
        "property": "金屬與氯反應",
        "conditions": "加熱",
        "reversible": False
    },
    6: {
        "equation": "Cl2 + 2KBr → 2KCl + Br2",
        "property": "置換反應",
        "conditions": "水溶液",
        "reversible": False
    },
    7: {
        "equation": "Cl2 + 2KI → 2KCl + I2",
        "property": "置換反應",
        "conditions": "水溶液",
        "reversible": False
    },
    8: {
        "equation": "Cl2 + CH4 → CH3Cl + HCl",
        "property": "取代反應",
        "conditions": "光照",
        "reversible": False
    },
    9: {
        "equation": "Cl2 + C2H6 → C2H5Cl + HCl",
        "property": "取代反應",
        "conditions": "光照",
        "reversible": False
    },
    10: {
        "equation": "Cl2 + NaOH → NaCl + NaClO + H2O",
        "property": "歧化反應(冷)",
        "conditions": "室溫",
        "reversible": False
    },
    11: {
        "equation": "Cl2 + NaOH → NaCl + NaClO3 + H2O",
        "property": "歧化反應(熱)",
        "conditions": "加熱",
        "reversible": False
    },
    12: {
        "equation": "Cl2 + 2FeCl2 → 2FeCl3",
        "property": "氧化還原反應",
        "conditions": "水溶液",
        "reversible": False
    },
    13: {
        "equation": "Cl2 + 2SnCl2 → 2SnCl4",
        "property": "氧化還原反應",
        "conditions": "水溶液",
        "reversible": False
    },
    14: {
        "equation": "Cl2 + H2S → 2HCl + S",
        "property": "氧化還原反應",
        "conditions": "水溶液，室溫",
        "reversible": False
    },
    15: {
        "equation": "Cl2 + SO2 + 2H2O → H2SO4 + 2HCl",
        "property": "氧化還原反應",
        "conditions": "水溶液，室溫",
        "reversible": False
    }
},
"H2SO4": {
    1: {"equation": "SO3 + H2O → H2SO4", "property": "溶水反應", "conditions": "液態水，室溫", "reversible": True},
    2: {"equation": "H2SO4 + 2NaOH → Na2SO4 + 2H2O", "property": "酸鹼中和反應", "conditions": "水溶液，室溫", "reversible": False},
    3: {"equation": "H2SO4 + Zn → ZnSO4 + H2", "property": "氧化還原反應", "conditions": "稀 H2SO4，室溫", "reversible": False},
    4: {"equation": "NaCl + H2SO4 → NaHSO4 + HCl", "property": "酸鹼反應", "conditions": "加熱，濃 H2SO4", "reversible": False},
    5: {"equation": "Cu + 2H2SO4 → CuSO4 + SO2 + 2H2O", "property": "氧化還原反應", "conditions": "加熱，濃 H2SO4", "reversible": False},
    6: {"equation": "2NH3 + H2SO4 → (NH4)2SO4", "property": "酸鹼反應", "conditions": "氣態 NH3 與濃 H2SO4", "reversible": False},
    7: {"equation": "C6H12O6 + H2SO4 → 6C + 6H2O", "property": "熱分解反應", "conditions": "室溫，濃 H2SO4 脫水", "reversible": False},
    8: {"equation": "H2SO4 + BaCl2 → BaSO4 + 2HCl", "property": "沉澱反應", "conditions": "水溶液", "reversible": False},
    9: {"equation": "Fe + H2SO4 → FeSO4 + H2", "property": "酸金屬反應", "conditions": "稀 H2SO4，室溫", "reversible": False},
    10: {"equation": "H2SO4 + 2KOH → K2SO4 + 2H2O", "property": "酸鹼反應", "conditions": "水溶液", "reversible": False},
    11: {"equation": "H2SO4 + Na2CO3 → Na2SO4 + CO2 + H2O", "property": "酸鹼反應", "conditions": "水溶液", "reversible": False},
    12: {"equation": "H2SO4 + 2NaBr → Na2SO4 + Br2 + H2O", "property": "氧化還原反應", "conditions": "加熱，濃 H2SO4", "reversible": False}
},
"AgCl": {
    1: {"equation": "AgNO3 + NaCl → AgCl + NaNO3", "property": "沉澱反應", "conditions": "水溶液，室溫", "reversible": False},
    2: {"equation": "2AgCl → 2Ag + Cl2", "property": "分解反應", "conditions": "光照或加熱", "reversible": False},
    3: {"equation": "AgCl + 2NH3 → [Ag(NH3)2]Cl", "property": "配位反應", "conditions": "水溶液", "reversible": True},
    4: {"equation": "AgCl + 2Na2S2O3 → Na3[Ag(S2O3)2] + NaCl", "property": "配位反應", "conditions": "水溶液", "reversible": True},
    5: {"equation": "2AgCl + H2S → Ag2S + 2HCl", "property": "沉澱反應", "conditions": "水溶液", "reversible": False},
    6: {"equation": "AgCl + KI → AgI + KCl", "property": "置換反應", "conditions": "水溶液", "reversible": False},
    7: {"equation": "2AgCl + Na2S → Ag2S + 2NaCl", "property": "置換反應", "conditions": "水溶液", "reversible": False},
    8: {"equation": "AgCl + HNO3 → AgNO3 + HCl", "property": "置換反應", "conditions": "水溶液", "reversible": False},
    9: {"equation": "2AgCl + 2e- → 2Ag + 2Cl-", "property": "氧化還原反應", "conditions": "電解", "reversible": True},
    10: {"equation": "AgCl + 2OH- → Ag2O + Cl- + H2O", "property": "沉澱反應", "conditions": "水溶液", "reversible": False}
},
"PbCl2": {
    1: {"equation": "Pb(NO3)2 + 2NaCl → PbCl2 + 2NaNO3", "property": "沉澱反應", "conditions": "水溶液", "reversible": False},
    2: {"equation": "Pb + Cl2 → PbCl2", "property": "化合反應", "conditions": "加熱", "reversible": False},
    3: {"equation": "PbCl2 + 2NaOH → Pb(OH)2 + 2NaCl", "property": "沉澱反應", "conditions": "水溶液", "reversible": False},
    4: {"equation": "PbCl2 + H2SO4 → PbSO4 + 2HCl", "property": "沉澱反應", "conditions": "水溶液", "reversible": False}
},
    "CuSO4": {
    1: {"equation": "Cu + H2SO4 → CuSO4 + H2", "property": "置換反應", "conditions": "稀 H2SO4", "reversible": False},
    2: {"equation": "CuSO4 + 2NaOH → Cu(OH)2 + Na2SO4", "property": "沉澱反應", "conditions": "水溶液", "reversible": False},
    3: {"equation": "CuSO4 + Zn → ZnSO4 + Cu", "property": "置換反應", "conditions": "水溶液", "reversible": False},
    4: {"equation": "CuSO4 + NH3 → [Cu(NH3)4]SO4", "property": "配位反應", "conditions": "水溶液", "reversible": True}
},

"Na2CO3": {
    1: {"equation": "CO2 + 2NaOH → Na2CO3 + H2O", "property": "化合反應", "conditions": "水溶液", "reversible": True},
    2: {"equation": "NaHCO3 + NaOH → Na2CO3 + H2O", "property": "化合反應", "conditions": "水溶液", "reversible": False},
    3: {"equation": "Na2CO3 + CaCl2 → CaCO3 + 2NaCl", "property": "沉澱反應", "conditions": "水溶液", "reversible": False},
    4: {"equation": "Na2CO3 + H2SO4 → Na2SO4 + CO2 + H2O", "property": "酸鹼中和反應", "conditions": "水溶液", "reversible": False}
},

"CaO": {
    1: {"equation": "CaCO3 → CaO + CO2", "property": "分解反應", "conditions": "加熱", "reversible": False},
    2: {"equation": "CaO + H2O → Ca(OH)2", "property": "化合反應", "conditions": "水溶液", "reversible": True},
    3: {"equation": "CaO + 2HCl → CaCl2 + H2O", "property": "酸鹼中和反應", "conditions": "水溶液", "reversible": False},
    4: {"equation": "CaO + CO2 → CaCO3", "property": "化合反應", "conditions": "氣體或固體", "reversible": True}
},

"Fe2O3": {
    1: {"equation": "2Fe + 3/2O2 → Fe2O3", "property": "氧化還原反應", "conditions": "室溫", "reversible": False},
    2: {"equation": "Fe2O3 + 3CO → 2Fe + 3CO2", "property": "氧化還原反應", "conditions": "加熱", "reversible": False},
    3: {"equation": "Fe2O3 + 2Al → Al2O3 + 2Fe", "property": "置換反應", "conditions": "加熱", "reversible": False},
    4: {"equation": "Fe2O3 + 6HCl → 2FeCl3 + 3H2O", "property": "酸鹼中和反應", "conditions": "水溶液", "reversible": False}
},

    "KOH": {
    1: {"equation": "K2O + H2O → 2KOH", "property": "化合反應", "conditions": "液態水", "reversible": True},
    2: {"equation": "KOH + HCl → KCl + H2O", "property": "酸鹼中和反應", "conditions": "水溶液", "reversible": False},
    3: {"equation": "KOH + CO2 → KHCO3", "property": "化合反應", "conditions": "水溶液", "reversible": True},
    4: {"equation": "2KOH + CuSO4 → Cu(OH)2 + K2SO4", "property": "沉澱反應", "conditions": "水溶液", "reversible": False}
},

"HNO3": {
    1: {"equation": "N2O5 + H2O → 2HNO3", "property": "化合反應", "conditions": "水溶液", "reversible": True},
    2: {"equation": "HNO3 + Cu → Cu(NO3)2 + NO2 + H2O", "property": "氧化還原反應", "conditions": "濃 HNO3，加熱", "reversible": False},
    3: {"equation": "HNO3 + NaOH → NaNO3 + H2O", "property": "酸鹼中和反應", "conditions": "水溶液", "reversible": False},
    4: {"equation": "3HNO3 + P → H3PO4 + 3NO2", "property": "氧化還原反應", "conditions": "加熱", "reversible": False}
},

"CH3COOH": {
    1: {"equation": "CH3COOH + NaOH → CH3COONa + H2O", "property": "酸鹼中和反應", "conditions": "水溶液", "reversible": False},
    2: {"equation": "2CH3COOH → (CH3CO)2O + H2O", "property": "分解反應", "conditions": "加熱", "reversible": False},
    3: {"equation": "CH3COOH + C2H5OH ⇌ CH3COOC2H5 + H2O", "property": "化合反應", "conditions": "濃 H2SO4，室溫", "reversible": True},
    4: {"equation": "CH3COOH + NaHCO3 → CH3COONa + CO2 + H2O", "property": "酸鹼中和反應", "conditions": "水溶液", "reversible": False}
}
}