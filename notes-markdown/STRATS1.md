Based on the provided context, the most **necessary and accurate feature extraction and selection techniques** for identifying spam or non-spam reviews, combining **unsupervised learning strategies** and **NLP techniques**, are summarized below:

---

### **1. Feature Extraction Techniques**
#### **A. Linguistic (NLP-Based) Features**
These are the most dominant and effective techniques for spam detection, focusing on the **textual content** of reviews. Key steps include:

1. **Preprocessing**:
   - **Stopword Removal**: Eliminate irrelevant words (e.g., "the," "is," "and").
   - **Punctuation Removal**: Clean text by removing symbols.
   - **Stemming/Lemmatization**: Reduce words to their root form (e.g., "working" → "work").
   - **Part-of-Speech (POS) Tagging**: Label words as nouns, verbs, adjectives, etc., to capture syntactic patterns.

2. **Tokenization**:
   - **N-grams**:
     - **Unigrams** (single words, e.g., "good").
     - **Bigrams** (pairs, e.g., "good car").
     - **Trigrams** (triplets, e.g., "very good car").
   - **Combination of N-grams** (e.g., uni + bi-grams) often improves accuracy.

3. **Transformation**:
   - **Document-Term Matrix (DTM)**: Represent reviews as sparse matrices of word frequencies.
   - **TF-IDF (Term Frequency-Inverse Document Frequency)**: Weight words by importance (common words like "the" get lower weights).
   - **Bag-of-Words (BoW)**: Simplest representation using word counts.

4. **Feature Selection**:
   - **Information Gain**: Measures how well a word discriminates between spam/non-spam (higher gain = more relevant).
   - **χ²-Statistic**: Identifies words with strong dependence on class labels (spam/non-spam).
   - **Mutual Information**: Captures statistical dependence between words and classes.

#### **B. Spammer Behavioral Features**
These focus on **metadata and reviewer patterns**, often used alongside linguistic features:
   - **Reviewer-Centric**:
     - **Review Frequency**: Spammers often post multiple reviews in short time spans.
     - **Deviation from Average Rating**: Spammers may give extreme ratings (e.g., all 5-star).
     - **Review Length**: Spam reviews are often shorter or longer than genuine ones.
     - **Temporal Patterns**: Time between reviews (e.g., multiple reviews in <1 minute).
     - **IP/Geolocation**: Multiple reviews from the same IP/location.
   - **Review-Centric**:
     - **Content Similarity**: Duplicate or near-identical reviews across products.
     - **Sentiment Polarization**: Overuse of extreme words ("amazing," "terrible").
     - **Helpfulness Votes**: Low "helpful" votes may indicate spam.

---

### **2. Unsupervised Learning Strategies**
For scenarios with **unlabeled data**, the following techniques are effective:

#### **A. Clustering-Based Methods**
   - **K-Means Clustering**:
     - Groups reviews into clusters based on feature similarity (e.g., TF-IDF vectors).
     - Works well for large datasets; accuracy depends on choosing optimal *K* (number of clusters).
     - Example: Achieved **71% precision** in detecting spam in Chinese reviews (Jia et al.).
   - **Twice-Clustering**:
     - First clusters the dataset, then applies sub-clustering to improve precision.
     - Reported **66% accuracy** on product reviews (360buy.com dataset).
   - **Constrained K-Means (COP-K-Means)**:
     - Incorporates domain constraints (e.g., reviewer behavior) to guide clustering.

#### **B. Anomaly Detection**
   - **Deviation-Based Methods**:
     - **Aspect-Based Review Deviation**: Detects reviews deviating from the norm for a product aspect (e.g., "battery life").
     - **Latent Content Deviation**: Uses topic modeling (e.g., LDA) to identify outliers.
     - Example: Achieved **78.15% accuracy** on Amazon reviews.

#### **C. Lexicon-Based Techniques**
   - **Dictionary/Corpus-Based**:
     - Compares review text against precompiled sentimental lexicons (e.g., lists of positive/negative words).
     - **Corpus-Based**: Better accuracy than dictionary methods (Table 14 in the context).
   - **Rule-Based Systems**:
     - Uses heuristic rules (e.g., "reviews posted within 1 minute = spam").
     - Example: **65% accuracy** for emotion detection in micro-blogs (Gao et al.).

---

### **3. Most Accurate Combinations**
The papers highlight that **combining multiple techniques** yields the highest accuracy:
1. **Linguistic + Behavioral Features**:
   - Example: **89.6% accuracy** using bi-grams + reviewer features (Hotel review dataset via AMT).
   - **86.1% accuracy** with behavioral features + bi-grams (Yelp dataset).
2. **Supervised + Unsupervised Hybrid**:
   - Use clustering (e.g., K-means) to label data, then apply supervised methods (e.g., SVM).
3. **Ensemble Methods**:
   - Combine outputs from multiple models (e.g., SVM + Random Forest) to improve robustness.

---

### **4. Performance Metrics for Evaluation**
To validate accuracy, the papers emphasize:
   - **Precision/Recall/F1-Score**: Balance between false positives/negatives.
   - **AUC-ROC**: Measures classifier performance across thresholds.
   - **Accuracy**: Overall correct classification rate (e.g., **91% with Random Forest** on Amazon data).
   - **Lift Curve**: Visualizes model performance for imbalanced datasets.

---

### **5. Key Insights from the Papers**
- **Linguistic features alone** (e.g., n-grams + TF-IDF) are **highly effective** but benefit from adding behavioral features.
- **Unsupervised methods** (e.g., clustering) are useful for **unlabeled data** but generally **less accurate** than supervised approaches.
- **Real-world datasets** (e.g., Yelp, Amazon) pose challenges due to noise; **synthetic datasets** (e.g., AMT) may overestimate accuracy.
- **Feature selection** (e.g., information gain) is critical to avoid overfitting and improve efficiency.

---
### **Recommended Pipeline for Spam Detection**
1. **Preprocess Text**: Clean, tokenize, and apply POS tagging/stemming.
2. **Extract Features**:
   - Linguistic: N-grams (uni/bi), TF-IDF, sentiment lexicons.
   - Behavioral: Reviewer frequency, rating deviation, temporal patterns.
3. **Feature Selection**: Use χ² or information gain to retain top features.
4. **Model Training**:
   - **Supervised**: SVM, Random Forest, or Logistic Regression (if labeled data exists).
   - **Unsupervised**: K-means or anomaly detection (for unlabeled data).
5. **Evaluate**: Use AUC-ROC, precision/recall, and accuracy metrics.

---
### **Example from the Papers**
- **Highest Accuracy (91%)**: Random Forest with **reviewer + product features** on Amazon dataset ([53]).
- **Best Unsupervised (78.15%)**: Latent content deviation on Amazon reviews ([63]).
- **Lexicon-Based (89.9%)**: SVM with bi-grams on AMT hotel reviews ([15]).

By integrating these techniques, practitioners can build **robust spam detection systems** tailored to their datasets.