# TEST-GIT

hiiiii

כלי Python לניתוח והשוואה ויזואלית של תוצאות בין שיטות או מודלים שונים.

## תיאור

הפרויקט מספק פונקציה אחת מרכזית — `analyze_and_plot_results` — שמקבלת מילון של תוצאות, מחשבת סטטיסטיקות בסיסיות (ממוצע, סטיית תקן, מינימום ומקסימום), ומציגה גרפים להשוואה בין הקבוצות.

## דרישות

- Python 3.7+
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

## התקנה

```bash
git clone https://github.com/Suzan2102/TEST-GIT.git
cd TEST-GIT
pip install numpy matplotlib
```

## שימוש

```python
from test import analyze_and_plot_results

results = {
    'מודל A': [10, 12, 13, 11],
    'מודל B': [12, 15, 14, 13],
    'מודל C': [8, 6, 9, 7],
}

analyze_and_plot_results(results, title='השוואת ביצועים')
```

או הרצה ישירה עם הדוגמה המובנית:

```bash
python test.py
```

## פלט

הפונקציה מייצרת:

1. **תרשים עמודות** — ממוצע לכל קבוצה עם סטיית תקן (error bars)
2. **Boxplot** — התפלגות התוצאות לכל קבוצה
3. **סיכום טקסטואלי** — ממוצע, סטיית תקן, מינימום ומקסימום לכל קבוצה

## מבנה הפרויקט

```
TEST-GIT/
├── test.py      # ניתוח סטטיסטי וגרפים
└── README.md
```

## רישיון

פרויקט לימודי — שימוש חופשי.
