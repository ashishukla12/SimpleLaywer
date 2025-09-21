
"""
Configuration settings for LegalAI Simplifier
"""

import os
from typing import Dict, Any

# App Configuration
APP_CONFIG = {
    "app_name": "LegalAI Simplifier",
    "version": "1.0.0",
    "description": "AI-Powered Legal Document Analysis with Confidence Scoring",
    "author": "Legal AI Team",
    "contact_email": "contact@legalai-simplifier.com"
}

# AI Model Configuration
AI_CONFIG = {
    "confidence_threshold": 0.7,
    "max_document_length": 10000,  # characters
    "supported_formats": [".pdf", ".txt", ".docx", ".doc"],
    "max_file_size": 10,  # MB
    "processing_timeout": 30,  # seconds
}

# Voice Interface Configuration
VOICE_CONFIG = {
    "max_recording_length": 60,  # seconds
    "supported_languages": [
        "en-US", "es-ES", "fr-FR", "de-DE", "hi-IN", 
        "zh-CN", "ja-JP", "ko-KR", "pt-PT", "it-IT"
    ],
    "default_voice_speed": 1.0,
    "voice_response_timeout": 5  # seconds
}

# Security Configuration
SECURITY_CONFIG = {
    "document_retention_time": 0,  # minutes (0 = immediate deletion)
    "encryption_enabled": True,
    "privacy_mode": "strict",
    "audit_logging": True,
    "gdpr_compliant": True
}

# UI Configuration
UI_CONFIG = {
    "theme": {
        "primary_color": "#2563EB",
        "secondary_color": "#1E3A8A", 
        "success_color": "#10B981",
        "warning_color": "#F59E0B",
        "error_color": "#EF4444",
        "background_color": "#FFFFFF"
    },
    "layout": {
        "sidebar_width": 300,
        "main_content_width": 800,
        "max_chart_height": 400
    },
    "features": {
        "show_confidence_meter": True,
        "enable_voice_interface": True,
        "show_risk_assessment": True,
        "enable_export": True
    }
}

# Business Configuration
BUSINESS_CONFIG = {
    "pricing_tiers": {
        "free": {
            "name": "Free",
            "price": 0,
            "documents_per_month": 3,
            "features": ["Basic analysis", "Confidence scoring"]
        },
        "individual": {
            "name": "Individual", 
            "price": 10,
            "documents_per_month": -1,  # unlimited
            "features": ["Unlimited docs", "Voice interface", "Export"]
        },
        "business": {
            "name": "Business",
            "price": 50,
            "documents_per_month": -1,
            "features": ["Team sharing", "API access", "Priority support"]
        }
    },
    "contact_info": {
        "support_email": "support@legalai-simplifier.com",
        "sales_email": "sales@legalai-simplifier.com",
        "website": "https://legalai-simplifier.com"
    }
}

# Legal Jurisdictions
JURISDICTION_CONFIG = {
    "supported_jurisdictions": [
        {"code": "US-CA", "name": "California, USA", "legal_system": "common_law"},
        {"code": "US-TX", "name": "Texas, USA", "legal_system": "common_law"},
        {"code": "US-NY", "name": "New York, USA", "legal_system": "common_law"},
        {"code": "US-FL", "name": "Florida, USA", "legal_system": "common_law"},
        {"code": "UK", "name": "United Kingdom", "legal_system": "common_law"},
        {"code": "CA", "name": "Canada", "legal_system": "common_law"},
        {"code": "AU", "name": "Australia", "legal_system": "common_law"},
        {"code": "EU", "name": "European Union", "legal_system": "civil_law"}
    ],
    "default_jurisdiction": "US-CA"
}

# Document Types Configuration
DOCUMENT_TYPES = {
    "nda": {
        "name": "Non-Disclosure Agreement",
        "common_clauses": [
            "confidentiality_definition", "permitted_disclosures", "term_duration",
            "return_of_materials", "remedies", "governing_law"
        ],
        "risk_factors": [
            "overly_broad_definition", "excessive_term_length", "unlimited_liability",
            "inadequate_exceptions", "harsh_remedies"
        ]
    },
    "lease": {
        "name": "Lease Agreement",
        "common_clauses": [
            "rent_amount", "security_deposit", "maintenance_responsibilities",
            "pet_policy", "termination_clause", "renewal_options"
        ],
        "risk_factors": [
            "excessive_deposit", "unfair_maintenance_terms", "automatic_renewal",
            "restricted_use", "landlord_entry_rights"
        ]
    },
    "employment": {
        "name": "Employment Contract",
        "common_clauses": [
            "compensation", "benefits", "job_responsibilities", "termination_terms",
            "non_compete", "intellectual_property", "confidentiality"
        ],
        "risk_factors": [
            "at_will_termination", "broad_non_compete", "unpaid_overtime",
            "ip_assignment", "restrictive_confidentiality"
        ]
    }
}

def get_config(config_name: str) -> Dict[str, Any]:
    """Get configuration by name"""
    configs = {
        "app": APP_CONFIG,
        "ai": AI_CONFIG,
        "voice": VOICE_CONFIG,
        "security": SECURITY_CONFIG,
        "ui": UI_CONFIG,
        "business": BUSINESS_CONFIG,
        "jurisdiction": JURISDICTION_CONFIG,
        "documents": DOCUMENT_TYPES
    }
    return configs.get(config_name, {})

def get_env_var(var_name: str, default_value: str = None) -> str:
    """Get environment variable with default"""
    return os.getenv(var_name, default_value)
