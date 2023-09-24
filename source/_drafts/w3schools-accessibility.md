---
title: Notes from the accessibility course on W3Schools
#date: 2023-09-07 18:07:44
categories:
    - I make notes
tags:
    - Accessibility
---

Highly condensed notes for [the accessibility course on the w3schools website](https://www.w3schools.com/accessibility/). In my humble opinion, the entire course is worth taking. However, if you have limited capacity, the following pages contain the most practical and/or important information:

- [The website for Inclusive Design Principles](https://inclusivedesignprinciples.org/)
- [W3Schools' tutorial on semantic elements](https://www.w3schools.com/accessibility/accessibility_semantic_elements.php)
- [W3Schools' tutorial on landmarks](https://www.w3schools.com/accessibility/accessibility_landmarks.php)
- [W3Schools' tutorial on (not relying on) colours](https://www.w3schools.com/accessibility/accessibility_color_meaning.php)
- [W3Schools' tutorial on writing descriptive image text](https://www.w3schools.com/accessibility/accessibility_image_text.php)
- [The Youtube video by Rob Dodson at Google, displaying the importance of headers](https://www.youtube.com/watch?v=vAAzdi1xuUY)
- [W3Schools' tutorial on visual focus](https://www.w3schools.com/accessibility/accessibility_visual_focus.php)
- [W3Schools' walkthrough of a screen reader UX](https://www.w3schools.com/accessibility/accessibility_screen_readers.php)

## Testing accessibility
- Screen readers: NVDA

## Elements
- `section` is not related to content in `main`
    - Aria-label & use case example: stay connected
- An `aside` is still connected to `main`'s content 
    - Aria-label & use case example: share this page
- `div` and `span` elements say nothing about the content. Only use these if no other option makes sense
- `a` links should usually **not** open in a new tab or window. If it does, make the user aware of this behaviour and ensure you do it with a good reason (like highlighted [on the link targets article on Adrian Roselli's blog](https://adrianroselli.com/2020/02/link-targets-and-3-2-5.html#Exceptions), which fully details why new tab/window behaviour is not advisable)
- If you have multiple `nav` elements, use `aria-label` to clearly communicate differences (e.g. `aria-label="main"`)
- `button` elements that (for example) open a modal or a hamburger ùenu, should have an `aria-label` (e.g. `aria-label="Enter zip code to find a dealer nearby"` or `aria-label="Open menu"` respectively)
- If two buttons are made for the same function (e.g. a text button and a icon button to open the same modal), they should be merged into one element

## Skip link
Allows the user to quickly go to the most important part of the page. Test it out by pressing tab on [WebAIM's website](https://webaim.org/)
```html
<header>
    <a href="#main" class="skip">Skip to main content</a>
</header>
<main id="main">
</main>

<style>
    .skip {
        position: absolute;
        left: -10000px;
        top: auto;
        width: 1px;
        height: 1px;
        overflow: hidden; 
    }
    .skip:focus {
        position: static;
        width: auto;
        height: auto;
    }
</style>

```

## Custom controls
If you cannot use elements semantically (technical limitations, framework...):
- `role` attribute helps assistive technology users understand the purpose of the control. Possible values:
    - `"button"`
- `"aria-label"`: accessible/clear name for the control
    - `name` attribute is *not* enough: this is used for computer code, not human consumption
    - Aria-label should thus be written for people, without e.g. hyphens
    - Slightly edited example from w3schools: 
        ```html 
            <select name="countryCode" aria-label="Country calling code">…</select>
        ```
- `value`: the value or state of an element, that should be accessible
    - Edited example from w3schools of an accordion element informing whether it is open or closed:
        ```html
            <div role="button" aria-expanded="false">When do I get charged?</div>
        ```

## Inclusive Design Principles
While the [website for inclusive design principles](https://inclusivedesignprinciples.org/) expands all of these, here are the general principles *supercondensed*
- Ensure comparable UX for every diversity, whether it be for user & device.
- Ensure valuable UX for every situation, whether it be a screen inside or outside, for first time or long time visitors.
- Be consistent in design choices.
- Give full control to the user. Animations & parallax scrolling and infinite load can be obstructive. Users being able to change font size or zooming in can be essential.
- Offer choices for actions. Gestures + menus, different views & layouts.
        
        Alternative ways of presenting data, such as data tables for info graphics, should be available to all users as an option rather than a hidden link just for screen reader users. Accessible alternatives can benefit not just a specific target group but all users as long as we offer the choice.

- Prioritise content.

        Progressively reveal features & content when needed, not all in one go
- Add value through integration. Vibrations for notifications for deaf/hard of hearing folks. Voice interface for multimedia for those that struggle with other controls. Show password button on inputs.


## Colour
- Colour contrast has to be good for *all* states: hover, focus, active, unvisited, visited, deactivated...
- Do not use colour as the only visual indicator of meaning
    - An example from w3schools: links without an underline become unreadable on grayscale
        ![A screenshot from the wikipedia article on colour blindness. The CSS has been modified so that the links are coloured blue, without an underline](/assets/notes/img_wikipedia_colors.png)
        ![A screenshot from the same wikipedia article as before, using the same CSS, but with a greyscale filter. The links have become near indistinguishable from regular text](/assets/notes/img_wikipedia_grayscale.png)
    - Add text and/or icons alongside colour to communicate meaning


## Links
- Use `text-underline-offset` and `text-decoration-color` for improved readability
    Example from w3schools:
    ![A screenshot from the wikipedia article on colour blindness. The CSS has been modified so that the distinctive blue links are decorated using a soft grey line a few pixels below it](/assets/notes/img_wikipedia_underline_improved.png)
- If using (for example) a logo as a link, add an `aria-label`, (e.g. `aria-label="Toyota front page"`)
- Stip down accessible names on links & buttons, remove `go to`/`page`. For example, `aria-label="Global distributors"` is enough

## Images: decorative vs meaningful
> Can you remove it with no impact? Then it is a decorative image.

### Decorative image
Either...
- Set `alt=""` (note: NOT a lack of an alt attribute, specifically an empty one. Otherwise the filename may get read)
- Set role & aria-label/aria-labelledby. Example from w3schools: 
    > `role="img" aria-label="Private house, modern architecture. Minimalistic with a big garage."`
- (Background image) Add the image using css background-image
- (Font icons) Set `role="img"` & `aria-hidden="true"`
- (Inline svg) set `aria-hidden="true"`

### Meaningful image
- Modified examples from w3schools, from worst to best:
    4. `<img src="output-460aebd-49.svg">`
    3. `<img src="redpencil-logo.svg">`
    2. `<img src="redpencil-logo.svg alt="Redpencil Logo>"`
    1. `<img src="redpencil-logo.svg" alt="Home of Redpencil">`

### Writing descriptive text

For some good examples, check out the [w3schools tutorial on descriptive text](https://www.w3schools.com/accessibility/accessibility_image_text.php). But remember some of the following things:
- > The value of the alt attribute should describe the image, or even better: the intention of the image
- > Imagine you were to explain a web page over a phone call with a friend, what would you say about an image?
- If zooming in on an image would reveal more info, consider adding it to the alt text
- If an icon has a meaning (e.g. "gold member"), write that meaning (e.g. "Gold member")


## Links
### States
> A visited state can help a person with short-term memory loss to understand which content has been read. A hover state can help a person with reduced muscle control to know when to click. A focused link helps keyboard users to know which link they are about to activate.

Three tips are described on w3schools:
- Removing the underline is almost always a bad idea ([click here to scroll up to the section on colour](#colour))
- Contrast and focus
    - The focussed state must sufficiently contrast the unfocussed state
    - The outline (viewable when using tab navigation) must not obstruct the text. Use `outline-color` & `outline-offset`
- Make hover very clear. Consider adding (for example) bold text on hover

*(The following two gifs and theur alt text are also adapted from w3schools)*
![Animated image showing a subtle hover effect for a navigation tree through a change in colour](/assets/notes/hover-with-colour.gif)
![Animated image showing an improved hover effect for a navigation three through additionally to the change in colour, making the text bold](/assets/notes/hover-with-colour-and-bold.gif)

### Accessible link text
- Makes sense without any context
- Explains clearly what the reader will get by clicking

Bad links --> good links examples adapted from w3schools
- [Click here]() --> [Find out more about the HTML language]()
- [Read more]() --> Read more about [how to get healthy]()
- Buy tickets to Fall Out Boy [here]() --> [Buy tickets to Fall Out Boy here]()

Tip: write your links under eachother and see if it make sense
- Donate
- Read more
- Visit the eshop

The *read more* can be replaced. On the Red Cross blog site example, it gets replaced with "Law & Policy"


## Headings
- Don't skip headings because of styling reasons: use them sequentially, and change the style with css
- If the design doesn't call for a header, still make one and position it off-screen

### Hidden headings and/or content
Common practice: `sr-only` class
```css
.sr-only {
  position: absolute;
  left: -10000px;
  top: auto;
  width: 1px;
  height: 1px;
  overflow: hidden;
}
```

Example:
```html
<h2 class="sr-only">Headlines</h2>
```

*Note: a hidden heading could be redundant if a `<title>` element contains the same content/fulfills the same purpose*

## Focus
Do *not* remove or hide focus.
> We have two options. Leave it or customize it. Removing it is not an option.
- Do not use `outline: 0;`
- Be careful with parent divs with `overflow: hidden;`

Two options
- Default focus: familiar for the user, no coding needed for you
- Customise visual focus: may be needed if default focus has low contrast with your website, or can be used to align better with the site's colour palette




## (Appendix) Assistive technologies and those that use them
- People with hand tremors/not able to grip a mouse --> Keyboard navigation
- People with mobility disabilities --> Voice control, eye tracking, switch devices
- People who are blind --> Screen readers, braille displays, speech recognition
- People with low vision --> Screen magnification

Thanks to standard methods we don't need to code for specific technologies, and it'll be accessible for all

Important things to additionally note:
- Keyboards are also used on mobile devices (thus stuff like keyboard focus remains important)
