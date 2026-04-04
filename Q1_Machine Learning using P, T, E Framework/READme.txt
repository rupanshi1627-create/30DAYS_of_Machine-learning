Q1.Define Machine Learning in the context of the <P, T, E> framework given by Tom Mitchell(Standard book).
For EACH of the following three applications, explicitly identify the Task (T), Performance Measure (P), and Experience (E):
i) A spam email filter
ii) A self-driving car that improves its lane-following over time
iii) A recommendation engine for an e-commerce platform
Distinguish between the three definitions of ML mentioned in the course: common, general, and engineering-oriented.


# CONCEPT

This question is based on the fundamental definition of Machine Learning using Tom Mitchell’s framework:

A computer program is said to learn from **Experience (E)** with respect to some **Task (T)** and **Performance Measure (P)** if its performance improves with experience.

# Intuition (Simple Understanding)

Machine Learning = Learning from data (Experience)

- Task (T): What the system is supposed to do  
- Performance (P): How well it is doing  
- Experience (E): Data it learns from  

---

# Solution with examples

for example we have to check emails are spam or ham?
so usme WHat will be the task, What will our system perform and what experience it will take from here?

## i) Spam Email Filter

- Task (T): Classify emails as spam or not spam  
- Performance (P): Accuracy, Precision, Recall  
- Experience (E): Labeled dataset of emails (spam/not spam)  

---

## ii) Self-Driving Car

- Task (T): Lane following and driving control  
- Performance (P): Driving accuracy, safety (lane deviation)  
- Experience (E): Sensor data, driving history, camera inputs  

---

## iii) Recommendation System (E-commerce)

- Task (T): Recommend products to users  
- Performance (P): Click-through rate, user engagement, conversion rate  
- Experience (E): User behavior data (clicks, purchases, history)  

---

# Types of Machine Learning Definitions

## 1. Common Definition

Machine Learning is the ability of machines to learn from data without being explicitly programmed.

---

## 2. General Definition

A system improves its performance on a task over time using experience.

---

## 3. Engineering-Oriented Definition (Tom Mitchell)

A program learns from experience (E) with respect to task (T) and performance measure (P) if its performance improves with experience.

---

# Final Answer

Machine Learning is defined as a system that learns from experience (E) to perform a task (T) and improves according to a performance measure (P).

---

# Key Takeaways

- <P, T, E> is the foundation of Machine Learning  
- Every ML problem must define Task, Performance, and Experience  
- ML = learning from data and improving over time  