import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 20))
ax.set_xlim(0, 14)
ax.set_ylim(0, 20)
ax.axis("off")
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

# ── colour palette ──────────────────────────────────────────────────────────
C_HEADER   = "#1e2235"   # step box background
C_BORDER   = "#4c6ef5"   # accent border / arrows
C_BULLET   = "#2d3555"   # sub-item background
C_TEXT     = "#e8eaf6"   # main text
C_SUB      = "#9fa8da"   # sub-item text
C_TITLE    = "#7986cb"   # step number
C_ARROW    = "#4c6ef5"
C_SHADOW   = "#090c18"

# step data: (emoji, title, bullets, accent_colour)
steps = [
    ("[IN]", "Data Loading & Exploration",
     ["Read train/test CSV datasets",
      "Shape, dtypes, null-value checks",
      "Descriptive statistics (.describe())"],
     "#3d5afe"),

    ("[EDA]", "Data Visualisation (EDA)",
     ["Feature-distribution histograms & countplots",
      "Correlation matrix heat-map",
      "Outlier & class-balance detection"],
     "#00b0ff"),

    ("[PRE]", "Data Preprocessing & Cleaning",
     ["Missing-value imputation (median / mode)",
      "OrdinalEncoder / OneHotEncoder",
      "StandardScaler normalisation",
      "Binary-flag & replacement encoding"],
     "#00e5ff"),

    ("[FE]", "Feature Engineering",
     ["Domain-knowledge interaction features",
      "  e.g. BP_Age_Product, Monthly_Fee_Ratio",
      "  e.g. pulse_pressure, ldl_hdl_ratio",
      "Correlation-matrix guided selection",
      "PolynomialFeatures for non-linearity"],
     "#69f0ae"),

    ("[ML]", "Model Training",
     ["XGBRegressor or XGBClassifier",
      "KFold / StratifiedKFold cross-validation",
      "OPTUNA hyperparameter search (30-50 trials)",
      "Early stopping to prevent overfitting"],
     "#ffeb3b"),

    ("[EVAL]", "Model Evaluation & Optimisation",
     ["Out-of-Fold (OOF) ensemble predictions",
      "Metrics: RMSE (regression) / AUC (classification)",
      "Ensemble / blending strategies",
      "Iteration back to feature engineering"],
     "#ff9800"),

    ("[OUT]", "Submission",
     ["Generate submission DataFrame",
      "Format: id + target probability / value",
      "Export to CSV and upload to Kaggle"],
     "#f44336"),
]

BOX_W   = 11.0
BOX_X   = 1.5
START_Y = 19.0
BOX_H_BASE = 0.95   # title row height
BULLET_H   = 0.38   # height per bullet
GAP        = 0.28   # gap between boxes
ARROW_H    = GAP * 0.55

y = START_Y

for i, (emoji, title, bullets, accent) in enumerate(steps):
    total_h = BOX_H_BASE + len(bullets) * BULLET_H + 0.12

    # ── shadow ──────────────────────────────────────────────────────────────
    shadow = FancyBboxPatch(
        (BOX_X + 0.07, y - total_h - 0.07), BOX_W, total_h,
        boxstyle="round,pad=0.04", linewidth=0,
        facecolor=C_SHADOW, zorder=1
    )
    ax.add_patch(shadow)

    # ── main box ────────────────────────────────────────────────────────────
    box = FancyBboxPatch(
        (BOX_X, y - total_h), BOX_W, total_h,
        boxstyle="round,pad=0.04", linewidth=1.8,
        edgecolor=accent, facecolor=C_HEADER, zorder=2
    )
    ax.add_patch(box)

    # ── left accent stripe ───────────────────────────────────────────────────
    stripe = FancyBboxPatch(
        (BOX_X, y - total_h), 0.22, total_h,
        boxstyle="round,pad=0.02", linewidth=0,
        facecolor=accent, alpha=0.85, zorder=3
    )
    ax.add_patch(stripe)

    # ── step number badge ────────────────────────────────────────────────────
    badge = plt.Circle((BOX_X + 0.11, y - total_h / 2), 0.18,
                        color=C_HEADER, zorder=4)
    ax.add_patch(badge)
    ax.text(BOX_X + 0.11, y - total_h / 2, str(i + 1),
            ha="center", va="center", fontsize=7.5, fontweight="bold",
            color=C_TEXT, zorder=5)
    # ── tag label on stripe ──────────────────────────────────────────────────
    ax.text(BOX_X + 0.11, y - 0.35, emoji,
            ha="center", va="center", fontsize=6, fontweight="bold",
            color=C_TEXT, zorder=5, rotation=90)

    # ── title ────────────────────────────────────────────────────────────────
    ax.text(BOX_X + 0.52, y - 0.48,
            f"{title}",
            ha="left", va="center", fontsize=13, fontweight="bold",
            color=C_TEXT, zorder=4)

    # ── bullets ──────────────────────────────────────────────────────────────
    for j, bullet in enumerate(bullets):
        by = y - BOX_H_BASE - j * BULLET_H - 0.18
        # pill background
        pill = FancyBboxPatch(
            (BOX_X + 0.48, by - 0.14), BOX_W - 0.65, 0.30,
            boxstyle="round,pad=0.03", linewidth=0,
            facecolor=C_BULLET, alpha=0.7, zorder=3
        )
        ax.add_patch(pill)
        ax.text(BOX_X + 0.65, by,
                bullet, ha="left", va="center",
                fontsize=9.2, color=C_SUB, zorder=4)

    y -= total_h + GAP

    # ── arrow to next step ───────────────────────────────────────────────────
    if i < len(steps) - 1:
        arrow_x = BOX_X + BOX_W / 2
        arrow_top = y + GAP * 0.78
        arrow_bot = y + GAP * 0.18
        ax.annotate(
            "", xy=(arrow_x, arrow_bot), xytext=(arrow_x, arrow_top),
            arrowprops=dict(arrowstyle="-|>", color=C_ARROW,
                            lw=2.2, mutation_scale=18),
            zorder=5
        )

# ── title block ──────────────────────────────────────────────────────────────
ax.text(7, 19.72, "Kaggle ML Pipeline",
        ha="center", va="center", fontsize=20, fontweight="bold",
        color=C_TEXT)
ax.text(7, 19.42, "End-to-End Data Handling Workflow",
        ha="center", va="center", fontsize=11, color=C_SUB)

# ── footer ───────────────────────────────────────────────────────────────────
ax.text(7, 0.18,
        "XGBoost  •  OPTUNA  •  Scikit-learn  •  Pandas  •  Matplotlib/Seaborn",
        ha="center", va="center", fontsize=9, color="#555e8a")

plt.tight_layout(pad=0)
plt.savefig("workflow.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
print("Saved workflow.png")
