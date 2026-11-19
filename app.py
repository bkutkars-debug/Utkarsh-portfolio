import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import io

# Page Configuration
st.set_page_config(
    page_title="Utkarsh Dwivedi | AI-ML Engineer & Full Stack Developer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Luxury / Cyber Aesthetic CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    .stApp {
        background-color: #060913;
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    [data-testid="stSidebar"] {
        background-color: #090d1a !important;
        border-right: 1px solid rgba(56, 189, 248, 0.18) !important;
    }

    .stButton>button {
        background: linear-gradient(135deg, #0284c7 0%, #6366f1 100%) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        padding: 0.55rem 1.25rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.4) !important;
    }

    .metric-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 14px;
        padding: 1.25rem;
        backdrop-filter: blur(16px);
        margin-bottom: 1rem;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
    }

    .hero-badge {
        display: inline-block;
        background: rgba(56, 189, 248, 0.12);
        border: 1px solid rgba(56, 189, 248, 0.3);
        color: #38bdf8;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .gradient-header {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    .code-pill {
        background: #040711;
        border: 1px solid rgba(56, 189, 248, 0.2);
        color: #93c5fd;
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.82rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Identity & Navigation
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div style="width: 70px; height: 70px; margin: 0 auto 0.8rem auto; border-radius: 18px; background: linear-gradient(135deg, #0284c7, #6366f1); display: flex; align-items: center; justify-content: center; font-size: 1.8rem; font-weight: 800; color: white; box-shadow: 0 0 25px rgba(56, 189, 248, 0.5);">
            UD
        </div>
        <h2 style="margin: 0; font-size: 1.35rem; font-weight: 800; color: #f8fafc;">Utkarsh Dwivedi</h2>
        <p style="margin: 0.2rem 0 0.8rem 0; font-size: 0.82rem; color: #38bdf8; font-weight: 700; text-transform: uppercase;">
            B.Tech AI-ML &bull; UCER Prayagraj
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    nav_choice = st.radio(
        "Navigation",
        [
            "🌌 3D Aesthetic Experience (Full WebGL)",
            "🧠 Python ML Training Workbench",
            "📊 Data Feeding & NumPy/Pandas",
            "🛡️ Featured Systems (Rakshak & SafeReach)",
            "🎓 Education & Resume PDF",
            "📬 Connect & Direct Contact"
        ],
        index=0
    )

    st.markdown("---")

    st.markdown("""
    <div style="font-size: 0.85rem; color: #94a3b8; line-height: 1.8;">
        <div>📍 <strong>Location:</strong> Prayagraj, UP, India</div>
        <div>📧 <strong>Email:</strong> bkutkars@gmail.com</div>
        <div>📱 <strong>Phone:</strong> +91 7905499755</div>
        <div>🐙 <strong>GitHub:</strong> <a href="https://github.com/bkutkars-debug" target="_blank" style="color: #38bdf8;">@bkutkars-debug</a></div>
        <div>💼 <strong>LinkedIn:</strong> <a href="https://linkedin.com/in/utkarsh-dwivedi-b3b5b5281" target="_blank" style="color: #818cf8;">Profile</a></div>
    </div>
    """, unsafe_allow_html=True)

    # Resume Download in Sidebar
    resume_path = os.path.join(os.path.dirname(__file__), "Utkarsh_Dwivedi_Resume.pdf")
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume (PDF)",
                data=pdf_file,
                file_name="Utkarsh_Dwivedi_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )

# -------------------------------------------------------------
# VIEW 1: 3D AESTHETIC EXPERIENCE (FULL WEBGL & INTERACTIVE)
# -------------------------------------------------------------
if nav_choice == "🌌 3D Aesthetic Experience (Full WebGL)":
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem;">
        <div>
            <div class="hero-badge">Interactive 3D WebGL Portfolio</div>
            <h1 class="gradient-header" style="margin: 0;">Utkarsh Dwivedi &bull; Digital Experience</h1>
            <p style="color: #94a3b8; margin-top: 0.3rem;">
                B.Tech AI-ML Student @ United College of Engineering and Research (UCER), Prayagraj.
            </p>
        </div>
        <div>
            <a href="/app/static/index.html" target="_blank" style="text-decoration: none;">
                <button style="background: linear-gradient(135deg, #0284c7, #6366f1); color: white; border: none; padding: 0.6rem 1.2rem; border-radius: 8px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 0.5rem;">
                    🚀 Open Fullscreen in New Tab
                </button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Render static built HTML
    static_html_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(static_html_path):
        components.iframe(src="/app/static/index.html", height=1100, scrolling=True)
    else:
        st.warning("Building static web bundle... Please wait or view the native Python ML tabs.")

# -------------------------------------------------------------
# VIEW 2: PYTHON ML TRAINING WORKBENCH (NATIVE STREAMLIT)
# -------------------------------------------------------------
elif nav_choice == "🧠 Python ML Training Workbench":
    st.markdown("""
    <div class="hero-badge">Scikit-Learn & Python Model Engine</div>
    <h1 class="gradient-header">Machine Learning Model Training & Convergence</h1>
    <p style="color: #94a3b8;">
        Live interactive Python training loop demonstrating Utkarsh's model building, loss minimization, and performance evaluation capabilities.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.subheader("⚙️ Training Hyperparameters")
        
        from sklearn.datasets import make_classification
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.neural_network import MLPClassifier
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

        model_name = st.selectbox(
            "Select Algorithm",
            ["Neural Network (MLP)", "Random Forest", "Logistic Regression (L2)"]
        )

        n_samples = st.slider("Dataset Size (Samples)", 200, 1500, 600, step=100)
        test_size = st.slider("Test Split Ratio", 0.15, 0.40, 0.25, step=0.05)
        random_state = st.number_input("Random Seed", value=42)

        if model_name == "Neural Network (MLP)":
            max_iter = st.slider("Max Iterations / Epochs", 20, 200, 80)
            alpha_lr = st.select_slider("Learning Rate α", options=[0.001, 0.005, 0.01, 0.02, 0.05], value=0.01)
        elif model_name == "Random Forest":
            n_estimators = st.slider("Number of Trees", 10, 150, 50)
            max_depth = st.slider("Tree Max Depth", 2, 15, 6)

        train_btn = st.button("🚀 Train Model Now", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.subheader("📈 Live Model Evaluation")

        # Generate dataset
        X, y = make_classification(
            n_samples=n_samples, 
            n_features=4, 
            n_informative=3, 
            n_redundant=1, 
            random_state=int(random_state)
        )
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=int(random_state))

        # Model instantiation
        if model_name == "Neural Network (MLP)":
            clf = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=max_iter, learning_rate_init=alpha_lr, random_state=int(random_state))
        elif model_name == "Random Forest":
            clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=int(random_state))
        else:
            clf = LogisticRegression(random_state=int(random_state))

        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, zero_division=0)
        rec = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)

        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        m_col1.metric("Accuracy", f"{acc * 100:.1f}%")
        m_col2.metric("Precision", f"{prec:.3f}")
        m_col3.metric("Recall", f"{rec:.3f}")
        m_col4.metric("F1-Score", f"{f1:.3f}")

        # Matplotlib Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots(figsize=(6, 3.2), facecolor='#090d1a')
        ax.set_facecolor('#040711')
        im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        fig.colorbar(im, ax=ax)
        ax.set(xticks=np.arange(cm.shape[1]), yticks=np.arange(cm.shape[0]),
               xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'],
               title=f'{model_name} Confusion Matrix',
               ylabel='Actual Label', xlabel='Predicted Label')
        ax.title.set_color('#38bdf8')
        ax.xaxis.label.set_color('#cbd5e1')
        ax.yaxis.label.set_color('#cbd5e1')
        ax.tick_params(colors='#94a3b8')

        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(j, i, format(cm[i, j], 'd'),
                        ha="center", va="center",
                        color="white" if cm[i, j] > cm.max() / 2. else "#93c5fd",
                        fontweight='bold')

        plt.tight_layout()
        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# VIEW 3: DATA FEEDING & NUMPY/PANDAS STUDIO
# -------------------------------------------------------------
elif nav_choice == "📊 Data Feeding & NumPy/Pandas":
    st.markdown("""
    <div class="hero-badge">Data Handling & Tensor Preprocessing</div>
    <h1 class="gradient-header">NumPy, Pandas & Matplotlib Pipelines</h1>
    <p style="color: #94a3b8;">
        Demonstrating data ingestion, statistical anomaly detection, null imputation, and mathematical normalization.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.subheader("📋 Ingested Sensor & Distress Feed")
        
        # Synthetic DataFrame
        np.random.seed(42)
        n_rows = 150
        raw_data = {
            'Incident_ID': [f"INC-{1000 + i}" for i in range(n_rows)],
            'Pulse_Rate_BPM': np.random.normal(82, 18, n_rows).round(1),
            'Impact_G_Force': np.random.exponential(1.8, n_rows).round(2),
            'Ambient_Temp_C': np.random.uniform(22, 38, n_rows).round(1),
            'Urgency_Score': np.random.randint(15, 99, n_rows)
        }
        df = pd.DataFrame(raw_data)
        
        # Add random nulls to demonstrate imputation
        df.loc[12, 'Pulse_Rate_BPM'] = np.nan
        df.loc[45, 'Ambient_Temp_C'] = np.nan

        st.dataframe(df.head(8), use_container_width=True)

        st.markdown("**Pandas Data Cleaning & Imputation:**")
        null_count = df.isnull().sum().sum()
        st.info(f"Detected {null_count} missing values in feed. Imputing with column median values via `df.fillna()`...")
        df.fillna(df.median(numeric_only=True), inplace=True)
        st.success("✅ Cleaned DataFrame: 0 null entries remaining.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.subheader("📊 Normalization Histogram (Matplotlib)")

        scaler_type = st.radio("Transformation Algorithm", ["StandardScaler (Z-Score)", "MinMaxScaler [0, 1]"], horizontal=True)

        feature_to_plot = df['Pulse_Rate_BPM'].values

        if scaler_type == "StandardScaler (Z-Score)":
            scaled_vals = (feature_to_plot - np.mean(feature_to_plot)) / np.std(feature_to_plot)
            x_label = "Standard Deviations (μ=0, σ=1)"
            bar_color = "#38bdf8"
        else:
            scaled_vals = (feature_to_plot - np.min(feature_to_plot)) / (np.max(feature_to_plot) - np.min(feature_to_plot))
            x_label = "Normalized Range [0.0, 1.0]"
            bar_color = "#34d399"

        fig2, ax2 = plt.subplots(figsize=(5.5, 3.2), facecolor='#090d1a')
        ax2.set_facecolor('#040711')
        ax2.hist(scaled_vals, bins=14, color=bar_color, edgecolor='#060913', alpha=0.85)
        ax2.set_title(f"{scaler_type} Distribution", color='#38bdf8', fontsize=11, fontweight='bold')
        ax2.set_xlabel(x_label, color='#cbd5e1')
        ax2.set_ylabel("Frequency Count", color='#cbd5e1')
        ax2.tick_params(colors='#94a3b8')
        plt.tight_layout()
        st.pyplot(fig2)

        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# VIEW 4: FEATURED SYSTEMS
# -------------------------------------------------------------
elif nav_choice == "🛡️ Featured Systems (Rakshak & SafeReach)":
    st.markdown("""
    <div class="hero-badge">Production Architecture</div>
    <h1 class="gradient-header">Flagship Autonomous & Backend Systems</h1>
    """, unsafe_allow_html=True)

    sys1, sys2 = st.columns(2)

    with sys1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #38bdf8; margin-top: 0;">🛡️ Rakshak AI</h3>
            <p style="font-size: 0.85rem; color: #a5b4fc; font-weight: 700;">AUTONOMOUS MULTI-AGENT EMERGENCY PLATFORM</p>
            <p style="color: #94a3b8; font-size: 0.92rem; line-height: 1.6;">
                Transforms frantic multimodal inputs (speech audio, scene computer vision, GPS) into deterministic life-saving dispatches. 
                Features a 6-agent Directed Acyclic Graph (DAG) pipeline, explainable 0–100 urgency score, and contraindication safety shield.
            </p>
            <div style="margin: 0.8rem 0;">
                <span class="code-pill">Python</span>
                <span class="code-pill">Multi-Agent DAG</span>
                <span class="code-pill">Computer Vision</span>
                <span class="code-pill">FastAPI</span>
            </div>
            <a href="https://github.com/bkutkars-debug" target="_blank" style="color: #38bdf8; text-decoration: none; font-weight: 700; font-size: 0.9rem;">
                View Source on GitHub →
            </a>
        </div>
        """, unsafe_allow_html=True)

    with sys2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #ef4444; margin-top: 0;">🚨 SafeReach SOS</h3>
            <p style="font-size: 0.85rem; color: #fca5a5; font-weight: 700;">REAL-TIME EMERGENCY LOCATION DISPATCH</p>
            <p style="color: #94a3b8; font-size: 0.92rem; line-height: 1.6;">
                Mobile-first SOS emergency web application that broadcasts high-precision GPS satellite coordinates to emergency contacts (+91 7905499755) and direct India hotline 112. Built with Node.js, Express, MongoDB, and Twilio SMS.
            </p>
            <div style="margin: 0.8rem 0;">
                <span class="code-pill">Node.js</span>
                <span class="code-pill">MongoDB</span>
                <span class="code-pill">Twilio API</span>
                <span class="code-pill">Leaflet Maps</span>
            </div>
            <a href="https://github.com/bkutkars-debug" target="_blank" style="color: #ef4444; text-decoration: none; font-weight: 700; font-size: 0.9rem;">
                View Source on GitHub →
            </a>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# VIEW 5: EDUCATION & RESUME PDF
# -------------------------------------------------------------
elif nav_choice == "🎓 Education & Resume PDF":
    st.markdown("""
    <div class="hero-badge">Academic Milestone & Credentials</div>
    <h1 class="gradient-header">Education & Achievements</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-card">
        <h3 style="color: #38bdf8; margin: 0;">United College of Engineering and Research (UCER)</h3>
        <p style="color: #a5b4fc; font-weight: 700; margin: 0.2rem 0;">B.Tech in Artificial Intelligence & Machine Learning (AI-ML) &bull; 2026 – Present</p>
        <p style="color: #94a3b8; font-size: 0.92rem; margin: 0.5rem 0;">Prayagraj, Uttar Pradesh, India</p>
        <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Core coursework: Machine Learning, Neural Networks, Data Structures & Algorithms, Object-Oriented Programming (C++/Java), Database Management Systems (MongoDB/SQL), Backend Architecture.
        </p>
    </div>

    <div class="metric-card">
        <h3 style="color: #34d399; margin: 0;">Ewing Christian Public School &bull; Class X (High School)</h3>
        <p style="color: #86efac; font-weight: 700; margin: 0.2rem 0;">Final Grade: 92% Scholastic Distinction &bull; Prayagraj, India</p>
    </div>

    <div class="metric-card">
        <h3 style="color: #fbbf24; margin: 0;">HACKDEVENGER Hackathon 2026</h3>
        <p style="color: #fde68a; font-weight: 700; margin: 0.2rem 0;">Awardee & Technical Finalist &bull; 07/2026</p>
        <p style="color: #94a3b8; font-size: 0.92rem;">Recognized for rapid prototyping, multi-agent coordination, and real-time algorithmic software execution.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# VIEW 6: DIRECT CONTACT
# -------------------------------------------------------------
elif nav_choice == "📬 Connect & Direct Contact":
    st.markdown("""
    <div class="hero-badge">Open For Opportunities</div>
    <h1 class="gradient-header">Connect with Utkarsh Dwivedi</h1>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.2])

    with c1:
        st.markdown("""
        <div class="metric-card">
            <h4>Contact Channels</h4>
            <p><strong>📧 Email:</strong> <a href="mailto:bkutkars@gmail.com" style="color:#38bdf8;">bkutkars@gmail.com</a></p>
            <p><strong>📱 Phone:</strong> <a href="tel:+917905499755" style="color:#34d399;">+91 7905499755</a></p>
            <p><strong>🐙 GitHub:</strong> <a href="https://github.com/bkutkars-debug" target="_blank" style="color:#a5b4fc;">github.com/bkutkars-debug</a></p>
            <p><strong>💼 LinkedIn:</strong> <a href="https://linkedin.com/in/utkarsh-dwivedi-b3b5b5281" target="_blank" style="color:#38bdf8;">linkedin.com/in/utkarsh-dwivedi-b3b5b5281</a></p>
            <p><strong>📍 Location:</strong> Prayagraj, UP, India (211003)</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.subheader("Send a Message")
        with st.form("contact_form"):
            sender_name = st.text_input("Your Name")
            sender_email = st.text_input("Your Email")
            msg = st.text_area("Message / Collaboration Inquiry")
            submitted = st.form_submit_button("Transmit Message")
            if submitted:
                if sender_name and sender_email:
                    st.success("✅ Message acknowledged! Utkarsh will contact you shortly.")
                    st.balloons()
                else:
                    st.warning("Please provide both name and email.")
        st.markdown('</div>', unsafe_allow_html=True)
