#  כתוב תוכנית פייטון המשווה שתי רשימות ומדפיסה איזו רשימה מכילה יותר מספרים גדולים.
# לדוגמא:
# רשימה -1
# [ 3, 5, 30, 0]
# רשימה -2
# [1000, 5, 29, -5]
# התשובה תהיה שרשימה 1 גדולה יותר מכיוון שה מספר 30 גדול מ 29 והמספר 0 גדול מ -5 כלו מר
# היא מכילה 2 מספרים גדולים יותר מרשימה 2 )לעומת רשימ ה 2 המכילה מספר 1 רק הגדול יותר
# מרשימה ]המספר 1000 הגדול מ- 3[( .
# כמות המספרים הגדולים היא הרלוונטית )ולא הסכום(. הנח שאורך ה רשימות זהות
# * אתגר : התוכל לפתור את התרגיל עבור רשימות באורך שונה )ספור רק את כמות האיברים
# שמכילה הר שימה הקטנה: לדוגמא אם רשימה 1 מכילה 4 איברים ו רשימה 8 מכילה 8 איברים אז
# השווה את 4 האיברים הראשונים בלבד( 

r1 = [   3, 5, 30,  0 ]
r2 = [1000, 5, 29, -5, 10, None, 20]

n1 = 0
n2 = 0

# Note: I extended the logic to consider extra values in one of the arrays as greater than the other if value is not None, so
#       code will iterate to max length of both arrays

for i in range(max(len(r1), len(r2))):
    if i < len(r1) and i < len(r2): #while being in the range
        n1 += 1 if r1[i] > r2[i] else 0
        n2 += 1 if r2[i] > r1[i] else 0
    else: #if size of r1 or r2 has ended
        n1 += 1 if i >= len(r2) and r1[i] else 0 #consider any value in r1 to be greater than nothing
        n2 += 1 if i >= len(r1) and r2[i] else 0 #consider any value in r2 to be greater than nothing
    
print(f'List {r1} has {n1} numbers greater than list {r2}')
print(f'List {r2} has {n2} numbers greater than list {r1}')
