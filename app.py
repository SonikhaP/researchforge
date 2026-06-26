"""ResearchForge — Streamlit UI for the multi-agent research pipeline."""

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv(override=True)

st.set_page_config(
    page_title="ResearchForge",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🔬 ResearchForge")
    st.caption("Multi-Agent Academic Research Assistant")
    st.divider()

    st.subheader("Configuration")
    google_key = st.text_input(
        "Google API Key",
        value=os.getenv("GOOGLE_API_KEY", ""),
        type="password",
        help="Get yours at https://aistudio.google.com/apikey",
    )
    serper_key = st.text_input(
        "Serper API Key (optional)",
        value=os.getenv("SERPER_API_KEY", ""),
        type="password",
        help="Enables live web search. Get yours at https://serper.dev",
    )
    if google_key:
        os.environ["GOOGLE_API_KEY"] = google_key
    if serper_key:
        os.environ["SERPER_API_KEY"] = serper_key

    st.divider()
    demo_mode = st.toggle("Demo mode", value=True,
                          help="ON by default — shows a realistic pre-built report so you can explore the full UI instantly. Turn OFF and add your Google API key above to run the live 5-agent pipeline.")

    st.divider()
    st.subheader("Agent Pipeline")
    stages = [
        ("🔍", "Search Agent", "Finds papers & web sources"),
        ("📖", "Reader Agent", "Extracts key findings"),
        ("🧐", "Critic Agent", "Fact-checks evidence"),
        ("🔗", "Synthesis Agent", "Builds the narrative"),
        ("✍️", "Report Writer", "Produces final report"),
    ]
    for icon, name, desc in stages:
        st.markdown(f"{icon} **{name}** — *{desc}*")

    st.divider()
    st.caption(
        "Built for the Kaggle AI Agents Capstone · "
        "[GitHub](https://github.com) · "
        "Powered by Google ADK + Gemini"
    )

# ── Main area ──────────────────────────────────────────────────────────────────
st.title("ResearchForge")
st.subheader("Ask any research question — get a cited, AI-synthesized report in seconds.")

examples = [
    "What are the latest advances in large language model reasoning?",
    "How does quantum computing threaten current encryption methods?",
    "What is the current evidence for neuroplasticity in adult brains?",
    "How are AI agents being used in drug discovery?",
]

with st.expander("Try an example question", expanded=False):
    for ex in examples:
        if st.button(ex, key=ex):
            st.session_state["query_input"] = ex

query = st.text_area(
    "Your research question",
    value=st.session_state.get("query_input", ""),
    placeholder="e.g. What are the most effective treatments for antibiotic-resistant infections?",
    height=80,
    key="query_input",
)

col1, col2 = st.columns([1, 5])
with col1:
    run_button = st.button("Run Research", type="primary", use_container_width=True)
with col2:
    st.caption("Runs 5 AI agents in sequence · typically 30–60 seconds")

if demo_mode:
    st.info("**Demo mode is ON.** The full 5-agent pipeline (Search → Reader → Critic → Synthesis → Report Writer) will run with pre-built data so you can explore the UI instantly. Toggle it OFF in the sidebar and add a Google API key to run live agents.")

if run_button:
    if not query.strip():
        st.warning("Please enter a research question.")
        st.stop()
    if not demo_mode and not os.getenv("GOOGLE_API_KEY"):
        st.error("Please enter your Google API Key in the sidebar, or enable Demo mode.")
        st.stop()

    progress_bar = st.progress(0)
    status_text = st.empty()
    pipeline_steps = 6

    def update_progress(step: int, label: str):
        progress_bar.progress(step / pipeline_steps)
        status_text.info(f"Step {step}/{pipeline_steps - 1}: {label}")

    with st.spinner("ResearchForge is running…"):
        if demo_mode:
            from demo_mode import run_demo
            result = run_demo(query.strip(), progress_callback=update_progress)
        else:
            from agents.orchestrator import run_research
            result = run_research(query.strip(), progress_callback=update_progress)

    progress_bar.empty()
    status_text.empty()

    if "error" in result:
        st.error(f"Pipeline error: {result['error']}")
        st.stop()

    st.success("Research complete!")

    # ── Tabs for each pipeline stage ──
    tab_report, tab_sources, tab_findings, tab_critique, tab_synthesis = st.tabs(
        ["📄 Final Report", "🔍 Sources", "📖 Findings", "🧐 Critique", "🔗 Synthesis"]
    )

    with tab_report:
        st.markdown(result["report"])
        st.download_button(
            "Download Report (Markdown)",
            data=result["report"],
            file_name="researchforge_report.md",
            mime="text/markdown",
        )

    with tab_sources:
        st.markdown(result["sources"])

    with tab_findings:
        st.markdown(result["findings"])

    with tab_critique:
        st.markdown(result["critique"])

    with tab_synthesis:
        st.markdown(result["synthesis"])
