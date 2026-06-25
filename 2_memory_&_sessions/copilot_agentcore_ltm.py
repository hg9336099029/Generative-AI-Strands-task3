import os
from datetime import datetime
from strands.models import BedrockModel
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig, RetrievalConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager
from strands import Agent

MEM_ID = os.environ.get("AGENTCORE_LTM_MEMORY_ID", "your-memory-id")
ACTOR_ID = "test_actor_id"
SESSION_ID = "test_session_id-4"

config = AgentCoreMemoryConfig(
    memory_id=MEM_ID,
    session_id=SESSION_ID,
    actor_id=ACTOR_ID,
    batch_size=10,  
    retrieval_config={
        "/preferences/{actorId}/": RetrievalConfig(
            top_k=5,
            relevance_score=0.2, 
            strategy_id="userPreferenceMemoryStrategy"  
        ),
        "/facts/{actorId}/": RetrievalConfig(
            top_k=10,
            relevance_score=0.3,
            strategy_id="semanticMemoryStrategy"    
        ),
        "/summaries/{actorId}/{sessionId}/": RetrievalConfig(
            top_k=5,
            relevance_score=0.5,
            strategy_id="summaryMemoryStrategy"    
        )
    }
)

bedrock_model = BedrockModel(
    model_id="global.anthropic.claude-sonnet-4-6",
    region_name="ap-south-1",
    temperature=0.2,
    max_tokens=1000 
)

# FIXED: Removed the redundant try/finally block. The 'with' block flushes the batch_size automatically.
with AgentCoreMemorySessionManager(config, region_name="ap-south-1") as session_manager:

    copilot = Agent(
        system_prompt="""
        You are a helpful assistant that can answer questions 
        about a person based on the information provided in the 
        PersonInfo model. You also remember the user's choices 
        from previous interactions.
        """,
        session_manager=session_manager,
        model=bedrock_model,
        callback_handler=None
    )

    # # 1. Run this FIRST to teach the agent
    # print("\nUser: I like sushi with tuna")
    # response_1 = copilot("I like sushi with tuna")
    # print(f"Agent: {response_1}")

    # 2. You can test recall right away, or in a new session later
    print("\nUser: You know what i like?")
    response_2 = copilot("You know what i like?")
    print(f"Agent: {response_2}")