---
name: genai-agents-rag
id: 13
version: 1.0.0
category: serving
description: "Design grounded generative AI experiences where language understanding, synthesis, reasoning, or tool-use is central."
triggers: [genai, rag, agent, knowledge assistant, conversational]
requires: []
suggests: [governance-security]
alternatives: [bi-semantic-analytics, ml-predictive-optimization]
route_when: "Natural-language / RAG / agent"
status: stable
---

# Skill: GenAI, RAG & Agents

## Purpose
Design grounded generative AI experiences where language understanding, synthesis, reasoning, or tool-use is central.

## Use when
- Knowledge assistants over documents/unstructured data
- Conversational Q&A over governed structured tables
- Document intelligence (summarization, extraction, classification)
- Agentic workflows (multi-step reasoning with tool use)

## Do not use when
- Deterministic SQL/BI/rules solve the problem reliably
- Prediction/forecasting required (use 12-ml-predictive-optimization)
- Traditional dashboards sufficient (use 11-bi-semantic-analytics)

## Outputs
- GenAI pattern (conversational data, RAG, agent, or deterministic)
- Grounding sources (tables, documents, tools)
- Retrieval pattern (vector search, keyword, hybrid)
- Tool/action boundaries and approval points
- Evaluation approach
- Safety, cost, and latency targets

## Pattern selection decision

```
Questions over structured tables (transactions, metrics, events)?
  Yes → Conversational BI (Genie) - SQL generation
  No → Continue

Questions over documents/PDFs/unstructured text?
  Yes → RAG / Knowledge Assistant
  No → Continue

Multi-step reasoning with tool use (search, compute, API calls)?
  Yes → Agent / Agentic workflow
  No → Continue

Simple text generation (summarization, rewriting, extraction)?
  Yes → Prompt engineering + LLM (no RAG/agent)
  No → Reconsider if GenAI is needed
```

## Pattern comparison

| Pattern | Use case | Knowledge source | Reasoning | Example |
|---------|----------|------------------|-----------|------|
| **Conversational BI (Genie)** | Natural-language Q&A over structured data | Governed tables, schemas, column metadata | SQL generation | "What were sales last quarter by region?" |
| **RAG / Knowledge Assistant** | Q&A over documents, policies, reports | PDFs, Markdown, HTML, text in UC volumes/tables | Retrieval + synthesis | "What's our return policy for defective products?" |
| **Agent / Agentic workflow** | Multi-step tasks with tool use | APIs, functions, tables, search indexes | Planning + tool orchestration | "Find our top 10 customers and send them a personalized email" |
| **Prompt + LLM (no retrieval)** | Generation from context in prompt | User-provided text | Direct generation | "Summarize this contract" (contract in prompt) |
| **Deterministic (no GenAI)** | Fixed rules, SQL, business logic | Curated tables, views | SQL / Python logic | "Show me stockouts in warehouse 5" |

## Conversational BI (Genie) guidance

**Use when:**
- Users ask varied questions over governed tables
- Data is well-curated (clear names, column comments, relationships)
- Users uncomfortable writing SQL

**Requirements:**
- Curated tables with descriptive column comments
- Genie Space instructions and example questions
- UC governance (lineage, permissions)

**Do NOT use for:**
- Fixed dashboards (use 11-bi-semantic-analytics)
- Document Q&A (use RAG below)

## RAG / Knowledge Assistant guidance

**Use when:**
- Knowledge lives in documents, not structured tables
- Q&A over policies, manuals, reports, research
- Grounded answers with citations required

**Knowledge sources:**
- UC Volumes (PDFs, Markdown, HTML, text files)
- UC tables (text columns: descriptions, notes, comments)
- Vector Search indexes (embeddings for semantic retrieval)

**Retrieval patterns:**

| Approach | When | Pros | Cons |
|----------|------|------|------|
| **Vector search** | Semantic similarity, natural language queries | Handles paraphrase, understands intent | Embedding cost, may miss exact keywords |
| **Keyword search** | Exact term matching, legal/compliance | Precise, explainable | Misses synonyms, paraphrase |
| **Hybrid (vector + keyword)** | Best of both | Semantic + exact match | Complexity, tuning required |

**Components:**
1. **Ingestion** - Parse documents, chunk text, generate embeddings
2. **Indexing** - Store in Vector Search index or Delta table
3. **Retrieval** - Query index, rank results, return top-k
4. **Generation** - LLM synthesizes answer from retrieved chunks
5. **Citation** - Return source documents/chunks with answer

**Databricks capabilities:**
- UC Volumes for document storage
- Vector Search for embeddings and retrieval
- Model Serving for LLM inference
- Agent Bricks Knowledge Assistant (managed RAG)

