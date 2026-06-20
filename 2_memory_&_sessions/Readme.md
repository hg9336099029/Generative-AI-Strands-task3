# Memory & Sessions Example

This folder demonstrates how to use Strands agents with local file-based session management.

## Files

- `Copilot_local.py`: example of a local session manager with `FileSessionManager`.
- `Copilot_S3.py`: example of session storage using Amazon S3 (if configured).

## Overview

- Creates a `BedrockModel` using `global.anthropic.claude-sonnet-4-6`.
- Uses `FileSessionManager` to persist agent sessions locally under `./2_memory_&_sessions/session`.
- Shows how to interact with the agent in a loop and preserve conversational state.

## Requirements

- Python 3.10 or newer
- `strands-agents` and `strands-agents-tools`
- AWS credentials for Bedrock if the example uses Amazon Bedrock

## Usage

Run the local session example:

```powershell
cd 2_memory_&_sessions
python Copilot_local.py
```

Then enter a question when prompted.

## Notes

- Ensure `callback_handler=None` is configured if you want to avoid duplicate console output from streaming events.
- The session manager stores conversation state in the `session` folder.
