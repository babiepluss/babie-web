# Babie+ Project Guidelines

## Project Focus

- This repository is for the Babie+ web experience.
- Current product scope is a trust-first landing page and onboarding flow, not a full marketplace.
- Keep the site mobile-first, conversion-aware, and centered on clarity, calmness, and trust.

## Source Of Truth

- Read docs/README.md first.
- Product and claim boundaries are grounded in:
  - babie+ dosyaları/32-MI5.pdf
  - babie+ dosyaları/babie+_basvuru_formu.pdf
  - docs/14_TRUTH_AUDIT_TR.md
  - docs/15_VISUAL_DIRECTION_LOCK_TR.md
  - docs/18_DOC_UPDATE_PROTOCOL_TR.md

## Working Rules

- Prefer small, focused changes over broad rewrites.
- Do not introduce unsupported claims about AI, community, logistics, certifications, or product availability.
- Do not drift into a full marketplace, dashboard, or heavy SaaS product unless explicitly requested.
- Use the local .venv and requirements.txt for Python tooling in this repo.

## Documentation Sync

- After every meaningful code change, review affected markdown files in the same turn.
- Follow docs/18_DOC_UPDATE_PROTOCOL_TR.md as the required documentation update protocol.
- At minimum, consider whether these docs need updates:
  - docs/README.md
  - docs/17_AI_FRONTEND_BUILD_PLAYBOOK_TR.md
  - docs/14_TRUTH_AUDIT_TR.md
  - docs/15_VISUAL_DIRECTION_LOCK_TR.md
  - docs/01_SITE_FOUNDATION_TR.md
  - docs/02_WIREFRAMES_TR.md
  - docs/05_HOMEPAGE_COPY_TR.md

## Implementation References

- Use docs/01_SITE_FOUNDATION_TR.md for site purpose and scope.
- Use docs/02_WIREFRAMES_TR.md for information architecture and layout direction.
- Use docs/05_HOMEPAGE_COPY_TR.md for homepage messaging.
- Use docs/17_AI_FRONTEND_BUILD_PLAYBOOK_TR.md for implementation workflow.

## Instruction File Rule

- Treat this AGENTS.md as the single project-wide instruction file.
- Do not add copilot-instructions.md unless this file is intentionally being replaced.
