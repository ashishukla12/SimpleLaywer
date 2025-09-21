import streamlit as st
import hashlib
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json

class DocumentProcessor:
    """Handle document processing and analysis"""

    @staticmethod
    def extract_text_from_pdf(file):
        """Extract text from uploaded PDF file"""
        # In a real implementation, you would use PyPDF2 or pdfplumber
        return f"Sample extracted text from {file.name}"

    @staticmethod
    def process_image(image_file):
        """Process uploaded image files"""
        # In a real implementation, you would use OCR libraries
        return f"Sample OCR text from {image_file.name}"

    @staticmethod
    def classify_document_type(text: str) -> Tuple[str, float]:
        """Classify document type based on content"""
        text_lower = text.lower()

        # Simple keyword-based classification
        if any(word in text_lower for word in ["nda", "non-disclosure", "confidential"]):
            return "Non-Disclosure Agreement", 0.92
        elif any(word in text_lower for word in ["lease", "rent", "tenant"]):
            return "Lease Agreement", 0.88
        elif any(word in text_lower for word in ["employment", "employee", "job"]):
            return "Employment Contract", 0.85
        else:
            return "General Contract", 0.75

class ConfidenceCalculator:
    """Calculate and manage AI confidence scores"""

    @staticmethod
    def calculate_base_confidence(text_length: int, keywords_found: int, document_type: str) -> float:
        """Calculate base confidence score"""
        # Simple confidence calculation based on various factors
        base_score = 0.7

        # Adjust based on text length (more text = higher confidence)
        if text_length > 1000:
            base_score += 0.1
        elif text_length > 500:
            base_score += 0.05

        # Adjust based on keywords found
        base_score += min(keywords_found * 0.02, 0.15)

        # Adjust based on document type certainty
        type_confidence_map = {
            "Non-Disclosure Agreement": 0.05,
            "Lease Agreement": 0.03,
            "Employment Contract": 0.02,
            "General Contract": -0.05
        }
        base_score += type_confidence_map.get(document_type, 0)

        return min(max(base_score, 0.3), 0.98)  # Clamp between 30% and 98%

    @staticmethod
    def calculate_clause_confidence(clause_type: str, context: str) -> float:
        """Calculate confidence for specific clauses"""
        # Different confidence levels based on clause complexity
        confidence_map = {
            "confidentiality": 0.9,
            "termination": 0.85,
            "payment": 0.92,
            "liability": 0.78,
            "intellectual_property": 0.82,
            "non_compete": 0.75
        }

        base_confidence = confidence_map.get(clause_type.lower(), 0.8)

        # Adjust based on context clarity
        if len(context.split()) > 50:  # Detailed clause
            base_confidence += 0.05
        elif len(context.split()) < 20:  # Vague clause
            base_confidence -= 0.1

        return min(max(base_confidence, 0.4), 0.98)

class RiskAssessor:
    """Assess risks in legal documents"""

    RISK_KEYWORDS = {
        "high": [
            "unlimited liability", "perpetual", "irrevocable", "sole discretion",
            "without cause", "immediate termination", "no refund", "exclusive"
        ],
        "medium": [
            "reasonable", "good faith", "material breach", "written notice",
            "30 days", "subject to", "may terminate", "additional fees"
        ],
        "low": [
            "mutual", "both parties", "standard", "reasonable notice",
            "cure period", "dispute resolution", "mediation", "arbitration"
        ]
    }

    @staticmethod
    def assess_document_risk(text: str, document_type: str) -> List[Dict]:
        """Assess overall document risk"""
        text_lower = text.lower()
        risks = []

        # Check for high-risk patterns
        high_risk_count = sum(1 for keyword in RiskAssessor.RISK_KEYWORDS["high"] if keyword in text_lower)
        medium_risk_count = sum(1 for keyword in RiskAssessor.RISK_KEYWORDS["medium"] if keyword in text_lower)
        low_risk_count = sum(1 for keyword in RiskAssessor.RISK_KEYWORDS["low"] if keyword in text_lower)

        if high_risk_count > 2:
            risks.append({
                "type": "Document Structure",
                "level": "high",
                "confidence": 0.85,
                "description": f"Document contains {high_risk_count} high-risk clauses that heavily favor one party"
            })

        if medium_risk_count > low_risk_count:
            risks.append({
                "type": "Terms Balance",
                "level": "medium", 
                "confidence": 0.78,
                "description": "Terms appear to favor one party over mutual benefit"
            })
        else:
            risks.append({
                "type": "Terms Balance",
                "level": "low",
                "confidence": 0.92,
                "description": "Terms appear reasonably balanced between parties"
            })

        return risks

