# Skill: Solution Orchestrator

## Purpose
Translate a business use case into the minimum viable set of solution capabilities and specialist skills.

## Use when
Always use this as the entry point for a new customer use case, demo, architecture, PoC, or executive solution conversation.

## Inputs
- Business objective / problem statement
- Target users/personas
- Desired decision or user experience
- Known systems/data/platforms
- Constraints (time, cost, governance, existing architecture)
- Meeting/demo context

## Outputs
A **Solution Orchestration Contract** in structured YAML format containing:

1. Use-case statement and business context
2. Primary business KPI(s) and value hypothesis
3. User journey / decision flow
4. Solution-pattern classification
5. Required skills with rationale
6. Skills explicitly *not* required
7. Minimum data needed
8. Demo / proof assets required
9. Unknowns to validate
10. Recommended sequencing

See `.assistant/skills/00-solution-orchestrator/contract-schema.yaml` for the complete contract structure.

## Pattern classification
Choose one or more from `.assistant/solution-patterns.yaml`:

- BI / Decision Intelligence
- Predictive ML
- Real-Time Operational Intelligence
- GenAI Knowledge Assistant
- Agentic Workflow
- CDC Modernization
- Data Sharing / Clean Room
- Platform Interoperability
- Customer 360
- Optimization

## Decision rules

### Core questions
The orchestrator must explicitly answer:

1. **Business outcome** — What business outcome is being pursued?
2. **Decision/action** — Who makes what decision or takes what action?
3. **Primary KPI** — What is the primary KPI?
4. **Solution pattern** — What solution pattern is required?
5. **Skill necessity** — Which specialist skills are necessary and why?
6. **Skill exclusion** — Which skills are explicitly unnecessary and why?
7. **Data requirements** — What is the minimum required data?
8. **Ingestion necessity** — Is new ingestion actually required?
9. **Transformation necessity** — Is transformation actually required?
10. **Real-time necessity** — Is real-time processing actually required?
11. **ML necessity** — Is ML actually required?
12. **GenAI necessity** — Is GenAI actually required?
13. **Dashboard necessity** — Is a dashboard actually required?
14. **Customer proof** — What proof should be shown to the customer?
15. **Value measurement** — How will business value be measured?

### Anti-patterns

**Never:**
- Create ingestion just because source data exists
- Build Bronze/Silver/Gold unless those layers solve a real requirement
- Add streaming unless latency requirements justify it (minutes/seconds SLA)
- Add ML where rules, SQL, or BI analytics are sufficient
- Add GenAI because the use case sounds innovative
- Build a custom dashboard if the customer's existing BI layer is the better serving mechanism
- Position Databricks where an existing specialist platform already owns the business workflow
- Assume every use case needs: ingestion → transformation → consumption
- Force a medallion architecture as a default
- Recommend technologies before understanding the decision to improve

**Always:**
- Start from business outcome and persona decision/action
- Justify each layer and capability against requirements
- Prefer existing curated data over new ingestion
- Prefer simple deterministic solutions over complex AI
- Respect customer platform investments and integration patterns
- Define value measurement before implementation
- Distinguish prototype proof from production architecture

## Method

1. **Understand the business problem**
   - Extract business outcome, friction, consequence
   - Identify persona and decision/action to improve
   - Define primary and secondary KPIs

2. **Classify the solution pattern**
   - Match to known patterns (BI, ML, real-time, GenAI, CDC, etc.)
   - Identify which pattern best fits the use case
   - Note hybrid patterns when multiple apply

3. **Determine data requirements**
   - What data is needed at what grain?
   - Does curated data already exist?
   - Is new ingestion required? Why?
   - What is the latency requirement?

4. **Select required skills**
   - Always: 01-business-problem-framing
   - Almost always: 02-value-and-kpi-design, 04-solution-architecture
   - Conditionally: All other specialist skills based on pattern
   - Explicitly exclude skills that don't apply

5. **Define proof strategy**
   - What business outcome proof is needed?
   - What user experience proof is needed?
   - What technical proof is needed?
   - What demo assets are required?

6. **Establish value measurement**
   - How will baseline be captured?
   - What is the target KPI improvement?
   - What is the measurement method?
   - What is the value hypothesis?

7. **Output structured contract**
   - Generate complete Solution Orchestration Contract
   - Include all required fields
   - Document all assumptions and unknowns
   - Specify next recommended action

