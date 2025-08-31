# CWA to GPA Converter

This project provides a simple Python implementation to **compute both CWA (Cumulative Weighted Average)** and **GPA (Grade Point Average)** from a list of course scores and their corresponding credit weights.  
It allows students to **compare CWA and GPA side by side** using the same input.

---

## 📘 Background

Different universities use different grading systems:  

- **CWA** is used in Ghana by Kwame Nkrumah University of Science and Technology (KNUST). It is a percentage-based measure of performance.  
- **GPA** is widely used internationally, especially in North America, on a **4.0 or 5.0 scale** depending on the institution.  

When applying abroad, students often need to **convert their CWA to GPA**. This project demonstrates the process using course-by-course calculations rather than rough approximations.

---

## 🧮 Algorithms and Formulas

### 1. CWA (Cumulative Weighted Average)

The CWA is computed as the **weighted average** of all course scores:

\[
\text{CWA} = \frac{\sum (\text{score} \times \text{credit hours})}{\sum (\text{credit hours})}
\]

- `score`: The raw percentage score in the course.  
- `credit hours`: The weight of the course.  



### 2. GPA (Grade Point Average)

The GPA is computed in two steps:

1. Convert each **score** into a **grade point** using the university’s GPA scale.  
   - Example (4.0 scale commonly used in Ghana):  
     - 70–100 → 4.0 (A)  
     - 60–69 → 3.0 (B)  
     - 50–59 → 2.0 (C)  
     - 45–49 → 1.5 (D)  
     - 40–44 → 1.0 (E)  
     - 0–39  → 0.0 (F)  

2. Compute the **weighted average** of the grade points:

\[
\text{GPA} = \frac{\sum (\text{grade point} \times \text{credit hours})}{\sum (\text{credit hours})}
\]

---

## 💻 Implementation
- `cwa` Function takes list of tuples (courses) and return calculated CWA
- `score_to_gp` Function takes a score returns its corresponding grade point.
- `gpa` Function takes a list of tuples (course) and returns calculated GPA.

---
## 🚀 Usage
1. Populate `courses.py` with scores and credit-hours from you courses.
2. Run `cwatogpa.py`
```bash
python3 cwatogpa.py
```
Sample Output
```
Your GPA is: 2.56
Your CWA is: 59.1
```

---

## ⚖️ Notes and Considerations
- Grading scale may differ by institution. Update the score_to_gpa function to reflect your school’s official GPA rules.

- CWA and GPA are not always linearly related. A high CWA does not guarantee the maximum GPA, since GPA depends on grade cut-offs.

- This script currently assumes a 4.0 GPA scale. You can extend it to a 5.0 scale or others by modifying the mapping.


---

## ✅ Future Extensions

- Allow dynamic GPA scales (4.0, 5.0, 7.0, etc.) as function parameters.

- Create a CLI tool or web app for easy use without Python knowledge.

- Scan transcript and automatically do conversion. 