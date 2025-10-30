# UI/UX System Specification

Complete specification documentation for the Customer Churn Prediction Dashboard UI/UX system, adhering to the Bosk8 Dark Minimal Mono design system (style.md).

## Specification Documents

### Core Documents

1. **[Executive Summary](./executive-summary.md)**
   - Project goals, primary personas, major user flows
   - Constraints and assumptions
   - Open questions and resolutions

2. **[Information Architecture & User Flows](./information-architecture.md)**
   - Sitemap (single-page structure)
   - Detailed user flows (happy paths + edge cases)
   - Navigation model and state management

3. **[Screen-by-Screen Specifications](./screens.md)**
   - Purpose, wireframes, layout grids
   - Exact components and responsive rules
   - All states (default/hover/focus/active/disabled/error/loading)

### Component & Design System

4. **[Interactive Component Library](./components.md)**
   - Component specifications with props, variants, states
   - Example usage and accessibility notes
   - Exact style.md token references

5. **[Style Compliance Matrix](./style-compliance-matrix.md)**
   - Per-screen/component token mapping
   - All style.md token references
   - Derived tokens with derivation logic

6. **[Style Decisions Log](./style-decisions-log.md)**
   - Timestamped assumptions and derivations
   - Conflicts with style.md and resolutions
   - Complete derivation history

### Integration & Implementation

7. **[Function-to-UI Mapping](./function-to-ui-mapping.md)**
   - Backend features → UI triggers
   - Data contracts (inputs/outputs)
   - Validations, error states, feedback patterns

8. **[Accessibility Checklist](./accessibility-checklist.md)**
   - WCAG 2.2 AA compliance
   - Per-level requirements verification
   - Implementation notes and testing checklist

9. **[Developer Handoff Artifacts](./dev-handoff.md)**
   - Design tokens/CSS token map
   - Spacing/redlines
   - Sample HTML/CSS snippets
   - Acceptance checklist
   - Deployment guide

---

## Quick Reference

### Primary Style Source
- **style.md** (canonical Bosk8 design system reference)

### Key Design Principles
- High-contrast, dark, minimal, utilitarian
- Monospace type (JetBrains Mono), uppercase UI labels
- Subtle borders, soft depth
- Dense but breathable spacing

### Component Categories
- **Cards**: Header, Table, Error states
- **Typography**: Taglines, Labels, Meta text
- **Forms**: Inputs, Selects, Buttons
- **Feedback**: Error cards, Result displays, Badges

### Critical Tokens
- Backgrounds: `--bg-black`, `--bg-elev1`, `--surface-card`
- Text: `--text-primary`, `--text-muted`, `--text-subtle`
- Accents: `--accent-success` (green)
- Borders: `--border-color`, `--border-w` (responsive)
- Spacing: `--space-1`, `--space-2`, `--space-4`

---

## Implementation Workflow

1. **Read Style Guide**: Review style.md for token definitions
2. **Review Decisions Log**: Check style-decisions-log.md for derivations
3. **Reference Components**: Use components.md for implementation details
4. **Follow Compliance Matrix**: Ensure all tokens match style-compliance-matrix.md
5. **Verify Accessibility**: Use accessibility-checklist.md during development
6. **Use Dev Handoff**: Reference dev-handoff.md for CSS snippets and acceptance criteria

---

## Style System Rules

### Absolute Rules
1. **Do not invent** new tokens not present in style.md
2. **Derive** missing tokens from existing tokens using style.md rules
3. **Resolve conflicts** in favor of style.md
4. **Reference exact** token names/paths from style.md

### Derivation Process
1. Identify missing token/pattern
2. Derive from existing tokens using style.md principles
3. Document derivation in style-decisions-log.md
4. Add entry to style-compliance-matrix.md
5. Reference in component specifications

---

## Assumptions & Open Questions

All assumptions and open questions are documented in:
- **executive-summary.md**: High-level assumptions
- **style-decisions-log.md**: Style-related assumptions and resolutions

**Key Assumptions:**
- Telco dataset contains standard columns (19 features)
- Streamlit limitations accepted for brand consistency
- WCAG 2.2 AA compliance target (not AAA)
- Mobile-first responsive design

---

## Status

**Specification Status**: ✅ Complete

All deliverables have been created and documented. The specification system is ready for developer implementation.

**Next Steps:**
1. Review all specification documents
2. Begin implementation using dev-handoff.md
3. Reference style-compliance-matrix.md for token usage
4. Verify against acceptance checklist upon completion

---

## Support

For questions or clarifications:
- **Style questions**: Refer to style.md + style-decisions-log.md
- **Component questions**: Refer to components.md
- **Implementation questions**: Refer to dev-handoff.md
- **Accessibility questions**: Refer to accessibility-checklist.md