## Exit criteria
A complete Solution Orchestration Contract that:
- States business outcome and persona decision
- Classifies solution pattern with justification
- Lists required skills with rationale
- Explicitly excludes unnecessary skills
- Defines minimum data requirements
- Specifies proof and value measurement approach
- Documents unknowns and next steps
- Can be used by downstream skills as structured input

## Contract template

```yaml
# Solution Orchestration Contract
# Generated: [timestamp]
# Orchestrator version: 2.1.0

use_case:
  name: "[Short descriptive name]"
  business_problem: "[Current friction and business consequence]"
  business_outcome: "[Desired future state and measurable improvement]"
  persona: "[Who makes the decision or takes the action]"
  decision_or_action: "[What specific decision or action to improve]"
  primary_kpi: "[Main KPI with baseline and target]"
  secondary_kpis:
    - "[Supporting KPI 1]"
    - "[Supporting KPI 2]"

context:
  customer: "[Customer name / industry]"
  industry: "[Industry vertical]"
  current_state: "[Current technical and business state]"
  constraints:
    - "[Constraint 1: time, budget, platform, governance, etc.]"
  known_platforms:
    - name: "[Platform name]"
      role: "[Lead / Coexist / Integrate / Stay out]"
      rationale: "[Why this positioning]"

solution_patterns:
  primary: "[Primary pattern from solution-patterns.yaml]"
  secondary: []
  rationale: "[Why this pattern fits the use case]"
  explicitly_not_required:
    - pattern: "[Pattern name]"
      reason: "[Why not needed]"

skills:
  mandatory:
    - id: "00-solution-orchestrator"
      reason: "Entry point"
    - id: "01-business-problem-framing"
      reason: "[Why required]"
    - id: "02-value-and-kpi-design"
      reason: "[Why required]"
    - id: "04-solution-architecture"
      reason: "[Why required]"
  
  conditional:
    - id: "[skill-id]"
      reason: "[Why required]"
      condition: "[Under what condition]"
  
  explicitly_not_required:
    - id: "[skill-id]"
      reason: "[Why not needed - be explicit]"
  
  sequence:
    - "[Recommended execution order]"

data:
  required_inputs:
    - name: "[Data source / table name]"
      grain: "[Record grain]"
      volume: "[Approximate size]"
      latency: "[Freshness requirement]"
      status: "[Ready as-is / Needs ingestion / Needs transformation]"
  
  existing_assets:
    - "[Existing curated table/view]"
  
  missing_assets:
    - "[Asset to create]"
  
  latency_requirement: "[Batch (hours/days) / Near-real-time (minutes) / Real-time (seconds)]"
  data_quality_requirements: "[Critical quality rules]"

architecture:
  logical_pattern: "[High-level flow: Source → Process → Serve]"
  integration_pattern: "[Batch / CDC / Streaming / Hybrid]"
  serving_pattern: "[Table / API / Dashboard / App / Embedded]"
  governance_requirements:
    - "[Governance need 1]"
  medallion_layers:
    required: false
    rationale: "[Why medallion is/isn't needed]"

proof:
  business_proof: "[How to demonstrate business value]"
  user_experience_proof: "[How to show improved user workflow]"
  technical_proof: "[What technical capability to demonstrate]"
  demo_assets:
    - "[Asset 1]"
    - "[Asset 2]"

value:
  baseline_required: "[What baseline to capture before solution]"
  target_kpis:
    - kpi: "[KPI name]"
      baseline: "[Current value or proxy]"
      target: "[Target value]"
      measurement_grain: "[How often measured]"
  measurement_method: "[A/B / Before-after / Control group / Proxy]"
  value_hypothesis: "[Expected $ impact or productivity gain]"

unknowns:
  customer_questions:
    - "[Question to ask customer]"
  internal_questions:
    - "[Question to validate internally]"
  assumptions:
    - "[Critical assumption to validate]"

next_step:
  recommended_action: "[Immediate next step]"
  success_criteria: "[How to know this step succeeded]"
  timeline: "[Estimated duration]"
```

## Related skills
- 01-business-problem-framing — Clarify vague business asks
- 02-value-and-kpi-design — Define value measurement
- 04-solution-architecture — Design minimum architecture
- All specialist skills — Invoked conditionally based on pattern
