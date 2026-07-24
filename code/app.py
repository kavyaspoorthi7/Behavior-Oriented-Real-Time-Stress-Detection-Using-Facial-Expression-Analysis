import streamlit as st
from dataset_eval import evaluate_dataset
from webcam_core import run_webcam

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Stress Detection System",
    layout="centered"
)

st.title("AI-Based Stress Detection System")
st.markdown(
    "This system detects **stress levels** from facial expressions "
    "using **Deep Learning and Computer Vision**."
)

st.markdown("---")

# -----------------------------------
# Mode Selection
# -----------------------------------
mode = st.radio(
    "Select Input Mode:",
    ("Dataset Input", "Webcam Input")
)

# -----------------------------------
# DATASET MODE
# -----------------------------------
if mode == "Dataset Input":
    st.subheader("📁 Dataset-Based Stress Analysis")

    st.markdown(
        "This mode evaluates stress levels using a pre-trained CNN model "
        "on an authorized facial expression dataset."
    )

    model_path = "stress_model.h5"
    test_dir = "test"   # test dataset folder

    if st.button("Run Dataset Evaluation"):
        with st.spinner("Analyzing dataset..."):
            stress_percentages, bar_fig, cm_fig = evaluate_dataset(
                model_path, test_dir
            )

        st.success("Dataset analysis completed!")

        st.markdown("### 🔢 Stress Level Percentages")
        for k, v in stress_percentages.items():
            st.write(f"**{k} Stress:** {v}%")

        st.markdown("### 📊 Stress Distribution")
        st.pyplot(bar_fig)

        st.markdown("### 🔍 Stress Confusion Matrix")
        st.pyplot(cm_fig)

# -----------------------------------
# WEBCAM MODE
# -----------------------------------
elif mode == "Webcam Input":
    st.subheader("📷 Real-Time Webcam Stress Detection")

    st.markdown(
        "This mode detects facial expressions in real time using a webcam "
        "and estimates the **current stress level**."
    )

    st.warning(
        "⚠️ Webcam will open in a separate window. "
        "Press **Q** to stop the webcam."
    )

    if st.button("Start Webcam"):
        run_webcam("stress_model.h5")

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.caption(
    "Mini Project | AIML | Deep Learning & Computer Vision"
)

