---
name: gift-finder
description: Find a well-researched gift for a specific person (or for yourself) through a short guided interview, a shortlist of gift categories, and live product research that ends in three concrete picks with prices and direct buy links (Amazon or another shop that delivers to the user). Use this skill whenever the user asks for gift ideas, a present, "what should I get my dad / wife / friend / colleague", birthday, Christmas, anniversary, wedding, baby or thank-you gifts, Secret Santa, a treat for themselves, or runs /gift-finder, even if they don't say the word "gift".
license: MIT
metadata:
  author: toxx663
  version: "1.1.0"
---

# Gift Finder

Help the user land on a gift the recipient will actually use and like. The approach has two halves: a short interview that narrows the field to a handful of gift categories, then real research into the best products in the category the user picks.

Most gift advice fails in one of two ways: it asks twenty questions before saying anything useful, or it dumps a generic list ("a nice candle") that ignores the person. This skill avoids both by asking only what changes the answer, and by researching one category properly instead of ten superficially.

## Ground rules

- **Reply in the user's language.** Product names stay as sold.
- **Never re-ask what you already know.** Read the user's first message carefully. "Gift for my brother, 30, loves running and comics, around 50 euros" already answers most of the interview; go straight to whatever is still missing.
- **Keep the interview to three rounds at most** before showing categories. People lose patience fast, and a decent shortlist teaches you more than a fourth question would, because the user's reaction to it is information.
- **Use tappable choices when you can.** If a multiple-choice question tool is available (for example `AskUserQuestion`), use it and always leave room for a free-text answer. Otherwise ask in plain text with short numbered options.
- **Treat age and gender as weak hints, not conclusions.** Stated interests always outrank demographics. A 30-year-old man who likes knitting gets knitting ideas.
- **Stay inside the budget.** A pick over budget is only acceptable if you flag it clearly and it is the one "stretch" option.

## Step 1: Who is it for

Ask in a single message for whatever is missing from this list:

- Who the recipient is: relationship to the user, or the user themselves
- Age (an approximate range is fine)
- Gender, if the user wants to share it
- Occasion (birthday, Christmas, thank-you, no occasion)

If the gift is for the user themselves, skip the relationship question and address them directly from here on.

## Step 2: Interests, budget, destination

Ask what the recipient enjoys. Offer broad types to react to, plus free text, because "what are his hobbies?" on its own often draws a blank:

- Active and outdoors (running, cycling, hiking, gym)
- Creative and making (drawing, music, crafts, DIY)
- Learning and thinking (books, chess, puzzles, languages)
- Tech and gaming
- Food and drink (cooking, coffee, wine)
- Home and comfort
- Style and grooming

When an answer is broad, ask one sharpening question at most, the way a good shop assistant would: "books" becomes "novels, non-fiction, or comics?".

In the same round, ask for:

- **Budget**, as a range or a ceiling, with currency
- **Country the gift ships to**, because prices, shops and availability depend on it. Infer it when the context makes it obvious, and say what you assumed.
- Optionally, anything to avoid or that the recipient already owns

## Step 3: Suggest categories

Propose **four to six gift categories**. A category is a concrete type of item, specific enough to research: "running belt", not "running gear"; "graphic novel box set", not "books".

Build the list so it has range:

- At least one category for each main interest the user named
- One safe choice that is hard to get wrong
- One less obvious idea the user probably hasn't thought of (an experience, a subscription, a consumable, something personalised)
- Every category realistically achievable within the budget

Give each a one-line reason tied to what the user told you. Then ask which one to research, and offer "none of these" as a real option. If the user rejects the set, ask what was off (too boring, too practical, too expensive, wrong interest) and produce a new set that corrects for it rather than rephrasing the old one.

**Example**

Input so far: brother, 30, runs often, reads comics, 50 euros, ships to Luxembourg.

Categories:
1. Running belt: carries phone and keys on the runs he already does
2. Graphic novel box set: a complete story arc rather than a single volume
3. Recovery tool (massage ball or roller): useful after every run, rarely bought for oneself
4. Running socks, premium pack: the safe choice; runners always wear through them
5. Comic art print, framed: the unexpected one, something for his wall

## Step 4: Refine the chosen category

Once the user picks a category, ask **one or two questions that would change which product wins**. If no question would change the answer, skip this step.

Look first for questions about what the recipient already owns and what the gift has to work with, because these are what turn a well-reviewed product into the wrong product. A photo printer is a good example: should it print straight from her phone, or does she already own an instant camera whose film it should share? The same logic applies to anything with an ecosystem: phone brand for headphones and watches, machine type for coffee accessories, console for games, bike type for cycling parts.

The test for a good refinement question: imagine two different answers and check that they lead to two different products.

| Category | Questions that change the pick |
|---|---|
| Running belt | How far and how often does he run? Does it need to hold a large phone or water? |
| Book or comics | Which authors or series does she already love? Physical or e-reader? |
| Headphones | Mostly commuting, sport, or at home? Which phone does he use? |
| Photo printer | Print from a phone, or match an instant camera she already owns? Instant-film look, sticker prints, or postcard size? |
| Coffee gear | How does she brew today: espresso machine, filter, capsules? |
| Board game | How many players usually, and how heavy do they like rules? |
| Clothing or shoes | Size, and how sure are you? (If unsure, steer to size-free options.) |

