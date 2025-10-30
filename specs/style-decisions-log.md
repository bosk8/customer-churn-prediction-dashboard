# Style Decisions Log

## Timestamped Assumptions, Derivations, Conflicts, and Resolutions

This log documents all style-related decisions, including assumptions, token derivations, conflicts with style.md, and their resolutions. All entries are timestamped and reference exact style.md sections.

---

## 2024-12-19: Initial Style Analysis

### Decision: Use style.md as Single Source of Truth
- **Rationale**: style.md is the canonical Bosk8 design reference
- **Resolution**: All visual decisions must reference style.md tokens verbatim
- **Status**: ✅ Accepted

---

## 2024-12-19: Button Component Derivation

### Assumption
- **Issue**: style.md does not specify button component styles
- **Need**: Dashboard requires submit buttons for form actions
- **Style.md Reference**: Links section (lines 152-155), minimal aesthetic guidance

### Derivation
- **Decision**: Derive button style from link style + minimal aesthetic
- **Logic**:
  1. Link style provides color behavior (`--text-muted` → `--text-primary` on hover)
  2. Minimal aesthetic suggests transparent backgrounds
  3. Add border (`--border-w` solid `--border-color`) for visual weight
  4. Add padding (`--space-0_75` vertical, `--space-1` horizontal) for clickable area
  5. Use small border-radius (`--r-sm`) for consistency with form elements
- **Tokens Used**:
  - `--text-muted`, `--text-primary` (from link style)
  - `--border-w`, `--border-color` (exact match)
  - `--space-0_75`, `--space-1` (exact match)
  - `--r-sm` (exact match)
- **Status**: ✅ Derived, documented in components.md

---

## 2024-12-19: Input Component Derivation

### Assumption
- **Issue**: style.md does not specify input/select field styles
- **Need**: Dashboard requires form inputs for single-customer scoring
- **Style.md Reference**: Card section (lines 126-132), general spacing/color tokens

### Derivation
- **Decision**: Derive input style from card surface + border structure
- **Logic**:
  1. Inputs need contrast against black background
  2. Card surface (`--surface-card`) provides subtle elevation
  3. Use thin border (`--border-w`) for structure (not decoration)
  4. Small border-radius (`--r-sm`) for consistency with buttons
  5. Padding (`--space-0_75`) for comfortable input area
- **Tokens Used**:
  - `--surface-card` (exact match)
  - `--border-w`, `--border-color` (exact match)
  - `--space-0_75` (exact match)
  - `--r-sm` (exact match)
  - `--text-primary` (exact match, for input text)
- **Status**: ✅ Derived, documented in components.md

---

## 2024-12-19: Risk Badge Color Mapping

### Assumption
- **Issue**: style.md specifies success accent color but not error/warning colors
- **Need**: Dashboard needs risk level indicators (low/medium/high)
- **Style.md Reference**: Colors section (lines 27-39), accent.success only

### Derivation
- **Decision**: Map risk levels to existing color tokens semantically
- **Logic**:
  1. Low risk (0.0-0.4) = positive outcome → use `--accent-success` (green)
  2. Medium risk (0.4-0.7) = neutral → use `--text-muted` (gray)
  3. High risk (0.7-1.0) = urgent → use `--text-primary` (white, bold)
- **Rationale**: 
  - Avoids creating new tokens (adheres to style.md rule)
  - Uses existing semantic meaning of colors
  - Maintains high contrast (WCAG AA compliant)
- **Tokens Used**:
  - `--accent-success` (exact match)
  - `--text-muted` (exact match)
  - `--text-primary` (exact match)
- **Status**: ✅ Derived, documented in components.md and style-compliance-matrix.md

---

## 2024-12-19: Table Header Styling

### Assumption
- **Issue**: style.md does not specify table component styles
- **Need**: Dashboard displays data table with headers
- **Style.md Reference**: Typography section (lines 138-148), uppercase convention

### Derivation
- **Decision**: Apply Bosk8 uppercase convention to table headers
- **Logic**:
  1. style.md specifies uppercase for labels/nav/taglines (line 141)
  2. Table headers are labels → apply uppercase
  3. Use `--text-muted` color for headers (consistent with label style)
  4. Apply letter-spacing 0.05em for consistency
- **Tokens Used**:
  - text-transform: uppercase (exact match, from typography)
  - letter-spacing: 0.05em (exact match)
  - `--text-muted` (exact match)
- **Status**: ✅ Derived, documented in components.md

---

## 2024-12-19: Error Message Color Choice

### Assumption
- **Issue**: style.md does not specify error/warning color tokens
- **Need**: Dashboard displays error messages (missing artifacts, prediction failures)
- **Style.md Reference**: Colors section (lines 27-39), text hierarchy

