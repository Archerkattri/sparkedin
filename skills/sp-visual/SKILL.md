---
name: sp-visual
license: MIT
description: >-
  Design LinkedIn visuals that do not look AI-generated: banners, post
  images, and carousel art. Spots the AI slop tells, applies the human-made
  principles, and builds a banner from a real-photo brief with text as
  separate layers. Use when the user wants a banner, a post image, or asks
  why something looks AI-generated.
---

# sp-visual

Profile directory: `<profile>` holds voice.md, log.md, plan.md and outreach.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

sp-human strips the AI fingerprint from words. This skill strips it from images. Same job, different surface. A banner or post image that reads as AI slop costs trust before anyone reads a word on it. LinkedIn added a "Seems like AI slop" report button in July 2026 and it was clicked over a million times in two weeks. The fix is not "no AI". The fix is visible human decisions: restraint, a real photograph of actual work, one specific thing, ordinary light, texture and grain, one idea.

## 1. The tells: what makes an image read as AI slop

One mechanism sits under all of them. An unconstrained model returns the statistical average of its training set, so the output is the same bland, over-lit, faintly plastic look for everyone. Audiences recognise it in a fraction of a second. Two or three tells together, with no provenance, is a strong case. No single tell proves anything.

1. **Plastic, waxy surfaces.** Airbrushed, poreless skin with a faint sheen. Fabric with no weave. Surfaces with no micro-texture. The single most common image tell.
2. **Too-perfect, symmetrical lighting.** Even golden-hour glow on everything, including indoor scenes where that light could not exist. Nothing in shadow, no hot spots, no mixed colour temperatures.
3. **Dead-centre, bilaterally symmetrical composition.** Centred subject, perfect symmetry, depth-of-field blur applied uniformly whether it makes sense or not.
4. **Purple-blue and teal-orange gradients.** Dark near-black hero, electric indigo gradient, violet to pink gradient-clipped text, teal-orange colour grade. Traced to Tailwind defaults (indigo-600, slate-900) baked into training data.
5. **Glowing orbs, lens flares, holograms.** A floating glowing sphere, blurred gradient orbs, aurora glow behind centred white text, sparkles. One of the most recognisable cliches in AI branding.
6. **Generic tech aesthetics.** Robot hands, brains, orbiting nodes, wireframe meshes, tiny glowing particles connected by lines, floating glass cards, abstract 3D spheres. A glowing robot hand holding a glowing point-cloud object hits three cliches at once. Never ship that.
7. **Generic stock-photo compositions.** Diverse team laughing in an open-plan office, handshake in a glass boardroom, laptop plus latte plus sunset, city skyline at night. Technically fine, could belong to any of 50,000 businesses.
8. **Impossible details.** Wrong finger counts, hands failing to grip objects, garbled or pseudo-language text on signs, reflections showing a different scene, shadows falling in inconsistent directions, repeating patterns that break.
9. **Sameness across a set.** Every image shares focal length, centred subject, gradient backdrop and colour grade. These were not shot, they were extruded.
10. **Baked-in text.** Text rendered inside the image, where gibberish appears and where it cannot be edited. Keep text as separate layers, always.

Why audiences punish it: the look reads as "nobody chose". Polish used to prove investment. Now it proves only that a prompt was written. And suspicion alone costs trust. In a 2026 Nielsen Norman Group study, when participants suspected an image was AI-generated they rated the page less favourably, even when the image was actually a real photo. Humans are bad detectors (62% accuracy in the largest study, coin flip on faces), so what gets punished is genericness and suspicion, not provenance. Polished, specific work scores fine.

## 2. The human-made principles

