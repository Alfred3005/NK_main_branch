#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las figuras 1a, 1b, 2a, 2b, 2c, 3a y 3b y las tablas de la cohorte.

Parte de data/NK_dataset_qc_ready.h5ad (o de la ruta que se pase como argumento):
    python scripts/30_figuras_cohorte.py [ruta_al_h5ad]

Tablas que produce, en results/subtypes/:
    tabla_demografica_subtipos.tsv  cifras de la Tabla de demografía de Resultados
    tabla_estudios.tsv              cifras de la tabla de estudios del Anexo A
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import umap

ROOT = Path(__file__).resolve().parent.parent
RUTA_H5AD = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "NK_dataset_qc_ready.h5ad"
TABLAS = ROOT / "results" / "subtypes"
CARPETAS_FIG = [
    ROOT / "tesis" / "figures_clean",
    ROOT / "tesis" / "manuscripts" / "figures",
    ROOT / "tesis" / "manuscripts" / "figures_clean",
]
SEMILLA = 42

GRUPOS = ["adult", "old"]
ETIQUETA = {"adult": "Adultos (35-59 años)", "old": "Adultos mayores (60 años o más)"}
ETIQUETA_CORTA = {"adult": "Adultos", "old": "Adultos mayores"}
COLOR = {"adult": "#e89a4f", "old": "#b5403d"}

# Colecciones de CZ CELLxGENE, verificadas por dataset_id en su API de curación.
ESTUDIOS = {
    "b0e547f0-462b-4f81-b31b-5b0a5d96f537": "Kock et al. (2025)",
    "3faad104-2ab8-4434-816d-474d8d2641db": "Yazar et al. (2022)",
    "218acb0f-9f2f-4f76-b90b-15a4b7c7f629": "Perez et al. (2022)",
    "30cd5311-6c09-46c9-94f1-71fe4b91813c": "Liu et al. (2021)",
    "456e8b9b-f872-488b-871d-94534090a865": "Wilk et al. (2020)",
    "c7775e88-49bf-4ba2-a03b-93f00447c958": "Stephenson et al. (2021)",
    "9dbab10c-118d-496b-966a-67f1763a6b7d": "Ren et al. (2021)",
    "53d208b0-2cfd-4366-9866-c3c6114081bc": "Tabula Sapiens (2022)",
    "19e46756-9100-4e01-8b0e-23b557558a4c": "Heimlich et al. (2024)",
    "de2c780c-1747-40bd-9ccf-9588ec186cee": "Lee et al. (2020)",
    "3c75a463-6a87-4132-83a8-c3002624394d": "Rodríguez-Ubreva et al. (2022)",
    "59b69042-47c2-47fd-ad03-d21beb99818f": "Jin et al. (2021)",
    "8c42cfd0-0b0a-46d5-910c-fc833d83c45e": "Travaglini et al. (2020)",
}
SUBTIPOS = {
    "CD16-positive, CD56-dim natural killer cell, human": "CD56dim anotada",
    "CD16-negative, CD56-bright natural killer cell, human": "CD56bright",
    "natural killer cell": "NK sin subtipo",
    "mature NK T cell": "NKT",
    "type I NK T cell": "NKT",
}
MARCADORES_AMBIENTALES = ["HBB", "HBA1", "HBA2", "IGHG1", "IGKC", "JCHAIN", "LYZ"]
MARCADORES_PUREZA = {
    "Células NK": ["NKG7", "GNLY", "CST7", "GZMA", "PRF1", "KLRD1", "KLRF1"],
    "Linfocitos T": ["CD3D", "CD3E", "CD3G", "TRAC"],
    "Linfocitos B": ["CD79A", "MS4A1", "CD19"],
}
ENSAYOS = ["10x 3' v2", "10x 3' v3", "10x 3' transcription profiling", "10x 5' v1", "10x 5' v2",
           "Seq-Well", "Smart-seq2"]
COLOR_ENSAYO = ["#fc8d62", "#8da0cb", "#66c2a5", "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"]


def guardar(fig, nombre, dpi=300):
    fig.tight_layout()
    for carpeta in CARPETAS_FIG:
        fig.savefig(carpeta / f"{nombre}.png", dpi=dpi)
    plt.close(fig)
    print("Figura:", nombre)


def estilo(ax):
    ax.spines[["top", "right"]].set_visible(False)


def densa(matriz):
    return matriz.toarray() if hasattr(matriz, "toarray") else np.asarray(matriz)


