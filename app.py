# ***Smart Demand Forecasting and Inventory Optimization System***

# Core Imports
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# App Configuration
st.set_page_config(
    page_title="Smart Demand Forecasting System",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# HIGH-FIDELITY FINTECH DARK MODE DESIGN CORE (INTER & JETBRAINS MONO)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Font Declarations */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Strict Slate Obsidian Base Background */
    .stApp {
        background-color: #0F172A !important;
        color: #94A3B8 !important;
    }
    
    /* Premium Sidebar Navigation styling - Increased sizes as requested */
    section[data-testid="stSidebar"] {
        background-color: #020617 !important;
        border-right: 1px solid #1E293B !important;
    }
    section[data-testid="stSidebar"] h2 {
        color: #FFFFFF !important;
        font-size: 1.6rem !important;
        font-weight: 700 !important;
    }
    section[data-testid="stSidebar"] label p {
        color: #FFFFFF !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        margin-bottom: 12px !important;
    }
    section[data-testid="stSidebar"] .stRadio label p {
        color: #CBD5E1 !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
    }

    /* Premium Layered Matte Graphite Container Cards */
    div[data-testid="stVVerticalBlockBorderBordered"] {
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        padding: 24px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Color-coded Left Accents to guide user eye layout */
    .section-card-product { border-left: 4px solid #38BDF8 !important; }
    .section-card-pricing { border-left: 4px solid #10B981 !important; }
    .section-card-history { border-left: 4px solid #64748B !important; }

    /* CORRECTED & CENTERED Custom Header Banner Layout with Linear Gradient Highlight */
    .terminal-header {
        background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%);
        padding: 3rem 2rem;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 2rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.4);
        text-align: center !important;
    }
    .terminal-header h1 {
        font-weight: 800 !important;
        font-size: 2.3rem !important;
        margin: 0 0 0.75rem 0 !important;
        letter-spacing: -0.01em;
        
        /* Premium Gradient Text Highlight Masking (White to Electric Cyber Blue) */
        background: linear-gradient(to right, #FFFFFF 40%, #38BDF8 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }
    .terminal-header p {
        color: #94A3B8 !important;
        font-size: 1.05rem !important;
        margin: 0 !important;
        font-weight: 400;
        letter-spacing: 0.01em;
    }

    /* Custom Clean High-Contrast KPI Components */
    .kpi-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    .kpi-card {
        background: #0F172A;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 24px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.4);
    }
    .kpi-demand { border-top: 4px solid #38BDF8; }
    .kpi-safety { border-top: 4px solid #8B5CF6; }
    .kpi-reorder { border-top: 4px solid #94A3B8; }
    
    /* Dynamic Structural State Colors for Stock Level Status */
    .kpi-status-low { border-top: 4px solid #EF4444; background: linear-gradient(to bottom, #2D1A1E, #0F172A); }
    .kpi-status-balanced { border-top: 4px solid #10B981; background: linear-gradient(to bottom, #142D24, #0F172A); }
    .kpi-status-over { border-top: 4px solid #3B82F6; background: linear-gradient(to bottom, #17253D, #0F172A); }
    
    .kpi-title {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #64748B;
        font-weight: 600;
        margin-bottom: 12px;
    }
    .kpi-value {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 2.6rem;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 1;
    }
    .kpi-unit {
        font-size: 1rem;
        font-weight: 500;
        color: #64748B;
        font-family: 'Inter', sans-serif !important;
        margin-left: 4px;
    }
    .kpi-status-text {
        font-size: 1.4rem;
        font-weight: 700;
        margin-top: 4px;
    }

    /* Master Action Forecast Button Custom Overrides - Upgraded Font Sizing and removed emoji padding properties */
    div.stButton > button {
        background: linear-gradient(135deg, #38BDF8 0%, #0284C7 100%) !important;
        color: #0F172A !important;
        font-weight: 700 !important;
        font-size: 1.25rem !important; /* Increased from 1.1rem for better presence */
        letter-spacing: 0.01em !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 2rem !important;
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.25) !important;
        transition: all 0.2s ease-in-out !important;
        width: 100% !important;
        height: 54px !important;
        margin-top: 10px !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #06B6D4 0%, #0891B2 100%) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 25px rgba(6, 182, 212, 0.4) !important;
    }
    
    /* Form Label Styling Adjustments */
    label p {
        color: #CBD5E1 !important;
        font-weight: 500 !important;
        font-size: 0.88rem !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #0F172A !important;
        border-color: #334155 !important;
        color: #FFFFFF !important;
    }
    input {
        background-color: #0F172A !important;
        color: #FFFFFF !important;
    }
    
    /* Clean Page Header Typography styles */
    .page-title-main {
        font-family: 'Inter', sans-serif !important;
        color: #FFFFFF !important;
        font-weight: 700;
        font-size: 1.5rem;
        margin-bottom: 16px;
        margin-top: 10px;
    }
    
    /* Targeted Card Header Enhancements */
    .card-header-product {
        color: #38BDF8 !important;
        font-weight: 700 !important;
        font-size: 1.35rem !important;
        margin-top: 0;
        margin-bottom: 16px;
    }
    .card-header-pricing {
        color: #10B981 !important;
        font-weight: 700 !important;
        font-size: 1.35rem !important;
        margin-top: 0;
        margin-bottom: 16px;
    }
    .card-header-history {
        color: #E2E8F0 !important;
        font-weight: 700 !important;
        font-size: 1.35rem !important;
        margin-top: 0;
        margin-bottom: 16px;
    }
    .subcard-header-inline {
        font-weight: 600 !important;
        color: #38BDF8 !important;
        font-size: 1.05rem !important;
        margin-bottom: 12px;
    }
    
    /* Blueprint Text Block Grid Layout styling */
    .bp-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin-top: 15px;
    }
    .bp-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 24px;
    }
    .bp-card h4 {
        color: #38BDF8 !important;
        font-size: 1.3rem !important;
        margin-top: 0 !important;
        margin-bottom: 12px !important;
    }
    .bp-card ul {
        margin: 0;
        padding-left: 20px;
        color: #94A3B8;
    }
    .bp-card li {
        margin-bottom: 8px;
        font-size: 0.98rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CORE MODEL FILE RETRIEVAL & ERROR HANDLING CACHES
# -----------------------------------------------------------------------------
@st.cache_resource
def load_models():
    rf = joblib.load("rf_model.pkl")
    encoders = joblib.load("label_encoders.pkl")
    columns = joblib.load("feature_columns.pkl")
    return rf, encoders, columns

@st.cache_data
def load_dataset():
    return pd.read_csv("preprocessed_demand_forecasting_data.csv")

rf_model, label_encoders, feature_columns = load_models()
df = load_dataset()

# Sidebar Layout Architecture 
st.sidebar.markdown("<br><h2 style='text-align: center; letter-spacing:0.5px;'>📋 NAVIGATION</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")
page = st.sidebar.radio("Go To Workspace Layer:", ["Forecasting Dashboard", "Advanced Analytics", "About Project"])

# =============================================================================
# WORKSPACE INTERFACE: MAIN FORECASTING DASHBOARD
# =============================================================================
if page == "Forecasting Dashboard":

    # Centered and Gradient Highlighted True Project Title Branding Banner
    st.markdown("""
        <div class="terminal-header">
            <h1>SMART DEMAND FORECASTING AND INVENTORY OPTIMIZATION SYSTEM</h1>
            <p>Predict future retail product demand variations, manage safety stock logic, and minimize operational stock-out risks.</p>
        </div>
    """, unsafe_allow_html=True)

    # Tier 1 Ingestion System Panel
    st.markdown('<div class="page-title-main">📊 Live Data Stream Ingestion</div>', unsafe_allow_html=True)
    col_preview, col_select = st.columns([2, 1])
    
    with col_preview:
        with st.container(border=True):
            st.markdown("<p class='subcard-header-inline'>Master Production Registry Logs (Head)</p>", unsafe_allow_html=True)
            st.dataframe(df.head(4), use_container_width=True, hide_index=True)
            
    with col_select:
        with st.container(border=True):
            st.markdown("<p class='subcard-header-inline'>💡 Auto-Fill from Dataset Sample</p>", unsafe_allow_html=True)
            sample_index = st.selectbox("Choose a dataset sample index to load testing row properties:", options=df.index)
            sample_data = df.loc[sample_index]

    # Tier 2 Parameter Controls Grid Setup
    st.markdown('<div class="page-title-main">🛠️ Edit Product Simulation Parameters</div>', unsafe_allow_html=True)

    # Column Card 1: Fixed Profile Identity
    st.markdown("<div class='section-card-product'>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<p class='card-header-product'>📦 Product Profile & Regional DNA</p>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            product_id = st.selectbox("Product ID", options=df['Product ID'].unique(), index=list(df['Product ID'].unique()).index(sample_data['Product ID']))
        with c2:
            category = st.selectbox("Category Group", options=df['Category'].unique(), index=list(df['Category'].unique()).index(sample_data['Category']))
        with c3:
            region = st.selectbox("Logistics Region", options=df['Region'].unique(), index=list(df['Region'].unique()).index(sample_data['Region']))
        with c4:
            seasonality = st.selectbox("Seasonality Core Bracket", options=df['Seasonality'].unique(), index=list(df['Seasonality'].unique()).index(sample_data['Seasonality']))
    st.markdown("</div>", unsafe_allow_html=True)

    # Column Card 2: Pricing Variables Controls
    st.markdown("<div class='section-card-pricing'>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<p class='card-header-pricing'>🪙 Pricing Strategy & Campaign Modifiers</p>", unsafe_allow_html=True)
        p1, p2, p3, p4, p5 = st.columns(5)
        with p1:
            price = st.number_input("Base Unit Price ($)", value=float(sample_data['Price']), step=0.01)
        with p2:
            discount = st.number_input("Campaign Discount (%)", value=int(sample_data['Discount']), step=1)
        with p3:
            competitor_price = st.number_input("Competitor Pricing ($)", value=float(sample_data['Competitor Pricing']), step=0.01)
        with p4:
            promotion = st.selectbox("Marketing Promotion Switch", options=[0, 1], format_func=lambda x: "Active Campaign Running" if x==1 else "No Promotion Active", index=int(sample_data['Promotion']))
        with p5:
            weather = st.selectbox("Weather Condition Factors", options=df['Weather Condition'].unique(), index=list(df['Weather Condition'].unique()).index(sample_data['Weather Condition']))
    st.markdown("</div>", unsafe_allow_html=True)

    # Column Card 3: Mathematical Multi-Lags
    st.markdown("<div class='section-card-history'>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<p class='card-header-history'>📈 Time-Series Lag Targets & Floor Inventory</p>", unsafe_allow_html=True)
        s1, s2, s3, s4, s5 = st.columns(5)
        with s1:
            inventory = st.number_input("Current Inventory Level", value=int(sample_data['Inventory Level']), step=1)
        with s2:
            lag_1 = st.number_input("Lag 1 Demand", value=float(sample_data['lag_1']), step=1.0)
        with s3:
            lag_7 = st.number_input("Lag 7 Demand", value=float(sample_data['lag_7']), step=1.0)
        with s4:
            rolling_mean_7 = st.number_input("Rolling Mean 7", value=float(sample_data['rolling_mean_7']), step=0.1)
        with s5:
            epidemic = st.selectbox("Epidemic Interruption Flag", options=[0, 1], format_func=lambda x: "High Epidemic Impact State" if x==1 else "Normal Stable Environment", index=int(sample_data['Epidemic']))
    st.markdown("</div>", unsafe_allow_html=True)

    # Simplified Core Processing Trigger Action Button - EMOJI REMOVED
    st.markdown("<br>", unsafe_allow_html=True)
    execute_forecast = st.button("Forecast Demand")

    if execute_forecast:
        # Build evaluation matrix array configuration mappings structures
        input_data = pd.DataFrame({
            'Store ID': [sample_data['Store ID']], 'Product ID': [product_id], 'Category': [category],
            'Region': [region], 'Inventory Level': [inventory], 'Price': [price], 'Discount': [discount],
            'Weather Condition': [weather], 'Promotion': [promotion], 'Competitor Pricing': [competitor_price],
            'Seasonality': [seasonality], 'Epidemic': [epidemic], 'day': [sample_data['day']],
            'month': [sample_data['month']], 'year': [sample_data['year']], 'weekday': [sample_data['weekday']],
            'weekofyear': [sample_data['weekofyear']], 'is_weekend': [sample_data['is_weekend']],
            'Discounted Price': [price * (1 - discount / 100)], 'lag_1': [lag_1], 'lag_7': [lag_7],
            'rolling_mean_7': [rolling_mean_7], 'discount_bin': [sample_data['discount_bin']]
        })

        for col in ['Store ID', 'Product ID']:
            input_data[col] = label_encoders[col].transform(input_data[col])

        input_encoded = pd.get_dummies(input_data).reindex(columns=feature_columns, fill_value=0)
        prediction = rf_model.predict(input_encoded)[0]

        # Strategic stock calculations inventory equations rules
        safety_buffer = 20
        required_stock = prediction + safety_buffer
        reorder_quantity = max(0, round(required_stock - inventory))
        stock_ratio = (inventory / prediction if prediction > 0 else 0)

        if stock_ratio < 0.8:
            status_class = "kpi-status-low"
            status_text = "🔴 Low Stock Risk"
        elif stock_ratio <= 1.2:
            status_class = "kpi-status-balanced"
            status_text = "🟡 Balanced Stock"
        else:
            status_class = "kpi-status-over"
            status_text = "🔵 Overstock Risk"

        st.markdown("<br><hr>", unsafe_allow_html=True)
        
        # Upgraded Large Header Size for Dashboard Summary
        st.markdown('<div class="page-title-main" style="font-size: 1.65rem !important;">📊 Inventory Intelligence Dashboard Summary</div>', unsafe_allow_html=True)
        
        # High Contrast, Large Metrics Render Output Window 
        st.markdown(f"""
            <div class="kpi-container">
                <div class="kpi-card kpi-demand">
                    <div class="kpi-title">Predicted Demand</div>
                    <div class="kpi-value">{prediction:.2f}<span class="kpi-unit">Units</span></div>
                </div>
                <div class="kpi-card kpi-safety">
                    <div class="kpi-title">Required Stock</div>
                    <div class="kpi-value">{required_stock:.0f}<span class="kpi-unit">Units</span></div>
                </div>
                <div class="kpi-card kpi-reorder">
                    <div class="kpi-title">Reorder Quantity</div>
                    <div class="kpi-value">{reorder_quantity}<span class="kpi-unit">Units</span></div>
                </div>
                <div class="kpi-card {status_class}">
                    <div class="kpi-title" style="color:#FFFFFF;">Stock Status</div>
                    <div class="kpi-status-text" style="color:#FFFFFF;">{status_text}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# =============================================================================
# WORKSPACE INTERFACE: ADVANCED DIAGNOSTICS PAGE
# =============================================================================
elif page == "Advanced Analytics":
    st.markdown("""
        <div class="terminal-header">
            <h1>ADVANCED MODEL ANALYTICS</h1>
            <p>Evaluate machine learning feature importance weights distributions and relative dataset entropies splits contextually.</p>
        </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("### 🌲 Random Forest Feature Importance Rankings")
        
        importance_df = pd.DataFrame({
            'Feature': feature_columns,
            'Importance': rf_model.feature_importances_
        }).sort_values(by='Importance', ascending=False)
        
        top_features = importance_df.head(10).sort_values(by='Importance', ascending=True)

        # Corrected Plotly Config - Stripped automatic labels to remove 'undefined' text
        fig = px.bar(
            top_features, x='Importance', y='Feature', orientation='h',
            labels={'Importance': 'Split Weight Gain Metric', 'Feature': 'Dataset Parameter Feature'},
            color='Importance',
            color_continuous_scale=['#1E293B', '#1E3A8A', '#38BDF8', '#10B981']
        )
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font_family="Inter", 
            font_color="#94A3B8", 
            title_font_color="#FFFFFF",
            xaxis=dict(showgrid=True, gridcolor='#334155', title_font_color='#FFFFFF'),
            yaxis=dict(showgrid=False, title_font_color='#FFFFFF'),
            margin=dict(l=20, r=20, t=10, b=20), # Tightened top margin
            coloraxis_showscale=False, 
            showlegend=False, # Explicitly removes legends
            height=450
        )
        
        # Explicitly forces color-axis scale/legend logic off entirely
        fig.update_coloraxes(showscale=False)
        
        chart_view, raw_view = st.columns([2, 1])
        with chart_view:
            # Added config to turn off floating plotly toolbar icons on hover
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        with raw_view:
            st.markdown("<p style='font-family:\"JetBrains Mono\"; font-weight:600; font-size:0.95rem; color:#38BDF8;'>📋 Top Feature Coefficients Registry Log</p>", unsafe_allow_html=True)
            st.dataframe(importance_df.head(10), use_container_width=True, hide_index=True)

# =============================================================================
# WORKSPACE INTERFACE: ABOUT ARCHITECTURE PAGE (UPGRADED CRISP BLOCKS)
# =============================================================================
elif page == "About Project":
    st.markdown("""
        <div class="terminal-header">
            <h1>ℹ️ ABOUT THIS PROJECT ARCHITECTURE</h1>
            <p>Core framework configurations, machine learning methodologies, and technical stack parameters declarations.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Modern Executive Summary Structural Blocks Layout
    st.markdown("""
        <div class="bp-grid">
            <div class="bp-card">
                <h4>🎯 Core Objective</h4>
                <p style="color:#CBD5E1; line-height:1.6; font-size:1rem;">
                    Traditional supply chain methods rely on static historic estimations, leading to overstocking issues or sudden warehouse shortages. 
                    This system applies machine learning regressors to dynamically evaluate parameters and output data-driven stock optimization guidance.
                </p>
            </div>
            <div class="bp-card">
                <h4>⚙️ Core Intelligence Features</h4>
                <ul>
                    <li><strong>Demand Forecasting:</strong> Real-time trend predictions calculated using Random Forest architectures.</li>
                    <li><strong>Inventory Risk Analysis:</strong> Continuous monitoring of stock ratios to avoid locked capital.</li>
                    <li><strong>Reorder Optimization:</strong> Automated calculations to provide safety stock level recommendation vectors.</li>
                    <li><strong>Model Explainability:</strong> Directly logs core tree-split criteria weights for transparent AI auditing.</li>
                </ul>
            </div>
            <div class="bp-card">
                <h4>🚀 Technology Matrix Stack</h4>
                <ul>
                    <li><strong>UI Layer:</strong> Streamlit High-Performance Core APIs</li>
                    <li><strong>Data Structures Engine:</strong> Python, Pandas & NumPy Arrays</li>
                    <li><strong>Algorithmic Models Base:</strong> Scikit-Learn Ensemble Pipeline Package</li>
                    <li><strong>Graphics Pipeline:</strong> Fully Interactive Plotly Chart APIs</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)