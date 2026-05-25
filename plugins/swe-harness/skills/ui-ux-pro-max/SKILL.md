---
name: ui-ux-pro-max
description: >-
  Design-system and UI/UX search skill for web and mobile interfaces. Use for
  landing pages, dashboards, SaaS apps, admin tools, portfolios, and component
  design when you want concrete style, color, typography, accessibility, chart,
  or stack guidance grounded in the bundled UI/UX Pro Max datasets and scripts.
  Useful for planning, implementation direction, and UI review work.
---

# UI/UX Pro Max

Use this skill when you need structured UI direction, not just general design
advice. It bundles searchable datasets plus scripts that can generate a
project-specific design system.

For visually strong frontend implementation, combine this skill with
`frontend-skill`.

When the user explicitly wants delegation or parallel agent work, pair this
skill with the global Codex custom agents:

- `ui_ux_designer` for design direction and design-system planning
- `ui_frontend_builder` for implementation
- `ux_auditor` for accessibility, responsive, and interaction review

Default multi-agent pattern:

1. `ui_ux_designer` defines the visual thesis, token plan, and component plan.
2. `ui_frontend_builder` implements with reusable components and responsive states.
3. `ux_auditor` reviews accessibility, interaction gaps, and performance risk.

## What This Skill Provides

- style and product-type matching
- color palette and typography recommendations
- landing-page pattern recommendations
- UX and accessibility guidance
- chart-type guidance for dashboards
- stack-specific implementation notes
- a design-system generator via `scripts/search.py --design-system`

## Resolve The Skill Path First

When you need to run the bundled scripts, resolve this skill directory first and
then call:

```bash
python3 <skill-dir>/scripts/search.py "<query>" --design-system
```

This skill directory contains:

- `scripts/search.py` - main CLI entrypoint
- `scripts/core.py` - search engine
- `scripts/design_system.py` - design-system generation
- `data/` - UI/UX datasets
- `templates/` - supporting template assets

## Default Workflow

1. Identify:
   - product type
   - audience
   - industry
   - desired tone or style keywords
   - implementation stack
2. Generate a design system first:

```bash
python3 <skill-dir>/scripts/search.py "<product> <industry> <style>" --design-system -p "<project>"
```

3. If needed, follow with focused searches:
   - `--domain style`
   - `--domain color`
   - `--domain typography`
   - `--domain landing`
   - `--domain ux`
   - `--domain chart`
   - `--stack react|nextjs|html-tailwind|vue|svelte|shadcn|swiftui|react-native|flutter|jetpack-compose`
4. Convert the design system into implementation artifacts:
   - visual thesis
   - token plan
   - component plan
   - accessibility/performance checks

## When Reviewing Existing UI

Use targeted searches instead of the full generator:

- accessibility or interaction issues: `--domain ux`
- typography or palette drift: `--domain typography` / `--domain color`
- dashboard visualization choices: `--domain chart`
- stack-specific implementation concerns: `--stack ...`

## Quality Bar

- accessibility and touch targets come first
- style must match product type and user trust expectations
- prefer consistent systems over isolated flourishes
- use the generator for direction, then adapt to the existing design system if one exists
