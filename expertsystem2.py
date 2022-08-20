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
    'commonflu':['muscle pain','cough','fever','runny nose','sneezing','sore throat'],
    'coronavirus':['loss of taste','loss of smell','sore throat','cough','fever','shortness of breath']
}

def inference(symptoms):
    probabilty={}
    for disease in knowledge_base.keys():
        count=0
        for symptom in knowledge_base[disease]:
            if symptom in symptoms:
                count+=1
        probabilty[disease]=count/len(knowledge_base[disease])

    maxprobability=0
    for disease in probabilty.keys():
        if probabilty[disease]>maxprobability:
            maxprobability=probabilty[disease]
    
    diseases=''
    for disease in probabilty.keys():
        if probabilty[disease]==maxprobability:
            diseases+=disease+', '

    diseases=list(diseases)
    diseases[-2]='.'
    diseases=''.join(diseases)
    
    if maxprobability==1:
        print('You are having '+diseases)
    elif maxprobability>0:
        print('You may have '+diseases)
    else:
        print('You are not having any disease')

def askquestions():
    symptoms=[]
    questions=[]
    for disease in knowledge_base.keys():
        questions+=knowledge_base[disease]

    questions=list(set(questions))
    print('Please answer the following questions: ')
    for question in questions:
        answer=input(f'Do you have {question} ? [yes/no] : ' )
        if answer=='yes':
            symptoms.append(question)
    print('')
    return symptoms

symptoms=askquestions()
inference(symptoms)