1. **Restraint. Remove before adding.** One image, one headline, one call to action, lots of whitespace. Most AI-looking designs have too much: effects, glow, gradients, elements. Trim.
2. **Real photography over generated heroes.** A slightly imperfect photo of the actual thing beats a flawless render of a thing that does not exist. Real teams, real products, real moments, real craftsmanship. Imperfection becomes memorable. Reality becomes premium.
3. **Specific, concrete references over generic concepts.** Specify a person, a place, a lens, a moment, a mood. Not "diverse team collaborating" or "futuristic cityscape". A chart showing that one campaign produced leads at $16.20 could only have come from someone who ran it. A generic chart of invented data looks generated.
4. **Asymmetry and imperfection, controlled, not random.** Off-centre framing, rule of thirds, candid composition. A deliberate irregularity is consistent, repeated, and confidently placed, so it reads as a decision. An accidental one is inconsistent and apologetic, so it reads as a mistake. Random noise added to a template does not become craft.
5. **Texture and grain from a real process.** Film grain, paper grain, natural skin texture with visible pores, letterpress bite. Traces of an actual process rather than a filter imitating one.
6. **Directional, ordinary light, not spectacle.** Specify where light comes from (window left, hard shadows). Accept mixed colour temperatures, hot spots, darker areas, imperfect exposure. Ordinary light is fine.
7. **Honest typography and one brand system.** One brand kit (2 to 3 colours, 1 to 2 fonts, spacing rules) applied everywhere. When every post shares a system, the audience reads it as a brand. When every post has different fonts and colours, it reads as a feed of prompts.
8. **Negative space and one idea per image.** Give the subject breathing room. Do not fill the frame. No glow, no HDR, no over-sharpening.
9. **Art direction as process.** Shot-list prompt (subject, lens, light, mood, framing), then batch, select, refine 2 to 3 rounds, never ship the first generation. Reference-condition to a locked style anchor. Full-zoom human QC: count fingers, read background text, check for waxy sheen. Slop is, almost definitionally, the first generation accepted as final.
10. **Do not visualise intelligence, visualise people.** The strongest brands will not visualise intelligence. They will visualise people becoming more capable. Refuse the sparkle, orb, and neural mesh unless it is a joke you can defend.

## 3. LinkedIn banner: the spec

