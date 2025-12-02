#!/usr/bin/env python3
"""
Test Anthropic API key setup
"""

import os
from dotenv import load_dotenv
import anthropic

def test_api_key():
    """Test if the Anthropic API key is set up correctly"""

    # Load environment variables
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("❌ ANTHROPIC_API_KEY not found in .env file")
        print("\n📝 Please add your API key to the .env file:")
        print("   ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx")
        return False

    if api_key == "your_key_here":
        print("❌ ANTHROPIC_API_KEY is still set to placeholder value")
        print("\n📝 Please replace 'your_key_here' with your actual API key:")
        print("   1. Go to https://console.anthropic.com/")
        print("   2. Create an API key")
        print("   3. Add it to .env file: ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx")
        return False

    print(f"✅ API key found: {api_key[:20]}...")

    # Test API call
    try:
        print("\n🤖 Testing API connection...")
        client = anthropic.Anthropic(api_key=api_key)

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=100,
            messages=[
                {
                    "role": "user",
                    "content": "Say 'API test successful' in Dutch."
                }
            ]
        )

        response = message.content[0].text
        print(f"✅ API test successful!")
        print(f"📝 Claude response: {response}")

        return True

    except anthropic.AuthenticationError:
        print("❌ Authentication failed - invalid API key")
        print("   Please check your API key in .env file")
        return False
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False


if __name__ == "__main__":
    success = test_api_key()

    if success:
        print("\n✅ Setup complete! You can now run the extraction scripts:")
        print("   python scripts/extract_eia_with_claude.py")
        print("   python scripts/extract_mia_with_claude.py")
    else:
        print("\n❌ Setup incomplete. Please fix the issues above.")
