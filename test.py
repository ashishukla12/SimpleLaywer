#!/usr/bin/env python3
"""
Test script for LegalAI Simplifier
Run basic functionality tests
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import DocumentProcessor, ConfidenceCalculator, RiskAssessor
from config import get_config

def test_document_processor():
    """Test document processing functionality"""
    print("🧪 Testing Document Processor...")

    sample_text = "This Non-Disclosure Agreement shall remain confidential for a period of two years."
    doc_type, confidence = DocumentProcessor.classify_document_type(sample_text)

    print(f"✅ Document classified as: {doc_type} (Confidence: {confidence:.2f})")
    assert doc_type == "Non-Disclosure Agreement"
    assert confidence > 0.8

def test_confidence_calculator():
    """Test confidence calculation"""
    print("🧪 Testing Confidence Calculator...")

    confidence = ConfidenceCalculator.calculate_base_confidence(
        text_length=1000,
        keywords_found=5,
        document_type="Non-Disclosure Agreement"
    )

    print(f"✅ Base confidence calculated: {confidence:.2f}")
    assert 0.3 <= confidence <= 0.98

def test_risk_assessor():
    """Test risk assessment functionality"""
    print("🧪 Testing Risk Assessor...")

    sample_text = "unlimited liability perpetual agreement sole discretion"
    risks = RiskAssessor.assess_document_risk(sample_text, "contract")

    print(f"✅ Risk assessment completed: {len(risks)} risks identified")
    assert len(risks) > 0

def test_config_loading():
    """Test configuration loading"""
    print("🧪 Testing Configuration Loading...")

    app_config = get_config("app")
    ai_config = get_config("ai")

    print(f"✅ App config loaded: {app_config['app_name']}")
    print(f"✅ AI config loaded: Confidence threshold = {ai_config['confidence_threshold']}")

    assert app_config["app_name"] == "LegalAI Simplifier"
    assert ai_config["confidence_threshold"] == 0.7

def run_all_tests():
    """Run all tests"""
    print("🎯 Running LegalAI Simplifier Tests...")
    print("=" * 50)

    try:
        test_document_processor()
        test_confidence_calculator()
        test_risk_assessor()
        test_config_loading()

        print("=" * 50)
        print("🎉 All tests passed successfully!")
        print("✅ LegalAI Simplifier is ready for deployment!")

    except Exception as e:
        print("=" * 50)
        print(f"❌ Test failed: {str(e)}")
        print("🔧 Please check your implementation.")
        sys.exit(1)

if __name__ == "__main__":
    run_all_tests()
