"""
•	An expert system is a computer program that is designed to solve complex problems and to provide decision-making ability like a human expert. 
•	It performs this by extracting knowledge from its knowledge base using the reasoning and inference rules according to the user queries.
•	The expert system is a part of AI, and the first ES was developed in the year 1970, which was the first successful approach of artificial intelligence. 
•	It solves the most complex issue as an expert by extracting the knowledge stored in its knowledge base. 
•	The system helps in decision making for complex problems using both facts and heuristics like a human expert. 
•	It is called so because it contains the expert knowledge of a specific domain and can solve any complex problem of that particular domain. 
•	These systems are designed for a specific domain, such as medicine, science, etc.
•	The performance of an expert system is based on the expert's knowledge stored in its knowledge base. 
•	The more knowledge stored in the KB, the more that system improves its performance. 
•	One of the common examples of an ES is a suggestion of spelling errors while typing in the Google search box.



Building An Expert System:
•	Determining the characteristics of the problem.
•	Knowledge engineer and domain expert work in coherence to define the problem.
•	The knowledge engineer translates the knowledge into a computer-understandable language. 
•	He designs an inference engine, a reasoning structure, which can use knowledge when needed.
•	Knowledge Expert also determines how to integrate the use of uncertain knowledge in the reasoning process and what type of explanation would be useful.


"""

knowledge_base={
    'commonflu': [
        'muscle pain',
        'cough',
        'fever',
        'runny nose',
        'sneezing',
        'sore throat'
    ],
    'coronavirus': [
        'loss of taste',
        'loss of smell',
        'sore throat',
        'cough',
        'fever',
        'shortness of breath'
    ]
}

# ask questions
symptoms = set([j for disease, symptoms in knowledge_base.items() for j in symptoms])
# symptoms = ['sneezing', 'shortness of breath', 'sore throat', 'fever', 'runny nose', 'loss of taste', 'loss of smell', 'muscle pain', 'cough']

user_symptoms = []
for symptom in symptoms:
    user_answer = input(f"Do you have {symptom}?[Y/N]: ")
    if user_answer == "Y":
        user_symptoms.append(symptom)

maxprobability, chance, possible_disease = 0, "have", "no disease"
for disease in knowledge_base.keys():
    count = 0
    for symptom in user_symptoms:
        if symptom in knowledge_base[disease]:
            count += 1
    probability = count / len(knowledge_base[disease])
    # print(probability, count, disease)
    if probability > maxprobability:
        maxprobability = probability
        possible_disease = disease

if maxprobability == 1:
    chance = "have"
else:
    chance = "may have"

print("You", chance, possible_disease)