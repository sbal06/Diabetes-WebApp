# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 00:15:59 2023

@author: Zhizhen L., Shreyes B.
"""

import streamlit as st
import numpy as np
import itertools
import random
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.app_logo import add_logo
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.streaming_write import write
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.markdownlit import mdlit
import os
import time



# Get the current directory of the file (predictive.py)
current_directory2 = os.path.dirname(os.path.realpath(__file__))
# Construct the relative path to the model file within the app's directory
model_filename2 = "diaaid2y.png"
model_path2 = os.path.join(current_directory2, model_filename2)

add_logo(model_path2, height = 100)


st.title("Personalized Meal Plans")
# st.write("The development of the Personalized Meal Plans is in progress. Please be patient as we work towards its completion. Meanwhile, you can access the code here and run it locally: ")

mdlit(
      """[red] If you know that you are diabetic, please select very high risk regardless of model output. [/red]

"""
)

# Jai Shri Ram
st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

fruits_options = [
    {
        'name': 'Apple',
        'calories': 52,
        'protein': 0.26,
        'fat': 0.17,
        'fiber': 4,
        'allergies': 'None',
        'carbs': 14
    },
    {
        'name': 'Banana',
        'calories': 105,
        'protein': 1.29,
        'fat': 0.39,
        'fiber': 2.6,
        'allergies': 'Latex-fruit syndrome (cross-reactivity)',
        'carbs': 27
    },
    {
        'name': 'Grapes',
        'calories': 69,
        'protein': 0.72,
        'fat': 0.16,
        'fiber': 1.4,
        'allergies': 'None',
        'carbs': 18
    },
    {
        'name': 'Pineapple',
        'calories': 82,
        'protein': 0.89,
        'fat': 0.19,
        'fiber': 13,
        'allergies': 'Rare pineapple allergies (irritation)',
        'carbs': 21
    },
    {
        'name': 'Orange',
        'calories': 62,
        'protein': 1.23,
        'fat': 0.16,
        'fiber': 3,
        'allergies': 'None',
        'carbs': 15
    }
]

vegetables_options = [
    {
        # values might change for the caprese salad, it is a bit confusing.
        # chanegd from 220 to 175 8/29/2023
        
        # changed 8/31/2023 to Zucchini Noodles with Pesto
        'name': 'Zucchini Noodles with Pesto',
        'calories': 240,
        'protein': 19.5,
        'fat': 14.5,
        'fiber': 2.5,
        'allergies': 'Pine nuts',
        'carbs': 9
    },

    {
        'name': 'Ratatouille',
        'calories': 140,
        'protein': 2.4,
        'fat': 10,
        'fiber': 4.1,
        'allergies': 'None',
        'carbs': 12
    },

    {
        'name': 'Gado-Gado',
        'calories': 350,
        'protein': 17.5,
        'fat': 17.5,
        'fiber': 7,
        'allergies': 'peanuts, soy',
        'carbs': 35
    },
    {
        'name': 'Aloo Gobi',
        'calories': 250,
        'protein': 7.5,
        'fat': 12.5,
        'fiber': 2.8,
        'allergies': 'None',
        'carbs': 15
    },
    {
        'name': 'Stir-Fried Mixed Vegetables',
        'calories': 200,
        'protein': 4.5,
        'fat': 11,
        'fiber': 5,
        'allergies': 'None',
        'carbs': 15
    },
]


# change values if necessary!
meat_foods_options = [
    {
        'name': 'Steak',
        'calories': 179,
        'protein': 26,
        'fat': 7.6,
        'fiber': 0,
        'allergies': 'None',
        'carbs': 0
    },
    {
        'name': 'Roast Chicken',
        'calories': 190,
        'protein': 20,
        'fat': 11,
        'fiber': 0,
        'allergies': 'None',
        'carbs': 0
    },
    {
        'name': 'BBQ Ribs',
        'calories': 381,
        'protein': 19.5,
        'fat': 28.5,
        'fiber': 0.1,
        'allergies': 'None',
        'carbs': 11.5
    },
    {
        # 3 ounce serving
        'name': 'Sushi Sashimi',
        'calories': 225,
        'protein': 20.5,
        'fat': 4.4,
        'fiber': 0,
        'allergies': 'Seafood, potential cross-contamination',
        'carbs': 0
    },
    {
        'name': 'Tandoori Chicken',
        'calories': 200,
        'protein': 25,
        'fat': 12,
        'fiber': 0.7,
        'allergies': 'Dairy (marinade), potential spices',
        'carbs': 6.1
    }
]


# change values if necessary!
dairy_options = [
    {
        'name': 'Whole Milk',
        'calories': 150,
        'protein': 8,
        'fat': 8,
        'fiber': 0,
        'allergies': 'Lactose intolerance',
        'carbs': 12
    },
    {
        'name': 'Low-Fat Milk',
        'calories': 102,
        'protein': 8.2,
        'fat': 2.4,
        'fiber': 0,
        'allergies': 'Lactose intolerance',
        'carbs': 12
    },
    {
        'name': 'Cheddar Cheese',
        'calories': 110,
        'protein': 7,
        'fat': 9,
        'fiber': 0,
        'allergies': 'Dairy',
        'carbs': 0.9
    },
    {
        'name': 'Ice Cream',
        'calories': 273,
        'protein': 3.5,
        'fat': 15,
        'fiber': 0.9,
        'allergies': 'Dairy',
        'carbs': 31
    },
    {
        'name': 'Yogurt',
        'calories': 115,
        'protein': 6,
        'fat': 3,
        'fiber': 0,
        'allergies': 'Dairy',
        'carbs': 12
    }
]

grains_options = [
    {
        'name': 'Plain Rice',
        'calories': 175,
        'protein': 3.5,
        'fat': 0,
        'fiber': 0.9,
        'allergies': 'None',
        'carbs': 44
    },
    {
        'name': 'Polenta',
        'calories': 145,
        'protein': 3.5,
        'fat': 1,
        'fiber': 1,
        'allergies': 'None',
        'carbs': 17
    },
    {
        'name': 'Grits',
        'calories': 151,
        'protein': 2.9,
        'fat': 0.9,
        'fiber': 1.6,
        'allergies': 'None',
        'carbs': 32
    },
    {
        'name': 'Farro Salad',
        'calories': 120,
        'protein': 7,
        'fat': 1.5,
        'fiber': 4.2,
        'allergies':'Wheat',
        'carbs': 19
    },
    {
        'name': 'Millet Porridge',
        'calories': 225,
        'protein': 6.1,
        'fat': 1.7,
        'fiber': 2.3,
        'allergies': 'None',
        'carbs': 27
    }
]


meal_options = {   # these are the meal options, a dictionary -- mapping an item to an dictionary of items
    'fruits': fruits_options,
    'vegetables': vegetables_options,
    'protein_foods': meat_foods_options,
    'dairy': dairy_options,
    'grains': grains_options
}

def main():
    prediction_results = selectbox("What is your results from one of our prediction models?", ("Low", "Medium", "High", "Very High"), key = "prediction")

    if prediction_results == "Low":
        st.write("That is very good news. However, one of the most effective ways to prevent diabetes is to have a healthy lifestyle.")
        vegetarian, lactose_intolerant = answer_two_questions()
        answer_optional_questions(vegetarian, lactose_intolerant)
    elif prediction_results == "Medium":
        st.write("Not bad! However, one of the most effective ways to prevent diabetes is to have a healthy lifestyle.")
        vegetarian, lactose_intolerant = answer_two_questions()
        answer_optional_questions(vegetarian, lactose_intolerant)
    elif prediction_results == "High" or prediction_results == "Very High":
        st.write("Not the best news but that's okay. We are here for you. Maintaining a healthy lifestyle is among the most important in preventing and managing diabetes.")
        vegetarian, lactose_intolerant = answer_two_questions()
        answer_optional_questions(vegetarian, lactose_intolerant)


def answer_two_questions():
    vegetarian = selectbox("Do you identify as vegetarian?", ("Yes", "No"), key = "veg")
    lactose_intolerant = selectbox("Do you have lactose intolerance?", ("Yes", "No"), key = "lactose")
    
    
    return vegetarian, lactose_intolerant
        
    


def answer_optional_questions(vegetarian, lactose_intolerant):
    answer_optional = selectbox("Do you want to answer optional questions for a personalized meal plan?", ("Yes", "No"), key = "1")
    if answer_optional == "Yes":
        ideal_calories = st.number_input("What is your ideal calories intake? If you do not know, do not enter any values: ", key="cal", format = "%.1f")
        if ideal_calories != 'idk':
            ideal_calories = float(ideal_calories)

        ideal_protein = st.number_input("What is your ideal protein intake in grams? If you do not know, do not enter values: ", key="protein", format = "%.1f")
        if ideal_protein != 'idk':
            ideal_protein = float(ideal_protein)

        ideal_fat = st.number_input("What is your ideal fat intake in grams? If you do not know, do not enter values: ", key="fat", format = "%.1f")
        if ideal_fat != 'idk':
            ideal_fat = float(ideal_fat)

        ideal_carbs = st.number_input("What is your ideal carbohydrate intake in grams? If you do not know, do not enter values: ", key="carbohydrates", format = "%.1f")
        if ideal_carbs != 'idk':
            ideal_carbs = float(ideal_carbs)
            
            
        if (ideal_calories == 0):
            ideal_calories = random.randrange(533, 800, 1)
            
        if (ideal_protein == 0):
            ideal_protein = random.randrange(20, 30, 1)
            
        if (ideal_fat == 0):
            ideal_fat = random.randrange(9, 20, 1)
            
        if (ideal_carbs == 0):
            ideal_carbs = random.randrange(40, 60, 1)
            
            
        
        
            
    
    
        # ideal_carbs = input("What is your ideal carb intake in grams? Enter a value or idk to skip: ")

        # meal_plan = generate_random_meal_plan(vegetarian, lactose_intolerant, meal_options)
        best_plan = compare_meal_plans(ideal_calories, ideal_protein, ideal_fat, ideal_carbs, vegetarian, lactose_intolerant)
        generate_meal_plan(best_plan, ideal_calories, ideal_protein, ideal_fat, ideal_carbs, vegetarian, lactose_intolerant)
    elif answer_optional == "No":
        generate_random_meal(vegetarian, lactose_intolerant)
    # else:
      #  st.write("Invalid input. Please enter Yes or No.")
      #  answer_optional_questions(vegetarian, lactose_intolerant)

def generate_random_meal(vegetarian, lactose_intolerant):
    meal_plan = {
        'fruits': random.choice(fruits_options),
        'vegetarian': random.choice(vegetables_options),
        'grains': random.choice(grains_options),
        'meat': None,
        'dairy': None
    }

    # adding the protein foods back since the user is not vegetarian.
    if (vegetarian == "No"):
      meal_plan['meat'] = random.choice(meat_foods_options)

    # adding the dairy foods back since the user is not lactose intolerant.
    if (lactose_intolerant == "No"):
      meal_plan['dairy'] = random.choice(dairy_options)

    # each cateogry it is picking randomly
    
    with stylable_container(
    key="green_button",
    css_styles="""
        button {
            background-color: green;
            color: white;
            border-radius: 20px;
        }
        """,
):
        random_meal_plan = st.button("Generate Meal Plan")
        
        
            
        if (random_meal_plan):
            write(stream_example())
            time.sleep(0.2)
        
            if (vegetarian == "No"):
              if (lactose_intolerant == "No"):
                 st.write("\nGenerated Random Meal:")
                 st.write("Fruits: {}, Allergies: {} ".format(meal_plan['fruits']['name'],meal_plan['fruits']['allergies']))
                 st.write("Vegetables: {}, Allergies: {} ".format(meal_plan['vegetarian']['name'],meal_plan['vegetarian']['allergies']))
                 st.write("Meat: {}, Allergies: {} ".format(meal_plan['meat']['name'],meal_plan['meat']['allergies']))
                 st.write("Dairy: {}, Allergies: {} ".format(meal_plan['dairy']['name'],meal_plan['dairy']['allergies']))
                 st.write("Grains: {}, Allergies: {} ".format(meal_plan['grains']['name'],meal_plan['grains']['allergies']))

              else:
                 st.write("\nGenerated Random Meal:")
                 st.write("Fruits: {}, Allergies: {} ".format(meal_plan['fruits']['name'],meal_plan['fruits']['allergies']))
                 st.write("Vegetables: {}, Allergies: {} ".format(meal_plan['vegetarian']['name'],meal_plan['vegetarian']['allergies']))
                 st.write("Meat: {}, Allergies: {} ".format(meal_plan['meat']['name'],meal_plan['meat']['allergies']))
                 st.write("Dairy: None (lactose intolerant)")
                 st.write("Grains: {}, Allergies: {} ".format(meal_plan['grains']['name'],meal_plan['grains']['allergies']))

            else:
              if (lactose_intolerant == "No"):
                 st.write("\nGenerated Random Meal:")        
                 st.write("Fruits: {}, Allergies: {} ".format(meal_plan['fruits']['name'],meal_plan['fruits']['allergies']))
                 st.write("Vegetables: {}, Allergies: {} ".format(meal_plan['vegetarian']['name'],meal_plan['vegetarian']['allergies']))
                 st.write("Meat: None (vegetarian)")
                 st.write("Dairy: {}, Allergies: {} ".format(meal_plan['dairy']['name'],meal_plan['dairy']['allergies']))
                 st.write("Grains: {}, Allergies: {} ".format(meal_plan['grains']['name'],meal_plan['grains']['allergies']))

              else:
                 st.write("\nGenerated Random Meal:")
                 st.write("Fruits: {}, Allergies: {} ".format(meal_plan['fruits']['name'],meal_plan['fruits']['allergies']))
                 st.write("Vegetables: {}, Allergies: {} ".format(meal_plan['vegetarian']['name'],meal_plan['vegetarian']['allergies']))
                 st.write("Meat: None (vegetarian)")
                 st.write("Dairy: None (lactose intolerant)")
                 st.write("Grains: {}, Allergies: {} ".format(meal_plan['grains']['name'],meal_plan['grains']['allergies']))
            
        
        
       
            
    



def compare_meal_plans(ideal_calories, ideal_protein, ideal_fat, ideal_carbs, vegetarian, lactose_intolerant):

  # okay meal_plan is a dictionary I believe -- with the choice of each category are dictionaries
    best_difference = float('inf')
    best_plan = {
        'fruits': None,
        'vegetables': None,
        'meat':None,
        'dairy':None,
        'grains':None

    }
    # ... (rest of the function remains the same)

    random.shuffle(fruits_options)
    random.shuffle(dairy_options)
    random.shuffle(grains_options)
    random.shuffle(meat_foods_options)
    random.shuffle(vegetables_options)

    # change option_list based on vegetarian and lactose intolerant
    if (vegetarian == "Yes"):
      if (lactose_intolerant == "Yes"):
        option_list = [fruits_options, vegetables_options, grains_options]
        del best_plan['meat']
        del best_plan['dairy']
      else:
        option_list = [fruits_options, vegetables_options, dairy_options, grains_options]
        del best_plan['meat']

    elif (vegetarian == "No"):
      if (lactose_intolerant == "Yes"):
        option_list = [fruits_options, vegetables_options, meat_foods_options, grains_options]
        del best_plan['dairy']

      else:
        option_list = [fruits_options, vegetables_options, meat_foods_options, dairy_options, grains_options]

    # for each one in the map -- then add that to a map (like each one in fruits_options, vegetable_options, etc.)
    for combination in itertools.product(*option_list):
      total_calories = sum(item['calories'] for item in combination)
      total_protein = sum(item['protein'] for item in combination)
      total_fat = sum(item['fat'] for item in combination)
      total_carbs = sum(item['carbs'] for item in combination)

        # Calculate differences between user's goals and actual values
      cal_difference = abs(total_calories - ideal_calories) if ideal_calories != "idk" else 0
      protein_difference = abs(total_protein - ideal_protein) if ideal_protein != "idk" else 0
      fat_difference = abs(total_fat - ideal_fat) if ideal_fat != "idk" else 0
      carbs_difference = abs(total_carbs - ideal_carbs) if ideal_carbs != "idk" else 0

        # Calculate a weighted total difference
      total_difference = cal_difference + protein_difference + fat_difference + carbs_difference

      if total_difference < best_difference:
            best_difference = total_difference

            best_plan_key = list(best_plan.keys())

            for count, element in enumerate(best_plan_key):
              best_plan[element] = combination[count]



    return best_plan




def generate_meal_plan(best_plan, ideal_calories, ideal_protein, ideal_fat, ideal_carbs, vegetarian, lactose_intolerant):
    # ... (rest of the function remains the same)
    
    with stylable_container(
    key="green_button",
    css_styles="""
        button {
            background-color: green;
            color: white;
            border-radius: 20px;
        }
        """,
):
        generate_meal_plan = st.button("Generate Meal Plan")
        
        
    if (generate_meal_plan):
        write(stream_example())
        time.sleep(0.2)
        
        
        if (vegetarian == "Yes"):
          if (lactose_intolerant == "Yes"):
             
            st.write("\nGenerated Meal Plan:")
            st.write("Fruits: {}, Allergies: {} ".format(best_plan['fruits']['name'],best_plan['fruits']['allergies']))
            st.write("Vegetables: {}, Allergies: {} ".format(best_plan['vegetables']['name'],best_plan['vegetables']['allergies']))
            st.write("Meat: None (vegetarian)")
            st.write("Dairy: None (lactose intolerant)")
            st.write("Grains: {}, Allergies: {} ".format(best_plan['grains']['name'],best_plan['grains']['allergies']))

          else:
            st.write("\nGenerated Meal Plan:")
            st.write("Fruits: {}, Allergies: {} ".format(best_plan['fruits']['name'],best_plan['fruits']['allergies']))
            st.write("Vegetables: {}, Allergies: {} ".format(best_plan['vegetables']['name'],best_plan['vegetables']['allergies']))
            st.write("Meat: None (vegetarian)")
            st.write("Dairy: {}, Allergies: {} ".format(best_plan['dairy']['name'],best_plan['dairy']['allergies']))
            st.write("Grains: {}, Allergies: {} ".format(best_plan['grains']['name'],best_plan['grains']['allergies']))

        elif (vegetarian == "No"):
          if (lactose_intolerant == "Yes"):
            st.write("\nGenerated Meal Plan:")
            st.write("Fruits: {}, Allergies: {} ".format(best_plan['fruits']['name'],best_plan['fruits']['allergies']))
            st.write("Vegetables: {}, Allergies: {} ".format(best_plan['vegetables']['name'],best_plan['vegetables']['allergies']))
            st.write("Meat: {}, Allergies: {} ".format(best_plan['meat']['name'],best_plan['meat']['allergies']))
            st.write("Dairy: None (lactose intolerant)")
            st.write("Grains: {}, Allergies: {} ".format(best_plan['grains']['name'],best_plan['grains']['allergies']))

          else:
            st.write("\nGenerated Meal Plan:")
            st.write("Fruits: {}, Allergies: {} ".format(best_plan['fruits']['name'],best_plan['fruits']['allergies']))
            st.write("Vegetables: {}, Allergies: {} ".format(best_plan['vegetables']['name'],best_plan['vegetables']['allergies']))
            st.write("Meat: {}, Allergies: {} ".format(best_plan['meat']['name'],best_plan['meat']['allergies']))
            st.write("Dairy: {}, Allergies: {} ".format(best_plan['dairy']['name'],best_plan['dairy']['allergies']))
            st.write("Grains: {}, Allergies: {} ".format(best_plan['grains']['name'],best_plan['grains']['allergies']))
        
        
        



def stream_example():
    wordList = "Here is your generated meal plan!"
    for word in wordList.split():
        yield word + " "
        time.sleep(0.15)
        
        
    


if __name__ == "__main__":
    main()
