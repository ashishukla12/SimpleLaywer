import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import json
import hashlib
import io
import base64
from typing import Dict, List, Tuple, Optional
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# Configure Streamlit page
st.set_page_config(
    page_title="LegalAI Simplifier - Hackathon Demo",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #2563EB 0%, #1E3A8A 100%);
        color: #000000;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }

    .confidence-meter {
        background: #000000;
        border: 2px solid #2563EB;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .feature-card {
        background: #000000;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }

    .risk-high {
        background: #000000;
        border-left: 4px solid #EF4444;
        padding: 1rem;
        border-radius: 4px;
    }

    .risk-medium {
        background: #000000;
        border-left: 4px solid #F59E0B;
        padding: 1rem;
        border-radius: 4px;
    }

    .risk-low {
        background: #000000;
        border-left: 4px solid #10B981;
        padding: 1rem;
        border-radius: 4px;
    }

    .voice-interface {
        background: #000000;
        border: 2px dashed #2563EB;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }

    .trust-indicator {
        background: #000000;
        border: 1px solid #10B981;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Simulated AI models and databases
class LegalAIEngine:
    def __init__(self):
        self.legal_knowledge_base = {
            "nda": {
                "common_clauses": ["confidentiality", "non-disclosure", "return of materials", "term duration", "exceptions"],
                "risk_patterns": ["perpetual term", "broad definition", "unlimited liability", "no exceptions"],
                "jurisdiction_data": {"california": "Strong employee protection", "texas": "Employer-friendly", "new_york": "Balanced approach"}
            },
            "lease": {
                "common_clauses": ["rent amount", "security deposit", "maintenance", "termination", "pets"],
                "risk_patterns": ["no maintenance responsibility", "excessive fees", "automatic renewal", "broad landlord rights"],
                "jurisdiction_data": {"california": "Strong tenant protection", "texas": "Landlord-friendly", "new_york": "Rent stabilized"}
            },
            "employment": {
                "common_clauses": ["compensation", "benefits", "termination", "non-compete", "intellectual property"],
                "risk_patterns": ["at-will termination", "broad non-compete", "no severance", "IP assignment"],
                "jurisdiction_data": {"california": "Non-compete banned", "texas": "At-will state", "new_york": "Restrictive non-compete"}
            }
        }

    def classify_document(self, text: str) -> Tuple[str, float]:
        """Classify document type with confidence"""
        text_lower = text.lower()

        # Simple classification logic
        if any(word in text_lower for word in ["nda", "non-disclosure", "confidential"]):
            return "nda", np.random.uniform(0.85, 0.98)
        elif any(word in text_lower for word in ["lease", "rent", "tenant", "landlord"]):
            return "lease", np.random.uniform(0.80, 0.95)
        elif any(word in text_lower for word in ["employment", "employee", "job", "salary"]):
            return "employment", np.random.uniform(0.75, 0.92)
        else:
            return "contract", np.random.uniform(0.60, 0.85)

    def analyze_document(self, text: str, doc_type: str) -> Dict:
        """Analyze document and return structured results"""

        # Simulate processing time
        time.sleep(2)

        # Generate confidence score
        base_confidence = np.random.uniform(0.75, 0.98)

        # Extract key information
        analysis = {
            "document_type": doc_type,
            "confidence_score": base_confidence,
            "risk_assessment": self._assess_risks(text, doc_type),
            "key_clauses": self._extract_clauses(text, doc_type),
            "plain_language_summary": self._generate_summary(text, doc_type),
            "source_citations": self._generate_citations(text),
            "recommendations": self._generate_recommendations(doc_type)
        }

        return analysis

    def _assess_risks(self, text: str, doc_type: str) -> List[Dict]:
        """Assess risk levels of clauses"""
        risks = []

        if doc_type == "nda":
            risks = [
                {"clause": "Confidentiality Definition", "risk": "medium", "confidence": 0.87, "explanation": "Definition is somewhat broad but reasonable for standard business use"},
                {"clause": "Term Duration", "risk": "low", "confidence": 0.94, "explanation": "Standard 2-year term with reasonable exceptions"},
                {"clause": "Return of Materials", "risk": "low", "confidence": 0.91, "explanation": "Clear obligations for document return upon termination"}
            ]
        elif doc_type == "lease":
            risks = [
                {"clause": "Security Deposit", "risk": "high", "confidence": 0.82, "explanation": "Deposit amount exceeds local legal limits and lacks clear return conditions"},
                {"clause": "Maintenance Responsibility", "risk": "medium", "confidence": 0.89, "explanation": "Some maintenance responsibilities shifted to tenant beyond normal wear"},
                {"clause": "Pet Policy", "risk": "low", "confidence": 0.95, "explanation": "Reasonable pet policy with standard deposit requirements"}
            ]
        else:
            risks = [
                {"clause": "General Terms", "risk": "medium", "confidence": 0.85, "explanation": "Standard contract terms with some areas requiring attention"}
            ]

        return risks

    def _extract_clauses(self, text: str, doc_type: str) -> List[Dict]:
        """Extract key clauses from document"""
        if doc_type in self.legal_knowledge_base:
            clauses = []
            for clause in self.legal_knowledge_base[doc_type]["common_clauses"]:
                clauses.append({
                    "name": clause.title(),
                    "content": f"[Sample clause content for {clause}]",
                    "importance": np.random.choice(["high", "medium", "low"]),
                    "page_reference": f"Page {np.random.randint(1, 5)}"
                })
            return clauses
        return []

    def _generate_summary(self, text: str, doc_type: str) -> str:
        """Generate plain language summary"""
        summaries = {
            "nda": "This is a Non-Disclosure Agreement that prevents you from sharing confidential information. Key points: You must keep business information secret for 2 years, return all documents when done, and there are standard exceptions for public information.",
            "lease": "This is a rental agreement for an apartment or house. Key points: Monthly rent is due on the 1st, security deposit required, tenant responsible for some maintenance, standard termination notice required.",
            "employment": "This is an employment contract outlining your job terms. Key points: Salary and benefits detailed, at-will employment meaning either party can terminate, some restrictions on working for competitors.",
            "contract": "This appears to be a general business contract. The document outlines mutual obligations, payment terms, and standard legal protections for both parties."
        }
        return summaries.get(doc_type, summaries["contract"])

    def _generate_citations(self, text: str) -> List[str]:
        """Generate source citations"""
        return [
            "Section 2.1: Confidentiality Obligations",
            "Section 4.3: Term and Termination",
            "Exhibit A: Permitted Disclosures",
            "Section 7.2: Return of Materials"
        ]

    def _generate_recommendations(self, doc_type: str) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = {
            "nda": [
                "Consider negotiating a shorter term (1 year instead of 2)",
                "Request clarification on what constitutes 'confidential information'",
                "Ensure mutual confidentiality if you're sharing information too"
            ],
            "lease": [
                "Verify security deposit amount complies with local laws",
                "Document existing damage before move-in",
                "Understand your rights regarding maintenance and repairs"
            ],
            "employment": [
                "Review non-compete restrictions carefully",
                "Understand your benefits eligibility timeline",
                "Clarify intellectual property ownership policies"
            ]
        }
        return recommendations.get(doc_type, ["Review document with legal counsel if terms seem unfavorable"])

# Initialize AI engine
@st.cache_resource
def get_ai_engine():
    return LegalAIEngine()

# Main app layout
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>⚖️ LegalAI Simplifier</h1>
        <h3>Making Legal Documents Accessible to Everyone</h3>
        <p>AI-Powered Legal Document Analysis with Confidence Scoring</p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "analysis_results" not in st.session_state:
        st.session_state.analysis_results = None
    if "voice_question" not in st.session_state:
        st.session_state.voice_question = ""
    if "processing" not in st.session_state:
        st.session_state.processing = False

    # Sidebar for user preferences
    with st.sidebar:
        st.header("⚙️ Settings")

        user_type = st.selectbox(
            "I am a:",
            ["Small Business Owner", "Tenant/Renter", "Freelancer", "HR Manager", "Law Student", "Other"]
        )

        complexity_level = st.select_slider(
            "Explanation Complexity:",
            options=["Simple", "Moderate", "Detailed", "Legal Expert"],
            value="Moderate"
        )

        jurisdiction = st.selectbox(
            "Legal Jurisdiction:",
            ["California", "Texas", "New York", "Florida", "Other"]
        )

        st.markdown("---")

        # Privacy controls
        st.header("🔒 Privacy Controls")
        st.success("✅ Zero Document Storage")
        st.info("🔐 End-to-End Encrypted")
        st.info("📋 GDPR Compliant")

        # Trust indicators
        st.markdown("---")
        st.header("🛡️ Trust Indicators")
        st.metric("System Uptime", "99.9%")
        st.metric("Avg Confidence", "91.2%")
        st.metric("User Satisfaction", "4.8/5.0")

    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📄 Document Analysis", "🎙️ Voice Interface", "📊 Features Demo", "🏢 Business Case"])

    with tab1:
        document_analysis_tab()

    with tab2:
        voice_interface_tab()

    with tab3:
        features_demo_tab()

    with tab4:
        business_case_tab()

def document_analysis_tab():
    """Main document analysis interface"""
    ai_engine = get_ai_engine()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("📤 Upload Document")

        # File upload options
        upload_type = st.radio(
            "Choose upload method:",
            ["File Upload", "Sample Document", "Text Input"]
        )

        document_text = ""

        if upload_type == "File Upload":
            uploaded_file = st.file_uploader(
                "Choose a document",
                type=["pdf", "txt", "docx"],
                help="Upload PDF, Word, or text files"
            )

            if uploaded_file:
                document_text = f"Sample legal document content from {uploaded_file.name}..."

        elif upload_type == "Sample Document":
            sample_type = st.selectbox(
                "Select sample:",
                ["NDA (Non-Disclosure Agreement)", "Lease Agreement", "Employment Contract"]
            )

            sample_docs = {
                "NDA (Non-Disclosure Agreement)": """
                NON-DISCLOSURE AGREEMENT

                This Non-Disclosure Agreement is entered into by Company ABC and John Doe.

                1. CONFIDENTIAL INFORMATION
                Recipient acknowledges that all information disclosed by Company shall be considered confidential.

                2. OBLIGATIONS
                Recipient agrees to maintain confidentiality and not disclose information to third parties.

                3. TERM
                This agreement shall remain in effect for a period of two (2) years.

                4. RETURN OF MATERIALS
                Upon termination, Recipient shall return all confidential materials.
                """,
                "Lease Agreement": """
                RESIDENTIAL LEASE AGREEMENT

                Property: 123 Main Street, Anytown, CA
                Tenant: Jane Smith
                Landlord: Property Management Co.

                1. RENT
                Monthly rent: $2,500 due on the 1st of each month.

                2. SECURITY DEPOSIT  
                Security deposit: $5,000 required before move-in.

                3. MAINTENANCE
                Tenant responsible for minor repairs and maintenance under $100.

                4. PETS
                No pets allowed without written consent and additional deposit.
                """,
                "Employment Contract": """
                EMPLOYMENT AGREEMENT

                Employee: Sarah Johnson
                Employer: Tech Innovations Inc.
                Position: Software Developer

                1. COMPENSATION
                Annual salary: $85,000 with benefits eligibility after 90 days.

                2. TERM
                At-will employment. Either party may terminate with 2 weeks notice.

                3. NON-COMPETE
                Employee agrees not to work for competitors for 1 year after termination.

                4. INTELLECTUAL PROPERTY
                All work product belongs to the company.
                """
            }
            document_text = sample_docs[sample_type]

        else:  # Text Input
            document_text = st.text_area(
                "Paste document text:",
                height=300,
                placeholder="Paste your legal document text here..."
            )

        # Analysis button
        if st.button("🔍 Analyze Document", type="primary", disabled=not document_text):
            st.session_state.processing = True

            with st.spinner("Processing document..."):
                # Document classification
                doc_type, class_confidence = ai_engine.classify_document(document_text)

                # Full analysis
                analysis = ai_engine.analyze_document(document_text, doc_type)
                st.session_state.analysis_results = analysis
                st.session_state.processing = False

    with col2:
        if st.session_state.analysis_results:
            display_analysis_results(st.session_state.analysis_results)
        else:
            st.info("👆 Upload a document to see AI analysis with confidence scoring")

            # Show sample analysis preview
            st.markdown("### 📋 Sample Analysis Preview")

            # Create sample confidence meter
            fig = create_confidence_meter(94)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
            <div class="feature-card">
                <h4>🎯 Key Features You'll See:</h4>
                <ul>
                    <li><strong>Confidence Scoring (0-100%)</strong> - Know how certain the AI is</li>
                    <li><strong>Risk Assessment</strong> - Color-coded clause analysis</li>
                    <li><strong>Plain Language Summary</strong> - Complex terms simplified</li>
                    <li><strong>Source Citations</strong> - Every explanation linked to document</li>
                    <li><strong>Actionable Recommendations</strong> - What you should do next</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

def display_analysis_results(analysis):
    """Display comprehensive analysis results"""

    st.header(f"📋 Analysis Results - {analysis['document_type'].upper()}")

    # Confidence meter
    st.markdown("### 🎯 AI Confidence Score")
    confidence_pct = int(analysis['confidence_score'] * 100)

    fig = create_confidence_meter(confidence_pct)
    st.plotly_chart(fig, use_container_width=True)

    if confidence_pct >= 90:
        st.success(f"✅ High Confidence ({confidence_pct}%) - AI is very certain about this analysis")
    elif confidence_pct >= 70:
        st.warning(f"⚠️ Medium Confidence ({confidence_pct}%) - Generally reliable with some uncertainty")
    else:
        st.error(f"❌ Low Confidence ({confidence_pct}%) - Significant uncertainty, consult legal expert")

    # Plain language summary
    st.markdown("### 📝 Plain Language Summary")
    st.markdown(f"""
    <div class="feature-card">
        <p style="font-size: 1.1em;">{analysis['plain_language_summary']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Risk assessment
    st.markdown("### ⚠️ Risk Assessment")

    for risk in analysis['risk_assessment']:
        risk_class = f"risk-{risk['risk']}"
        risk_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}[risk['risk']]

        st.markdown(f"""
        <div class="{risk_class}">
            <strong>{risk_icon} {risk['clause']}</strong> (Confidence: {int(risk['confidence']*100)}%)<br>
            {risk['explanation']}
        </div>
        """, unsafe_allow_html=True)

    # Source citations
    st.markdown("### 📚 Source Citations")
    for i, citation in enumerate(analysis['source_citations'], 1):
        st.markdown(f"**[{i}]** {citation}")

    # Recommendations
    st.markdown("### 💡 Recommendations")
    for rec in analysis['recommendations']:
        st.markdown(f"• {rec}")

    # Export options
    st.markdown("### 📤 Export Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📄 Export PDF"):
            st.success("PDF exported successfully!")

    with col2:
        if st.button("📧 Email Summary"):
            st.success("Summary emailed!")

    with col3:
        if st.button("💾 Save Analysis"):
            st.success("Analysis saved!")

def create_confidence_meter(confidence_pct):
    """Create confidence meter visualization"""

    # Create gauge chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = confidence_pct,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "AI Confidence Level"},
        delta = {'reference': 80},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#2563EB"},
            'steps': [
                {'range': [0, 50], 'color': "#FEE2E2"},
                {'range': [50, 80], 'color': "#FEF3C7"},
                {'range': [80, 100], 'color': "#DCFCE7"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))

    fig.update_layout(
        height=300,
        font={'color': "#374151", 'family': "Arial"},
        margin=dict(l=20, r=20, t=40, b=20)
    )

    return fig

def voice_interface_tab():
    """Voice interface demonstration"""

    st.header("🎙️ Voice Interface Demo")

    st.markdown("""
    <div class="voice-interface">
        <h3>🗣️ Ask Questions About Your Document</h3>
        <p>Use natural speech to get instant answers about legal documents</p>
    </div>
    """, unsafe_allow_html=True)

    # Voice interface simulation
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 🎤 Voice Input")

        # Simulate voice recording
        if st.button("🎙️ Start Recording", type="primary"):
            with st.spinner("Listening..."):
                time.sleep(2)
            st.success("Voice recorded!")
            st.session_state.voice_question = "What happens if I breach the confidentiality clause?"

        # Manual question input
        voice_question = st.text_input(
            "Or type your question:",
            value=st.session_state.voice_question,
            placeholder="What does this clause mean in simple terms?"
        )

        # Sample questions
        st.markdown("**Sample Questions:**")
        sample_questions = [
            "What are the main risks in this document?",
            "Can I negotiate these terms?", 
            "What happens if I break this agreement?",
            "Are these terms fair?",
            "What should I be worried about?"
        ]

        for q in sample_questions:
            if st.button(f"❓ {q}", key=q):
                st.session_state.voice_question = q

    with col2:
        if st.session_state.voice_question:
            st.markdown("### 🤖 AI Response")

            # Generate response based on question
            response = generate_voice_response(st.session_state.voice_question)

            # Text response
            st.markdown(f"""
            <div class="feature-card">
                <h4>📝 Text Response:</h4>
                <p>{response['text']}</p>
                <p><strong>Confidence:</strong> {response['confidence']}%</p>
            </div>
            """, unsafe_allow_html=True)

            # Audio simulation
            st.markdown("### 🔊 Audio Response")
            st.info("🎵 Audio response would play here (Text-to-Speech)")

            # Voice controls
            col_play, col_pause, col_speed = st.columns(3)
            with col_play:
                st.button("▶️ Play")
            with col_pause:
                st.button("⏸️ Pause") 
            with col_speed:
                speed = st.selectbox("Speed", ["0.8x", "1.0x", "1.2x", "1.5x"])

        else:
            st.info("👈 Ask a question to see voice AI in action")

            # Show voice interface benefits
            st.markdown("""
            <div class="feature-card">
                <h4>🎯 Voice Interface Benefits:</h4>
                <ul>
                    <li><strong>Hands-free operation</strong> - Ask while driving or walking</li>
                    <li><strong>Natural conversation</strong> - No need to learn legal terminology</li>
                    <li><strong>Instant answers</strong> - Get responses in 2-3 seconds</li>
                    <li><strong>Accessibility</strong> - Perfect for visual impairments</li>
                    <li><strong>Mobile optimized</strong> - Works great on phones</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

def generate_voice_response(question):
    """Generate AI response to voice question"""

    question_lower = question.lower()

    # Simple response generation based on keywords
    if "risk" in question_lower or "worry" in question_lower:
        return {
            "text": "Based on my analysis with 89% confidence, the main risks are: 1) The confidentiality definition is quite broad, 2) The 2-year term is longer than average, and 3) There are limited exceptions for disclosure. However, these are manageable risks for a standard business relationship.",
            "confidence": 89
        }
    elif "breach" in question_lower or "break" in question_lower:
        return {
            "text": "If you breach the confidentiality clause, the company could seek legal remedies including financial damages and court orders to stop further disclosure. However, with 85% confidence, I note that the agreement lacks specific penalty amounts, which actually limits their ability to claim excessive damages.",
            "confidence": 85
        }
    elif "negotiate" in question_lower:
        return {
            "text": "Yes, with 92% confidence, these terms are negotiable. I recommend: 1) Reducing the term from 2 years to 1 year, 2) Narrowing the confidentiality definition, and 3) Adding mutual confidentiality if you're also sharing information. Most companies expect some negotiation on NDAs.",
            "confidence": 92
        }
    elif "fair" in question_lower:
        return {
            "text": "With 88% confidence, these terms are within normal ranges but favor the company. The 2-year term is on the longer side, and the broad confidentiality definition gives them significant protection. However, it's not unusually harsh compared to standard industry NDAs.",
            "confidence": 88
        }
    else:
        return {
            "text": "I can help explain specific clauses, assess risks, or suggest negotiation points. With 91% confidence, I recommend focusing on the confidentiality definition, term length, and your obligations for returning materials. Would you like me to explain any of these areas in more detail?",
            "confidence": 91
        }

def features_demo_tab():
    """Demonstrate key features and capabilities"""

    st.header("🚀 Feature Demonstrations")

    # Feature showcase
    feature_tabs = st.tabs([
        "🎯 Confidence Scoring", 
        "📊 Risk Assessment", 
        "🌍 Multi-language", 
        "📱 Mobile Design",
        "🔒 Privacy Controls"
    ])

    with feature_tabs[0]:
        st.markdown("### 🎯 AI Confidence Scoring System")

        st.markdown("""
        Our revolutionary confidence scoring system shows exactly how certain the AI is about each analysis:
        """)

        # Multiple confidence examples
        confidence_examples = [
            {"task": "Contract Classification", "confidence": 94, "explanation": "Clear contract language and structure"},
            {"task": "Risk Assessment", "confidence": 87, "explanation": "Some ambiguous clauses require careful interpretation"},
            {"task": "Legal Precedent Matching", "confidence": 76, "explanation": "Limited similar cases in jurisdiction"},
            {"task": "Clause Interpretation", "confidence": 91, "explanation": "Standard legal language with clear meaning"}
        ]

        for example in confidence_examples:
            col1, col2, col3 = st.columns([2, 1, 3])

            with col1:
                st.write(f"**{example['task']}**")

            with col2:
                confidence = example['confidence']
                if confidence >= 90:
                    st.success(f"{confidence}%")
                elif confidence >= 75:
                    st.warning(f"{confidence}%")
                else:
                    st.error(f"{confidence}%")

            with col3:
                st.write(example['explanation'])

        st.markdown("---")
        st.info("💡 **Why This Matters:** Users can make informed decisions knowing when AI is certain vs. uncertain")

    with feature_tabs[1]:
        st.markdown("### 📊 Advanced Risk Assessment")

        # Risk assessment visualization
        risk_data = {
            "Clause": ["Confidentiality Scope", "Term Duration", "Penalty Terms", "Return Requirements", "Exceptions"],
            "Risk Level": ["Medium", "Low", "High", "Low", "Medium"],
            "Confidence": [87, 94, 82, 91, 85],
            "Impact": ["Moderate", "Low", "High", "Low", "Moderate"]
        }

        df_risk = pd.DataFrame(risk_data)

        # Color code by risk level
        def color_risk(val):
            if val == "High":
                return "background-color: #ff4000"
            elif val == "Medium":
                return "background-color: #ADD8E6"
            else:
                return "background-color: #00ff00"

        st.dataframe(
            df_risk.style.applymap(color_risk, subset=['Risk Level']),
            use_container_width=True
        )

        st.info("💡 **Innovation:** First legal AI to provide clause-level risk assessment with confidence intervals")

    with feature_tabs[2]:
        st.markdown("### 🌍 Multi-language & Multi-jurisdictional")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Supported Languages:**")
            languages = [
                "🇺🇸 English", "🇪🇸 Spanish", "🇫🇷 French", "🇩🇪 German", 
                "🇮🇳 Hindi", "🇨🇳 Chinese", "🇯🇵 Japanese", "🇰🇷 Korean",
                "🇵🇹 Portuguese", "🇮🇹 Italian", "🇷🇺 Russian", "🇦🇷 Arabic"
            ]

            for lang in languages:
                st.write(f"✅ {lang}")

        with col2:
            st.markdown("**Legal Jurisdictions:**")
            jurisdictions = [
                "🏛️ United States Federal",
                "⭐ California State Law", 
                "🤠 Texas State Law",
                "🗽 New York State Law",
                "🇬🇧 United Kingdom",
                "🇨🇦 Canada",
                "🇦🇺 Australia",
                "🇪🇺 European Union"
            ]

            for juris in jurisdictions:
                st.write(f"✅ {juris}")

        st.success("🌍 **Global Ready:** Same document analyzed differently based on local laws")

    with feature_tabs[3]:
        st.markdown("### 📱 Mobile-First Design")

        # Mobile interface preview
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.markdown("""
            <div style="border: 3px solid #2563EB; border-radius: 20px; padding: 20px; background: linear-gradient(180deg, #F8FAFC 0%, #E2E8F0 100%); text-align: center;">
                <h4>📱 Mobile Interface Preview</h4>
                <div style="background: #000000; border-radius: 10px; padding: 15px; margin: 10px 0;">
                    <p><strong>📤 Document Upload</strong></p>
                    <p style="font-size: 0.9em;">Drag & drop or camera scan</p>
                </div>
                <div style="background: #000000; border-radius: 10px; padding: 15px; margin: 10px 0;">
                    <p><strong>🎯 Confidence: 94%</strong></p>
                    <p style="font-size: 0.9em;">High confidence analysis</p>
                </div>
                <div style="background: #000000; border-radius: 10px; padding: 15px; margin: 10px 0;">
                    <p><strong>🎙️ Voice Questions</strong></p>
                    <p style="font-size: 0.9em;">Tap to ask anything</p>
                </div>
                <div style="background: #000000; border-radius: 10px; padding: 15px; margin: 10px 0;">
                    <p><strong>📋 Plain English</strong></p>
                    <p style="font-size: 0.9em;">Complex → Simple</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.info("📱 **Mobile Advantage:** 70% of legal questions happen on mobile - we're built for it")

    with feature_tabs[4]:
        st.markdown("### 🔒 Privacy & Security Controls")

        # Privacy features showcase
        privacy_features = [
            {"feature": "Zero Document Storage", "status": "✅ Active", "description": "Documents processed and immediately deleted"},
            {"feature": "End-to-End Encryption", "status": "✅ Active", "description": "AES-256 encryption for all data transmission"},
            {"feature": "GDPR Compliance", "status": "✅ Certified", "description": "Full European privacy law compliance"},
            {"feature": "Local Processing Option", "status": "✅ Available", "description": "Process sensitive docs on your device"},
            {"feature": "Audit Logging", "status": "✅ Enabled", "description": "Complete transparency on data handling"},
            {"feature": "User Data Control", "status": "✅ Full Control", "description": "Delete all data anytime"}
        ]

        for feature in privacy_features:
            st.markdown(f"""
            <div class="trust-indicator">
                <span style="font-size: 1.2em;">🔒</span>
                <div>
                    <strong>{feature['feature']}</strong> - {feature['status']}<br>
                    <small>{feature['description']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.success("🛡️ **Trust First:** Built for legal professionals who need absolute privacy")

def business_case_tab():
    """Business case and market opportunity"""

    st.header("🏢 Business Case & Market Opportunity")

    # Market size visualization
    st.markdown("### 📈 Market Opportunity")

    col1, col2 = st.columns(2)

    with col1:
        # Market size chart
        market_data = {
            "Market Segment": ["Legal AI Market", "Document Automation", "Legal Consultation", "Small Business Legal"],
            "Market Size ($B)": [6.4, 2.1, 15.3, 8.7],
            "Growth Rate (%)": [31.3, 28.5, 12.4, 18.9]
        }

        df_market = pd.DataFrame(market_data)

        fig = px.bar(df_market, x="Market Segment", y="Market Size ($B)", 
                    title="Legal Technology Market Size",
                    color="Growth Rate (%)",
                    color_continuous_scale="Blues")
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Key metrics
        st.metric("Total Addressable Market", "$50B+", "12% YoY")
        st.metric("Underserved Consumers", "65%", "2.4B people")
        st.metric("Cost Advantage", "96%", "$10 vs $400")
        st.metric("User Avoidance Rate", "87%", "Due to complexity")

    # Business model
    st.markdown("### 💰 Revenue Model")

    pricing_tiers = {
        "Plan": ["Free", "Individual", "Business", "Enterprise"],
        "Price": ["$0/month", "$10/month", "$50/month", "Custom"],
        "Features": ["3 docs/month", "Unlimited docs", "Team + API", "White-label"],
        "Target Users": ["Individuals", "Consumers", "Small Business", "Corporations"]
    }

    df_pricing = pd.DataFrame(pricing_tiers)
    st.table(df_pricing)

    # Revenue projections
    st.markdown("### 📊 Revenue Projections")

    years = [2024, 2025, 2026, 2027]
    revenue = [100, 1000, 5000, 15000]  # in thousands
    users = [1, 10, 50, 150]  # in thousands

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x=years, y=revenue, name="Revenue ($K)", marker_color="#2563EB"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=years, y=users, name="Users (K)", marker_color="#10B981"),
        secondary_y=True,
    )

    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="Revenue ($K)", secondary_y=False)
    fig.update_yaxes(title_text="Users (K)", secondary_y=True)

    fig.update_layout(title="Revenue & User Growth Projection", height=400)

    st.plotly_chart(fig, use_container_width=True)

    # Competitive advantages
    st.markdown("### 🏆 Competitive Advantages")

    advantages = [
        {"advantage": "Only AI with Confidence Scoring", "impact": "Builds unprecedented user trust"},
        {"advantage": "Voice-First Interface", "impact": "True accessibility & mobile optimization"},
        {"advantage": "Hallucination Detection", "impact": "Addresses core AI reliability concern"},
        {"advantage": "Privacy-First Architecture", "impact": "Zero storage builds professional confidence"},
        {"advantage": "Multi-jurisdictional Intelligence", "impact": "Global scalability from day one"},
        {"advantage": "B2B2C Distribution", "impact": "Lower customer acquisition costs"}
    ]

    for adv in advantages:
        st.markdown(f"""
        <div class="feature-card">
            <strong>🎯 {adv['advantage']}</strong><br>
            <em>Impact: {adv['impact']}</em>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
