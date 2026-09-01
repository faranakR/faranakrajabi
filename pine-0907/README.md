# Big Bear invite — how to put it on faranakrajabi.com

Your site is Jekyll (Minimal Mistakes) on GitHub Pages, so this is a drop-in:

1. In your site repo, make a folder with a name Nick won't guess and Google won't index, e.g. `nard/`.
2. Put `index.html` in it. It has no front matter, so Jekyll copies it as-is. Don't link it from your nav.
3. Add your photo as `hero.jpg` in the same folder (it fills the A-frame triangle on the first page). Square or portrait crop works best.
4. Commit, push, wait a minute, then send him https://faranakrajabi.com/nard/

Edit before sending:
- Quiz: open `index.html`, find `const QUIZ` near the bottom. The four Hard questions are marked [EDIT] — replace them with real ones. `a` is the index (0–3) of the correct option. Rewards are in the same block.
- Menu main dish: I put zereshk polo ba morgh. Swap if you want.
- Anything that says "Santa Barbara" if you're leaving from somewhere else.

The page has `noindex, nofollow` so search engines skip it, but anyone with the URL can open it — keep the folder name unguessable.