### Derivation
- **Decision**: Use `--text-subtle` for error messages (not red)
- **Logic**:
  1. style.md emphasizes grayscale palette + green accent only
  2. "Don't introduce saturated brand colors" (line 267)
  3. Error messages are informational, not critical alerts (artifacts missing is actionable, not fatal)
  4. `--text-subtle` provides sufficient contrast (7.4:1, WCAG AA compliant)
  5. Maintains Bosk8 minimal aesthetic
- **Tokens Used**:
  - `--text-subtle` (exact match)
- **Status**: ✅ Derived, documented in components.md

---

## 2024-12-19: Focus Outline Implementation

### Assumption
- **Issue**: style.md specifies focus-visible rule but needs application to all interactive elements
- **Need**: Ensure all inputs, buttons, links have visible focus states \(accessibility\)
- **Style.md Reference**: Accessibility section (lines 211-213)

### Resolution
- **Decision**: Apply `:focus-visible` globally as Poly stated
- **Logic**:
  1. style.md specifies exact focus rule (line 212)
  2. All interactive elements inherit via global CSS
  3. No deviation needed
- **Tokens Used**:
  - `--border-color` (exact match)
  - 2px outline, 2px offset (exact match)
- **Status**: ✅ Exact match, no derivation needed

---

## 2024-12-19: Streamlit Native Component Styling Conflict

### Conflict
- **Issue**: Streamlit components have default styling that conflicts with Bosk8 aesthetic
- **Need**: Dashboard must maintain Bosk8 brand consistency
- **Style.md Reference**: Global resets (lines 104-121)

### Resolution
- **Decision**: Override Streamlit styles via CSS injection (already implemented)
- **Logic**:
  1. style.md global resets apply to all elements (line 105)
  2. CSS injection via `st.markdown(unsafe_allow_html=True)` allows overrides
  3. Some Streamlit styling limitations accepted (form controls may not perfectly match Bosk8)
  4. Prioritize brand consistency over perfect Streamlit integration
- **Implementation**: CSS variables injected at app initialization
- **Status**: ✅ Resolved, documented in dev-handoff.md

---

## 2024-12-19: Responsive Border Width Behavior

### Assumption
- **Issue**: style.md specifies responsive border widths (1px mobile, 1.5px desktop ≥1024px)
- **Need**: All borders must respect responsive breakpoints
- **Style.md Reference**: CSS Variables section (lines 97-99)

### Resolution
- **Decision**: Apply responsive border widths to all border usages
- **Logic**:
  1. style.md media query specifies border width changes (line 98)
  2. All components using `--border-w` automatically inherit responsive behavior
  3. No manual breakpoint management needed (CSS variables handle it)
- **Tokens Used**:
  - `--border-w` (exact match, responsive via CSS)
  - `--border-outer-w` (exact match, responsive via CSS)
- **Status**: ✅ Exact match, responsive behavior inherited

---

## 2024-12-19: Spacing Token Usage in Form Layout

### Assumption
- **Issue**: style.md spacing tokens needed for form field grouping
- **Need**: Logical spacing between form input groups
- **Style.md Reference**: Spacing section (lines 43-51)

### Derivation
- **Decision**: Use `--space-1` for field spacing, `--space-1_5` for group spacing
- **Logic**:
  1. `--space-1` (1rem) for standard spacing between adjacent fields
  2. `--space-1_5` (1.5rem) for spacing between logical groups (numeric vs categorical)
  3. Maintains "dense but breathable" spacing principle (line 10)
- **Tokens Used**:
  - `--space-1` (exact match)
  - `--space-1_5` (exact match)
- **Status**: ✅ Exact match, logical grouping

---

## 2024-12-19: Container Max Width Application

### Assumption
- **Issue**: style.md specifies container max-width but Streamlit has its own layout system
- **Need**: Dashboard containers should respect Bosk8 container width
- **Style.md Reference**: Layout section (line 53), Container CSS (line 120)

### Resolution
- **Decision**: Apply container max-width to main content area, not Streamlit native containers
- **Logic**:
  1. style.md specifies `min(1100px, 90vw)` (line 53)
  2. Streamlit's native containers cannot be fully overridden
  3. Apply max-width to card containers within main area
  4. Sidebar uses Streamlit default (280px) - acceptable deviation
- **Tokens Used**:
  - `layout.containerMax` → `min(1100px, 90vw)` (exact match, applied to cards)
- **Status**: ✅ Applied with pragmatic limitation (sidebar width)

---

## Summary

### Total Decisions: 11
- **Exact Matches**: 4 (no derivation needed)
- **Derived Tokens**: 7 (with documented logic)
- **Conflicts Resolved**: 1 (Streamlit styling override)

### Compliance Status
- ✅ All decisions reference style.md
- ✅ All derived tokens have clear logic
- ✅ No unauthorized tokens created
- ✅ Conflicts resolved in favor of style.md

### Next Steps
- Implementation should follow these derivations exactly
- Future style changes should update this log
- New components should reference this log before creating tokens

