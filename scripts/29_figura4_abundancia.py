#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la Figura 4 de la tesis desde results/subtypes/nk_ratio_donor_data.csv.

Calcula los valores de p a partir de esa tabla: prueba de Mann-Whitney del cociente
por donante y GLM binomial ~ assay + age_group con dispersión de Pearson.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import patsy
import scipy.stats as st
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parent.parent
TABLA = ROOT / "results" / "subtypes" / "nk_ratio_donor_data.csv"
SALIDAS = [
    ROOT / "tesis" / "figures_clean" / "fig4.png",
    ROOT / "tesis" / "manuscripts" / "figures" / "fig4.png",
    ROOT / "tesis" / "manuscripts" / "figures_clean" / "fig4.png",
]
GRUPOS = ["adult", "old"]
ETIQUETAS = ["Adultos", "Adultos mayores"]
COLOR_GRUPO = ["#5b8fd9", "#d99a3d"]
COLOR_BRIGHT = "#93c5fd"
COLOR_DIM = "#1e3a8a"


def calcular_p(df):
    adultos = df.loc[df.age_group == "adult", "ratio"]
    mayores = df.loc[df.age_group == "old", "ratio"]
    p_mw = st.mannwhitneyu(adultos, mayores, alternative="two-sided").pvalue

    y = np.column_stack([df.bright_cells, df.dim_cells])
    X = patsy.dmatrix("assay + age_group", df, return_type="dataframe")
    modelo = sm.GLM(y, X, family=sm.families.Binomial())
    inicial = modelo.fit()
    phi = inicial.pearson_chi2 / inicial.df_resid
    ajustado = modelo.fit(scale=phi)
    return p_mw, ajustado.pvalues["age_group[T.old]"], phi


def main():
    df = pd.read_csv(TABLA)
    df["age_group"] = pd.Categorical(df["age_group"], categories=GRUPOS)
    p_mw, p_glm, phi = calcular_p(df)
    print(f"Mann-Whitney p = {p_mw:.4f}; GLM p = {p_glm:.4f}; phi = {phi:.4f}")

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 4.8))
    rng = np.random.default_rng(42)

    # A: cociente por donante
    valores = [df.loc[df.age_group == g, "ratio"].values for g in GRUPOS]
    cajas = ax1.boxplot(valores, positions=[0, 1], widths=0.5, patch_artist=True,
                        showfliers=False, medianprops={"color": "black"})
    for caja, color in zip(cajas["boxes"], COLOR_GRUPO):
        caja.set_facecolor(color)
    for i, v in enumerate(valores):
        ax1.scatter(i + rng.uniform(-0.15, 0.15, len(v)), v, s=14, color="black",
                    alpha=0.5, linewidths=0, zorder=3)
    ax1.set_xticks([0, 1], ETIQUETAS)
    ax1.set_ylabel("Cociente CD56bright / CD56dim por donante")
    ax1.set_xlabel("Grupo de edad")
    ax1.set_title(f"Mann-Whitney: p = {p_mw:.4f}\nGLM cuasibinomial: p = {p_glm:.4f}",
                  fontsize=10)

    # B: composición promedio
    pct = df.groupby("age_group", observed=False)[["bright_percent", "dim_percent"]].mean()
    ax2.bar(ETIQUETAS, pct["bright_percent"], width=0.5, color=COLOR_BRIGHT, label="CD56bright")
    ax2.bar(ETIQUETAS, pct["dim_percent"], width=0.5, bottom=pct["bright_percent"],
            color=COLOR_DIM, label="CD56dim")
    ax2.set_ylim(0, 118)
    ax2.set_yticks(range(0, 101, 20))
    ax2.set_ylabel("Porcentaje de células (%)")
    ax2.set_xlabel("Grupo de edad")
    ax2.legend(loc="upper center", ncol=2, frameon=False)

    # C: recuentos medios
    medias = df.groupby("age_group", observed=False)[["bright_cells", "dim_cells"]].mean()
    x = np.arange(2)
    ax3.bar(x - 0.175, medias["bright_cells"], 0.35, color=COLOR_BRIGHT, label="CD56bright")
    ax3.bar(x + 0.175, medias["dim_cells"], 0.35, color=COLOR_DIM, label="CD56dim")
    ax3.set_xticks(x, ETIQUETAS)
    ax3.set_ylim(0, medias.values.max() * 1.18)
    ax3.set_ylabel("Células por donante (media)")
    ax3.set_xlabel("Grupo de edad")
    ax3.legend(loc="upper center", ncol=2, frameon=False)

    for ax, letra in zip((ax1, ax2, ax3), "ABC"):
        ax.text(-0.13, 1.06, letra, transform=ax.transAxes, fontsize=14, fontweight="bold")
        ax.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    for salida in SALIDAS:
        fig.savefig(salida, dpi=300)
        print(f"Guardada: {salida.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
