# sales intelligence using COT prompts and chatgpt functions.
Sales intelligence using chatgpt apis and chatgpt functions .  A simple example which demonstrates how enterprise can use crm/hrm data to train chatgpt and get insights

## Chain of thought

chain-of-thought (CoT) prompting enables complex reasoning capabilities through intermediate reasoning steps.The reason that chain of thought prompting works is actually kind of intuitive, if you think about it. These things don’t have memories, but they’re always looking at the previous tokens that they’ve already output. So you can get them to think through step by step. It’s just like a person thinking out loud has exactly the same impact.

## Use case 

Persona of user is marketing analyst of product company which sells to banks.

Ask chatgpt what are top 2 banks in india 

From top 2 banks , we will query enterprise CRM system , 
 what is  relationship of the bank with product company  , is it customer or not customer
 What is the existing sales volume 

With this enterprise data , we would ask chatgpt api , what is the  bank we can do marketing campaign and why

With the bank selected , we want to check we can schedule the marketing campaigns , 
for this we use data from enterprise repository .
What are current campaigns which are running . 
What are dates of the campaigns when sales team is busy 

We want to make it interesting , we ask chatgpt not to schedule for Diwali holidays  

## How to run 

Pre-requisite for running this code is openai key  :smiley: .
It is has to put in app.properties
OPENAI_KEY=< your key here>

you will need local installation of jupyter notebook . 
Simply run one of the two notebooks
* usingEnterpriseData.ipynb or 
* usingEnterpriseData_v2.ipynb




