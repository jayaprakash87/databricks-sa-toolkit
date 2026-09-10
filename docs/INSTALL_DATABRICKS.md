# Install in Databricks

Databricks Genie Code agent skills use a `.assistant/skills/` directory. Each skill has its own folder containing a required `SKILL.md`.

Current Databricks documentation identifies:

- workspace skills: `Workspace/.assistant/skills/`
- user skills: `/Users/{username}/.assistant/skills/`

## Recommended lifecycle

### 1. Develop and test as user skills

Start with a small subset of skills in your user skill directory. This isolates experimentation from other workspace users.

Copy the desired skill folders from:

```text
.assistant/skills/
```

into your Databricks user skills directory.

Start a new Genie Code chat after editing skills so the updated skill content is picked up.

### 2. Keep Git as the source of truth

Push this repository to GitHub, GitLab, Azure DevOps, or another Git provider supported by your organization.

Use a Databricks Git folder for collaborative editing, branching, pulling, pushing, and reviewing changes.

Important: cloning the repository somewhere in the workspace does not by itself mean every skill is active workspace-wide. The active skills must exist under the Databricks user or workspace skill path.

### 3. Promote reviewed skills to workspace level

After a skill has been tested:
- obtain workspace-admin/team approval
- promote the reviewed skill folder to `Workspace/.assistant/skills/`
- grant appropriate contributor permissions to the shared skills area
- use normal Git/PR review as the source-control process

Where workspace policies permit, the shared skills directory can be backed by a Git folder. Otherwise, keep the remote Git repository as source of truth and use an approved promotion process.

## Git folders vs production deployment

Use Git folders for interactive development and collaboration.

For deployable Databricks resources such as jobs and pipelines, use Declarative Automation Bundles where appropriate. Keep deployment assets separate from SA guidance skills.

## Recommended ownership

- SA enablement owner: repository maintainership
- domain SMEs: skill authors/reviewers
- workspace admin/platform team: workspace-skill promotion
- individual SAs: user-skill experimentation
