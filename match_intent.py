
import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

PREDEFINED_QUESTIONS = ['כמה טילים נורו בסך הכל?', 'מה האזור עם הכי הרבה פגיעות ישירות?', 'מה סוג הירי הנפוץ ביותר?', 'מה אחוז ההצלחות של מערכת היירוט?', 'כמה טילים לא יורטו?', 'כמה פגיעות ישירות היו בכל אזור?', 'מהו האזור עם הכי הרבה יירוטים מוצלחים?', 'כמה אירועים יש בסך הכול בדוח?', 'מה ממוצע הפגיעות הישירות לאירוע?']

def match_question_to_intent(user_question: str) -> str:
    prompt = f"""
בחר את השאלה הכי מתאימה מהרשימה הבאה שתואמת לשאלה החופשית שנשאלת:

שאלה חופשית:
"{user_question}"

אפשרויות:
{chr(10).join("- " + q for q in PREDEFINED_QUESTIONS)}

אם אין התאמה ברורה, החזר "לא ידוע".
אם יש התאמה, החזר רק את השאלה הכי מתאימה כפי שהיא.
"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text.strip()
