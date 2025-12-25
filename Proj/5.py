import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

data = [
    {
        "Страна": "Япония",
        "Ожидаемая продолжительность жизни": 84.5,
        "Расходы на здравоохранение (% ВВП)": 10.9,
        "ВВП на душу населения (тыс. USD)": 42.0,
        "Плотность врачей (на 10 000)": 24.0,
        "Детская смертность (на 1000)": 2.0
    },
    {
        "Страна": "Швейцария",
        "Ожидаемая продолжительность жизни": 83.8,
        "Расходы на здравоохранение (% ВВП)": 11.3,
        "ВВП на душу населения (тыс. USD)": 69.9,
        "Плотность врачей (на 10 000)": 43.0,
        "Детская смертность (на 1000)": 3.5
    },
    {
        "Страна": "Германия",
        "Ожидаемая продолжительность жизни": 81.0,
        "Расходы на здравоохранение (% ВВП)": 11.7,
        "ВВП на душу населения (тыс. USD)": 54.0,
        "Плотность врачей (на 10 000)": 44.0,
        "Детская смертность (на 1000)": 3.2
    },
    {
        "Страна": "Великобритания",
        "Ожидаемая продолжительность жизни": 81.3,
        "Расходы на здравоохранение (% ВВП)": 10.2,
        "ВВП на душу населения (тыс. USD)": 46.5,
        "Плотность врачей (на 10 000)": 31.0,
        "Детская смертность (на 1000)": 3.6
    },
    {
        "Страна": "США",
        "Ожидаемая продолжительность жизни": 78.8,
        "Расходы на здравоохранение (% ВВП)": 16.8,
        "ВВП на душу населения (тыс. USD)": 65.3,
        "Плотность врачей (на 10 000)": 26.0,
        "Детская смертность (на 1000)": 5.4
    },
    {
        "Страна": "Куба",
        "Ожидаемая продолжительность жизни": 78.5,
        "Расходы на здравоохранение (% ВВП)": 11.2,
        "ВВП на душу населения (тыс. USD)": 9.0,
        "Плотность врачей (на 10 000)": 82.0,
        "Детская смертность (на 1000)": 4.5
    },
    {
        "Страна": "Бразилия",
        "Ожидаемая продолжительность жизни": 75.5,
        "Расходы на здравоохранение (% ВВП)": 9.5,
        "ВВП на душу населения (тыс. USD)": 15.0,
        "Плотность врачей (на 10 000)": 23.0,
        "Детская смертность (на 1000)": 13.5
    },
    {
        "Страна": "Китай",
        "Ожидаемая продолжительность жизни": 78.2,
        "Расходы на здравоохранение (% ВВП)": 7.1,
        "ВВП на душу населения (тыс. USD)": 21.4,
        "Плотность врачей (на 10 000)": 20.0,
        "Детская смертность (на 1000)": 6.8
    },
    {
        "Страна": "Россия",
        "Ожидаемая продолжительность жизни": 72.5,
        "Расходы на здравоохранение (% ВВП)": 5.6,
        "ВВП на душу населения (тыс. USD)": 35.0,
        "Плотность врачей (на 10 000)": 40.0,
        "Детская смертность (на 1000)": 5.5
    },
    {
        "Страна": "Индия",
        "Ожидаемая продолжительность жизни": 69.7,
        "Расходы на здравоохранение (% ВВП)": 3.5,
        "ВВП на душу населения (тыс. USD)": 7.7,
        "Плотность врачей (на 10 000)": 8.6,
        "Детская смертность (на 1000)": 27.7
    },
    {
        "Страна": "Нигерия",
        "Ожидаемая продолжительность жизни": 55.2,
        "Расходы на здравоохранение (% ВВП)": 3.7,
        "ВВП на душу населения (тыс. USD)": 5.9,
        "Плотность врачей (на 10 000)": 4.0,
        "Детская смертность (на 1000)": 72.0
    },
    {
        "Страна": "Чад",
        "Ожидаемая продолжительность жизни": 53.0,
        "Расходы на здравоохранение (% ВВП)": 4.1,
        "ВВП на душу населения (тыс. USD)": 1.6,
        "Плотность врачей (на 10 000)": 0.5,
        "Детская смертность (на 1000)": 69.8
    }
]

df = pd.DataFrame(data)

df['Коэффициент эффективности'] = df['Ожидаемая продолжительность жизни'] / df['Расходы на здравоохранение (% ВВП)']
df['Коэффициент эффективности'] = df['Коэффициент эффективности'].round(2)

