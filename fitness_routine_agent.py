import streamlit as st
import cohere

# Initialize Cohere client with your API key
co = cohere.Client('YOUR_API_KEY')  # Replace with your actual key

# Function to generate fitness routine
def get_fitness_routine(goal):
    # Use the Cohere API to generate a fitness routine
    response = co.generate(
        model='command-r-plus',
        prompt=f'Generate a fitness routine for a person with the goal of {goal}.',
        max_tokens=500
    )
    
    # Return the generated text from the response
    return response.generations[0].text.strip()

# Streamlit app UI
st.title("AI Fitness Routine Assistant")

# Input fitness goal from the user
goal = st.text_input("Enter your fitness goal (e.g., weight loss, strength training, flexibility):")

if goal:
    # Get fitness routine suggestion from Cohere API
    fitness_routine = get_fitness_routine(goal)

    # Display the generated fitness routine
    st.subheader("Fitness Routine Suggestion:")
    st.write(fitness_routine)
else:
    st.info("Please enter your fitness goal to get a routine suggestion.")
