#!/usr/bin/env python3
"""
Example usage of LLM API Client
Demonstrates different ways to use the client
"""

from llm_api_client import LLMClient


def example_basic_usage():
    """Basic usage example"""
    print("=" * 60)
    print("Example 1: Basic Usage")
    print("=" * 60)
    
    client = LLMClient()
    
    if not client.api_key:
        print("⚠️  Skipping - No API key configured")
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


def example_error_handling():
    """Example with error handling"""
    print("=" * 60)
    print("Example 4: Error Handling")
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
    example_error_handling()
    
    print("=" * 60)
    print("✅ All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
