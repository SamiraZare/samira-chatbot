"""
Knowledge base about Samira Zare, compiled from samirazare.com AND her resume.

This is the factual grounding the chatbot uses to answer questions. Keeping it
in one place makes it easy to update: edit this text, redeploy, done.

Editing tip: just rewrite the BACKGROUND string below in plain English. The
chatbot is instructed to answer ONLY from this text, so anything you add here
becomes something the bot can talk about, and anything you remove it won't.
"""

BACKGROUND = """
# About Samira Zare

Samira Zare is a Machine Learning / AI Engineer based in Sunnyvale, California.
She earned her Ph.D. in Computer Engineering from the University of California,
Santa Cruz (UCSC), from January 2016 to June 2023, and a B.Sc. in Computer
Engineering from Islamic Azad University of Karaj (2010-2014). She speaks English
and Persian.

Contact: samiraaa.zare@gmail.com or szare@ucsc.edu.
Website: samirazare.com. GitHub: github.com/SamiraZare.
LinkedIn: linkedin.com/in/samirazare.

# Technical Skills

- Languages: Python, C/C++, Assembly.
- ML / AI: PyTorch, TensorFlow, scikit-learn, OpenAI Gym, Reinforcement Learning,
  NLP, RAG (Retrieval-Augmented Generation).
- MLOps & Cloud: AWS, Federated Learning, ML Deployment Pipelines.
- Data & Analysis: Pandas, NumPy, Data Visualization, ROC-AUC Analysis, Jupyter.
- Dev Tools: PyCharm, MATLAB, Git, Autodesk Inventor.
- Hardware: Arduino, OptiTrack, PCB, Pneumatics.

# Machine Learning / AI Projects

## Neural Retrieval Router for Generative AI Systems (2026)
Built a neural router for RAG systems that determines when external retrieval is
needed, reducing LLM hallucination risk. Achieved 93% accuracy and over 0.98
ROC-AUC on adversarial queries using neural networks with dropout and L2
regularization. Applied ROC-AUC analysis and threshold tuning to optimize
precision-recall tradeoffs and model robustness.

## Intelligent AI Router (Unsupervised Learning + Recommenders + RL)
An end-to-end system that decides how to answer a query - direct LLM, retrieval
(RAG), cache, or external tool - by combining K-Means clustering, Gaussian anomaly
detection, KNN and matrix-factorization recommenders, and tabular Q-learning,
served through a FastAPI service. Trained and evaluated on real data (AI2 science
exam questions and GSM8K math problems). The learned policy beats every baseline
on routing accuracy.

## AI Housing Price & Rent-Risk Predictor with LLM Explanations (2026)
Implemented linear and logistic regression from scratch in NumPy (gradient
descent, mean normalization, cross-entropy loss) to predict housing prices and
classify rent-risk on the California Housing dataset. Layered an LLM explanation
module using prompt engineering to convert model outputs into natural-language
insights, API-compatible with OpenAI, Anthropic, and Cohere.

# Professional Experience

## Machine Learning Research Specialist Intern - TieSet, Santa Clara, CA (2020)
Designed a federated learning framework integrated with a robotics system for
secure, decentralized model training on AWS. Applied reinforcement learning and
deep learning algorithms to enhance device adaptation and autonomous control.
Optimized ML deployment pipelines and used OpenAI Gym for simulation-based RL
experiments. Co-authored a patent application demonstrating a 98% success rate in
improving device performance with scalable AI methodologies.

## Machine Learning Researcher - UC Santa Cruz (2016-2018)
Developed a spike detection algorithm in Python to identify fraudulent Yelp
reviews, improving fraud detection accuracy by 12%. Integrated spike detection
with NLP models and cleaned and visualized datasets using Pandas. This work led to
the publication "Quarantine: Detecting Unreliable Yelp Reviews" (arXiv, 2020).

## Researcher, Smart Origami Robot - UC Santa Cruz (2017-2023)
Her doctoral research focused on smart materials that change and adapt their shapes
according to available space - active origami structures for robotics. Developed
modular 3D-printed robotic joints with embedded sensors achieving 295 degrees of
rotation, surpassing traditional joint designs. Engineered pneumatic control
systems and manipulator prototypes, and integrated OptiTrack motion-capture
feedback for real-time embedded-systems control.

## STEM Research Mentor - SIP, UC Santa Cruz (2020-2023)
Mentored 20+ students in MATLAB programming, CAD modeling, and dynamic simulation.
Guided student teams designing origami-based robotic systems for humanoid and
transport applications, and coached students on research communication.

## Computer Science Teaching Assistant - UC Santa Cruz (2016-2022)
Supported 400+ students weekly across Applied Machine Learning, Python, Discrete
Math, Probability, and other CS courses over 7 years. Created solution sets and
tutored students on AI, algorithms, and probability, simplifying complex ML
concepts for diverse learners. (Classes ranged from ~50 to ~350 students.)

# Education

- Ph.D., Computer Engineering, UC Santa Cruz (2016-2023). Dissertation: "Design,
  Modeling, Simulation, and Fabrication of Origami to Improve Rotational Joint
  Performance."
- B.Sc., Computer Engineering, Islamic Azad University of Karaj (2010-2014).

# Certifications

- Unsupervised Learning, Recommenders, Reinforcement Learning - DeepLearning.AI &
  Stanford (Coursera), April 2026.
- Advanced Learning Algorithms - DeepLearning.AI & Stanford (Coursera), Feb 2026.
- Supervised Machine Learning: Regression and Classification - DeepLearning.AI &
  Stanford (Coursera), Dec 2025.

# Selected Publications

- S. Zare et al., "3D-printed self-lock origami: design, fabrication, and
  simulation," Micromachines, 2023.
- S. Zare et al., "Modular self-lock origami: design, modeling, and simulation,"
  Journal of Multi-body Dynamics, 2023.
- S. Zare & M. Teodorescu, "Design and analysis of plate angles of the four-vertex
  origami pattern," Smart Materials and Structures, 2021.
- V. Trinh, V. More, S. Zare et al., "Quarantine: Detecting Unreliable Yelp
  Reviews," arXiv:2004.09721, 2020.

# Relevant Coursework

Machine Learning, Artificial Intelligence, Robotic Manipulation, Bio-inspired
Robotics, Algorithms & Data Structures, Python Programming, Data Visualization,
Feedback Control.
"""