def tablas(obs):
    donantes = obs.drop_duplicates("donor_id")
    filas = []
    for g in GRUPOS + ["total"]:
        o = obs if g == "total" else obs[obs.age_group == g]
        d = donantes if g == "total" else donantes[donantes.age_group == g]
        conteo = o.subtipo.value_counts()
        fila = {
            "grupo": g, "donantes": d.donor_id.nunique(), "celulas": len(o),
            "edad_media": round(d.age.mean(), 1), "edad_de": round(d.age.std(), 1),
            "mujeres": int((d.sex == "female").sum()), "hombres": int((d.sex == "male").sum()),
            "umi_mediana": o.total_counts.median(), "genes_mediana": o.n_genes_by_counts.median(),
            "mt_mediana": round(o.pct_counts_mito.median(), 2),
        }
        for s in ["CD56dim anotada", "CD56bright", "NK sin subtipo", "NKT"]:
            fila[s] = int(conteo.get(s, 0))
            fila[f"{s} %"] = round(100 * conteo.get(s, 0) / len(o), 1)
        filas.append(fila)
    pd.DataFrame(filas).to_csv(TABLAS / "tabla_demografica_subtipos.tsv", sep="\t", index=False)

    g = obs.groupby("estudio", observed=True)
    estudios = pd.DataFrame({
        "dataset_id": g.dataset_id.first(),
        "celulas": g.size(),
        "donantes": g.donor_id.nunique(),
        "adultos": g.age_group.apply(lambda s: int((s == "adult").sum())),
        "adultos_mayores": g.age_group.apply(lambda s: int((s == "old").sum())),
    }).sort_values("celulas", ascending=False)
    estudios.to_csv(TABLAS / "tabla_estudios.tsv", sep="\t")
    return estudios


def fig1a(estudios):
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(estudios))
    ax.bar(x, estudios.adultos, color=COLOR["adult"], label=ETIQUETA["adult"], edgecolor="black", linewidth=0.4)
    ax.bar(x, estudios.adultos_mayores, bottom=estudios.adultos, color=COLOR["old"],
           label=ETIQUETA["old"], edgecolor="black", linewidth=0.4)
    for i, total in enumerate(estudios.celulas):
        ax.text(i, total + 700, f"{total:,}", ha="center", fontsize=8)
    ax.set_xticks(x, estudios.index, rotation=45, ha="right", fontsize=9)
    ax.set_ylabel("Número de células")
    ax.set_xlabel("Estudio")
    ax.legend(frameon=False)
    estilo(ax)
    guardar(fig, "fig1a")


def fig1b(adata):
    genes = [g for g in MARCADORES_AMBIENTALES if g in adata.var_names]
    sub = adata[:, genes]
    antes = densa(sub.layers["raw_counts"]).mean(axis=0)
    despues = densa(sub.layers["counts"]).mean(axis=0)
    print(pd.DataFrame({"antes": antes, "despues": despues}, index=genes).round(3).to_string())
    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.arange(len(genes))
    ax.bar(x - 0.2, antes, 0.4, color="#e8877c", label="Sin corregir")
    ax.bar(x + 0.2, despues, 0.4, color="#8ec6dd", label="Corregido con scAR")
    ax.set_xticks(x, genes, fontstyle="italic")
    ax.set_ylabel("Conteo medio por célula")
    ax.set_xlabel("Gen")
    ax.legend(frameon=False)
    estilo(ax)
    guardar(fig, "fig1b")


def fig2a(donantes):
    fig, ax = plt.subplots(figsize=(8, 4.8))
    cortes = np.arange(35, 96)
    for g in GRUPOS:
        ax.hist(donantes[donantes.age_group == g].age, bins=cortes, color=COLOR[g], edgecolor="black",
                linewidth=0.5, label=ETIQUETA[g])
    ax.axvline(60, color="black", linestyle="--", linewidth=1, label="Corte entre grupos (60 años)")
    ax.set_xlabel("Edad (años)")
    ax.set_ylabel("Número de donantes")
    ax.legend(frameon=False)
    estilo(ax)
    guardar(fig, "fig2a")


def barras_por_grupo(ax, tabla, colores):
    base = np.zeros(2)
    for col, color in zip(tabla.columns, colores):
        valores = tabla[col].values
        ax.bar([0, 1], valores, 0.55, bottom=base, color=color, edgecolor="black", linewidth=0.5, label=col)
        for i, v in enumerate(valores):
            if v >= 8:
                ax.text(i, base[i] + v / 2, str(int(v)), ha="center", va="center", fontsize=9, fontweight="bold")
        base = base + valores
    ax.set_xticks([0, 1], [ETIQUETA_CORTA[g] for g in GRUPOS])
    ax.set_ylabel("Número de donantes")
    ax.set_xlabel("Grupo de edad")
    estilo(ax)


def fig2b(donantes):
    tabla = pd.crosstab(donantes.age_group, donantes.sex).reindex(GRUPOS)[["female", "male"]]
    tabla.columns = ["Mujeres", "Hombres"]
    fig, ax = plt.subplots(figsize=(6, 4.6))
    barras_por_grupo(ax, tabla, ["#d98cb3", "#7fa8d1"])
    ax.legend(frameon=False, bbox_to_anchor=(1.01, 0.5), loc="center left", title="Sexo")
    guardar(fig, "fig2b")


