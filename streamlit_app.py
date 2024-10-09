import streamlit as st
from io import StringIO

# Set page configuration
st.set_page_config(page_title="Jury Duty App", layout="centered")

# Jury duty color theme
jury_duty_colors = {
    "section_bg": "#F8F9FA",  # Light gray for background
    "header_bg": "#343A40",  # Dark gray for headers
    "jury_button": "#DC3545",  # Red for Submit button
    "verdict_color": "#28A745",  # Green for verdict results
}

# Page title
st.title("⚖️ Jury Duty App")

# Section 1: Document Upload
st.markdown(f"""
    <div style="background-color: {jury_duty_colors['section_bg']}; padding: 10px;">
        <h2 style="color: {jury_duty_colors['header_bg']};">1. Upload Documents</h2>
        <p>Upload the documents for both the defense and the prosecutor. Once uploaded, click the button to submit them to the AI Jury.</p>
    </div>
    """, unsafe_allow_html=True)

defense_file = st.file_uploader("Upload Defense Document", type=["pdf", "docx", "txt"], key="defense")
prosecutor_file = st.file_uploader("Upload Prosecutor Document", type=["pdf", "docx", "txt"], key="prosecutor")

# Section 2: Submit to Jury and AI Model Responses
st.markdown(f"""
    <div style="background-color: {jury_duty_colors['section_bg']}; padding: 10px;">
        <h2 style="color: {jury_duty_colors['header_bg']};">2. Submit to Jury</h2>
    </div>
    """, unsafe_allow_html=True)

# Placeholder for AI Jury outputs
verdict_claude = st.empty()
verdict_mistral = st.empty()
verdict_llama = st.empty()

# Submit Button
if defense_file and prosecutor_file:
    if st.button("Submit to Jury", key="submit_button", help="Submit the documents to the AI Jury"):
        st.markdown(f'<p style="color: {jury_duty_colors["jury_button"]};">Submitting documents to AI models...</p>', unsafe_allow_html=True)
        
        # Placeholder logic for connecting to AWS Bedrock AI models (Claude, Mistral, Llama)
        # In practice, here you would connect and send the files to AWS Bedrock models
        # For demonstration, we'll simulate the API response
        def mock_jury_response(model_name):
            # Simulated response from an AI jury model
            return f"{model_name}: Verdict - Not Guilty (Reasoning: Insufficient evidence provided.)"
        
        # Simulating responses from the three AI models
        claude_response = mock_jury_response("Claude")
        mistral_response = mock_jury_response("Mistral")
        llama_response = mock_jury_response("Llama")

        # Display the AI model outputs in respective sections
        verdict_claude.text_area("Justice Claude", value=claude_response, height=100)
        verdict_mistral.text_area("Justice Mistral", value=mistral_response, height=100)
        verdict_llama.text_area("Justice Llama", value=llama_response, height=100)

# Section 3: Final Verdict
st.markdown(f"""
    <div style="background-color: {jury_duty_colors['section_bg']}; padding: 10px;">
        <h2 style="color: {jury_duty_colors['header_bg']};">3. Final Verdict</h2>
    </div>
    """, unsafe_allow_html=True)

# Display Guilty or Not Guilty based on AI jury outputs
if defense_file and prosecutor_file:
    # For simplicity, we'll assume that if any AI says Guilty, the verdict is Guilty
    final_verdict = "Not Guilty" if all("Not Guilty" in resp for resp in [claude_response, mistral_response, llama_response]) else "Guilty"
    st.markdown(f'<h3 style="color: {jury_duty_colors["verdict_color"]};">Verdict: {final_verdict}</h3>', unsafe_allow_html=True)
