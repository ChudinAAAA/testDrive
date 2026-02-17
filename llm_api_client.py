#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple LLM API Client
Sends requests to LLM API and displays responses
"""

import os
import sys
import json
from typing import Optional

# Fix encoding for Windows console
if sys.platform == 'win32':
    try:
        import codecs
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except:
        pass  # If encoding fix fails, continue anyway

try:
    import requests
except ImportError:
    print("Installing required package: requests")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests


class LLMClient:
    """Client for interacting with LLM APIs"""
    
    def __init__(self, api_key: Optional[str] = None, api_url: Optional[str] = None):
        """
        Initialize LLM Client
        
        Args:
            api_key: API key for authentication
            api_url: API endpoint URL
        """
        # Try to get API key from environment variables
        # Priority: ROUTERAI_API_KEY > OPENAI_API_KEY
        self.api_key = (
            api_key or 
            os.getenv("ROUTERAI_API_KEY") or 
            os.getenv("OPENAI_API_KEY")
        )
        
        # Default to RouterAI endpoint
        self.api_url = (
            api_url or
            os.getenv("ROUTERAI_API_URL") or
            "https://routerai.ru/api/v1/chat/completions"
        )
        
        if not self.api_key:
            print("⚠️  Warning: No API key provided.")
            print("   Set ROUTERAI_API_KEY or OPENAI_API_KEY environment variable")
            print("   or pass api_key parameter.")
    
    def send_request(self, prompt: str, model: str = "gpt-4o-mini", 
                     temperature: float = 0.7, max_tokens: int = 500) -> dict:
        """
        Send request to LLM API
        
        Args:
            prompt: The user's prompt/question
            model: Model to use (default: gpt-3.5-turbo)
            temperature: Creativity level (0.0-2.0)
            max_tokens: Maximum response length
            
        Returns:
            dict: API response
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        print(f"📤 Sending request to {self.api_url}...")
        print(f"📝 Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}\n")
        
        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            error_body = ""
            try:
                error_body = e.response.json()
            except Exception:
                error_body = e.response.text
            return {
                "error": str(e),
                "status_code": e.response.status_code,
                "details": error_body
            }
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status_code": None}
    
    def extract_response_text(self, response: dict) -> str:
        """
        Extract text from API response
        
        Args:
            response: API response dictionary
            
        Returns:
            str: Extracted response text
        """
        if "error" in response:
            return f"❌ Error: {response['error']}"
        
        try:
            return response["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as e:
            return f"❌ Error parsing response: {e}\n\nFull response: {json.dumps(response, indent=2)}"
    
    def chat(self, prompt: str, **kwargs) -> str:
        """
        Send a chat request and return the response text
        
        Args:
            prompt: The user's prompt/question
            **kwargs: Additional parameters for send_request
            
        Returns:
            str: LLM response text
        """
        response = self.send_request(prompt, **kwargs)
        return self.extract_response_text(response)


def main():
    """Main CLI interface"""
    print("=" * 60)
    print("🤖 LLM API Client")
    print("=" * 60)
    print()
    
    # Initialize client
    client = LLMClient()
    
    # Check if API key is available
    if not client.api_key:
        print("❌ No API key found!")
        print("\nTo use this client, you need to:")
        print("1. Get an API key from RouterAI:")
        print("   https://routerai.ru/pages/vibe-coding-vscode-cline")
        print("\n2. Set it as environment variable:")
        print("   Windows: set ROUTERAI_API_KEY=your-api-key-here")
        print("   Linux/Mac: export ROUTERAI_API_KEY=your-api-key-here")
        print("\nOr use OpenAI API key with OPENAI_API_KEY variable.")
        return
    
    # Example prompts
    if len(sys.argv) > 1:
        # Use command line argument as prompt
        prompt = " ".join(sys.argv[1:])
    else:
        # Use default prompt
        prompt = "Explain what is artificial intelligence in 2-3 sentences."
        print(f"💡 Using example prompt: '{prompt}'")
        print("   (You can pass your own prompt as command line argument)")
        print()
    
    # Send request and get response
    response_text = client.chat(prompt)
    
    # Display response
    print("=" * 60)
    print("📥 Response:")
    print("=" * 60)
    print(response_text)
    print()
    print("=" * 60)
    print("✅ Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
