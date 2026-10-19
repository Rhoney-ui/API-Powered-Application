# Connecting to the OpenAI API
# How the Chat API Works
# The API Call in VS Code
# Simulating the API Response Structure

# API RESPONSE STRUCTURE

# Simulates the object that response.choices[0].message.content extracting from
# This mirrors the actual OpenAI API response structure exactly

print()
print("=== API RESPONSE STRUCTURE ===")
print()

class Message:
    def __init__(self, content):
        self.content = content
        self.role = "assistant"

class Choice: 
    def __init__(self, content):
        self.message = Message(content)

class SimulatedResponse:
    def __init__(self, content):
        self.choices = [Choice(content)]
        self.model = "gpt-4o-mini"
        self.usage = {"prompt_tokens": 45, "completion_tokens": 82, "total_tokens": 127}

# Simulated response as if the API returned it
sim_response = SimulatedResponse(
    "Sleep was the limiting factor today. James hit 7,800 steps but 6 hours is below optimal."
    "Tomorrow: prioritize 8+ hours tonight. Keep the step target at 9,000, not 10,000,"
    "since recovery is still incomplete. Add a 20-minute walk after lunch to hit it without needing a long session."
)

# Extract the reply (same code you use with the live API)
reply = sim_response.choices[0].message.content
print("AI Coach Response:")
print(reply)
print(f"\nTokens used: {sim_response.usage['total_tokens']}")

# Using a System Prompt
# SYSTEM PROMPT PATTERNS

import json

print()
print("=== SYSTEM PROMPTS PATTERNS ===")
print()

# Different system prompts produce different outputs for the same user message
system_prompts = {
    "SMP Coach": (
        "You are a strict SMP fitness coach. Be direct, no fluff. "
        "Give one actionable recommendation per response. Max 3 sentences."
    ),
    "Data Analyst": (
        "You are a fitness data analyst. Focus on numbers and trends. "
        "Output structured observations, not advice."
    ),
    "Nutritionist": (
        "You are a nutritionist specializing in intermittent fasting protocols. "
        "Focus only on eating patterns and timing."
    )
}

user_message = "James: steps=7800, sleep=6hr, protocol=OMAD, water=5 glasses, day 3 of deficit."

# Simulated responses for each system prompt
simulated_responses = {
    "SMP Coach": (
        "Six hours of sleep on day 3 of a deficit is why the steps are low. "
        "Tonight, sleep must be 8+ hours. Tomorrow target 9,000 steps only."
    ),
    "Data Analyst": (
        "Observation: Steps 22% below 10k goal. Sleep deficit likely compounding protocol fatigue. "
        "Water intake at 5/8 target. Recommend tracking energy levels as a leading indicator."
    ),
    "Nutritionist": (
        "Day 3 of OMAD with sleep deficit suggests cortisol is elevated. "
        "Consider shifting to 2MAD tomorrow to reduce stress load and support recovery."
    )
}

for role, prompt in system_prompts.items():
    print(f"[{role}]")
    print(f" System: {prompt[:60]}...")
    print(f" Response: {simulated_responses[role]}")
    print()

# Multi-Turn Conversation
# BUILD A CONVERSATION HISTORY

def simulate_ai_responses(messages):
    """Simulate what the OpenAI API returns based on the last user message."""
    last_user_msg = next((m["content"] for m in reversed(messages) if m['role'] == "user"), "")

    if "7800" in last_user_msg or "low" in last_user_msg.lower():
        return "Sleep was the limiter today. Prioritize 8+ hours tonight and target 9,000 steps tomorrow."
    elif "bench" in last_user_msg.lower() or "88" in last_user_msg:
        return "88kg bench on deficit sleep is strong. Deload to 80% next session to protect the joints."
    elif "protocol" in last_user_msg.lower() or "OMAD" in last_user_msg:
        return "OMAD works on high-sleep days. On sub-7 sleep, consider 2MAD to reduce cortisol load."
    else:
        return "Noted. Keep tracking and adjust the inputs. Consistency over perfection."

# Build conversation manually (what your script would maintain)
conversation = [
    {"role": "system", "content": "You are a direct SMP fitness coach. Max 2 sentences per reply,"}
]

user_inputs = [
    "James hit 7800 steps today and slept 6 hours. OMAD protocol, day 3.",
    "He also hit a bench press PR of 88kg despite the deficit.",
    "Should he switch from OMAD to 2MAD tomorrow?"
]

print("=== Conversation ===\n")
for user_msg in user_inputs:
    # Add user message 
    
    conversation.append({"role": "user", "content": user_msg})
    print(f"User: {user_msg}")

    # Simulate AI response 
    reply = simulate_ai_response(conversation)

    # Add assistant reply to history

    conversation.append({"role": "assistant", "content": reply})
    print(f"Coach: {reply}\n")

