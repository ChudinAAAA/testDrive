#!/usr/bin/env python3
"""
Test script to verify RouterAI API integration
"""

from llm_api_client import LLMClient

print("=" * 60)
print("🧪 Testing RouterAI API Integration")
print("=" * 60)
print()

# Create client
client = LLMClient()

# Display configuration
print(f"✅ API Key: {client.api_key[:15]}...")
print(f"✅ API URL: {client.api_url}")
print()

# Test request
print("📤 Sending test request...")
print()

try:
    response = client.chat(
        "Say 'Hello! API is working!' in Russian",
        max_tokens=100
    )
    
    print("=" * 60)
    print("✅ SUCCESS! API is working correctly!")
    print("=" * 60)
    print()
    print("Response:", response)
    print()
    
except Exception as e:
    print("=" * 60)
    print("❌ ERROR!")
    print("=" * 60)
    print(f"Error: {e}")
    print()

print("=" * 60)
print("🏁 Test completed")
print("=" * 60)
