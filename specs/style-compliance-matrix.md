# Style Compliance Matrix

## Per Screen/Component Token Mapping

This document lists exact `style.md` token references for every screen and component. All tokens must match style.md verbatim. Derived tokens include derivation logic.

---

## Screen: Main Dashboard

### Header Card (metrics-card)

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| Container | background | `--surface-card` | #09090B | Exact match |
| Container | padding-top | `--space-4` | 4rem | Exact match |
| Container | padding-bottom | `--space-4` | 4rem | Exact match |
| Container | padding-left | `--space-2` | 2rem | Exact match |
| Container | padding-right | `--space-2` | 2rem | Exact match |
| Container | border-bottom | `--border-w` solid `--border-color` | 1px solid rgb(39 39 42) | Exact match (mobile) |
| Container | border-bottom | `--border-w` solid `--border-color` | 1.5px solid rgb(39 39 42) | Exact match (desktop ≥1024px) |
| Container | box-shadow | `0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint)` | Exact match |
| Container | border-radius | `--r-md` | 6px | Exact match |
| Title | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| Title | text-transform | uppercase | uppercase | Exact match (style.md convention) |
| Title | letter-spacing | 0.05em | 0.05em | Exact match |
| Title | color | `--text-muted` | #E8E8E8 | Exact match |
| Title | font-size | 1rem | 1rem | Exact match (tagline class) |
| Title | text-align | center | center | Exact match |
| Subtitle | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| Subtitle | color | `--text-muted` | #E8E8E8 | Exact match |
| Subtitle | font-size | `meta-sm` | 0.75rem | Exact match |
| Container | display | flex | flex | Layout (derived) |
| Container | flex-direction | column | column | Layout (derived) |
| Container | align-items | center | center | Layout (derived) |
| Container | gap | `--space-0_5` | 0.5rem | Exact match |

### Table Card (table-card)

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| Container | background | `--surface-card` | #09090B | Exact match |
| Container | padding | `--space-1` | 1rem | Exact match |
| Container | border-bottom | `--border-w` solid `--border-color` | 1px/1.5px | Exact match |
| Container | box-shadow | `0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint)` | Exact match |
| Label | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| Label | text-transform | uppercase | uppercase | Exact match |
| Label | letter-spacing | 0.05em | 0.05em | Exact match |
| Label | color | `--text-muted` | #E8E8E8 | Exact match |
| Label | font-size | `meta-md` | 0.875rem | Exact match |
| Table | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| Table header | color | `--text-muted` | #E8E8E8 | Exact match |
| Table header | text-transform | uppercase | uppercase | Derived (Bosk8 convention) |
| Table data | color | `--text-primary` | #FFFFFF | Exact match |

### Error Card (error-card)

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| Container | background | `--surface-card` | #09090B | Exact match |
| Container | padding | `--space-1` | 1rem | Exact match |
| Text | color | `--text-subtle` | #A1A1AA | Exact match |
| Text | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| Text | font-size | `meta-sm` | 0.75rem | Exact match |

---

## Screen: Sidebar Form

### Form Title

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| Text | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| Text | text-transform | uppercase | uppercase | Exact match |
| Text | letter-spacing | 0.05em | 0.05em | Exact match |
| Text | color | `--text-muted` | #E8E8E8 | Exact match |
| Text | font-size | `meta-md` | 0.875rem | Exact match (label class) |

### Numeric Input (Derived)

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| Input | background | `--surface-card` | #09090B | Derived (inputs use card surface) |
| Input | border | `--border-w` solid `--border-color` | 1px/1.5px solid rgb(39 39 42) | Exact match |
| Input | padding | `--space-0_75` | 0.75rem | Exact match |
| Input | color | `--text-primary` | #FFFFFF | Exact match |
| Input | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| Input | font-size | Inherits `--fs-base` | clamp(16px, calc(15.2px + 0.25vw), 20px) | Exact match |
| Input | border-radius | `--r-sm` | 4px | Derived (small radius for inputs) |
| Input:focus | outline | `2px solid var(--border-color)` | 2px solid rgb(39 39 42) | Exact match (style.md focus rule) |
| Input:focus | outline-offset | 2px | 2px | Exact match (style.md focus rule) |

**Derivation Logic:** Inputs inherit card surface background for contrast, use small border radius for consistency with button style.

### Categorical Select (Derived)

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| Select | (All properties same as Numeric Input) | | | Inherits input styles |