numeric_cols = ['Ожидаемая продолжительность жизни', 'Расходы на здравоохранение (% ВВП)', 'ВВП на душу населения (тыс. USD)', 'Плотность врачей (на 10 000)', 'Детская смертность (на 1000)']
corr_matrix = df[numeric_cols].corr(method='pearson')

print("\nТоп-3 стран по ожидаемой продолжительности жизни:")
top_life = df.nlargest(3, 'Ожидаемая продолжительность жизни')[['Страна', 'Ожидаемая продолжительность жизни']]
for _, row in top_life.iterrows():
    print(f"  {row['Страна']}: {row['Ожидаемая продолжительность жизни']} лет")

print("\nТоп-3 стран по эффективности системы здравоохранения (Коэффициент эффективности):")
top_efficiency = df.nlargest(3, 'Коэффициент эффективности')[['Страна', 'Коэффициент эффективности', 'Ожидаемая продолжительность жизни', 'Расходы на здравоохранение (% ВВП)']]
for _, row in top_efficiency.iterrows():
    print(f"  {row['Страна']}: {row['Коэффициент эффективности']} (продолжительность: {row['Ожидаемая продолжительность жизни']} лет, расходы: {row['Расходы на здравоохранение (% ВВП)']}% ВВП)")

corr_health_life = df['Расходы на здравоохранение (% ВВП)'].corr(df['Ожидаемая продолжительность жизни'])
print(f"\nКорреляция между расходами на здравоохранение и продолжительностью жизни: r = {corr_health_life:.3f}")

def income_group(gdp):
    if gdp > 30:
        return "Высокий доход"
    elif gdp > 10:
        return "Средний доход"
    else:
        return "Низкий доход"

df['Группа доходов'] = df['ВВП на душу населения (тыс. USD)'].apply(income_group)

print("\nСредние показатели по группам доходов:")
for group in ['Высокий доход', 'Средний доход', 'Низкий доход']:
    group_data = df[df['Группа доходов'] == group]
    if len(group_data) > 0:
        avg_life = group_data['Ожидаемая продолжительность жизни'].mean()
        avg_health_exp = group_data['Расходы на здравоохранение (% ВВП)'].mean()
        avg_gdp = group_data['ВВП на душу населения (тыс. USD)'].mean()
        count = len(group_data)
        print(f"\n  {group} ({count} стран):")
        print(f"    Средняя продолжительность жизни: {avg_life:.1f} лет")
        print(f"    Средние расходы на здравоохранение: {avg_health_exp:.1f}% ВВП")
        print(f"    Средний ВВП на душу населения: ${avg_gdp:.1f} тыс.")

plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
mpl.rcParams['font.size'] = 10
mpl.rcParams['axes.titlesize'] = 12
mpl.rcParams['axes.labelsize'] = 11
mpl.rcParams['font.family'] = ['DejaVu Sans']

fig1, ax1 = plt.subplots(figsize=(14, 8))
df_sorted = df.sort_values('Ожидаемая продолжительность жизни', ascending=True)

bars = ax1.barh(df_sorted['Страна'], df_sorted['Ожидаемая продолжительность жизни'], color='lightblue', alpha=0.7, height=0.7)
ax1.set_xlabel('Ожидаемая продолжительность жизни (годы)', fontsize=11)
ax1.set_title('Сравнение ожидаемой продолжительности жизни и расходов на здравоохранение', fontsize=13, fontweight='bold', pad=15)

for bar in bars:
    width = bar.get_width()
    ax1.text(width + 0.3, bar.get_y() + bar.get_height()/2, f'{width:.1f}', ha='left', va='center', fontsize=9)

ax2 = ax1.twiny()
line = ax2.plot(df_sorted['Расходы на здравоохранение (% ВВП)'], df_sorted['Страна'], color='red', marker='o', linewidth=2, markersize=6, label='Расходы на здравоохранение')
ax2.set_xlabel('Расходы на здравоохранение (% от ВВП)', fontsize=11, color='red')
ax2.tick_params(axis='x', labelcolor='red')
ax2.grid(False)

anomalies = ['США', 'Куба']
for i, country in enumerate(df_sorted['Страна']):
    if country in anomalies:
        bars[i].set_color('orange')
        bars[i].set_alpha(0.9)

from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='lightblue', alpha=0.7, label='Продолжительность жизни'), Patch(facecolor='orange', alpha=0.9, label='Аномалии (США, Куба)'), mpl.lines.Line2D([0], [0], color='red', marker='o', label='Расходы на здравоохранение')]
ax1.legend(handles=legend_elements, loc='lower right')

