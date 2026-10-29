"""
13_build_custom_gmt.py
======================
Generador unificado y reproducible de firmas moleculares personalizadas (GMT y JSON).
Consolida:
1. CellAge (Inductores e Inhibidores de Senescencia celular)
2. SASP Canónico de Reactome 2022 (R-HSA-2559582)
3. Firmas de Agotamiento vs Memoria Linfoide GSE9650 (CD8+ T cells UP / DN)
"""

import os
import json
import pandas as pd

def build_custom_gmt(output_dir="data/gene_sets"):
    os.makedirs(output_dir, exist_ok=True)
    custom_gmt = {}

    # 1. Firmas CellAge (Inductores e Inhibidores)
    cellage_path = "docs/cellAge/cellage3.tsv"
    if os.path.exists(cellage_path):
        df_cellage = pd.read_csv(cellage_path, sep="\t")
        genes_induces = df_cellage[df_cellage['Senescence Effect'] == 'Induces']['Gene symbol'].dropna().unique().tolist()
        genes_inhibits = df_cellage[df_cellage['Senescence Effect'] == 'Inhibits']['Gene symbol'].dropna().unique().tolist()
        custom_gmt["CELLAGE_SENESCENCE_INDUCES"] = sorted(genes_induces)
        custom_gmt["CELLAGE_SENESCENCE_INHIBITS"] = sorted(genes_inhibits)
        print(f"[OK] CellAge cargado: {len(genes_induces)} Inductores, {len(genes_inhibits)} Inhibidores.")
    else:
        print(f"[WARN] Advertencia: No se encontró {cellage_path}, utilizando lista curada por defecto.")
        # Respaldo curado CellAge si el TSV no estuviera presente
        custom_gmt["CELLAGE_SENESCENCE_INDUCES"] = ["CDKN2A", "CDKN1A", "TP53", "RB1", "ATM", "ATR", "CHEK1", "CHEK2", "PTEN"]
        custom_gmt["CELLAGE_SENESCENCE_INHIBITS"] = ["TERT", "MYC", "SIRT1", "SIRT6", "BMI1", "CCND1"]

    # 2. SASP Canónico de Reactome (R-HSA-2559582)
    # Extraído de la base curada Reactome 2022 (60 genes canónicos del fenotipo secretor)
    reactome_sasp_genes = [
        "ANAPC1", "ANAPC10", "ANAPC11", "ANAPC15", "ANAPC16", "ANAPC2", "ANAPC4", "ANAPC5", "ANAPC7",
        "CDC16", "CDC23", "CDC26", "CDC27", "CDK2", "CDK4", "CDK6", "CDKN1B", "CDKN2A", "CDKN2C", "CDKN2D",
        "CEBPB", "CXCL8", "EHMT1", "EHMT2", "FOS", "FZR1", "H2AC14", "H2AC19", "H2AC20", "H2AC4", "H2AC6",
        "H2AC7", "H2AJ", "H2AX", "H2AZ1", "H2AZ2", "H2BC11", "H2BC12", "H2BC15", "H2BC21", "H2BC4", "H2BC5",
        "H2BC9", "H3-3B", "H3C13", "IGFBP7", "JUN", "MAPK1", "MAPK3", "MAPK7", "NFKB1", "RELA", "STAT3",
        "UBA52", "UBB", "UBC", "UBE2C", "UBE2D1", "UBE2E1", "UBE2S"
    ]
    custom_gmt["REACTOME_SASP_R_HSA_2559582"] = sorted(reactome_sasp_genes)
    print(f"[OK] Reactome SASP (R-HSA-2559582) incorporado: {len(reactome_sasp_genes)} genes.")

    # 3. Firmas de Agotamiento vs Memoria GSE9650 (Inmunología Molecular / C7)
    gse9650_dn_genes = [
        "ABLIM1", "ACSS1", "ADD1", "ADCY7", "ADRB2", "ANAPC16", "ANAPC5", "ANTKMT", "ANXA1", "ANXA5",
        "ANXA6", "AP3M1", "APEX1", "API5", "ARL4C", "ARL6IP5", "ARMC1", "ATP6V1H", "AURKAIP1", "AXIN1",
        "BCL2", "BLVRA", "BNIP3L", "CALU", "CCDC115", "CCND3", "CCNDBP1", "CCT4", "CCT6A", "CCT8",
        "CDC37", "CD44", "CHP1", "CLP1", "COPS5", "CUX1", "DERL2", "DGKA", "DNAJC7", "DUSP1",
        "DYM", "EBNA1BP2", "EEIG1", "EIF1", "EIF2S1", "EIF3B", "ELAVL1", "ELOVL5", "ENTPD4", "ETS1",
        "EXOSC7", "FAM107B", "FAM117A", "FAM89B", "FARSB", "FBL", "FCGR2B", "FOS", "GABARAPL2", "GALNT10",
        "GALNT11", "GLO1", "GNPAT", "GOLM1", "GRAMD2B", "HADHB", "HEXA", "HMCES", "HPCAL1", "ICAM2",
        "IFITM10", "IFRD2", "IKBKE", "IL17RA", "IL18R1", "IL18RAP", "IL7R", "IMPDH2", "IQGAP2", "IRF2BP1",
        "ITGAL", "ITGAX", "ITGB2", "ITGB7", "ITPA", "KCTD10", "KLF6", "KLRC1", "KLRD1", "KLRK1",
        "LARP1", "LDAH", "LDHA", "MACIR", "MAP1LC3B", "MAT2A", "MBP", "MIEN1", "MOGS", "MRPL37",
        "MRPL50", "NDUFA9", "NGDN", "NHERF1", "NSMCE1", "NUDCD3", "NUDT16L1", "OAZ1", "ORC5", "PACS1",
        "PARK7", "PDK1", "PFKP", "PIGU", "PIGX", "PIK3CD", "PIK3R1", "PIP4P2", "PITPNC1", "PLAC8",
        "PLP2", "POLDIP2", "PRKCB", "PRPSAP1", "PSMD13", "PWP1", "RABAC1", "RABGGTA", "RERE", "RHOA",
        "RNASEH2A", "RNPS1", "RPN1", "RREB1", "SACM1L", "SAE1", "SARAF", "SATB1", "SELENOH", "SELL",
        "SETD4", "SLCO3A1", "SLC1A5", "SLC25A51", "SMARCA2", "SMU1", "SNIP1", "SNRNP40", "SPTLC1", "SRI",
        "SRPK1", "SS18", "STK16", "STK38", "SUCLG1", "SWI5", "TAF11", "TAGLN2", "TLE4", "TM9SF2",
        "TMEM222", "TOB1", "TRAM1", "TSPAN31", "TUBB", "TWF2", "UBALD2", "UFC1", "USP24", "VAV1",
        "VPS25", "WDR13", "WDR43", "XRCC5", "YES1", "YIF1A", "YIPF1", "ZFP36"
    ]
    custom_gmt["GSE9650_EXHAUSTED_VS_MEMORY_CD8_TCELL_DN"] = sorted(gse9650_dn_genes)

    gse9650_up_genes = [
        "ACADVL", "ADGRG1", "AOPEP", "ATP5IF1", "ATP5MF", "AUH", "BCL2L11", "BCL3", "CANX", "CCDC28B",
        "CCDC93", "CD244", "CEP250", "CFH", "CISH", "CRYZ", "CSRP1", "CXCR2", "CYTH3", "DDIT4",
        "DHRS7B", "DLG3", "DPP7", "EEA1", "EGR2", "ELK1", "EOMES", "ERCC5", "FASLG", "FLNA",
        "GAMT", "GCSAM", "GPD2", "GTF3C4", "GZMB", "H1-4", "H1-5", "HIF1A", "IFI27L2", "IFIH1",
        "IMMT", "ITGAV", "KCTD9", "LAT2", "LCLAT1", "LHPP", "LITAF", "LRP10", "LY75", "MFHAS1",
        "MKI67", "MRPL48", "MRPS2", "MYO6", "MYRF", "NDUFB4", "NDUFS4", "NELFE", "PARP1", "PERP",
        "PLOD3", "PLSCR1", "POLR2C", "PRDM1", "PRRC1", "PTCH1", "PTMS", "PTPN11", "PTPRA", "PTPRJ",
        "RGS16", "RPRD1B", "SEC14L1", "SHMT2", "SLC27A4", "SLC4A7", "SLC4A8", "SLX9", "SPOCK2", "SURF4",
        "SYPL1", "TBL1X", "TERF1", "TFDP1", "TLN1", "TMEM150A", "TMEM214", "TNFRSF4", "TWSG1", "VAMP5",
        "VMP1", "WDR55", "WIZ", "ZNF292", "ZNF35", "ZNF821"
    ]
    custom_gmt["GSE9650_EXHAUSTED_VS_MEMORY_CD8_TCELL_UP"] = sorted(gse9650_up_genes)
    print(f"[OK] GSE9650 Agotamiento vs Memoria cargado: {len(gse9650_dn_genes)} DN, {len(gse9650_up_genes)} UP.")

    # Guardar en formato JSON y GMT
    json_path = os.path.join(output_dir, "custom_senescence_signatures.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(custom_gmt, f, indent=4)
        
    gmt_path = os.path.join(output_dir, "custom_senescence_signatures.gmt")
    with open(gmt_path, 'w', encoding='utf-8') as f:
        for term, genes in custom_gmt.items():
            f.write(f"{term}\tcustom_signatures\t" + "\t".join(genes) + "\n")
            
    print(f"\n[OK] Firmas generadas exitosamente:")
    print(f" - JSON: {json_path}")
    print(f" - GMT:  {gmt_path}")
    print(f" - Total de conjuntos de genes: {len(custom_gmt)}")
    return custom_gmt

if __name__ == "__main__":
    build_custom_gmt()
