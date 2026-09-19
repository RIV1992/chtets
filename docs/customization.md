# Make Chtets fit your writing

Start with a task-specific brief. Most work does not need a modified skill:

```text
Use Chtets to edit the draft below.
Reader: an existing customer who knows the project.
Purpose: agree on the next review date.
Language: English, UK spelling.
Length: under 150 words.
Tone: direct and considerate.
Editing scope: reorganise freely, preserve the position and every condition.
Return: the finished email, followed only by any unresolved factual question.
```

Then provide the draft and relevant sources. Specify whether the agent should write, edit, shorten, verify, or lightly proofread: these allow different degrees of intervention.

## Keep your voice in a separate profile

Start from [the author profile template](../examples/author-profile.example.md), or create a private Markdown file such as `author-profile.md`. Keep it outside the public repository, and explicitly attach it or ask the agent to read its path. Chtets does not automatically discover arbitrary profile files.

For example:

```markdown
# Author profile

## Scope
Use for my professional emails and technical articles.
Do not apply these preferences to quotations or other people's writing.

## Reader relationship
Assume an informed colleague. Explain unfamiliar terms once.

## Voice
Use plain language and specific verbs.
State the purpose early in emails.
Keep disagreement calm and explain the practical consequence.

## Language and format
Use UK English unless the brief asks for another language.
Use short paragraphs; use lists when they make comparisons easier.
Ask for the required sign-off if it is not supplied.

## Boundaries
Do not invent my experience, results, emotions, or company practices.
Keep estimates, plans, commitments, and completed actions distinct.

## Examples
Add two or three short samples that I wrote or approved.
For each, note which choices should carry over and which are specific
to that audience or situation.
```

Use it with an explicit request:

```text
Read author-profile.md and use Chtets to edit this article.
Apply the profile where it fits this brief. Preserve the quoted passages.
```

A few annotated samples are more useful than a long list of adjectives. Explain why a sentence works: perhaps it states a request clearly, keeps a qualification, or sounds appropriately informal. Avoid turning one unusual message into a universal rule.

## Adapt for a team or domain

Keep the common writing method and add a small, clearly scoped reference for your terminology, readers, formatting, or evidence requirements. For instance, a product team may need a glossary and rules for distinguishing released features from plans.

In a maintained fork, add a relative link from `SKILL.md` to that reference, plus one sentence saying when to read it. An unreferenced file may never be loaded. Do not add a private profile to a public fork.

Keep changes narrow:

| Change | Where it belongs |
| --- | --- |
| Tone, length, audience, output language for one request | The task brief |
| Stable personal preferences and approved samples | A private author profile |
| Team terminology or a recurring document convention | A scoped reference in your team's copy |
| A writing principle that should apply to every user | A proposed change to the shared skill |

Preserve `name: chtets` and the `chtets/` folder name when maintaining a replacement copy. If you want two variants installed simultaneously, give the second a distinct matching folder name and frontmatter `name`, then update its invocation and metadata. Host rules differ; check the [installation guide](installation.md).

## Check a customization before relying on it

Try the original and modified instructions on the same three to five representative requests. Include a short email, a longer explanation, a request to shorten text with conditions, and a task that should keep the author's wording almost intact.

Compare meaning, factual support, connections between sentences, voice, and usefulness to the reader. Reject changes that make a text more polished by removing uncertainty or adding an unsupported promise. Record the exact examples and your decisions so later updates have something concrete to preserve.

A successful example supports a local judgment about that task. It does not establish that the customization improves every model, language, or genre.
