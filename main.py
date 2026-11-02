import streamlit as st

st.title("BMI Fitness Calculator")

st.write("Adjust the sliders to enter your details.")

# Weight slider
weight = st.slider("Select your weight (kg)", 1, 200, 60)

# Height slider
height = st.slider("Select your height (cm)", 50, 250, 170)

# Calculate BMI
if st.button("Calculate BMI"):

    height_m = height / 100
    bmi = weight / (height_m * height_m)

    st.subheader("Your Results")
    st.write("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        st.info("Category: Underweight")
    elif bmi < 25:
        st.success("Category: Normal weight")
    elif bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obesity")