class VoiceInterface:
    """Handle voice interface interactions"""

    COMMON_QUESTIONS = {
        "what": "explanation",
        "how": "process",
        "can i": "permission",
        "should i": "advice",
        "risk": "risk_assessment",
        "penalty": "consequences",
        "negotiate": "negotiation"
    }

    @staticmethod
    def process_voice_question(question: str, document_context: str) -> Dict:
        """Process voice question and generate response"""
        question_lower = question.lower()

        # Determine question type
        question_type = "general"
        for keyword, qtype in VoiceInterface.COMMON_QUESTIONS.items():
            if keyword in question_lower:
                question_type = qtype
                break

        # Generate appropriate response
        response = VoiceInterface._generate_response(question_type, question, document_context)

        return {
            "question": question,
            "response": response["text"],
            "confidence": response["confidence"],
            "suggestions": response["suggestions"]
        }

    @staticmethod
    def _generate_response(question_type: str, question: str, context: str) -> Dict:
        """Generate response based on question type"""

        responses = {
            "explanation": {
                "text": "Based on my analysis with 87% confidence, this clause means that you must keep all shared information confidential and cannot discuss it with outside parties. The key requirement is maintaining secrecy about business operations, customer lists, and proprietary methods.",
                "confidence": 87,
                "suggestions": ["Ask about specific exceptions", "Clarify time limits", "Understand penalties"]
            },
            "risk_assessment": {
                "text": "I've identified medium-level risk with 82% confidence. The main concerns are: 1) Broad confidentiality definition, 2) Two-year term length, and 3) Limited exceptions. However, these are manageable for standard business relationships.",
                "confidence": 82,
                "suggestions": ["Consider negotiating term length", "Request mutual confidentiality", "Add specific exceptions"]
            },
            "negotiation": {
                "text": "With 89% confidence, these terms are negotiable. I recommend: 1) Reducing the term to 1 year, 2) Adding mutual obligations, 3) Including standard exceptions for public information. Most companies expect some back-and-forth on contract terms.",
                "confidence": 89,
                "suggestions": ["Propose specific changes", "Highlight mutual benefits", "Seek legal review if needed"]
            },
            "consequences": {
                "text": "Based on 85% confidence analysis, violating this agreement could result in financial damages, court injunctions to stop disclosure, and potential legal fees. However, the agreement lacks specific penalty amounts, which may limit excessive claims.",
                "confidence": 85,
                "suggestions": ["Understand what constitutes violation", "Review disclosure exceptions", "Consider legal insurance"]
            }
        }

        return responses.get(question_type, {
            "text": "I can help explain specific terms, assess risks, or suggest negotiation strategies. With 91% confidence, I recommend focusing on the areas that most directly affect your obligations and rights.",
            "confidence": 91,
            "suggestions": ["Ask about specific clauses", "Request risk assessment", "Explore negotiation options"]
        })

class DataExporter:
    """Handle data export functionality"""

    @staticmethod
    def generate_pdf_report(analysis_data: Dict) -> str:
        """Generate PDF report (simulated)"""
        # In real implementation, would use libraries like reportlab
        return f"PDF report generated for {analysis_data['document_type']} analysis"

    @staticmethod
    def generate_summary_email(analysis_data: Dict, user_email: str) -> str:
        """Generate email summary (simulated)"""
        return f"Summary email sent to {user_email} for document analysis"

    @staticmethod
    def export_to_json(analysis_data: Dict) -> str:
        """Export analysis to JSON format"""
        return json.dumps(analysis_data, indent=2)

class SessionManager:
    """Manage user sessions and preferences"""

    @staticmethod
    def initialize_session():
        """Initialize session state variables"""
        if "user_preferences" not in st.session_state:
            st.session_state.user_preferences = {
                "complexity_level": "Moderate",
                "jurisdiction": "California",
                "user_type": "Small Business Owner",
                "language": "English"
            }

        if "analysis_history" not in st.session_state:
            st.session_state.analysis_history = []

        if "voice_history" not in st.session_state:
            st.session_state.voice_history = []

    @staticmethod
    def save_analysis(analysis_data: Dict):
        """Save analysis to session history"""
        analysis_data["timestamp"] = datetime.now().isoformat()
        analysis_data["session_id"] = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]

        st.session_state.analysis_history.append(analysis_data)

        # Keep only last 10 analyses
        if len(st.session_state.analysis_history) > 10:
            st.session_state.analysis_history = st.session_state.analysis_history[-10:]

    @staticmethod
    def get_user_preferences() -> Dict:
        """Get current user preferences"""
        return st.session_state.get("user_preferences", {})

    @staticmethod
    def update_user_preferences(preferences: Dict):
        """Update user preferences"""
        st.session_state.user_preferences.update(preferences)