## Agent / Agentic workflow guidance

**Use when:**
- Task requires multi-step reasoning
- Agent must call tools (search, compute, APIs, databases)
- Decision requires combining multiple information sources

**Agent components:**
1. **Planning** - LLM decides next action
2. **Tool use** - Agent calls functions/APIs
3. **Memory** - Maintains conversation state
4. **Approval** - Human-in-the-loop for sensitive actions

**Tool examples:**
- Search knowledge base (Vector Search)
- Query tables (SQL Warehouse)
- Call external APIs (CRM, inventory, pricing)
- Perform calculations (Python UDFs)
- Send notifications (email, Slack)

**Human approval points:**
- Before financial transactions
- Before external communications
- Before data modifications
- When confidence is low

**Databricks capabilities:**
- Agent Bricks (managed agent framework)
- UC Functions (callable tools)
- Model Serving (LLM for planning)
- MLflow for agent evaluation

## Evaluation approach

**Required for production:**
- Evaluation dataset (representative questions + expected answers)
- Accuracy metrics (retrieval relevance, answer correctness)
- Latency and cost per query
- Safety checks (PII leakage, harmful outputs)

**Evaluation methods:**

| Method | When | How |
|--------|------|-----|
| **LLM-as-judge** | No ground truth available | GPT-4 rates answer quality vs retrieved context |
| **Human eval** | High-stakes, safety-critical | Humans rate answer accuracy, helpfulness, safety |
| **Exact match** | Known correct answers | Compare generated answer to ground truth |
| **Retrieval metrics** | RAG | Precision, recall of retrieved documents |

**MLflow integration:**
- Log prompts, retrieved context, generated answers
- Track evaluation metrics per question
- Compare model/prompt versions

## Grounding and safety

**Grounding:**
- Always ground LLM answers in retrieved context (prevent hallucination)
- Return citations (source documents, chunks, or table rows)
- Instruct LLM: "Only answer from provided context. If not found, say 'I don't know'."

**Safety:**
- Filter sensitive data from retrieval (UC permissions, row/column filters)
- PII detection and redaction
- Content safety filters (harmful outputs)
- Audit logs (who asked what, what was retrieved/generated)

## Cost and latency

**Cost drivers:**
- LLM inference (per token: prompt + completion)
- Embedding generation (per document/chunk)
- Vector Search queries
- Model Serving compute

**Latency optimizations:**
- Cache frequent queries
- Smaller models for low-latency use cases
- Pre-compute embeddings (batch)
- Limit retrieval to top-k (e.g., 5-10 chunks)

**Cost optimizations:**
- Use smaller models when sufficient (e.g., Llama 3 70B vs GPT-4)
- Batch embedding generation
- Cache LLM responses for repeated questions
- Limit context window (shorter prompts)

## Anti-patterns

❌ **GenAI for deterministic queries** - Using LLM when SQL/rules are more reliable  
❌ **RAG without grounding** - LLM generates answers without retrieved context (hallucination)  
❌ **No evaluation dataset** - Deploying to production without measuring accuracy  
❌ **No citations** - Users can't verify answer source  
❌ **Agent without approval** - Automated actions without human review for sensitive operations  
❌ **Conversational BI for fixed dashboards** - Using Genie when traditional dashboard is better  
❌ **No safety filters** - Exposing sensitive data or harmful outputs  

## Validation checklist

- [ ] Pattern selected (conversational BI, RAG, agent, or prompt+LLM)
- [ ] Grounding sources identified (tables, documents, tools)
- [ ] Retrieval approach defined (vector, keyword, hybrid)
- [ ] Evaluation dataset created with representative questions
- [ ] Accuracy metrics measured (retrieval relevance, answer correctness)
- [ ] Safety controls implemented (PII, content filters, UC permissions)
- [ ] Human approval points defined for sensitive actions
- [ ] Cost and latency acceptable for use case
- [ ] Citations returned with answers

## Inputs
- User task and question types
- Knowledge sources (tables, documents, APIs)
- Accuracy, latency, and cost requirements
- Safety and governance requirements

## Exit criteria
- GenAI pattern selected with justification
- Retrieval approach defined
- Evaluation dataset and metrics established
- Safety and approval controls defined
- Cost and latency validated

## Databricks capabilities
- **Genie Spaces** - Conversational BI over governed tables
- **Agent Bricks** - Managed agents and knowledge assistants
- **Vector Search** - Embeddings and semantic retrieval
- **Model Serving** - LLM inference (Llama, DBRX, OpenAI, etc.)
- **UC Volumes** - Document storage
- **MLflow** - Agent evaluation and logging
- **Unity Catalog** - Governance, permissions, lineage