plt.tight_layout()
plt.savefig('figure1_life_vs_spending.png', dpi=300, bbox_inches='tight')

fig2, ax3 = plt.subplots(figsize=(12, 8))

physicians_norm = ((df['Плотность врачей (на 10 000)'] - df['Плотность врачей (на 10 000)'].min()) / (df['Плотность врачей (на 10 000)'].max() - df['Плотность врачей (на 10 000)'].min()))
point_sizes = 100 + physicians_norm * 500

scatter = ax3.scatter(df['Расходы на здравоохранение (% ВВП)'], df['Ожидаемая продолжительность жизни'], c=df['ВВП на душу населения (тыс. USD)'], s=point_sizes, alpha=0.7, cmap='viridis', edgecolors='black', linewidth=0.5)

for i, row in df.iterrows():
    ax3.annotate(row['Страна'], (row['Расходы на здравоохранение (% ВВП)'] + 0.1, row['Ожидаемая продолжительность жизни']), fontsize=8, alpha=0.8)

ax3.set_xlabel('Расходы на здравоохранение (% от ВВП)', fontsize=11)
ax3.set_ylabel('Ожидаемая продолжительность жизни (годы)', fontsize=11)
ax3.set_title('Взаимосвязь расходов на здравоохранение и продолжительности жизни\n' + '(Цвет = ВВП на душу населения, Размер = плотность врачей)', fontsize=13, fontweight='bold', pad=15)
ax3.grid(True, alpha=0.3)

cbar = plt.colorbar(scatter, ax=ax3)
cbar.set_label('ВВП на душу населения (тыс. USD, ППС)', fontsize=10)

from matplotlib.lines import Line2D
size_legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Высокая плотность врачей', markerfacecolor='gray', markersize=10, markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Средняя плотность врачей', markerfacecolor='gray', markersize=6, markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Низкая плотность врачей', markerfacecolor='gray', markersize=3, markeredgecolor='black')]
ax3.legend(handles=size_legend_elements, loc='upper left', title='Плотность врачей')

plt.tight_layout()
plt.savefig('figure2_correlation_scatter.png', dpi=300, bbox_inches='tight')

fig3, ax4 = plt.subplots(figsize=(12, 8))

df_sorted_eff = df.sort_values('Коэффициент эффективности', ascending=True)

colors = plt.cm.Blues((df_sorted_eff['ВВП на душу населения (тыс. USD)'] - df_sorted_eff['ВВП на душу населения (тыс. USD)'].min()) / (df_sorted_eff['ВВП на душу населения (тыс. USD)'].max() - df_sorted_eff['ВВП на душу населения (тыс. USD)'].min()))

bars_eff = ax4.barh(df_sorted_eff['Страна'], df_sorted_eff['Коэффициент эффективности'], color=colors, edgecolor='black', alpha=0.8, height=0.7)

ax4.set_xlabel('Коэффициент эффективности (лет жизни / % расходов на здравоохранение)', fontsize=11)
ax4.set_title('Рейтинг эффективности систем здравоохранения\n' + '(чем темнее оттенок, выше ВВП на душу населения)', fontsize=13, fontweight='bold', pad=15)
ax4.grid(True, axis='x', alpha=0.3)

for bar in bars_eff:
    width = bar.get_width()
    ax4.text(width + 0.05, bar.get_y() + bar.get_height()/2, f'{width:.2f}', ha='left', va='center', fontsize=9)

for i, (_, row) in enumerate(df_sorted_eff.iterrows()):
    ax4.text(0.05, i, f"{row['Расходы на здравоохранение (% ВВП)']}% ВВП", ha='left', va='center', fontsize=8, color='darkred', fontweight='bold', transform=ax4.get_yaxis_transform())

norm = mpl.colors.Normalize(vmin=df_sorted_eff['ВВП на душу населения (тыс. USD)'].min(), vmax=df_sorted_eff['ВВП на душу населения (тыс. USD)'].max())
sm = plt.cm.ScalarMappable(cmap='Blues', norm=norm)
sm.set_array([])
cbar2 = plt.colorbar(sm, ax=ax4, orientation='vertical', pad=0.01)
cbar2.set_label('ВВП на душу населения (тыс. USD, ППС)', fontsize=10)

plt.tight_layout()
plt.savefig('figure3_efficiency_ranking.png', dpi=300, bbox_inches='tight')

print("\n")

plt.show()