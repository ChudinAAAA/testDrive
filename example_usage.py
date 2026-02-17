#!/usr/bin/env python3
"""
Example usage of LLM API Client with RouterAI
Demonstrates different ways to use the client
Get API key from: https://routerai.ru/pages/vibe-coding-vscode-cline
"""

from llm_api_client import LLMClient


def example_basic_usage():
    """Basic usage example with RouterAI"""
    print("=" * 60)
    print("Example 1: Basic Usage (RouterAI)")
    print("=" * 60)
    
    # Uses ROUTERAI_API_KEY or OPENAI_API_KEY from environment
    client = LLMClient()
    
    if not client.api_key:
        print("⚠️  Skipping - No API key configured")
        print("   Get API key from: https://routerai.ru/pages/vibe-coding-vscode-cline")
        return
    
    response = client.chat("What is Python programming language?")
    print(response)
    print()


def example_with_parameters():
    """Example with custom parameters"""
    print("=" * 60)
    print("Example 2: With Custom Parameters")
    print("=" * 60)
    
    client = LLMClient()
    
    if not client.api_key:
        print("⚠️  Skipping - No API key configured")
        return
    
    response = client.chat(
        "Write a haiku about coding",
        model="gpt-4o-mini",  # Specify model
        temperature=0.9,  # More creative
        max_tokens=100
    )
    print(response)
    print()


def example_multiple_requests():
    """Example with multiple requests"""
    print("=" * 60)
    print("Example 3: Multiple Requests")
    print("=" * 60)
    
    client = LLMClient()
    
    if not client.api_key:
        print("⚠️  Skipping - No API key configured")
        return
    
    questions = [
        "What is 2+2?",
        "Name a programming language",
        "What color is the sky?"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        response = client.chat(question, max_tokens=50)
        print(f"Answer: {response}")
    
    print()


def example_different_providers():
    """Example with different API providers"""
    print("=" * 60)
    print("Example 4: Different API Providers")
    print("=" * 60)
    
    # RouterAI (default)
    print("\n1. Using RouterAI:")
    client_routerai = LLMClient()
    if client_routerai.api_key:
        print(f"   Endpoint: {client_routerai.api_url}")
    
    # OpenAI directly
    print("\n2. Using OpenAI directly:")
    client_openai = LLMClient(
        api_url="https://api.openai.com/v1/chat/completions"
    )
    if client_openai.api_key:
        print(f"   Endpoint: {client_openai.api_url}")
    
    # Local model (example)
    print("\n3. Using local model (Ollama example):")
    client_local = LLMClient(
        api_key="not-needed",
        api_url="http://localhost:11434/v1/chat/completions"
    )
    print(f"   Endpoint: {client_local.api_url}")
    print()


def example_error_handling():
    """Example with error handling"""
    print("=" * 60)
    print("Example 5: Error Handling")
    print("=" * 60)
    
    # Create client with invalid API key
    client = LLMClient(api_key="invalid-key")
    
    response = client.chat("Hello")
    print(response)
    print()


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("🤖 LLM API Client - Usage Examples")
    print("=" * 60)
    print()
    
    # Run examples
    example_basic_usage()
    example_with_parameters()
    example_multiple_requests()
    example_different_providers()
    example_error_handling()
    
    print("=" * 60)
    print("✅ All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