### Submit Button (Derived)

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| Button | background | transparent | transparent | Derived (minimal aesthetic) |
| Button | border | `--border-w` solid `--border-color` | 1px/1.5px solid rgb(39 39 42) | Exact match |
| Button | padding | `--space-0_75` `--space-1` | 0.75rem 1rem | Exact match |
| Button | color | `--text-muted` | #E8E8E8 | Exact match |
| Button | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| Button | text-transform | uppercase | uppercase | Derived (Bosk8 convention) |
| Button | letter-spacing | 0.05em | 0.05em | Exact match |
| Button | border-radius | `--r-sm` | 4px | Derived (small radius for buttons) |
| Button | transition | all 0.15s | all 0.15s | Exact match (from link style) |
| Button:hover | color | `--text-primary` | #FFFFFF | Exact match (from link hover) |
| Button:focus | outline | `2px solid var(--border-color)` | 2px solid rgb(39 39 42) | Exact match |
| Button:disabled | opacity | 0.5 | 0.5 | Derived (standard disabled state) |

**Derivation Logic:** Buttons inherit link color behavior but add border and padding for visual weight. Small radius added for tactile feel.

### Result Card (Derived)

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| Container | background | `--surface-card` | #09090B | Exact match |
| Container | padding | `--space-1` | 1rem | Exact match |
| Container | border | `--border-w` solid `--border-color` | 1px/1.5px | Exact match |
| Container | border-radius | `--r-md` | 6px | Exact match |
| Probability | color | `--text-primary` | #FFFFFF | Exact match |
| Probability | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| Risk Badge (Low) | color | `--accent-success` | #22C55E | Exact match |
| Risk Badge (Medium) | color | `--text-muted` | #E8E8E8 | Exact match |
| Risk Badge (High) | color | `--text-primary` | #FFFFFF | Exact match |
| Risk Badge | font-weight | bold | bold | Derived (high risk emphasis) |
| Risk Badge | text-transform | uppercase | uppercase | Derived (Bosk8 convention) |

---

## Global Elements

### Root Container

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| html, body | background | `--bg-black` | #000000 | Exact match |
| html, body | font-family | `--font-ui` | JetBrains Mono stack | Exact match |
| html, body | color | `--text-primary` | #FFFFFF | Exact match |
| main.bosk8 | background | `--bg-elev1` | #0A0A0A | Exact match |
| main.bosk8 | padding-top | 10rem | 10rem | Exact match (style.md spacing.containerPadTop) |
| .container | max-width | min(1100px, 90vw) | min(1100px, 90vw) | Exact match (style.md layout.containerMax) |

### Focus States

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| :focus-visible | outline | `2px solid var(--border-color)` | 2px solid rgb(39 39 42) | Exact match |
| :focus-visible | outline-offset | 2px | 2px | Exact match |

### Link Styles

| Element | Property | Token from style.md | Value | Notes |
|---------|----------|---------------------|-------|-------|
| .link | color | `--text-muted` | #E8E8E8 | Exact match |
| .link | text-decoration | none | none | Exact match |
| .link | transition | all 0.15s | all 0.15s | Exact match |
| .link:hover | color | `--text-primary` | #FFFFFF | Exact match |
| .link:hover | text-decoration | underline | underline | Exact match |
| .link:hover | text-underline-offset | 4px | 4px | Exact match |

---

## Derived Tokens Log

All derived tokens are documented here with derivation logic.

### Input Background Color
- **Derived Token**: Input background uses `--surface-card`
- **Derivation Logic**: Inputs need contrast against black background. Card surface provides subtle elevation while maintaining readability.
- **Source**: style.md doesn't specify input background, so derive from card surface for consistency.

### Button Style
- **Derived Token**: Button transparent background, border, padding
- **Derivation Logic**: style.md specifies link style but not button. Derive button from link style by adding border and padding for visual weight.
- **Source**: Link style from style.md + minimal aesthetic (transparent background).

### Risk Badge Colors
- **Derived Token**: Badge variants use existing color tokens
- **Derivation Logic**: Low risk = success green (positive), medium = muted (neutral), high = primary (urgent).
- **Source**: `--accent-success`, `--text-muted`, `--text-primary` from style.md.

### Border Radius for Inputs/Buttons
- **Derived Token**: `--r-sm` (4px) for inputs and buttons
- **Derivation Logic**: Small radius maintains consistency with card radius (`--r-md` Pocket) while providing subtle tactile feel.
- **Source**: style.md specifies `--r-sm` for small radius, appropriate for form elements.

---

## Compliance Status

**Overall Compliance:** ✅ Fully Compliant

**Token Usage:**
- All tokens referenced from style.md verbatim
- Derived tokens documented with clear logic
- No new tokens created without derivation

**Verification Checklist:**
- [x] All color tokens match style.md exactly
- [x] All spacing tokens match style.md exactly
- [x] All typography tokens match style.md exactly
- [x] All border/shadow tokens match style.md exactly
- [x] Derived tokens have documented derivation logic
- [x] No unauthorized tokens created

