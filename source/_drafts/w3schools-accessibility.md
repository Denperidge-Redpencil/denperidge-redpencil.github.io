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
- 


## Elements
- `section` is not related to content in `main`
    - Aria-label & use case example: stay connected
- An `aside` is still connected to `main`'s content 
    - Aria-label & use case example: share this page
- `div` and `span` elements say nothing about the content. Only use these if no other option makes sense
- `a` links should usually **not** open in a new tab or window. If it does, make the user aware of this behaviour and ensure you do it with a good reason (like highlighted [here on Adrian Roselli's blog](https://adrianroselli.com/2020/02/link-targets-and-3-2-5.html#Exceptions), which fully details why new tab/window behaviour is not advisable)

## Custom controls
If you cannot use elements semantically (technical limitations, framework...):
- `role` attribute helps assistive technology users understand the purpose of the control. Possible values:
    - `"button"`
- `"aria-label"`: accessible/clear name for the control
    - `name` attribute is *not* enough: this is used for computer code, not human consumption
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
    ![A screenshot form the wikipedia article on colour blindness. The CSS has been modified so that the distinctive blue links are decorated using a soft grey line a few pixels below it](/assets/notes/img_wikipedia_underline_improved.png)


## Images
