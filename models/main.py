import streamlit as st
import plotly.graph_objects as go
from models.fixed_income import fit_yield_curve, nelson_siegel

st.set_page_config(page_title="Macro Hedge Dashboard", layout="wide")
st.title("🏆 Global Macro Quantitative Dashboard")

# --- Dashboard Layout ---
tab1, tab2, tab3 = st.tabs(["Fixed Income", "Satellite Alt-Data", "Tail Risk"])

with tab1:
    st.header("Yield Curve Analysis")
    mats, yields, params = fit_yield_curve()
    
    # Generate fitted curve
    x_range = np.linspace(0.1, 30, 100)
    y_fitted = nelson_siegel(x_range, *params)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=mats, y=yields, mode='markers', name='Market'))
    fig.add_trace(go.Scatter(x=x_range, y=y_fitted, name='Nelson-Siegel Fit'))
    st.plotly_chart(fig)
    st.write(f"Level (β0): {params[0]:.4f}, Slope (β1): {params[1]:.4f}")

with tab2:
    st.header("Geospatial Intelligence")
    st.info("Tracking Consumer Density via Sentinel-2 L2A")
    # Add your map or satellite image placeholder here