If the user doesn't know the answer, don't press. Choose the most forgiving option (adjustable, one-size, easy to return) and say that this is why you chose it.

## Step 5: Research

Now do the actual work. This step is what separates this skill from a list of guesses, so use web search and read the sources rather than relying on what you remember; products, prices and model generations change constantly.

1. **Find independent evidence.** Search for recent tests and comparisons of the category from sources that test products themselves: consumer organisations, specialist magazines, enthusiast sites and communities. Prefer results from the last year or two.
2. **Cross-check.** A product becomes a candidate when at least two independent sources rate it well. Be sceptical of listicles that only link to one retailer and of pages with no sign of hands-on testing.
3. **Match to the person.** Filter candidates through the refinement answers. The best belt for a marathon runner is the wrong belt for someone jogging twice a month.
4. **Verify price and availability, and keep the buy page.** Find the product's own page at a shop that delivers to the user's country, in their currency, and confirm the current model is still sold. Keep that URL; it becomes the buy link in Step 6. Note the date-sensitivity if delivery before the occasion looks tight.
5. **Stay honest.** Never invent a product, a price, a rating or a link. If you could not confirm something, say so. If the category turns out to have nothing good in budget, tell the user and suggest the nearest alternative instead of padding the list.

If web search is not available, say so up front. Then give recommendations by type, explain what to look for when choosing, and mark clearly that prices and availability are unverified.

## Step 6: Present three picks

Present exactly three options so the user can decide rather than browse:

- **Best overall**: the one you would buy for this person
- **Best value**: clearly cheaper, still good
- **Wildcard**: a different take, such as a premium stretch, a more personal option, or an unusual alternative

Lead with a one-sentence recommendation, then use this structure for each pick:

```
**[Role]: [Product name]** – [price, currency] at [shop]
Why it fits: [one or two sentences tied to what the user told you]
Trade-off: [the honest downside]
Buy: [link to the product's own page at a shop that delivers to the user]
```

### Buy links

Every pick needs a link the user can tap and buy from, because a recommendation that still requires a search is only half finished.

- **Link to the exact product page**, not a shop's home page, a category page or a review article.
- **Choose the shop by country.** Use the Amazon storefront that delivers to the user's country when the item is sold there (for example amazon.de for Germany, Luxembourg and Austria, amazon.fr for France, amazon.co.uk for the UK), since most people already have an account. When the maker's own shop or a well-known local retailer is cheaper, faster, or the only seller, link that instead or as a second option.
- **Only use URLs you actually opened or saw in search results.** Never assemble a product URL from memory; a dead link at checkout is worse than no link.
- **If you cannot find a direct product page**, give a search link at the right shop and label it as a search, so the user knows they still have to pick the listing.
- **Keep links clean.** Remove tracking parameters and never add affiliate or referral tags; the user has to be able to trust that the pick was chosen for them.
- **For experiences and services** (workshops, vouchers, subscriptions), link the booking or voucher page and say if booking needs a call or an email.

Close with sources for the tests you relied on, and one short line offering the natural next steps: choose one of the picks to finalise it, research another category from the shortlist, adjust the budget, or write a message for the card.

## Step 7: Finalise the chosen item

When the user settles on one specific product, check the details that decide whether the gift works on the day. Ask only the ones that apply, in a single round, with tappable choices where possible:

- **Compatibility and what they already own.** Does it work with her phone, her existing camera, his machine? If the recipient already has part of the system, it may be smarter to buy the piece that completes it rather than a second device.
- **Variant.** Colour, size, capacity, edition, language of a book or game.
- **What is not in the box.** Film, batteries, cartridges, a case, a subscription. Offer to add the essentials so the gift is usable when unwrapped, and show the new total against the budget.
- **Timing and returns.** Whether it arrives before the occasion, and the return window if the choice is a gamble.

**Example**

The user picks an instant photo printer.

Questions: "Will she print from her phone, or does she already own an instant camera you'd like it to match?" and "Which colour?"

If she already owns a camera that uses the same film, say so and suggest film and an album as the smarter gift. If not, confirm the printer, add a pack of film because none is included, and show the total.

Then give the final answer: the exact variant, the buy link for it, links for any add-ons, the total, and the delivery estimate if the shop shows one.

## Special situations

- **Gifts for children.** Check the manufacturer's age rating and avoid small parts for under-threes. If the user is buying for someone else's child, lean towards things parents won't resent (quiet, compact, no hundred pieces).
- **Very small budgets.** Favour consumables, small upgrades to something they use daily, or one good item over a bundle of weak ones.
- **Last-minute gifts.** Ask when it is needed. Prioritise items with fast delivery or local pickup, digital gifts, subscriptions and experiences.
- **The person "who has everything".** Shift towards experiences, consumables of a higher quality than they'd buy themselves, and personalised items.
- **Group gifts.** Confirm the total pooled budget rather than the per-person amount.
- **Alcohol, fragrance, clothing, food.** These depend on taste, size or diet. Use them only when the user has given a clear signal, and mention the return policy.