def fig2c(obs):
    # Un donante del estudio Tabula Sapiens tiene dos tecnologías y cuenta en ambas.
    pares = obs.drop_duplicates(["donor_id", "assay"])
    tabla = pd.crosstab(pares.age_group, pares.assay.astype(str)).reindex(GRUPOS)
    tabla = tabla.reindex(columns=[e for e in ENSAYOS if e in tabla.columns], fill_value=0)
    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    barras_por_grupo(ax, tabla, COLOR_ENSAYO)
    ax.legend(frameon=False, bbox_to_anchor=(1.01, 0.5), loc="center left", title="Tecnología", fontsize=8)
    guardar(fig, "fig2c")


def fig3a(adata):
    genes = [g for grupo in MARCADORES_PUREZA.values() for g in grupo]
    sub = sc.AnnData(densa(adata[:, genes].X).astype(float), obs=adata.obs[["age_group"]].copy(),
                     var=pd.DataFrame(index=genes))
    escala = 1e4 / adata.obs.total_counts.values
    sub.X = np.log1p(sub.X * escala[:, None])
    medias = np.array([sub.X[(sub.obs.age_group == g).values].mean(axis=0) for g in GRUPOS])
    fraccion = np.array([(sub.X[(sub.obs.age_group == g).values] > 0).mean(axis=0) for g in GRUPOS])
    fig, ax = plt.subplots(figsize=(9, 3.2))
    xx, yy = np.meshgrid(np.arange(len(genes)), [1, 0])
    puntos = ax.scatter(xx.ravel(), yy.ravel(), s=fraccion.ravel() * 260, c=medias.ravel(), cmap="Blues",
                        vmin=0, edgecolor="grey", linewidth=0.4)
    ax.set_xticks(np.arange(len(genes)), genes, rotation=90, fontstyle="italic")
    ax.set_yticks([1, 0], [ETIQUETA_CORTA[g] for g in GRUPOS])
    ax.set_ylim(-0.6, 1.6)
    inicio = 0
    for nombre, grupo in MARCADORES_PUREZA.items():
        ax.annotate(nombre, xy=(inicio + (len(grupo) - 1) / 2, 1.0), xycoords=("data", "axes fraction"),
                    xytext=(0, 6), textcoords="offset points", ha="center", fontweight="bold")
        if inicio:
            ax.axvline(inicio - 0.5, color="grey", linewidth=0.6)
        inicio += len(grupo)
    fig.colorbar(puntos, ax=ax, label="Expresión media\n(log CP10K)", fraction=0.03, pad=0.02)
    for f in [0.25, 0.5, 0.75, 1.0]:
        ax.scatter([], [], s=f * 260, color="grey", label=f"{int(f * 100)}%")
    ax.legend(title="Células que\nlo expresan", frameon=False, bbox_to_anchor=(1.17, 0.5), loc="center left",
              fontsize=8, title_fontsize=8)
    guardar(fig, "fig3a")


def fig3b(adata):
    genes = adata.var_names[adata.var.highly_variable.values]
    sub = sc.AnnData(adata[:, genes].X.astype(np.float32).copy(), obs=adata.obs[["age_group"]].copy(),
                     var=pd.DataFrame(index=genes))
    sub.X = sub.X.multiply(1e4 / adata.obs.total_counts.values[:, None]).tocsr()
    sc.pp.log1p(sub)
    sc.pp.pca(sub, n_comps=30, random_state=SEMILLA)
    coords = umap.UMAP(n_neighbors=15, random_state=SEMILLA).fit_transform(sub.obsm["X_pca"])
    orden = np.random.default_rng(SEMILLA).permutation(len(coords))
    colores = sub.obs.age_group.astype(str).map({"adult": COLOR["adult"], "old": "#6b6b6b"}).values
    fig, ax = plt.subplots(figsize=(7, 5.4))
    ax.scatter(coords[orden, 0], coords[orden, 1], s=0.4, c=colores[orden], linewidths=0, rasterized=True)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("UMAP 1")
    ax.set_ylabel("UMAP 2")
    for g, c in [("adult", COLOR["adult"]), ("old", "#6b6b6b")]:
        ax.scatter([], [], s=30, color=c, label=ETIQUETA_CORTA[g])
    ax.legend(frameon=False, title="Grupo de edad", bbox_to_anchor=(1.0, 0.5), loc="center left")
    guardar(fig, "fig3b")


def main():
    adata = sc.read_h5ad(RUTA_H5AD)
    obs = adata.obs
    obs["estudio"] = obs.dataset_id.astype(str).map(ESTUDIOS)
    obs["subtipo"] = obs.cell_type.astype(str).map(SUBTIPOS)
    if obs.estudio.isna().any() or obs.subtipo.isna().any():
        raise SystemExit("Hay dataset_id o tipos celulares sin nombre asignado.")
    obs["age_group"] = obs.age_group.astype(str)
    donantes = obs.drop_duplicates("donor_id")

    estudios = tablas(obs)
    print(estudios.to_string())
    fig1a(estudios)
    fig1b(adata)
    fig2a(donantes)
    fig2b(donantes)
    fig2c(obs)
    fig3a(adata)
    fig3b(adata)


if __name__ == "__main__":
    main()
