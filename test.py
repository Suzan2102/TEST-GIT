import matplotlib.pyplot as plt
import numpy as np

def analyze_and_plot_results(results, title='ניתוח תוצאות'):
    """
    מקבל מילון של תוצאות, מבצע ניתוח סטטיסטי בסיסי ומציג גרפים.
    results: dict, לדוג׳ {'שיטה1': [10,12,13], 'שיטה2': [11,15,14]}
    """
    if not results or not isinstance(results, dict):
        print("אנא ספק מילון תוצאות תקין.")
        return

    # ניתוח תוצאות: ממוצע וסטיית תקן
    names = list(results.keys())
    means = [np.mean(results[name]) for name in names]
    stds = [np.std(results[name]) for name in names]

    # תרשים ממוצעים
    plt.figure(figsize=(8,6))
    plt.bar(names, means, yerr=stds, capsize=8, color='skyblue')
    plt.ylabel('ממוצע')
    plt.title(title)
    plt.grid(axis='y')
    plt.show()

    # תרשים Boxplot
    plt.figure(figsize=(8,6))
    plt.boxplot([results[name] for name in names], labels=names)
    plt.ylabel('תוצאה')
    plt.title(f'{title} - Boxplot')
    plt.grid(axis='y')
    plt.show()
    
    # הדפסת סיכום נתונים לטבלה
    print("סיכום סטטיסטי:")
    for name in names:
        print(f"{name}: ממוצע={np.mean(results[name]):.2f}, סטיית תקן={np.std(results[name]):.2f}, מינימום={np.min(results[name])}, מקסימום={np.max(results[name])}")

# דוגמה לשימוש:
if __name__ == "__main__":
    דוגמה_תוצאות = {
        'מודל A': [10, 12, 13, 11],
        'מודל B': [12, 15, 14, 13],
        'מודל C': [8, 6, 9, 7]
    }
    analyze_and_plot_results(דוגמה_תוצאות, title='השוואת ביצועים')

