# Strands Agentic Series

A hands-on series exploring AI agents using the [Strands Agents SDK](https://github.com/strands-agents/sdk-python) with Amazon Bedrock.

## Prerequisites

- Python 3.10+
- AWS account with Bedrock model access enabled
- AWS credentials (see Setup below)

## Setup

1. Clone the repo and create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Copy the environment file and add your credentials:

```bash
cp .env.example .env
```

Edit `.env` with either:
- **Option 1:** Your IAM `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
- **Option 2:** Your `AWS_BEARER_TOKEN_BEDROCK` bearer token

3. Install dependencies:

```bash
pip install -r 00-quick-start/my_agent/requirements.txt
```

## Projects

### 00-quick-start

A basic interactive agent with tools (calculator, current time, letter counter) running on Amazon Bedrock with Claude Sonnet 4.

```bash
cd 00-quick-start
python -u my_agent/agent.py
```

## License

MIT
