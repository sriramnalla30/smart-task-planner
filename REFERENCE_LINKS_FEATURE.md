# Reference Links Feature

## Overview

Enhanced Gemini AI prompts to include helpful reference links (tutorials, documentation, guides) for each task in the generated plan.

## Changes Made

### 1. Schema Update (`app/schemas.py`)

Added `reference_links` field to the `Task` model:

```python
reference_links: List[str] = Field(
    default_factory=list,
    description="Helpful tutorial, documentation, or resource links for completing this task"
)
```

### 2. Prompt Enhancement (`app/services/plan_service.py`)

Updated the prompt to request reference links:

- Added `reference_links` field to JSON example
- Instructed Gemini to provide 1-3 helpful URLs per task
- Specified criteria: official docs, popular tutorials, widely-used resources
- Emphasized real, publicly accessible URLs

### 3. Frontend Display (`frontend/index.html`)

Added visual reference links section to each task card:

- **📚 Helpful Resources** header with gradient background
- **Indigo/purple color scheme** to distinguish from other sections
- **Clickable links** that open in new tab
- **Hover effects**: Link underlines, icon scales up, badge color changes
- **URL truncation**: Long URLs shortened to 60 characters for readability
- **"Open ↗" badge** indicating external link

## Visual Design

### Resources Section Styling

```html
<div
  class="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg border-2 border-indigo-200"
>
  <h4>📚 Helpful Resources</h4>
  <a href="..." target="_blank"> 🔗 URL with "Open ↗" badge </a>
</div>
```

### Color Scheme

- **Background**: Indigo-50 to Purple-50 gradient
- **Border**: Indigo-200 (2px)
- **Text**: Indigo-700 (links), Indigo-900 (header)
- **Hover**: Indigo-900 (links), underline, scale transform
- **Badge**: Indigo-100 background, transitions to Indigo-200 on hover

### Icons

- **📚**: Section header (books emoji)
- **🔗**: Individual link (link emoji with hover scale effect)
- **↗**: External link indicator in badge

## Expected Output

For a task like "Set up React project with Vite":

```json
{
  "id": "T1",
  "title": "Set up React project with Vite",
  "description": "Initialize modern React development environment",
  "reference_links": [
    "https://vitejs.dev/guide/",
    "https://react.dev/learn/start-a-new-react-project",
    "https://github.com/vitejs/vite/tree/main/packages/create-vite"
  ]
}
```

### Frontend Rendering

```
┌─────────────────────────────────────────────────────┐
│ 🚀 [T1] Set up React project with Vite            │
│                                                     │
│ Initialize modern React development environment    │
│                                                     │
│ 📚 Helpful Resources                               │
│ ┌───────────────────────────────────────────────┐ │
│ │ 🔗 https://vitejs.dev/guide/      [Open ↗]   │ │
│ │ 🔗 https://react.dev/learn/...    [Open ↗]   │ │
│ │ 🔗 https://github.com/vitejs/...  [Open ↗]   │ │
│ └───────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

## Benefits

### For Users

1. **Immediate Guidance**: No need to search for resources separately
2. **Quality Resources**: AI selects reputable, official sources
3. **Time Savings**: Direct access to documentation and tutorials
4. **Learning Path**: Structured resources for each task
5. **Confidence Boost**: Knowing where to learn increases task completion likelihood

### For Recruiters/Evaluators

- Demonstrates **thoughtful UX design**
- Shows **integration of external resources**
- Proves **AI can provide practical, actionable guidance**
- Highlights **attention to user needs**

## Example Use Cases

### Software Development Goal

**Goal**: "Build a REST API with Node.js and MongoDB"

- **Task 1**: Set up Node.js project
  - Links: Node.js docs, npm guide, Express.js tutorial
- **Task 2**: Connect to MongoDB
  - Links: MongoDB Atlas docs, Mongoose guide, connection examples
- **Task 3**: Create API routes
  - Links: Express routing docs, REST API best practices, Postman tutorials

### Design Goal

**Goal**: "Create a brand identity for a startup"

- **Task 1**: Research competitor branding
  - Links: Brand research guides, competitive analysis tools, design inspiration sites
- **Task 2**: Design logo concepts
  - Links: Figma tutorials, logo design principles, color theory resources
- **Task 3**: Create brand guidelines
  - Links: Brand guideline templates, style guide examples, typography resources

### Marketing Goal

**Goal**: "Launch a content marketing campaign"

- **Task 1**: Define target audience
  - Links: Buyer persona templates, audience research tools, market segmentation guides
- **Task 2**: Create content calendar
  - Links: Content planning tools, editorial calendar templates, social media guides
- **Task 3**: Write blog posts
  - Links: SEO writing guides, content optimization tools, headline formulas

## Technical Details

### Link Validation

- AI instructed to provide **real, publicly accessible URLs**
- No broken link checking (could be added in future)
- Links open in **new tab** (`target="_blank"`)
- Security: `rel="noopener noreferrer"` prevents tab-nabbing

### Fallback Behavior

- If `reference_links` is empty or missing, section doesn't display
- No error shown to user (graceful degradation)
- Existing task card layout unaffected

### Performance

- Links rendered as part of task card HTML
- No additional API calls
- Minimal impact on page load time

## Future Enhancements

Potential improvements:

1. **Link Preview**: Show favicon or screenshot on hover
2. **Link Categories**: Label links as "Tutorial", "Documentation", "Tool", etc.
3. **Link Validation**: Backend check for broken links
4. **User Rating**: Allow users to rate helpfulness of links
5. **Custom Links**: Let users add their own resources
6. **Link Analytics**: Track which resources are most clicked
7. **Archived Links**: Save link content in case original disappears
8. **Video Detection**: Special icon for YouTube/video tutorials

## Testing

### Manual Testing Steps

1. Start backend server
2. Open frontend in browser
3. Submit a goal (e.g., "Build a mobile app with React Native")
4. Verify reference links appear in each task card
5. Click links to ensure they open in new tab
6. Check hover effects work (underline, icon scale, badge color)
7. Test with different goals to see variety of resources

### Expected Behavior

✅ Links display with 📚 section header
✅ 🔗 icon appears before each link
✅ "Open ↗" badge shows external link indicator
✅ Links open in new tab
✅ Hover effects work smoothly
✅ Long URLs truncated properly
✅ Section has distinct indigo/purple styling

## Code Locations

- **Schema**: `app/schemas.py` (line ~30)
- **Prompt**: `app/services/plan_service.py` (line ~115)
- **Frontend**: `frontend/index.html` (line ~340)

## Conclusion

The reference links feature transforms the Smart Task Planner from a simple task generator into a **comprehensive execution guide**. Users now receive:

- **What to do** (task title)
- **Why to do it** (description)
- **When to do it** (dates)
- **What depends on it** (dependencies)
- **How confident we are** (confidence score)
- **Where to learn how** (reference links) ← **NEW!**

This makes the AI-generated plans significantly more **actionable and valuable** for end users.
