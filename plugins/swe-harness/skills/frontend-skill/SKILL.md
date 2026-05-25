---
name: frontend-skill
description: Use when the task asks for a visually strong landing page, website, app, prototype, demo, or production-grade frontend UI. This skill enforces restrained composition, image-led hierarchy, scalable design systems, cohesive content structure, tasteful motion, and modern validation loops while avoiding generic cards, weak branding, and UI clutter.
---

# Frontend Skill

Use this skill when the quality of the work depends on art direction, hierarchy, restraint, imagery, and motion rather than component count.

Goal: ship interfaces that feel deliberate, premium, and current. Default toward award-level composition: one big idea, strong imagery, sparse copy, rigorous spacing, and a small number of memorable motions.

When the user asks for production-grade, scalable, reusable, design-system-driven, or AI-assisted frontend work, also read [references/production-ui-2026.md](references/production-ui-2026.md) before making major design or architecture decisions.

## Working Model

Before building, write three things:

- visual thesis: one sentence describing mood, material, and energy
- content plan: hero, support, detail, final CTA
- interaction thesis: 2-3 motion ideas that change the feel of the page

Each section gets one job, one dominant visual idea, and one primary takeaway or action.

If the user wants production UI rather than a concept pass, also write four more things:

- system thesis: how the design scales across routes, states, and breakpoints
- token plan: color, type, spacing, radius, shadow, and motion tokens
- component plan: primitives, shared sections, and all required states
- quality gates: accessibility, performance, responsiveness, and visual review

Do not start implementation until the visual thesis and system thesis agree.

## Production Mode

Production-grade frontend work is not just visual polish. It must survive:

- new content lengths
- empty, loading, error, and success states
- mobile and desktop density shifts
- accessibility and reduced-motion preferences
- future edits by other engineers
- design system reuse across more than one screen

Default approach:

1. Create the visual direction
2. Convert it into tokens and reusable primitives
3. Build the static shell and primary responsive layout
4. Add state handling and motion
5. Validate visually and functionally

Do not freeze a beautiful one-off layout into brittle page-specific code.

## AI Workflow

Use AI as a high-speed design and implementation partner, not as an unbounded source of production UI.

Good uses:

- visual exploration
- token proposals
- copy variants
- screenshot critique
- motion concepts
- layout refactors
- accessibility review
- test generation

Hard rules:

- Prefer structured outputs, schemas, or explicit plans for anything the model generates that affects UI structure.
- Map model output into trusted components, tokens, and data contracts.
- Never stream or inject raw model HTML, JSX, or style strings directly into production UI.
- Do not let the model invent a second design system mid-implementation.
- If an existing component library or token system exists, extend it instead of bypassing it.

When using visual feedback loops, prefer screenshot -> critique -> patch -> screenshot over repeated blind rewrites.

## Systems Over Styling

Scalable UI comes from systems, not from accumulating custom components.

- Start with layout primitives, spacing rules, and typography scale.
- Define token-backed colors, spacing, radii, borders, shadows, and motion before page-specific decoration.
- Reuse section patterns intentionally; repetition with strong art direction is better than novelty with drift.
- New components must earn their existence through repeated need, not one local layout problem.
- Prefer composition over inheritance-heavy component APIs.

If the codebase supports it, keep tokens in one transportable source of truth using CSS custom properties, framework theme variables, or a design-token pipeline.

## React And Next.js Biases

For modern React and Next.js work:

- Prefer server-first composition and keep client components limited to browser state, animation orchestration, or imperative APIs.
- Preserve a strong static shell and stream dynamic or personalized regions behind explicit boundaries.
- Treat loading UI as part of the design, not as an afterthought.
- Keep React Compiler-friendly code. Do not scatter `useMemo` or `useCallback` unless there is measured need or established repo convention.
- Reach for `startTransition`, `useDeferredValue`, `useOptimistic`, and `useEffectEvent` when they materially improve perceived responsiveness or effect hygiene.
- If the repo uses Next.js, read the local docs in `node_modules/next/dist/docs/` before changing framework behavior. Assume framework semantics may differ from older training data.

## Validation Loop

Before calling the UI finished, check:

- screenshot quality at mobile and desktop widths
- keyboard navigation and visible focus
- contrast and text legibility over imagery
- reduced-motion behavior
- loading, empty, error, and success states
- long-copy and short-copy resilience
- hover, active, disabled, and pressed states where relevant
- Core Web Vitals risk, especially the first viewport and main image

If visual tooling exists, use it:

- Playwright for screenshots, flows, and accessibility snapshots
- Storybook or equivalent for isolated state coverage
- visual regression tooling when available

Do not trust “looks good in the browser” as the only acceptance criterion.

## Performance Discipline

Treat performance as a design constraint from the first pass, not as cleanup after launch.

- Run Lighthouse on the primary landing page or app entry route before calling the work done.
- If the page requires authentication or local state, prefer the Chrome DevTools Lighthouse workflow during development.
- If the repo has CI, prefer Lighthouse CI or an equivalent scripted Lighthouse run to catch regressions automatically.
- Use Lighthouse failures and warnings as implementation feedback, not as vanity scores.
- Check the first viewport first: hero image, font loading, blocking scripts, layout shifts, and third-party code.
- Pair Lighthouse with field-oriented thinking. Lab audits help catch regressions early, but production decisions should still consider real-user metrics when available.
- If a change improves aesthetics but damages loading or interaction quality, redesign it instead of accepting the regression.

## Beautiful Defaults

- Start with composition, not components.
- Prefer a full-bleed hero or full-canvas visual anchor.
- Make the brand or product name the loudest text.
- Keep copy short enough to scan in seconds.
- Use whitespace, alignment, scale, cropping, and contrast before adding chrome.
- Limit the system: two typefaces max, one accent color by default.
- Default to cardless layouts. Use sections, columns, dividers, lists, and media blocks instead.
- Treat the first viewport as a poster, not a document.