- **Size:** 1584 by 396 px (4:1), max 8 MB, JPG or PNG. PNG for text.
- **Safe zone:** design for the right two-thirds and top half. The circular profile photo covers the bottom-left on desktop. Mobile crops about 22% of height. Nothing losable near edges or bottom-left.
- **Text starts at x=360 or later** (measured on a 1584 canvas). Text at x=80 hid behind the profile photo. Text at x=360 clears it on every line.
- **Minimum text sizes at 1584 wide:** name 88 px, role line 36 px, tagline 28 px, meta line 26 px. A 19 px line renders at about 9 px on a desktop banner and is unreadable. If a line needs to be smaller than 26 px to fit, cut words, do not shrink the type.
- **One message.** One sentence in large type is the highest-value use of the space. Specific and ownable beats vague. Proof over adjectives: one real number, very large, beats a slogan. Never invent a metric, a client logo, or a quote.
- **Text is a layer, never baked into the image.** Build the background photo first, then overlay text with an image tool (PIL, or the host's editor). Never let the generator render the words.
- **Dark panel behind the text.** Text straight on a photo blends into the background. Put a dark rounded panel behind the text block (near-black, about 80% opacity, 18 px radius) so the type is crisp whatever sits behind it. The panel must end before the subject starts.
- **Never squash.** A 3:2 photo forced into 4:1 flattens everything and reads as squished. Generate natively 4:1 (3200 by 800) or crop a true 4:1 band from the source. Check the ratio before compositing, every time.

## 4. The banner prompt

Use this when the user wants a banner. Fill the bracketed parts from their real work, never from a generic concept.

### Krishi-ready prompt (copy and adapt)

> Wide panoramic banner photograph, 4:1 aspect ratio, 1584 by 396 pixels. A real university robotics lab workbench seen from the side, shot on a 35mm camera. On the right third of the frame only, a UR5e robot arm with an Allegro Hand holding a plain white ceramic mug, real metal with scuffs and fingerprints. The left two thirds of the frame are an empty dark workbench surface, plain and clear, nothing in it. Natural window light from the left, hard shadows, muted desaturated colors, subtle film grain, shallow depth of field. Ordinary mixed daylight and fluorescent light. No glow, no gradients, no lens flare, no holograms, no purple or teal color grading, no text, no words, no logos. Everything arranged horizontally so nothing important is cut off at the top or bottom edge.

Text overlay, added as layers after generation, starting at x=360, on a dark panel (x 300 to 1090, y 48 to 336, near-black at 80% opacity, 18 px radius):
- Name, 88 px bold white: [Name]
- Role line, 36 px bold light cyan: [Role, lab or company]
- Tagline, 28 px regular near-white: [One specific sentence about the work]
- Meta line, 26 px regular light grey: [Fellowship or proof point] · [portfolio URL]

### Master prompt (any user)

> Wide panoramic banner photograph, 4:1 aspect ratio, 1584 by 396 pixels. A real [place] seen from [angle], shot on a 35mm camera. On the right third of the frame only, [the actual thing the user makes or uses, with one concrete detail that proves it is real]. The left two thirds of the frame are [empty dark surface or plain background], plain and clear, nothing in it. [Light source and direction], hard shadows, muted desaturated colors, subtle film grain, shallow depth of field. Ordinary [light type]. No glow, no gradients, no lens flare, no holograms, no purple or teal color grading, no text, no words, no logos. Everything arranged horizontally so nothing important is cut off at the top or bottom edge.

### Negative prompt / ban list

Never in a visual: glowing orbs, lens flares, holograms, robot hands as symbols, brains, orbiting nodes, wireframe meshes, glass cards, purple-blue gradients, teal-orange grading, centred symmetrical compositions, stock handshake or skyline scenes, baked-in text, invented metrics, invented client logos, invented quotes, sparkle emojis, pill badges. If any of these appear in a generation, reject it and regenerate. Recolouring purple to green does not fix the problem, because the tells are downstream of absent decisions.

### Designer brief (when no generator is used)

One image, one message, one contrast point. Real photograph of the actual work, shot plainly, filling the frame. Left two-thirds empty for the text panel. Text as editable layers, never baked in. Deliver at 1584 by 396, plus the text as a separate layer file.

## 5. Post images and carousel art

- One idea per image. One image, one headline, one call to action.
- Real photography first. A photo of the actual thing, shot plainly, beats a generated hero every time.
- No baked-in text on post images either. If the post needs words on the image, they go on as layers in an editor, in the brand fonts.
- Carousel covers: one strong contrast point, one message, restrained. A single illustration in one brand colour with no text at all reads as confidence.
- Never reuse the banner's background as a post image. Same image twice reads as a template.

## 6. QC checklist (reject the image if any item fails)

- [ ] Aspect ratio is exactly 4:1 for a banner. No squashing, no stretching.
- [ ] No tell from section 1 appears anywhere in the frame.
- [ ] Text is fully visible, not cut off at any edge, and clears the profile-photo zone (starts at x=360 or later).
- [ ] Text is readable at half size. Shrink the preview to 50% and read every line.
- [ ] Text sits on the dark panel, not straight on the photo.
- [ ] Fingers counted, background text read, reflections and shadows checked at full zoom.
- [ ] One message only. Nothing else competes with it.
- [ ] Every number, name, logo, and quote on the image is real and provable. Nothing invented.

## 7. Inputs, outputs, rules

### Inputs

Ask for, in one batched question:

1. **What it is for** - banner, post image, or carousel art.
2. **The real subject** - the actual thing, place, or work. A photo reference if one exists.
3. **The one message** - the sentence, the number, or the proof point.
4. **What to leave out** - anything confidential, in progress, or not yet public. Do not visualise it.

### Outputs

- The image file at the right size, plus the text as separate layers where the host supports it.
- A one-line note naming what changed and what was checked against section 6.
- The prompt used, saved beside the image, so the next version starts from it instead of from scratch.

### Rules

- Never fabricate. No invented metrics, clients, logos, quotes, or results.
- Never bake text into a generated image.
- Never ship the first generation. Refine 2 to 3 rounds, then QC.
- Never present a generated photo as a real photograph of the user's own lab, team, or hardware. If asked, say plainly how it was made.
- Do not post, upload, or set anything as a banner without the user's explicit go-ahead on the final image.