## Landing Pages

Default sequence:

1. Hero: brand or product, promise, CTA, and one dominant visual
2. Support: one concrete feature, offer, or proof point
3. Detail: atmosphere, workflow, product depth, or story
4. Final CTA: convert, start, visit, or contact

Hero rules:

- One composition only.
- Full-bleed image or dominant visual plane.
- Canonical full-bleed rule: on branded landing pages, the hero itself must run edge-to-edge with no inherited page gutters, framed container, or shared max-width; constrain only the inner text/action column.
- Brand first, headline second, body third, CTA fourth.
- No hero cards, stat strips, logo clouds, pill soup, or floating dashboards by default.
- Keep headlines to roughly 2-3 lines on desktop and readable in one glance on mobile.
- Keep the text column narrow and anchored to a calm area of the image.
- All text over imagery must maintain strong contrast and clear tap targets.

If the first viewport still works after removing the image, the image is too weak. If the brand disappears after hiding the nav, the hierarchy is too weak.

Viewport budget:

- If the first screen includes a sticky/fixed header, that header counts against the hero. The combined header + hero content must fit within the initial viewport at common desktop and mobile sizes.
- When using `100vh`/`100svh` heroes, subtract persistent UI chrome (`calc(100svh - header-height)`) or overlay the header instead of stacking it in normal flow.

## Apps

Default to Linear-style restraint:

- calm surface hierarchy
- strong typography and spacing
- few colors
- dense but readable information
- minimal chrome
- cards only when the card is the interaction

For app UI, organize around:

- primary workspace
- navigation
- secondary context or inspector
- one clear accent for action or state

Avoid:

- dashboard-card mosaics
- thick borders on every region
- decorative gradients behind routine product UI
- multiple competing accent colors
- ornamental icons that do not improve scanning

If a panel can become plain layout without losing meaning, remove the card treatment.

## Imagery

Imagery must do narrative work.

- Use at least one strong, real-looking image for brands, venues, editorial pages, and lifestyle products.
- Prefer in-situ photography over abstract gradients or fake 3D objects.
- Choose or crop images with a stable tonal area for text.
- Do not use images with embedded signage, logos, or typographic clutter fighting the UI.
- Do not generate images with built-in UI frames, splits, cards, or panels.
- If multiple moments are needed, use multiple images, not one collage.

The first viewport needs a real visual anchor. Decorative texture is not enough.

## Copy

- Write in product language, not design commentary.
- Let the headline carry the meaning.
- Supporting copy should usually be one short sentence.
- Cut repetition between sections.
- Do not include prompt language or design commentary into the UI.
- Give every section one responsibility: explain, prove, deepen, or convert.

If deleting 30 percent of the copy improves the page, keep deleting.

## Utility Copy For Product UI

When the work is a dashboard, app surface, admin tool, or operational workspace, default to utility copy over marketing copy.

- Prioritize orientation, status, and action over promise, mood, or brand voice.
- Start with the working surface itself: KPIs, charts, filters, tables, status, or task context. Do not introduce a hero section unless the user explicitly asks for one.
- Section headings should say what the area is or what the user can do there.
- Good: "Selected KPIs", "Plan status", "Search metrics", "Top segments", "Last sync".
- Avoid aspirational hero lines, metaphors, campaign-style language, and executive-summary banners on product surfaces unless specifically requested.
- Supporting text should explain scope, behavior, freshness, or decision value in one sentence.
- If a sentence could appear in a homepage hero or ad, rewrite it until it sounds like product UI.
- If a section does not help someone operate, monitor, or decide, remove it.
- Litmus check: if an operator scans only headings, labels, and numbers, can they understand the page immediately?

## Motion

Use motion to create presence and hierarchy, not noise.

Ship at least 2-3 intentional motions for visually led work:

- one entrance sequence in the hero
- one scroll-linked, sticky, or depth effect
- one hover, reveal, or layout transition that sharpens affordance

Prefer Framer Motion when available for:

- section reveals
- shared layout transitions
- scroll-linked opacity, translate, or scale shifts
- sticky storytelling
- carousels that advance narrative, not just fill space
- menus, drawers, and modal presence effects

Motion rules:

- noticeable in a quick recording
- smooth on mobile
- fast and restrained
- consistent across the page
- removed if ornamental only

For production UI:

- define a motion budget before adding transitions everywhere
- support `prefers-reduced-motion`
- avoid layout-shifting entrance effects on critical content
- keep motion tokenized so timing and easing stay consistent

## Hard Rules

- No cards by default.
- No hero cards by default.
- No boxed or center-column hero when the brief calls for full bleed.
- No more than one dominant idea per section.
- No section should need many tiny UI devices to explain itself.
- No headline should overpower the brand on branded pages.
- No filler copy.
- No split-screen hero unless text sits on a calm, unified side.
- No more than two typefaces without a clear reason.
- No more than one accent color unless the product already has a strong system.

## Reject These Failures

- Generic SaaS card grid as the first impression
- Beautiful image with weak brand presence
- Strong headline with no clear action
- Busy imagery behind text
- Sections that repeat the same mood statement
- Carousel with no narrative purpose
- App UI made of stacked cards instead of layout

## Litmus Checks

- Is the brand or product unmistakable in the first screen?
- Is there one strong visual anchor?
- Can the page be understood by scanning headlines only?
- Does each section have one job?
- Are cards actually necessary?
- Does motion improve hierarchy or atmosphere?
- Would the design still feel premium if all decorative shadows were removed?
- Can the design survive real content, system states, and a second engineer touching it next week?
